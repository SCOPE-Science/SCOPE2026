"""Exact arithmetic checks for the split degree-d surface line configuration.

The mathematical proof of exhaustive line classification uses the rank of
coordinate-pair projections and the Möbius-invariant concyclicity criterion;
this script independently checks the polynomial and lattice computations.
"""
import sympy as sp

s, t, a, b = sp.symbols('s t a b')

for d in (4, 5, 6):
    f = a**d + a
    g = b**d - 1
    F_on_line = sp.expand((a*s)**d + a*s*s**(d-1) + (b*t)**d - t**d)
    assert sp.expand(F_on_line - (s**d*f + t**d*g)) == 0
    # Both binary forms have d simple projective roots.
    assert sp.gcd(f, sp.diff(f, a)) == 1
    assert sp.gcd(g, sp.diff(g, b)) == 1
    assert sp.degree(f, a) == d and sp.degree(g, b) == d

    n = d*d
    G = sp.zeros(n)
    for i in range(d):
        for j in range(d):
            p = d*i + j
            for k in range(d):
                for l in range(d):
                    q = d*k + l
                    G[p, q] = (2-d if p == q else (1 if i == k or j == l else 0))
    # An explicit tensor-product eigenbasis, checked over the integers.
    ones = sp.ones(d, 1)
    basis = [ones] + [sp.eye(d)[:,i]-sp.eye(d)[:,d-1] for i in range(d-1)]
    for i, vi in enumerate(basis):
        for j, vj in enumerate(basis):
            v = sp.kronecker_product(vi, vj)
            ev = (d if i==0 and j==0 else (0 if i==0 or j==0 else -d))
            assert G*v == ev*v
    # Basis independence follows because the d vectors above form a basis.
    assert sp.det(sp.Matrix.hstack(*basis)) != 0
    expected = {d: 1, 0: 2*(d-1), -d: (d-1)**2}
    rank = (d-1)**2 + 1

    # The possible rational roots of the monic affine equations are 0,+1,-1.
    qa = [r for r in (sp.Integer(-1), sp.Integer(0), sp.Integer(1)) if f.subs(a,r)==0]
    qb = [r for r in (sp.Integer(-1), sp.Integer(1)) if g.subs(b,r)==0]
    assert len(qa)*len(qb) == (4 if d%2==0 else 1)
    print('d=',d,'lines=',n,'line_class_rank=',G.rank(),
          'rational_lines=',len(qa)*len(qb),'spectrum=',expected)
print('VERIFY_OK')
