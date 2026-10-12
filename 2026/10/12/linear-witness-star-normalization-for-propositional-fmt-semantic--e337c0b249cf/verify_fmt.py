"""Finite sanity checks for the rooted FMT witness-compression lemma.

Run: python3 verify_fmt.py. Python 3 standard library only.
The executable tests do not replace the unrestricted inductive proof.
"""
from functools import lru_cache
from itertools import product
import random

P = lambda i: ('p', i)
BOT = ('bot',)
AND = lambda a,b: ('and', a,b)
OR = lambda a,b: ('or', a,b)
IMP = lambda a,b: ('imp', a,b)
TOP = IMP(BOT, BOT)
NOT = lambda a: IMP(a, BOT)


def subforms(f):
    found = {f}
    for child in f[1:]:
        if isinstance(child, tuple):
            found.update(subforms(child))
    return found


def eval_model(f, v, rel, w):
    @lru_cache(None)
    def ev(g, u):
        op=g[0]
        if op=='p': return bool(v[u] & (1 << g[1]))
        if op=='bot': return False
        if op=='and': return ev(g[1],u) and ev(g[2],u)
        if op=='or': return ev(g[1],u) or ev(g[2],u)
        if op=='imp':
            return all((not ev(g[1],z)) or ev(g[2],z)
                       for z in rel[g][u])
        raise ValueError(op)
    return ev(f,w)


def compress(forms, v, rel):
    """Root 0 has all vertices as successors for each implication formula."""
    subs=set().union(*(subforms(f) for f in forms))
    imps=sorted((f for f in subs if f[0]=='imp'), key=repr)
    defects={}
    for f in imps:
        if not eval_model(f,v,rel,0):
            witnesses=[w for w in range(len(v))
                       if eval_model(f[1],v,rel,w) and
                          not eval_model(f[2],v,rel,w)]
            assert witnesses
            defects[f]=witnesses[0]
    old_ids=[0]+sorted(set(defects.values())-{0})
    index={old:i for i,old in enumerate(old_ids)}
    nr={}
    for f in imps:
        rows=[]
        for old in old_ids:
            if old==0:
                rows.append(tuple(range(len(old_ids))))
            elif eval_model(f,v,rel,old):
                rows.append(())
            else:
                assert f in defects
                rows.append((index[defects[f]],))
        nr[f]=rows
    nv=[v[old] for old in old_ids]
    for f in subs:
        for old in old_ids:
            assert eval_model(f,v,rel,old)==eval_model(f,nv,nr,index[old]), (f, old)
    assert len(old_ids)<=len(imps)+1
    return len(old_ids)


def random_formula(rng,depth):
    if depth==0 or rng.random()<0.22:
        return rng.choice([P(0),P(1),BOT])
    op=rng.choice([AND,OR,IMP,IMP])
    return op(random_formula(rng,depth-1),random_formula(rng,depth-1))


def check_compression():
    rng=random.Random(26052026)
    cases=0
    max_size=0
    for n in range(1,6):
        for _ in range(230):
            forms=[random_formula(rng,3),NOT(BOT),NOT(NOT(TOP)),NOT(IMP(TOP,NOT(TOP)))]
            subs=set().union(*(subforms(f) for f in forms))
            imps=sorted((f for f in subs if f[0]=='imp'), key=repr)
            v=[rng.randrange(4) for z in range(n)]
            rel={f:[tuple(range(n)) if w==0 else
                    tuple(z for z in range(n) if rng.randrange(2))
                    for w in range(n)] for f in imps}
            # Closed axioms that happen to hold everywhere can be retained.
            closed=forms[1:]
            forms=[forms[0]]+[f for f in closed if all(eval_model(f,v,rel,w) for w in range(n))]
            size=compress(forms,v,rel)
            max_size=max(size,max_size)
            cases+=1
    return cases,max_size


def dualrail(clauses,n):
    parts=[]
    for i in range(n):
        parts += [OR(P(2*i),P(2*i+1)),IMP(AND(P(2*i),P(2*i+1)),BOT)]
    for clause in clauses:
        s=P(2*clause[0][0]+(1 if clause[0][1] else 0))
        for var,negative in clause[1:]:
            s=OR(s,P(2*var+(1 if negative else 0)))
        parts.append(s)
    ans=parts[0]
    for part in parts[1:]: ans=AND(ans,part)
    return ans


def check_dualrail():
    checked=0
    for n in (1,2,3):
        literals=list(product(range(n),[False,True]))
        clause_list=list(product(literals,repeat=3))
        rng=random.Random(7+n)
        for _ in range(120):
            clauses=[rng.choice(clause_list) for __ in range(rng.randrange(1,5))]
            sat=any(all(any(bool(bits & (1<<i)) != neg for i,neg in clause)
                            for clause in clauses)
                    for bits in range(1<<n))
            f=dualrail(clauses,n)
            imps=[s for s in subforms(f) if s[0]=='imp']
            rr={s:[(0,)] for s in imps}
            model_sat=any(eval_model(f,[bits],rr,0) for bits in range(1<<(2*n)))
            assert sat==model_sat,(n,clauses,sat,model_sat)
            checked+=1
    return checked


def check_distinct_witnesses():
    forms=[IMP(P(i),BOT) for i in range(3)]
    v=[0,1,2,4]
    # Every root implication is false, each at a different original world.
    rel={f:[tuple(range(4)),(),(),()] for f in forms}
    assert compress(forms,v,rel)==4


if __name__=='__main__':
    trials,large=check_compression()
    check_distinct_witnesses()
    dr=check_dualrail()
    print(f'CHECK_OK compression_cases={trials} max_random_retained_worlds={large} distinct_witness_worlds=4 dualrail_instances={dr}')
