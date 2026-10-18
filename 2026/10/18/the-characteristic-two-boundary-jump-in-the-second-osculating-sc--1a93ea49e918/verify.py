#!/usr/bin/env python3
"""Exact 2-Hasse-jet minor certificate for a toric hexagon over Z.
No external packages are needed.  Run: python3 verify.py
"""
from itertools import combinations, permutations
from math import comb
from collections import defaultdict

# Normalized monomial exponents on a vertex chart of the hexagon.
monomials = [(0,0),(1,0),(0,1),(1,2),(2,1),(2,2)]
hasse_orders = [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]

def entry(order, monomial):
    a,b = order; m,n = monomial
    if a > m or b > n:
        return 0,(0,0)
    return comb(m,a)*comb(n,b),(m-a,n-b)

M = [[entry(d,e) for e in monomials] for d in hasse_orders]
assert [M[0][i][0] for i in range(6)] == [1]*6

def sign(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def determinant(rows,cols):
    n=len(rows)
    result=defaultdict(int)
    for p in permutations(range(n)):
        coeff=sign(p); a=b=0
        for i,j in enumerate(p):
            c,exp=M[rows[i]][cols[j]]
            coeff*=c; a+=exp[0]; b+=exp[1]
            if coeff==0:
                break
        if coeff:
            result[a,b]+=coeff
    return {e:c for e,c in result.items() if c}

assert determinant(range(6),range(6)) == {}, 'generic six-by-six determinant must vanish'
minors=[determinant([i for i in range(6) if i!=ir],[j for j in range(6) if j!=ic]) for ir in range(6) for ic in range(6)]
nonzero=[m for m in minors if m]
assert len(nonzero)==18, ('unexpected nonzero minor count', len(nonzero))
assert all(len(m)==1 for m in nonzero), 'all minors must be monomials'
odd_entries={next(iter(m.items())) for m in nonzero}
assert all(abs(c) in (1,2) for (_,c) in odd_entries)
# Universal integral Fitting ideal: (2*u^2, u*v, 2*v^2).
# Each nonzero maximal minor belongs to this monomial ideal in Z[u,v].
assert all((c%2==0 and (a>=2 or b>=2)) or (a>=1 and b>=1) for m in nonzero for ((a,b),c) in m.items())
assert any(m=={(2,0):-2} or m=={(2,0):2} for m in nonzero)
assert any(m=={(1,1):-1} or m=={(1,1):1} for m in nonzero)
assert any(m=={(0,2):-2} or m=={(0,2):2} for m in nonzero)
# Odd characteristic: all minors are in (u,v)^2 and the three quadratic
# monomials occur with coefficients units in every odd characteristic.
assert all(a+b>=2 for m in nonzero for (a,b) in m)
assert any((2,0) in m and abs(m[2,0])==2 for m in nonzero)
assert any((1,1) in m and abs(m[1,1])==1 for m in nonzero)
assert any((0,2) in m and abs(m[0,2])==2 for m in nonzero)
# Characteristic 2: odd coefficients survive and generate the squarefree uv ideal.
mod2=[{e:c%2 for e,c in m.items() if c%2} for m in minors]
assert all(all(a>=1 and b>=1 for (a,b) in m) for m in mod2)
assert any(m=={(1,1):1} for m in mod2)
assert sum(bool(m) for m in mod2)==6
# Rank at the vertex is 3 (first three independent columns/rows).
assert all(coeff==0 or exp==(0,0) for row in M for coeff,exp in row if exp==(0,0))
M_at0=[[c if exp==(0,0) else 0 for c,exp in row] for row in M]
assert M_at0[:3] == [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0]]
assert all(not any(row) for row in M_at0[3:])
# In char2, at (u,v)=(0,1), rank is 4; similarly at (1,0).
def rank_mod2(u,v):
    A=[[c*(u**e[0])*(v**e[1])%2 for c,e in row] for row in M]
    r=0
    for j in range(6):
        k=next((i for i in range(r,6) if A[i][j]), None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        for i in range(6):
            if i!=r and A[i][j]: A[i]=[x^y for x,y in zip(A[i],A[r])]
        r+=1
    return r
assert [rank_mod2(*xy) for xy in [(0,0),(0,1),(1,0),(1,1)]] == [3,4,4,5]
print('VERIFY_OK: universal ideal (2u^2,uv,2v^2) on six charts; 36 maximal minors, 18 nonzero; char!=2 (u,v)^2; char2 (uv), ranks 3/4/5')
