"""Finite reproducibility checks for the stated analytic Gaussian Fock identities.
These checks do not replace the infinite-dimensional proof in RESULT.md.
"""
from math import sqrt, isclose
from sympy import symbols, simplify, Rational

s,t=symbols('s t', positive=True)
H=s*s-t*t
eta=t*(H-1)/s
b0=(H-1)/(2*s*(s+t))
assert simplify(1-2*b0-(1+eta)/H)==0
for ss,tt,rr in [(2.,1.,1.),(2.,1.,.90),(2.,1.,.82),(3.,1.,.90),(1.2,.2,1.)]:
    HH=ss*ss-tt*tt
    et=tt*(HH-1)/ss
    Q=1/(rr*rr*HH)
    P=-et*Q
    D=1/(rr*rr*sqrt(HH))
    assert Q-P<1
    A=1+P*P-Q*Q
    h=(A-sqrt(A*A-4*P*P))/(2*P)
    q=Q/(1-P*h)
    v0=D/sqrt(1-P*h)
    assert -1<h<0 and 0<q<1
    assert isclose((h-P)*(1-P*h),h*Q*Q,rel_tol=1e-10)
    assert isclose(v0/(1-q),D/sqrt((1-Q)**2-P*P),rel_tol=1e-10)
    c=P/(2*(1-P*h)*(q*q-1))
    assert isclose(c,-h/(2*(1-h*h)),rel_tol=1e-10)
ss,tt=2.,1.
rr=sqrt(2/3)
Q=1/(rr*rr*(ss*ss-tt*tt))
P=-Q
D=1/(rr*rr*sqrt(ss*ss-tt*tt))
assert isclose(Q,.5) and isclose(P,-.5)
assert isclose(D/sqrt(Q),1/rr)
print('All Gaussian coefficient, spectrum/trace, and endpoint identity checks passed.')
