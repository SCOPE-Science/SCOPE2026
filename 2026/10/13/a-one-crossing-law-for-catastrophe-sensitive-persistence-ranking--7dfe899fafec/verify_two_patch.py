#!/usr/bin/env python3
"""Exact rational spot checks for the stated two-patch extinction-time identities.

This finite checker supplements the analytic proof; it does not certify a universal
identity on its own. It requires only Python 3 standard library.
"""
from fractions import Fraction as F
from itertools import product


def expected_closed(u, v, a, b, r):
    E, K, U, A = u + v, a + b, u * v, a * b
    N = r*r + (2*E+K)*r + E*E-U+E*K+A
    D = r*r*r + (2*E+K)*r*r + (E*E+U+E*K+A)*r + U*(E+K)
    assert D > 0
    return N / D, D


def expected_steps(u, v, a, b, r):
    # Solve first-step equations without invoking the closed coefficient formula.
    z10 = r + u + a
    z01 = r + v + b
    t11 = (1 + v/z10 + u/z01)/(r + u + v - v*a/z10-u*b/z01)
    t10 = (1+a*t11)/z10
    t01 = (1+b*t11)/z01
    assert (r+u+v)*t11 == 1 + v*t10 + u*t01
    assert z10*t10 == 1+a*t11
    assert z01*t01 == 1+b*t11
    return t11


def poly_add(p, q):
    return tuple((p[i] if i < len(p) else 0)+(q[i] if i < len(q) else 0)
                 for i in range(max(len(p),len(q))))


def poly_mul(p, q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            out[i+j]+=x*y
    return tuple(out)


def coeffs(E,K,U,A):
    return (E*E-U+E*K+A,2*E+K,F(1)), \
           (U*(E+K),E*E+U+E*K+A,2*E+K,F(1))


def check_comparison(u,v,a,b,uu,vv,aa,bb):
    E,K=u+v,a+b
    assert (uu+vv,aa+bb)==(E,K)
    U,A=u*v,a*b
    V,B=uu*vv,aa*bb
    N,D=coeffs(E,K,U,A)
    NN,DD=coeffs(E,K,V,B)
    # The coefficient polynomial for T_P - T_Q:
    lhs=poly_add(poly_mul(N,DD),tuple(-x for x in poly_mul(NN,D)))
    # -(E+K+2r)*[(U-V)(r+E)(r+E+K)+BU-AV]
    mid=(F((U-V)*E*(E+K)+B*U-A*V),F((U-V)*(2*E+K)),F(U-V))
    rhs=tuple(-x for x in poly_mul((E+K,F(2)),mid))
    assert tuple(lhs[:len(rhs)]) == rhs and all(x==0 for x in lhs[len(rhs):]), (lhs,rhs)


def main():
    trials=0
    vset=[F(1,5),F(1,2),F(1),F(3,2),F(2)]
    rset=[F(0),F(1,7),F(1),F(2),F(17)]
    # All 5^4 positive parameter combinations and multiple catastrophe rates.
    for u,v,a,b in product(vset,repeat=4):
        for r in rset:
            assert expected_steps(u,v,a,b,r)==expected_closed(u,v,a,b,r)[0]
            trials+=1
    comparisons=0
    for E,K in product((F(2),F(4),F(7)),repeat=2):
        for pu,pa,qu,qa in product((F(1,4),F(1,3),F(1,2)),repeat=4):
            u,v=E*pu,E*(1-pu)
            a,b=K*pa,K*(1-pa)
            uu,vv=E*qu,E*(1-qu)
            aa,bb=K*qa,K*(1-qa)
            check_comparison(u,v,a,b,uu,vv,aa,bb)
            comparisons+=1
    P=(F(1),F(1),F(2),F(2))
    Q=(F(4,5),F(6,5),F(1),F(3))
    for r in (F(0),F(1,10),F(1),F(2),F(99)):
        p,_=expected_closed(*P,r)
        q,_=expected_closed(*Q,r)
        expression=-F(2)*(r-1)*(r+9)/((r*r+5*r+2)*(25*r*r*r+200*r*r+399*r+144))
        assert p-q==expression
        assert (p>q if r<1 else p==q if r==1 else p<q)
    print(f'VERIFY_OK first_step_exact={trials} comparison_polynomials={comparisons} sharp_example=5')


if __name__=='__main__':
    main()
