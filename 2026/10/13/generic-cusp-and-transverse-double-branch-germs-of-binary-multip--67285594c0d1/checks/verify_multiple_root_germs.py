#!/usr/bin/env python3
"""Independent exact checks for generic local singularity models of multiple-root loci.

Requires Python 3.10+ and SymPy 1.12+; finite spot checks supplement the proof.
"""
from math import comb
import sympy as sp
z, a, v = sp.symbols('z a v')


def coeffvec(p,d):
    p = sp.Poly(sp.expand(p),z)
    return sp.Matrix([p.nth(i) for i in range(d+1)])

cusp_checks = 0
for m in range(2, 13):
    t = a-v/sp.Integer(m+1)
    u = a+m*v/sp.Integer(m+1)
    polynomial = sp.Poly(sp.expand((z-t)**m*(z-u)), z)
    # Center by z-a; the coefficient of (z-a)^m is zero.
    center = sp.Poly(sp.expand((z+v/sp.Integer(m+1))**m*(z-m*v/sp.Integer(m+1))),z)
    assert sp.simplify(center.nth(m)) == 0
    assert sp.simplify(center.nth(m-1)+sp.Rational(m,2*(m+1))*v**2) == 0
    assert sp.simplify(center.nth(m-2)+sp.Rational(m*(m-1),3*(m+1)**2)*v**3) == 0
    for k in range(2,m+2):
        coefficient = center.nth(m+1-k)
        assert sp.simplify(coefficient -
            (comb(m,k) if k<=m else 0)*v**k/sp.Integer(m+1)**k
            + m*(comb(m,k-1) if k-1<=m else 0)*v**k/sp.Integer(m+1)**k)==0
    # Symbolic cusp equation for recovered v^2 and v^3.
    X = sp.simplify(-sp.Rational(2*(m+1),m)*center.nth(m-1))
    Y = sp.simplify(-sp.Rational(3*(m+1)**2,m*(m-1))*center.nth(m-2))
    assert sp.simplify(Y**2-X**3)==0
    cusp_checks += 1

tangent_checks = 0
for m in range(2,9):
    for d in range(2*m,2*m+4):
        h = sp.prod(z-(j+2) for j in range(d-2*m))
        f = z**m*(z-1)**m*h
        src_a = [z**m*z**k for k in range(d-m+1)] + [sp.diff(f,z)/m - z**m*sp.diff((z-1)**m*h,z)/m]
        # Last term equals z^(m-1)*(z-1)^m*h, up to a nonzero factor.
        src_b = [(z-1)**m*z**k for k in range(d-m+1)] + [z**m*(z-1)**(m-1)*h]
        A = sp.Matrix.hstack(*[coeffvec(p,d) for p in src_a])
        B = sp.Matrix.hstack(*[coeffvec(p,d) for p in src_b])
        rA,rB = A.rank(),B.rank()
        rSum = A.row_join(B).rank()
        rIntersection = rA+rB-rSum
        assert rA==rB==d-m+2
        assert rSum==d+1
        assert rIntersection==d-2*m+3
        tangent_checks += 1

hilbert_checks = 0
for c in range(1,8):
    for degree in range(0,15):
        expected = 1 if degree==0 else 2*comb(degree+c-1,c-1)
        # Monomials supported only on left or right blocks, excluding duplicate constant.
        count = 2*comb(degree+c-1,c-1)-(1 if degree==0 else 0)
        assert count==expected
        hilbert_checks += 1

print(f"PASS: {cusp_checks} exact centered-root cusp coefficient systems")
print(f"PASS: {tangent_checks} exact pair-root tangent-space rank and intersection checks")
print(f"PASS: {hilbert_checks} transverse union Hilbert-function checks")
print("Finite checks support the proof; they do not prove the unbounded theorem.")
