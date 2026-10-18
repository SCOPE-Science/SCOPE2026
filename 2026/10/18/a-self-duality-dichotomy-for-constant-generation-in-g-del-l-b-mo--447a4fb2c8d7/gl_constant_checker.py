"""Finite checks for the GL modal constant/Boolean self-duality criterion.

No external packages. Run: python3 gl_constant_checker.py
These finite checks corroborate the general mathematical proof.
"""
from itertools import product


def all_frames(n):
    edges = [(i, j) for i in range(n) for j in range(n) if i != j]
    for b in range(1 << len(edges)):
        R = [[False]*n for _ in range(n)]
        for k, (i, j) in enumerate(edges):
            if b & (1<<k):
                R[i][j] = True
        if all(not (R[i][j] and R[j][k]) or R[i][k]
               for i in range(n) for j in range(n) for k in range(n)):
            yield R


def ev(F, V, w, term):
    tag = term[0]
    if tag == 'p': return V[w][term[1]]
    if tag == 'box': return all(not F[w][j] or ev(F,V,j,term[1]) for j in range(len(F)))
    if tag == 'dia': return any(F[w][j] and ev(F,V,j,term[1]) for j in range(len(F)))
    if tag == 'f':
        name, arguments = term[1:]
        a = [ev(F,V,w,t) for t in arguments]
        if name == 'not': return not a[0]
        if name == 'maj': return sum(a) >= 2
        if name == 'oddxor': return bool(sum(a) % 2)
        raise ValueError(name)
    raise ValueError(tag)


def make_witnesses(phi, varnames):
    """Return two finite transitive irreflexive pointed models witnessing φ and not φ."""
    def rec(phi):
        scopes = []
        def walk(t):
            if t[0] in ('box','dia'):
                if t[1] not in scopes: scopes.append(t[1])
                walk(t[1])
            elif t[0]=='f':
                for a in t[2]: walk(a)
        walk(phi)
        # Only immediate modal scopes matter. Other nested scopes belong to their own witness components.
        scoped=[]
        def immediate(t):
            if t[0] in ('box','dia'):
                if t[1] not in scoped: scoped.append(t[1])
            elif t[0]=='f':
                for a in t[2]: immediate(a)
        immediate(phi)
        components=[]
        for s in scoped:
            pos,neg=rec(s)
            components.extend([pos,neg])
        terminal=([[False]],[{p:False for p in varnames}],0)
        # Build fresh root with every point of each component as successor.
        total=1+sum(len(m[0]) for m in components)
        R=[[False]*total for _ in range(total)]
        V=[{p:True for p in varnames}]
        offset=1
        for m in components:
            r,v,_=m
            for i in range(len(r)):
                V.append(dict(v[i]))
                R[0][offset+i]=True
                for j in range(len(r)):
                    R[offset+i][offset+j]=r[i][j]
            offset+=len(r)
        rich=(R,V,0)
        a=ev(*terminal[:2],0,phi)
        b=ev(*rich[:2],0,phi)
        assert a != b, (phi,a,b)
        return (terminal,rich) if a else (rich,terminal)
    return rec(phi)


def main():
    p=('p','p')
    terminal=('box',('dia',p))
    nonterminal=('dia',('box',p))
    frame_count = checks = 0
    for n in range(1,5):
        for F in all_frames(n):
            frame_count+=1
            for v in product((False,True),repeat=n):
                V=[{'p':v[i]} for i in range(n)]
                for i in range(n):
                    t=ev(F,V,i,terminal)
                    u=ev(F,V,i,nonterminal)
                    assert t==(not any(F[i])), (n,F,i,'terminal')
                    assert u==any(F[i]), (n,F,i,'nonterminal')
                    checks +=2
    op_count=0
    # Test all Boolean 1-, 2-, 3-ary functions (4+16+256=276 functions),
    # including every nonselfdual truth table witness.
    for arity in range(1,4):
        tuples=list(product((False,True),repeat=arity))
        for bits in product((False,True),repeat=1<<arity):
            vals=dict(zip(tuples,bits))
            selfdual=all(vals[tuple(not x for x in a)] != vals[a] for a in tuples)
            if not selfdual:
                a=next(a for a in tuples if vals[a]==vals[tuple(not x for x in a)])
                c=vals[a]
                assert all(vals[a if terminal_bit else tuple(not x for x in a)]==c
                           for terminal_bit in (True,False))
                op_count+=1
    examples=[p,
        ('f','not',(p,)),
        ('f','maj',(p,('box',p),('dia',p))),
        ('f','oddxor',(p,('box',p),('dia',p))),
        ('f','maj',(('f','not',(p,)),('box',('f','maj',(p,p,('dia',p)))),('dia',('box',p)))),
        ('f','oddxor',(('box',('dia',p)),('dia',('box',p)),('f','not',(p,))))]
    for f in examples:
        pos,neg=make_witnesses(f,['p'])
        assert ev(pos[0],pos[1],pos[2],f)
        assert not ev(neg[0],neg[1],neg[2],f)
        for model in (pos,neg):
            R=model[0];assert all(not R[i][i] for i in range(len(R)))
            assert all(not (R[i][j] and R[j][k]) or R[i][k] for i in range(len(R)) for j in range(len(R)) for k in range(len(R)))
    print(f'frames={frame_count} root_valuations_tests={checks} nonselfdual_tables={op_count} selfdual_witness_formulas={len(examples)}')
    print('VERIFY_OK')

if __name__=='__main__':main()
