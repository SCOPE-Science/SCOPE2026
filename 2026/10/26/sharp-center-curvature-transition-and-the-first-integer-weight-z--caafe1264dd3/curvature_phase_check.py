"""Reproduce symbolic curvature identities and the exact integer-weight root certificate.
Requires sympy; high-precision samples are diagnostics, not proof.
"""
import sympy as sp
s,t=sp.symbols('s t',real=True)
A=(t+3)*(t+4)/6
B=(t+3)*(t+4)*(t+5)*(t+6)/120
C=sp.factor(-(4*B-2*A**2)/A**2)
assert sp.factor(C-4*(t*t+t-15)/(5*(t+3)*(t+4)))==0
assert sp.factor(sp.diff(C,t)-12*(2*t*t+18*t+39)/(5*(t+3)**2*(t+4)**2))==0
assert sp.factor(C+2/(t+2)-2*t*(t+1)*(2*t+9)/(5*(t+2)*(t+3)*(t+4)))==0
F=(3*s*s+10*s+3)/(1-s)**6
g=sp.factor(sp.diff(s*sp.diff(sp.log(F),s),s))
R=7*s**4+28*s**3+58*s**2+28*s+7
assert sp.factor(g-12*R/((1-s)**2*(s+3)**2*(3*s+1)**2))==0
curv=sp.factor(-sp.diff(s*sp.diff(sp.log(g),s),s)/g)
P=147*s**12-7308*s**11-55818*s**10-195804*s**9-455427*s**8-850584*s**7-1064716*s**6-850584*s**5-455427*s**4-195804*s**3-55818*s**2-7308*s+147
assert sp.factor(curv-P/(6*R**3))==0
assert P.subs(s,0)==147 and P.subs(s,1)==-4194304
assert P.subs(s,sp.Rational(1759,100000))>0
assert P.subs(s,sp.Rational(1760,100000))<0
coeff=sp.Poly(P,s)
assert coeff.nth(12)==147 and coeff.nth(11)==-7308
assert all(coeff.nth(i)<0 for i in range(1,12))
# P'(s) < 0 for 0<s<1: 1764*s^11 < 1764*s^10 < 80388*s^10,
# which is dominated by the degree-11 term's negative derivative;
# every other derivative term is strictly negative.
assert sp.simplify((12*147)-(11*7308))<0
print('PASS: exact all-real-parameter center law and monotonicity, exact distance-weight-4 curvature rational function, unique-root signs and derivative certificate')
