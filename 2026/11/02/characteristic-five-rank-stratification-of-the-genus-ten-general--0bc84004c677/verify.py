#!/usr/bin/env python3
"""Exact Hasse--Witt calculation for a two-cubic genus-ten curve in characteristic five.
Only Python's standard library is required. Polynomial coefficients are in F_5[L].
"""
from itertools import product

P = 5

def addpoly(a, b):
    z = dict(a)
    for k, v in b.items():
        z[k] = (z.get(k, 0) + v) % P
    return {i: v for i, v in z.items() if v}

def mulpoly(a, b):
    z = {}
    for i, v in a.items():
        for j, w in b.items():
            z[i + j] = (z.get(i + j, 0) + v*w) % P
    return {i: v for i, v in z.items() if v}

def mul(a, b):
    z = {}
    for x, cx in a.items():
        for y, cy in b.items():
            e = tuple(r+s for r,s in zip(x,y))
            z[e] = addpoly(z.get(e, {}), mulpoly(cx,cy))
    return {e:c for e,c in z.items() if c}

f1 = {(3,0,0,0):{0:1},(0,3,0,0):{0:1},(0,0,3,0):{0:1}}
f2 = {(3,0,0,0):{1:1},(0,3,0,0):{0:1},(0,0,0,3):{0:1}}
Q = mul(f1,f2)
R = {(0,0,0,0):{0:1}}
for _ in range(4):
    R = mul(R,Q)
assert len(R) == 125
basis = [tuple(t+1 for t in z) for z in product(range(3),repeat=4) if sum(z)==2]
assert len(basis)==10
M = [[R.get(tuple(5*a[k]-b[k] for k in range(4)),{}) for a in basis] for b in basis]
expected = {
    (1,8):{0:1,1:4,2:4,3:1},
    (8,1):{0:1,1:1},
    (3,7):{2:3,3:1},
    (7,3):{0:3,1:1},
    (4,6):{0:1,1:3},
    (6,4):{0:1,1:3},
}
actual = {(i,j):c for i,row in enumerate(M) for j,c in enumerate(row) if c}
assert actual == expected, (actual,expected)

def rank(mat):
    a = [row[:] for row in mat]
    n = len(a); m = len(a[0]); r = 0
    for col in range(m):
        pivot = next((i for i in range(r,n) if a[i][col] % P), None)
        if pivot is None: continue
        a[r],a[pivot] = a[pivot],a[r]
        inverse = pow(a[r][col],-1,P)
        a[r] = [v*inverse % P for v in a[r]]
        for k in range(n):
            if k == r: continue
            t = a[k][col]
            a[k] = [(v-t*w)%P for v,w in zip(a[k],a[r])]
        r += 1
    return r

for lam in range(P):
    mat = [[sum(v*pow(lam,i,P) for i,v in c.items())%P for c in row] for row in M]
    if lam not in (0,1):
        assert rank(mat) == 4
    print('LAMBDA_F5',lam,'HASSE_RANK',rank(mat))
print('BASIS_POSITIVE_EXPONENTS',basis)
print('SIX_NONZERO_MATRIX_ENTRIES', sorted((i,j,sorted(v.items())) for (i,j),v in actual.items()))
print('FORMAL_PAIR_FACTORS: (1,8)=(L+1)(L-1)^2,L+1; (3,7)=L^2(L-2),L-2; (4,6)=3(L-3),3(L-3)')
print('ALL_SMOOTH_PARAMETERS: RANK_6_EXCEPT_L_IN_{-1,2,3}_RANK_4')
print('A_NUMBERS: GENERIC_4_SPECIAL_6; P_RANKS: GENERIC_6_SPECIAL_4')
print('VERIFY_OK')
