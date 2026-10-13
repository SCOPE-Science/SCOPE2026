#!/usr/bin/env python3
import sympy as s

k,t=s.symbols('k t', integer=True, positive=True)
S=(k-1)*t

def ratio_coeff(m):
    return (m,
            m*(m*m-1)/s.Integer(6),
            m*(3*m**4-10*m*m+7)/s.Integer(360))

def log_coeff(y0,y2,y4):
    return s.simplify(y2/y0), s.simplify(y4/y0-y2*y2/(2*y0*y0))

A0,A2,A4=ratio_coeff(k-1)
B0,B2,B4=ratio_coeff(k)
C0=s.Integer(1)
C2=k*k/s.Integer(2)
C4=k**4/s.Integer(24)

L0=t*A0-2*C0
L2=t*A2-2*C2
L4=t*A4-2*C4
D0=(t+1)*A0-2*C0
D2=(t+1)*A2-2*C2
D4=(t+1)*A4-2*C4
l2,l4=log_coeff(L0,L2,L4)
b2,b4=log_coeff(B0,B2,B4)
d2,d4=log_coeff(D0,D2,D4)
c2=s.factor(l2+k*b2-k*d2)
c4=s.factor(l4+k*b4-k*d4)

Q=3*S**2+(7*k-11)*S-18*k+6
c2_expected=k*(k-1)*Q/(6*(S-2)*(S+k-3))
assert s.factor(c2-c2_expected)==0

P=s.factor(-180*(S-2)**2*(S+k-3)**2*c4/(k*(k-1)))
R=14*k**3*S-36*k**3-21*k**2*S+183*k**2-21*k*S+69*k+14*S-42
H=(45*k**4*t**2 + 57*k**4*t - 16*k**4
   -135*k**3*t**2 - 615*k**3*t - 118*k**3
   +180*k**2*t**2 + 540*k**2*t + 1272*k**2
   -135*k*t**2 - 195*k*t + 512*k
   +45*t**2 + 213*t + 218)
assert s.factor(27*P-8*(k+1)**2*R-Q*H)==0

q187=s.factor(Q.subs(t, s.Rational(18,7)/(k-1)))
r187=s.factor(R.subs(t, s.Rational(18,7)/(k-1)))
drds=s.factor(s.diff(R,t)/(k-1))
assert q187 == -s.Rational(120,49)
assert s.simplify(r187-3*(43*k*k+5*k-2))==0
assert s.simplify(drds-7*(k-2)*(k+1)*(2*k-1))==0

# At the critical positive root S=s*, Q=0. Check the coefficient formulas numerically.
for kval in range(2,41):
    Sstar=(11-7*kval+s.sqrt(49*kval*kval+62*kval+49))/6
    assert float(Sstar) > 18/7
    Rstar=s.N((14*kval**3*Sstar-36*kval**3-21*kval**2*Sstar+183*kval**2
               -21*kval*Sstar+69*kval+14*Sstar-42),50)
    assert Rstar > 0
    Astar=s.N(kval*(kval-1)**2*(6*Sstar+7*kval-11)/(6*(Sstar-2)*(Sstar+kval-3)),50)
    c4star=s.N(-2*kval*(kval-1)*(kval+1)**2*Rstar/(1215*(Sstar-2)**2*(Sstar+kval-3)**2),50)
    Cstar=s.N(-Astar/(2*c4star),50)
    assert Astar > 0 and c4star < 0 and Cstar > 0

print('VERIFY_OK symbolic=1 k_range=2..40')
