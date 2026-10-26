#!/usr/bin/env python3
"""Exact universal Hasse-Witt determinantal verification for a quartic Artin-Schreier family.
No third-party packages: all polynomials have coefficients in F_7.
"""
from itertools import combinations, permutations
from math import comb
P = 7

def clean(z):
    return {k: v % P for k, v in z.items() if v % P}

def add(x, y):
    z = dict(x)
    for k, v in y.items(): z[k] = (z.get(k, 0) + v) % P
    return clean(z)

def mul(x, y):
    z = {}
    for u, a in x.items():
        for v, b in y.items():
            w = tuple(c + d for c, d in zip(u, v))
            z[w] = (z.get(w, 0) + a*b) % P
    return clean(z)

def scale(x, c):
    return clean({k: v*c for k, v in x.items()})

# Triple (x-degree, a-degree, b-degree).
f = {(4,0,0):1, (2,1,0):1, (1,0,1):1}
f_pow = [{(0,0,0):1}]
for j in range(4): f_pow.append(mul(f_pow[-1], f))
# Lexicographically sorted Boseck regular differential basis.
basis = [(i,j) for i in range(3) for j in range(5) if 7*i + 4*j <= 16]
assert len(basis) == 9
N = len(basis)
M = [[{} for j in range(N)] for i in range(N)]
for column,(i,j) in enumerate(basis):
    for ell in range(j+1):
        coeff = (-1)**(j-ell)*comb(j,ell)
        for (xd,ad,bd),val in f_pow[j-ell].items():
            xd += i
            if xd % 7 != 6: continue
            pair = ((xd-6)//7,ell)
            if pair not in basis: continue
            row = basis.index(pair)
            M[row][column] = add(M[row][column], {(ad,bd):coeff*val})
expected = {
    (0,2):{(1,0):2},
    (0,3):{(3,0):-1,(0,2):-3},
    (0,4):{(2,2):-1},
    (0,7):{(0,1):2},
    (1,3):{(1,0):-1},
    (1,4):{(3,0):3,(0,2):2},
    (2,4):{(1,0):-2},
    (5,4):{(0,1):-3},
}
assert all(M[i][j] == clean(expected.get((i,j),{}))
           for i in range(N) for j in range(N))

def determinant(rows, cols):
    n = len(rows)
    ans = {}
    for perm in permutations(range(n)):
        inversion = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        term = {(0,0): (-1)**inversion}
        for i,j in enumerate(perm):
            term = mul(term, M[rows[i]][cols[j]])
            if not term: break
        ans = add(ans, term)
    return ans

ideals = {
    1:((1,0),(0,1)),
    2:((2,0),(1,1),(0,2)),
    3:((3,0),(2,1),(1,2)),
}
for size, generators in ideals.items():
    found = set()
    num = 0
    for rows in combinations(range(N),size):
        for cols in combinations(range(N),size):
            det = determinant(rows,cols)
            if not det: continue
            num += 1
            assert all(any(exp[0]>=g[0] and exp[1]>=g[1] for g in generators)
                       for exp in det)
            if len(det)==1:
                exp, coeff = next(iter(det.items()))
                if exp in generators and coeff != 0: found.add(exp)
    assert found == set(generators), (size,found)
    print('I_%s generators = '%size, generators, 'nonzero minors =',num)
assert all(not determinant(rows,cols)
           for rows in combinations(range(N),4)
           for cols in combinations(range(N),4))

# Independent pointwise ranks for all 49 F_7-specializations, using elimination.
def rank_mod_7(matrix):
    mat = [list(row) for row in matrix]
    r=0
    for c in range(len(mat[0])):
        pivot=next((u for u in range(r,len(mat)) if mat[u][c]%7),None)
        if pivot is None: continue
        mat[r],mat[pivot]=mat[pivot],mat[r]
        fac=pow(mat[r][c]%7,-1,7)
        mat[r]=[(x*fac)%7 for x in mat[r]]
        for u in range(len(mat)):
            if u!=r and mat[u][c]%7:
                z=mat[u][c]
                mat[u]=[(mat[u][v]-z*mat[r][v])%7 for v in range(len(mat[0]))]
        r+=1
    return r
for av in range(7):
    for bv in range(7):
        mat = [[sum(c*pow(av,u,7)*pow(bv,v,7) for (u,v),c in M[i][j].items())%7
                for j in range(N)] for i in range(N)]
        want = 3 if av else (2 if bv else 0)
        assert rank_mod_7(mat)==want,(av,bv)
print('F7 parameter checks: 49/49, rank 3/2/0')
print('VERIFY_OK')
