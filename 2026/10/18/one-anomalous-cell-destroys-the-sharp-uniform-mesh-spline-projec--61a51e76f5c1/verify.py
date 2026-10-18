#!/usr/bin/env python3
"""Exact algebraic checks for a one-cell spline Gram defect; requires sympy."""
import sympy as S

s, t = S.symbols('s t')
r = 2 - s
c = s / 6
A = (s + 2*t)/((s+t)*(s+3*t))
B = t/((s+t)*(s+3*t))
D = c + r*r*(A-c)
F = lambda u,v:(u*u+v*v)/(u+v)
L0 = 2*s*(A+B)+3*t*F(A,B)
Lleft = 2*s*(D+B*r)+3*F(D,A*r)+3*t*r*F(A,B)
E0 = 3*t*(1-t*t)/((s+t)*(s+3*t)**2)
Eleft = (2*r/3)*(t*t-1)*(t+s/2)*(t*t+(5*s/3-1)*t+1) / ((t+s/3)**2*(t+s)*(t*t+(2+2*s/3)*t+s))

def identical_zero_in_quadratic_field(expr):
    """Numerator reduction modulo s*s-3, with rational-function t coefficients."""
    num=S.together(expr).as_numer_denom()[0]
    domain=S.QQ.frac_field(t)
    rem=S.Poly(num,s,domain=domain).rem(S.Poly(s*s-3,s,domain=domain))
    return rem.is_zero

checks={
    'row 0 junction source': (s+2*t)*A-t*B-1,
    'row 0 junction neighbor': (s+2*t)*B-t*A,
    'row -1 source': (4-r)*D-r*A-1,
    'row -1 neighbor': 2*(1+t)*r*A-D-t*r*B,
    'short-cell excess': L0-2-E0,
    'long-cell excess': Lleft-2-Eleft,
    'uniform a=c': A.subs(t,1)-c,
    'uniform b=cr': B.subs(t,1)-c*r,
    'uniform d=c': D.subs(t,1)-c,
}
for name,expr in checks.items():
    assert identical_zero_in_quadratic_field(expr),name

# Positive factors require only 0<r<1, s>0, 5s/3-1>0 and
# 2+2s/3>0, all immediate from s=sqrt(3).
assert 1<S.sqrt(3)<2
assert 5*S.sqrt(3)/3-1>0
for tau in [S.Rational(1,10),S.Rational(1,2),S.Rational(3,4),S.Rational(2),S.Rational(4),S.Rational(10)]:
    e0=S.N(E0.subs({s:S.sqrt(3),t:tau}),25)
    el=S.N(Eleft.subs({s:S.sqrt(3),t:tau}),25)
    assert (e0>0)==(tau<1)
    assert (el>0)==(tau>1)

# Independent finite-interval Gram-matrix checks: interior nodal row
# converges geometrically to the infinite-mesh witness formula.
for tau in [S.Rational(1,2),S.Rational(2),S.Rational(4)]:
    N=9
    nodes=list(range(-N,N+2))
    h=[tau if i==0 else S.Integer(1) for i in range(-N,N+1)]
    n=len(nodes)
    Q=S.zeros(n)
    for k,ell in enumerate(h):
        Q[k,k]+=2*ell
        Q[k+1,k+1]+=2*ell
        Q[k,k+1]=Q[k+1,k]=ell
    for target,ideal in [(0,L0),(-1,Lleft)]:
        k=nodes.index(target)
        sol=Q.inv()[:,k]
        # Q=6M. On each cell the nodal kernel has values 6*sol_i.
        exact=S.Integer(0)
        for j,ell in enumerate(h):
            u=abs(sol[j]);v=abs(sol[j+1]);
            exact+=3*ell*(u*u+v*v)/(u+v)
        exact=float(exact)
        limit=float(S.N(ideal.subs({s:S.sqrt(3),t:tau}),20))
        assert abs(exact-limit)<0.00005,(tau,target,exact,limit)
print('PASS: 9 exact algebraic identities, 12 sign checks, 6 finite-interval comparisons')
