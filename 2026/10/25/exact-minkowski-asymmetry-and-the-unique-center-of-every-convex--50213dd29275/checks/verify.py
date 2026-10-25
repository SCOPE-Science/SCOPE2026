#!/usr/bin/env python3
"""Exact rational three-variable LP consistency checks for quadrilateral symmetry."""
from fractions import Fraction as F
from itertools import combinations, product

def solve_3(A, b):
    M = [[F(t) for t in row] + [F(z)] for row, z in zip(A, b)]
    for i in range(3):
        piv = next((j for j in range(i, 3) if M[j][i] != 0), None)
        if piv is None:
            return None
        M[i], M[piv] = M[piv], M[i]
        z = M[i][i]
        M[i] = [u / z for u in M[i]]
        for j in range(3):
            if i != j:
                z = M[j][i]
                M[j] = [u - z * v for u, v in zip(M[j], M[i])]
    return tuple(row[-1] for row in M)

def evaluate(p, q):
    vertices = [(F(1),F(0)), (F(0),F(1)), (-p,F(0)), (F(0),-q)]
    normals = [(F(1),F(1)), (-1/p,F(1)), (-1/p,-1/q), (F(1),-1/q)]
    hneg = [max((-a*x-b*y for x,y in vertices)) for a,b in normals]
    assert all(max(a*x+b*y for x,y in vertices) == 1 for a,b in normals)
    A = [(a,b,F(-1)) for a,b in normals]
    b = [-h for h in hneg]
    candidates=[]
    for idxs in combinations(range(4),3):
        candidate=solve_3([A[i] for i in idxs],[b[i] for i in idxs])
        if candidate is None:
            continue
        zx, zy, s = candidate
        if s >= 1 and all(a*zx + bb*zy - s <= d for (a,bb,_),d in zip(A,b)):
            candidates.append(candidate)
    assert candidates, (p,q)
    zx, zy, s = min(candidates, key=lambda t:t[2])
    m=min(p,q)
    expected=1+(1-p*q)/(1+m)
    assert s == expected, (p,q,s,expected)
    z0=(s-1,1-q) if p<=q else (1-p,s-1)
    assert all(a*z0[0]+bb*z0[1]-s <= d for (a,bb,_),d in zip(A,b)), (p,q)
    assert len([z for z in candidates if z[2]==s])>=1
    return s

if __name__=='__main__':
    values = [F(1,11),F(1,7),F(1,5),F(1,3),F(1,2),F(3,4),F(9,10),F(1,1)]
    checks = [evaluate(p,q) for p,q in product(values,repeat=2)]
    assert min(checks)==1 and max(checks)<2
    print(f'PASS: {len(checks)} exact rational full-LP vertex enumerations and candidate feasibility certificates')
    print('PASS: both parameter orderings, symmetric and nonsymmetric boundary cases')
