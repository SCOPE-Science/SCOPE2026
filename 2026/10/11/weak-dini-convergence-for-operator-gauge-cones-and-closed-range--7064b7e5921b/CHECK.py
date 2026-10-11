#!/usr/bin/env python3
"""Exact rational finite stress tests for the operator-gauge cone construction.
The infinite-dimensional and all-dual-functionals assertions require the analytic proof.
"""
from fractions import Fraction as Q
from itertools import combinations

def nullvec(a, width):
    a = [list(map(Q, row)) for row in a]
    piv=[]; row=0
    for col in range(width):
        p=next((k for k in range(row,len(a)) if a[k][col]),None)
        if p is None: continue
        a[row],a[p]=a[p],a[row]
        z=a[row][col];a[row]=[u/z for u in a[row]]
        for k in range(len(a)):
            if k!=row and a[k][col]:
                z=a[k][col];a[k]=[u-z*v for u,v in zip(a[k],a[row])]
        piv.append(col);row+=1
        if row==len(a):break
    free=next(i for i in range(width) if i not in piv)
    x=[Q(0)]*width;x[free]=Q(1)
    for i,p in enumerate(piv):x[p]=-a[i][free]
    total=sum(map(abs,x));return [v/total for v in x]

def phi(i,k):
    if i==0:return Q(1)
    if i==1:return Q((-1)**k)
    if i==2:return Q(1) if k%3==0 else Q(0)
    return Q((k%5)-2)

# The finite search uses the diagonal injection T: x_k -> 2^{-k} x_k.
fs=[frozenset(combo) for s in range(5) for combo in combinations(range(4),s)]
profiles={}; checked_annihilation=0
for F in fs:
    for n in range(1,5):
        r=len(F)+n; delta=Q(1,4**r)
        K=2*r+2; coords=list(range(K,K+len(F)+1))
        vals=nullvec([[phi(i,k) for k in coords] for i in sorted(F)],len(coords))
        y=dict(zip(coords,vals));
        assert sum(map(abs,vals))==1
        assert sum(Q(1,2**k)*abs(v) for k,v in y.items())<=delta
        for i in F:
            assert sum(phi(i,k)*v for k,v in y.items())==0
            checked_annihilation+=1
        profiles[F,n]=(delta,y)
checks=0
for (F,n),(d,y) in profiles.items():
    for (G,m),(e,z) in profiles.items():
        if F.issubset(G) and n<=m and (F,n)!=(G,m):
            assert e<=d/4
            lhs=sum(Q(1,2**k)*abs(z.get(k,Q(0))-y.get(k,Q(0))) for k in set(y)|set(z))
            assert lhs<=2*(d-e)
            checks+=1
assert len(profiles)==64 and checks>500
print(f'VERIFY_OK rational_profiles={len(profiles)} annihilator_tests={checked_annihilation} exact_order_pairs={checks} infinite_net_proof_is_analytic=True')
