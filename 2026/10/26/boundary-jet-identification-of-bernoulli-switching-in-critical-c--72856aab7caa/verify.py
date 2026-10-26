"""Exact checks for boundary-jet identification in a two-map cusp mixture.

Requires Python 3 and SymPy. The proof of density existence and infinite
asymptotics is analytical and is not replaced by these checks.
"""
import sympy as sp

z, K, theta = sp.symbols('z K theta', positive=True)
w = (1 - K / sp.sqrt(K**2 + theta*z)) / theta
series = sp.series(2*w, z, 0, 4).removeO().expand()
want = z/K**2 - 3*theta*z**2/(4*K**4) + 5*theta**2*z**3/(8*K**6)
assert sp.simplify(series - want) == 0
print('INVERSE_BRANCH_THIRD_ORDER_JET_PASS')

p, a0, a1, r0, r1 = sp.symbols('p a0 a1 r0 r1', real=True)
A = (1-p)*a0+p*a1
B = (1-p)*a0*r0+p*a1*r1
C = (1-p)*a0*r0**2+p*a1*r1**2
assert sp.factor(A*C-B**2 - p*(1-p)*a0*a1*(r1-r0)**2) == 0
T = B/A
reconstructed = a0*(T-r0)/(a0*(T-r0)+a1*(r1-T))
assert sp.factor(reconstructed-p) == 0
assert sp.factor(sp.diff(T,p) - a0*a1*(r1-r0)/A**2) == 0
print('MIXTURE_VARIANCE_AND_INVERSE_IDENTITIES_PASS')

th0,th1=sp.Rational(5,4),sp.Rational(7,4)
P=sp.Rational(1,3)
k2=lambda th:(2-th)**2/sp.Integer(8)
AA0=1/k2(th0); AA1=1/k2(th1)
RR0=th0/k2(th0); RR1=th1/k2(th1)
TT=sp.factor(T.subs({p:P,a0:AA0,a1:AA1,r0:RR0,r1:RR1}))
PP=sp.factor(reconstructed.subs({p:P,a0:AA0,a1:AA1,r0:RR0,r1:RR1}))
assert TT==sp.Rational(18464,99)
assert PP==P
DD=sp.factor((sp.Rational(45,8)*(A*C-B**2)).subs({p:P,a0:AA0,a1:AA1,r0:RR0,r1:RR1}))
assert DD==sp.Rational(70548193280,729)
print('RATIONAL_EXAMPLE_EXACTLY_RECONSTRUCTED',str(TT),str(PP))
print('THIRD_JET_DISCRIMINANT_POSITIVE_EXACT',str(DD))
print('DENSITY_EXISTENCE_AND_INFINITE_TIME_SCOPE_REQUIRE_ANALYTIC_PROOF')
