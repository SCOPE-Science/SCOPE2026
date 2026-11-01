"""Independent finite checks of the multipartite negative-type theorem.

Uses Python 3, sympy and numpy. Analytical proof is in RESULT.md.
Run: python checker.py
"""
from fractions import Fraction
from itertools import combinations_with_replacement
from math import log2
import numpy as np
import sympy as sp

R = sp.Symbol('R')

def polynomial(sizes):
    return sp.Poly(sp.expand(sum(
        sizes[i]*sp.prod(sizes[j]-R*(sizes[j]-1)
                         for j in range(len(sizes)) if j != i)
        for i in range(len(sizes)))), R)

def threshold(sizes):
    if max(sizes) == 1:
        return float('inf'), 0
    largest = max(sizes)
    k = sizes.count(largest)
    if k > 1:
        return largest / (largest - 1), k - 1
    ordered = sorted(sizes, reverse=True)
    q1 = 1.0 - 1.0/ordered[0]
    q2 = 1.0 - 1.0/ordered[1]
    lo = 1.0/q1
    hi = 1.0/q2 if q2 else max(100., lo * 2)
    def fun(r):
        return sum(1/(1-r*(1-1/n)) for n in sizes)
    if not q2:
        while fun(hi) < 0:
            hi *= 2
    # avoid endpoint division by zero
    lo = float(np.nextafter(lo, hi))
    hi = float(np.nextafter(hi, lo)) if q2 else hi
    for _ in range(100):
        mid = (lo + hi)/2
        if fun(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi)/2, 1

def compressed_matrix(sizes, rho):
    verts = [i for i,n in enumerate(sizes) for _ in range(n)]
    n = len(verts)
    d = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1,n):
            d[i,j] = d[j,i] = float(rho) if verts[i] == verts[j] else 1.
    basis = np.vstack((np.eye(n-1),-np.ones((1,n-1))))
    return basis.T @ (-d) @ basis

def verify_exact_quadratic(sizes, rho):
    n = sum(sizes)
    verts = [i for i,m in enumerate(sizes) for _ in range(m)]
    x = [Fraction((11*j*j + 3*j+7)%17-8,1) for j in range(n-1)]
    x.append(-sum(x))
    S = [sum(x[j] for j,g in enumerate(verts) if g==i) for i in range(len(sizes))]
    lhs = -sum(x[i]*x[j]*(rho if verts[i]==verts[j] else 1)
               for i in range(n) for j in range(n) if i!=j)
    rhs = rho*sum((x[j]-S[g]/sizes[g])**2 for j,g in enumerate(verts))
    rhs += sum((1-rho*Fraction(sizes[i]-1,sizes[i]))*S[i]**2
               for i in range(len(sizes)))
    assert lhs == rhs

assert sp.simplify(polynomial((3,2,1)).as_expr() - 2*(R**2 - 7*R + 9)) == 0
assert sp.simplify(polynomial((3,2,2)).as_expr() - (R-2)*(11*R-18)) == 0
assert sp.simplify(polynomial((3,3,3)).as_expr() - 9*(2*R-3)**2) == 0
assert sp.simplify(polynomial((3,1,1)).as_expr() - (9-4*R)) == 0
assert abs(threshold((3,2,1))[0]-(7-13**0.5)/2) < 1e-12
assert abs(threshold((3,2,2))[0]-18/11) < 1e-12
assert abs(threshold((3,1,1))[0]-9/4) < 1e-12
assert threshold((3,3,3)) == (1.5, 2)
assert threshold((1,1,1))[0] == float('inf')
checks = 9
for r in range(2,6):
    for sizes in combinations_with_replacement(range(1,6), r):
        if sum(sizes) > 16:
            continue
        ns = list(sizes)
        verify_exact_quadratic(ns, Fraction(7,5))
        verify_exact_quadratic(ns, Fraction(11,5))
        checks += 2
        t, nullity = threshold(ns)
        if np.isinf(t):
            for rho in (1.,3.,10.):
                eig = np.linalg.eigvalsh(compressed_matrix(ns, rho))
                assert eig[0] > 1e-8
                checks += 1
            continue
        for rho in (1.,1+(t-1)*0.35,1+(t-1)*0.8):
            eig = np.linalg.eigvalsh(compressed_matrix(ns, rho))
            assert eig[0] > 1e-7, (ns,t,rho,eig)
            checks += 1
        eig = np.linalg.eigvalsh(compressed_matrix(ns,t))
        assert sum(abs(z)<1e-7 for z in eig) == nullity, (ns,t,nullity,eig)
        assert eig[nullity]>1e-7, (ns,t,nullity,eig)
        checks += 2
        for rho in (t+min(0.2,t/10), t*1.5):
            eig = np.linalg.eigvalsh(compressed_matrix(ns,rho))
            assert eig[0] < -1e-7, (ns,t,rho,eig)
            checks += 1
print(f'PASS: {checks} exact-rational, symbolic and numerical assertions on finite part-size profiles.')
print('Limits: finite matrices and numerical eigenspectra are diagnostics, not the proof.')
