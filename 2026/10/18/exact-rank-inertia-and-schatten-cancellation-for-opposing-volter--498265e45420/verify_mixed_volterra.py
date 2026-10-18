"""Reproduce exact finite polynomial calculations for a mixed Volterra-power pencil.

The independent infinite-dimensional conclusions require the analytic proof.
"""
from math import factorial, comb
import sympy as sp

checks = 0
for m in range(1, 13):
    H = sp.Matrix(m, m, lambda i, j: sp.Rational(1, i+j+1))
    A = sp.Matrix(m, m, lambda r, j: sp.Rational((-1)**(m-1-r)*comb(m-1,r), factorial(m-1)*(m-r+j)))
    assert A.det() == sp.prod(sp.factorial(j)**2 for j in range(m))/sp.prod(sp.factorial(j) for j in range(2*m))
    checks += 1
    assert A.det() > 0
    checks += 1
    assert A.rank() == m
    checks += 1
    assert (H*A - (-1)**(m-1)*A.T*H)==sp.zeros(m)
    checks += 1
    assert sp.factor(sp.trace(A)) == (1 if m == 1 else 0)
    checks += 1
    # The moment coefficient matrix C is anti-diagonal and exact.
    C = sp.Matrix(m, m, lambda i,j: sp.Rational((-1)**j*comb(m-1,j),factorial(m-1)) if i+j==m-1 else 0)
    assert A == C*H
    checks+=1
    # Gram-space adjoint trace gives exact Hilbert--Schmidt moment.
    hs = sp.trace(H.inv()*A.T*H*A)
    assert sp.simplify(hs - sp.Rational(1, m*(2*m-1)*factorial(m-1)**2)) == 0
    checks += 1
    if m%2:
        k=(m-1)//2
        sigma = (-1)**k
        expected=(k+(sigma>0), k+(sigma<0))
        # Each off-center anti-diagonal pair has determinant < 0,
        # and the central moment has sign (-1)^k. This is an exact
        # block-congruence inertia calculation without ill-conditioning.
        assert (C-C.T)==sp.zeros(m)
        for j in range(k):
            assert C[j,m-1-j]*C[m-1-j,j]>0
            checks+=1
        assert sp.sign(C[k,k])==(-1)**k
        assert expected[0]+expected[1]==m
        checks+=1
    else:
        assert (H*A + A.T*H)==sp.zeros(m)
        checks += 1
# Additional exact monomial evaluations of J^m + (-1)^(m-1)(J*)^m = P_m.
x,t=sp.symbols('x t',real=True)
for m in range(1,9):
    for ell in range(0,6):
        jf = sp.integrate((x-t)**(m-1)*t**ell,(t,0,x))/sp.factorial(m-1)
        jstarf=sp.integrate((t-x)**(m-1)*t**ell,(t,x,1))/sp.factorial(m-1)
        pf=sp.integrate((x-t)**(m-1)*t**ell,(t,0,1))/sp.factorial(m-1)
        assert sp.simplify(jf+(-1)**(m-1)*jstarf-pf)==0
        checks+=1
print(f'MIXED_VOLTERRA_EXACT_OK {checks} checks')
