#!/usr/bin/env python3
"""Standalone finite checks of the support-separating projection lemma for BALFIs.

Usage: python3 verify.py

This checks finite instances. The unbounded conclusion relies on the proof,
not on the enumerations below. Uses only Python's standard library.
"""
from itertools import product
import random


def V(name): return ("v", name)
def N(x): return ("n", x)
def C(x): return ("c", x)
def A(x,y): return ("and",x,y)
def O(x,y): return ("or",x,y)
def I(x,y): return ("imp",x,y)

FORMULAS = [
    I(N(C(A(N(V("p")), V("q")))), O(C(V("p")), N(V("q")))),
    I(C(O(N(N(V("p"))), C(V("q")))), O(N(C(V("p"))), V("q"))),
    N(A(C(N(V("p"))), N(C(V("q"))))),
    O(I(C(V("p")), N(V("q"))), C(I(V("q"), N(V("p"))))),
    C(N(C(I(V("p"), V("q"))))),
]


def subformulas(f):
    acc = []
    seen = set()
    def rec(x):
        if x in seen: return
        seen.add(x)
        for y in x[1:]:
            if isinstance(y, tuple): rec(y)
        acc.append(x)
    rec(f)
    return acc


def operation_options(q):
    top = (1<<q)-1
    return [[(b,c) for b in range(top+1) if (a|b)==top
                     for c in range(top+1) if (a&b&c)==0]
            for a in range(top+1)]


def evaluation(f, neg, circ, env, q):
    top = (1<<q)-1
    cache = {}
    for x in subformulas(f):
        op = x[0]
        if op=="v": a = env[x[1]]
        elif op=="n": a = neg[cache[x[1]]]
        elif op=="c": a = circ[cache[x[1]]]
        elif op=="and": a = cache[x[1]]&cache[x[2]]
        elif op=="or": a = cache[x[1]]|cache[x[2]]
        elif op=="imp": a = (top^cache[x[1]])|cache[x[2]]
        else: raise AssertionError(op)
        cache[x]=a
    return cache


def compressed_certificate(f, neg, circ, env, q):
    prior = evaluation(f,neg,circ,env,q)
    top=(1<<q)-1
    if prior[f]==top: return None
    sub = subformulas(f)
    S = set(prior.values())
    T = S | {top}
    # Preserve one failing atom first, then separate all distinct support values.
    bits=[next(j for j in range(q) if not (prior[f]>>j)&1)]
    def proj(a):
        return sum(((a>>j)&1)<<i for i,j in enumerate(bits))
    while len({proj(v) for v in T}) < len(T):
        pair = next((a,b) for a in T for b in T if a!=b and proj(a)==proj(b))
        j=next(j for j in range(q) if j not in bits and ((pair[0]^pair[1])>>j)&1)
        bits.append(j)
    assert len(bits)<=len(T)-1
    m=len(bits); out_top=(1<<m)-1
    D={proj(a): (proj(neg[a]),proj(circ[a])) for a in S}
    assert len(D)==len(S)
    newneg=[D[a][0] if a in D else out_top^a for a in range(out_top+1)]
    newcirc=[D[a][1] if a in D else out_top for a in range(out_top+1)]
    assert all((a|newneg[a])==out_top and (a&newneg[a]&newcirc[a])==0
               for a in range(out_top+1))
    nextval=evaluation(f,newneg,newcirc,{v:proj(a) for v,a in env.items()},m)
    assert all(nextval[x]==proj(prior[x]) for x in sub)
    assert nextval[f]!=out_top
    # Certificate verification independent of construction: only bitvectors,
    # their Boolean equations, and functionality are used.
    s={x:nextval[x] for x in sub}
    eta={x:newneg[s[x]] for x in sub}
    kappa={x:newcirc[s[x]] for x in sub}
    assert all((s[x]|eta[x])==out_top and (s[x]&eta[x]&kappa[x])==0 for x in sub)
    assert all(s[x]!=s[y] or (eta[x],kappa[x])==(eta[y],kappa[y])
               for x in sub for y in sub)
    for x in sub:
        op=x[0]
        if op=='v': continue
        if op=='n': assert s[x]==eta[x[1]]
        if op=='c': assert s[x]==kappa[x[1]]
        if op=='and': assert s[x]==(s[x[1]]&s[x[2]])
        if op=='or': assert s[x]==(s[x[1]]|s[x[2]])
        if op=='imp': assert s[x]==((out_top^s[x[1]])|s[x[2]])
    return m


def run():
    total=0; compressed=0; worst=0
    for q in (1,2):
        count=0
        opts=operation_options(q)
        for rows in product(*opts):
            count+=1
            neg=tuple(v[0] for v in rows)
            circ=tuple(v[1] for v in rows)
            for p in range(1<<q):
                for t in range(1<<q):
                    env={'p':p,'q':t}
                    for f in FORMULAS:
                        total+=1
                        m=compressed_certificate(f,neg,circ,env,q)
                        if m is not None:
                            compressed+=1
                            worst=max(m,worst)
        assert count==(6 if q==1 else 1296), (q,count)
    # Random tests on three-atom Boolean carriers, beyond exhaustive q<=2.
    rng=random.Random(171104)
    opts=operation_options(3)
    for _ in range(1000):
        rows=[rng.choice(row) for row in opts]
        neg=tuple(v[0] for v in rows)
        circ=tuple(v[1] for v in rows)
        env={'p':rng.randrange(8),'q':rng.randrange(8)}
        for f in FORMULAS:
            total+=1
            m=compressed_certificate(f,neg,circ,env,3)
            if m is not None:
                compressed+=1
                worst=max(m,worst)
    # Optimal trace family: top and all distinct coatoms of an (r-1)-atom BA.
    # Each omitted coordinate conflates top with the corresponding coatom.
    from itertools import combinations
    for r in range(2,10):
        top=(1<<(r-1))-1
        trace={top} | {top^(1<<j) for j in range(r-1)}
        assert len(trace)==r
        for m in range(r-1):
            for coords in combinations(range(r-1),m):
                def signature(a): return tuple((a>>j)&1 for j in coords)
                assert len({signature(a) for a in trace}) < r
    print('VERIFY_OK')
    print('formula_checks',total,'nonvalid_projections',compressed,
          'maximum_selected_atoms',worst)
    print('all_BALFIs_q1',6,'all_BALFIs_q2',1296,'random_BALFIs_q3',1000,'sharp_trace_r_2_to_9',True)

if __name__=='__main__':run()
