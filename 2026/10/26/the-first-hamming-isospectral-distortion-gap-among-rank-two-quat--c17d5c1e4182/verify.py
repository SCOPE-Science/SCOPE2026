#!/usr/bin/env python3
"""Independent finite check of projective rank-two quaternary examples.
Uses direct F4 arithmetic and all invertible 2-by-2 F4 matrices.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

Q=range(4)
def mul(a,b):
    z=0
    for i in range(2):
        if (b>>i)&1: z ^= a<<i
    if z&8: z ^= 0b1100
    if z&4: z ^= 0b111
    return z

def det(M):
    a,b,c,d=M
    return mul(a,d)^mul(b,c)

def vtimes(v,M):
    x,y=v;a,b,c,d=M
    return (mul(x,a)^mul(y,c),mul(x,b)^mul(y,d))

def projective(v):
    x,y=v
    if y: return (mul(x,next(z for z in (1,2,3) if mul(y,z)==1)),1)
    assert x
    return (1,0)

# Explicit column directions (in canonical order) for PG(1,4).
cols=[(0,1),(1,0),(1,1),(1,2),(1,3)]
ann=[(1,0),(0,1),(1,1),(2,1),(3,1)]
assert all(mul(a,x)^mul(b,y)==0 for (a,b),(x,y) in zip(ann,cols))
matrices=[m for m in product(Q,repeat=4) if det(m)]
assert len(matrices)==180
perms=set()
for m in matrices:
    seq=tuple(ann.index(projective(vtimes(v,m))) for v in ann)
    assert len(set(seq))==5
    perms.add(seq)
assert len(perms)==60

def sign(p): return (-1)**sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))
assert all(sign(p)==1 for p in perms)

# The semilinear Frobenius x -> x^2 fixes infinity, 0, 1 and swaps omega, omega^2.
frobenius=(0,1,2,4,3)
assert sign(frobenius)==-1
assert len({tuple(frobenius[p[i]] for i in range(5)) for p in perms}|perms)==120

# For GF(2),GF(3), all permutations of the projective line are realized.
from math import factorial
for q in (2,3):
    pts=[(1,t) for t in range(q)]+[(0,1)]
    def norm(v):
        a,b=v
        if a: return (1,b*pow(a,-1,q)%q)
        assert b
        return (0,1)
    group=set()
    for a,b,c,d in product(range(q),repeat=4):
        if (a*d-b*c)%q==0: continue
        group.add(tuple(pts.index(norm(((u*a+v*c)%q,(u*b+v*d)%q))) for u,v in pts))
    assert len(group)==factorial(q+1),(q,len(group))
    print('PGL2(F%d) acts as S%d'%(q,q+1))

# Hamming weight evaluated from actual generator columns.
def columns(s,swap):
    counts=[s+i for i in range(5)]
    if swap: counts[0],counts[1]=counts[1],counts[0]
    return [c for c,n in zip(cols,counts) for _ in range(n)]

def weight(u,g):
    x,y=u
    return sum((mul(x,a)^mul(y,b))!=0 for (a,b) in g)

for s in [0,1,2,3,7,20]:
    G=columns(s,False);H=columns(s,True)
    assert len(G)==len(H)==5*s+10
    hist_G=Counter(weight(u,G) for u in product(Q,repeat=2))
    hist_H=Counter(weight(u,H) for u in product(Q,repeat=2))
    assert hist_G==hist_H
    assert hist_G==Counter({0:1,**{4*s+10-j:3 for j in range(5)}})
    extrema=[]
    for mat in matrices:
        ratios=[Fraction(weight(vtimes(u,mat),H),weight(u,G)) for u in ann]
        extrema.append(max(ratios)/min(ratios))
    best=min(extrema)
    wanted=Fraction((4*s+10)**2,(4*s+9)**2)
    assert best==wanted,(s,best,wanted)
    assert best>1
    print('s=%d n=%d distortion=%s realizations=%d' %(s,len(G),best,extrema.count(best)))

# Minimum distinct nonnegative projective column counts.
for n in range(10):
    assert not any(sum(k)==n and len(set(k))==5 for k in product(range(n+1),repeat=5))
assert sum(range(5))==10
print('PGL2(F4) order=60, all projective transformations even; exact first exceptional length=10')
print('VERIFY_OK')
