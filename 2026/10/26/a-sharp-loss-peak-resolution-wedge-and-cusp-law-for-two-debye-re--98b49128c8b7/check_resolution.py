"""Independent algebraic and numerical checks of the two-Debye peak-resolution theorem.

Run: python check_resolution.py
Requires: Python 3, sympy, mpmath.
Analytic verification is in RESULT.md; numerical checks do not prove global assertions.
"""
import math
import sympy as S
import mpmath as mp

x,q=S.symbols('x q',positive=True)
P=3*q*x**2-(q+1)*x+3
J=(1-x)*(1+q*x)**2/(S.sqrt(q)*(q*x-1)*(1+x)**2)
check=S.factor(S.diff(J,x)/J+(q-1)*P/((1-x*x)*(q*q*x*x-1)))
assert check==0,check
assert S.factor(J*J.subs(x,1/(q*x))-1)==0
assert S.factor(S.discriminant(P,x))==q**2-34*q+1
Rcrit=3+2*S.sqrt(2)
qcrit=S.expand(Rcrit**2)
assert S.simplify(qcrit-(17+12*S.sqrt(2)))==0
assert S.simplify((qcrit+1)/(6*qcrit)-1/Rcrit)==0

# Exact global stationary-polynomial equation for two Debye terms.
rho,lam,y=S.symbols('rho lam y',positive=True)
loss=y/(1+y*y)+lam*rho*y/(1+rho*rho*y*y)
num=S.factor(S.together(S.diff(loss,y)).as_numer_denom()[0])
expect=(1-y*y)*(1+rho*rho*y*y)**2+lam*rho*(1-rho*rho*y*y)*(1+y*y)**2
assert S.expand(num-expect)==0

# The balanced-strength profile in centered log-frequency.
s,a,z=S.symbols('s a z',real=True)
profile=(S.sech(s-a)+S.sech(s+a))/2
closed=S.cosh(a)*S.cosh(s)/(S.cosh(s)**2+S.sinh(a)**2)
assert S.simplify(S.expand_trig(profile-closed).rewrite(S.exp))==0
critical_series=S.series(S.sqrt(2)*S.cosh(s)/(S.cosh(s)**2+1),s,0,6)
assert S.simplify(critical_series.removeO() - S.sqrt(2)*(S.Rational(1,2)-s**4/16))==0

mp.mp.dps=60
qc=mp.mpf(17)+12*mp.sqrt(2)
qm=mp.mpf(17)-12*mp.sqrt(2)
C=(qc-qm)**mp.mpf('1.5')/(108*qc*(qc-1))
for offset in (mp.mpf('0.1'),mp.mpf('0.01'),mp.mpf('0.001')):
    qq=qc+offset
    D=mp.sqrt(qq*qq-34*qq+1)
    xm=(qq+1-D)/(6*qq);xp=(qq+1+D)/(6*qq)
    JJ=lambda t:(1-t)*(1+qq*t)**2/(mp.sqrt(qq)*(qq*t-1)*(1+t)**2)
    lo,hi=JJ(xm),JJ(xp)
    assert 0<lo<1<hi and mp.almosteq(lo*hi,1,rel_eps=mp.mpf('1e-55'))
    ratio=mp.log(hi)/(offset**mp.mpf('1.5'))
    assert abs(ratio/C-1)<2*offset

# Direct stationary root counts using exact rational coefficients, no plotting heuristics.
for rr,ll,expected_roots in [(S.Integer(5),S.Integer(1),1),
                             (S.Integer(10),S.Integer(1),3),
                             (S.Integer(10),S.Rational(1,2),1),
                             (S.Integer(10),S.Integer(2),1),
                             (S.Integer(12),S.Rational(11,10),3)]:
    pol=S.Poly(expect.subs({rho:rr,lam:ll,y:S.sqrt(z)}).expand(),z)
    roots=S.polys.polytools.intervals(pol,eps=S.Rational(1,10**9))
    inside=[]
    for interval,mult in roots:
        lower,upper=interval
        if 0<lower and upper<S.Integer(1):
            inside.extend([interval]*mult)
    # Instead count all positive stationary squared frequencies.
    positive=[(a,b,m) for ((a,b),m) in roots if a>0]
    assert sum(m for a,b,m in positive)==expected_roots,(rr,ll,positive)

print('PASS: exact identities, quartic cusp, balanced profile, sample root counts, and cusp asymptotics.')
print('Critical ratio:',S.sstr(Rcrit),'critical squared ratio:',S.sstr(qcrit))
print('Cusp coefficient in q:',mp.nstr(C,22))
