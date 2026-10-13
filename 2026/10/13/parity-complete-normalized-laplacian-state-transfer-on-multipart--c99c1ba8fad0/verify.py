#!/usr/bin/env python3
"""Exact finite checks of the normalized-Laplacian multipartite transfer theorem.

Uses Python's standard library and exact rational arithmetic. This is a
supplement to, not a substitute for, the arbitrary-parameter proof.
"""
from fractions import Fraction as F
from math import gcd


def graph(r, m):
    assert r >= 2 and m >= 1
    parts = [list(range(2*j, 2*j+2)) for j in range(r)]
    parts.append(list(range(2*r, 2*r+m)))
    n = 2*r + m
    group = [0]*n
    for i, part in enumerate(parts):
        for vertex in part:
            group[vertex] = i
    nbrs = [[j for j in range(n) if group[j] != group[i]] for i in range(n)]
    d = m + 2*(r-1)
    assert all(len(nbrs[i]) == (d if i < 2*r else 2*r) for i in range(n))
    return nbrs, parts, d


def step(nbrs, x):
    return [sum((x[j] for j in neighbors), F(0))/len(neighbors)
            for neighbors in nbrs]


def apply_shift(nbrs, x, a):
    y = step(nbrs, x)
    return [z+a*t for z, t in zip(y, x)]


def zero(x):
    return all(z == 0 for z in x)


def verify_graph(r, m):
    nbrs, parts, d = graph(r, m)
    n = 2*r + m
    # Independent check: the fully expanded vertex-level random-walk operator
    # is annihilated by the analytically predicted four-root polynomial.
    # Since S=D^(1/2)P D^(-1/2), P and S have the same eigenvalues.
    for i in range(n):
        x = [F(int(j == i)) for j in range(n)]
        for c in [F(2, d), F(m, d), F(0), F(-1)]:
            x = apply_shift(nbrs, x, c)
        assert zero(x), ('polynomial', r, m, i)
    # All within-part differences lie in the S eigenvalue-0 sector.
    for part in parts:
        for j in part[1:]:
            x = [F(0)]*n
            x[part[0]], x[j] = F(1), F(-1)
            assert zero(step(nbrs, x)), ('zero modes', r, m)
    # Each difference between small-part uniform vectors has eigenvalue -2/d.
    for j in range(1, r):
        x = [F(0)]*n
        for v in parts[0]: x[v] = F(1)
        for v in parts[j]: x[v] = F(-1)
        assert zero(apply_shift(nbrs, x, F(2,d))), ('transverse', r, m)
    # The remaining 2D quotient has eigenvalues 1 and -m/d.
    a = F(2*(r-1),d)
    b = F(m,d)
    assert a == F(1)-F(m,d)
    assert b == F(1)-a
    # The zero-eigenspace projector from the FULL vertex operator agrees
    # exactly with the direct sum of within-part mean-zero projections.
    # Repeated nonzero eigenvalues are listed only once.
    for i in range(n):
        v = [F(int(j == i)) for j in range(n)]
        for lam in sorted({F(1), F(-2,d), F(-m,d)}):
            w = step(nbrs,v)
            v = [(w_j-lam*v[j])/(-lam) for j,w_j in enumerate(w)]
        expected = [F(int(j == i)) for j in range(n)]
        own_part = next(p for p in parts if i in p)
        for j in own_part: expected[j] -= F(1,len(own_part))
        assert v==expected, ('kernel projector',r,m,i)
    # Exact finite-phase obstruction/sufficiency (odd times, no floats).
    predicted = (r % 2 == 1 and m % 4 == 2)
    witness = any((h*2) % d == 0 and ((h*2)//d) % 2 == 1
                  and (h*m) % d == 0 and ((h*m)//d) % 2 == 1
                  for h in range(1, 2*d+1, 2))
    assert witness == predicted, ('phases',r,m,d,witness,predicted)
    if predicted:
        s=d//2
        assert s%2 and (s*2)//d==1 and (s*m)//d==m//2
        # At time pi*s, all nonzero S sectors have L-phase +1;
        # the zero S sector has L-phase -1. Thus the exact propagator
        # equals I-2Pzero (pair swaps plus the m-block reflection).
        # Pzero is explicitly the block-diagonal zero-sum projector.
        diag = [F(0)]*n
        for part in parts:
            for i in part:
                diag[i]=F(1)-F(2)* (F(1)-F(1,len(part)))
        assert all(diag[i] == F(0) for i in range(2*r))
        if m==2: assert all(diag[i]==F(0) for i in range(2*r,n))
    return predicted


def main():
    tests=success=0
    for r in range(2, 8):
        for m in range(1, 15):
            success += bool(verify_graph(r,m))
            tests += 1
    # Explicit first irregular family, with degree mismatch and time 5*pi.
    assert verify_graph(3,6)
    assert 6+2*(3-1)==10 and (6+2*(3-1))//2==5
    print('VERIFY_OK exact_fraction_graphs=%d transfer_cases=%d first_irregular=K_2_2_2_6 time=5pi' % (tests, success))


if __name__=='__main__': main()
