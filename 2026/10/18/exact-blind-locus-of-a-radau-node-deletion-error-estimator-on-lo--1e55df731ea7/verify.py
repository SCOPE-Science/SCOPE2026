"""Exact algebraic verification for the two-stage Radau IIA logistic test.

Requires Python 3 and SymPy; optionally uses mpmath for numerical samples.
Every universal assertion is proved in RESULT.md rather than inferred from sampling.
"""
import sympy as S
from mpmath import mp

checks = 0

def ok(condition, description):
    global checks
    assert condition, description
    checks += 1

s = S.symbols('s', real=True)
a = (1 - s)/2
h = 12*s/(4-s*s)
c = 3*s/4
q = S.Matrix([[S.Rational(5, 12), -S.Rational(1, 12)],
              [S.Rational(3, 4), S.Rational(1, 4)]])
U = S.Matrix([a+c/3, a+c])
f = lambda z: z*(1-z)
ok(S.simplify(U[0] - (2-s)/4) == 0, 'first stage')
ok(S.simplify(U[1] - (2+s)/4) == 0, 'second stage')
ok(S.simplify(f(U[0])-f(U[1])) == 0, 'logistic reflection')
for j in (0,1):
    ok(S.simplify(U[j]-a-h*(q*S.Matrix([f(U[0]),f(U[1])]))[j]) == 0,
       'Radau collocation equation')
ok(S.simplify(S.Rational(2,3)*a+S.Rational(1,3)*U[1]-U[0]) == 0,
   'deleted-node estimator')
ok(S.simplify(h*f(U[0])-c) == 0, 'collocation polynomial derivative')

# Exact low-dimensional uniqueness calculation for the nontrivial rational case.
x, y = S.symbols('x y')
a0, h0 = S.Rational(1,6), S.Rational(9,4)
eq1 = S.factor(16*(x-a0-h0*(S.Rational(5,12)*f(x)-S.Rational(1,12)*f(y))))
eq2 = S.factor(16*(y-a0-h0*(S.Rational(3,4)*f(x)+S.Rational(1,4)*f(y))))
res = S.factor(S.resultant(eq1,eq2,y))
ok(S.factor(res/(192*(3*x-1)*(81*x**3-27*x**2-26*x-8))) == 1,
   'resultant factorization')
ok(81*(S.Rational(77,192))**2 < 26, 'root exclusion for positive stages')
ok(S.simplify(eq1.subs({x:S.Rational(1,3), y:S.Rational(2,3)})) == 0,
   'rational witness first equation')
ok(S.simplify(eq2.subs({x:S.Rational(1,3), y:S.Rational(2,3)})) == 0,
   'rational witness second equation')

# Coefficient positivity proof starts at j=2: 2*4^j > 3*(2*j+1).
for j in range(2,21):
    ok(2*4**j > 3*(2*j+1), 'Taylor-coefficient dominance')

mp.dps = 70
for k in range(1,50):
    ss = mp.mpf(k)/50
    aa=(1-ss)/2
    hh=12*ss/(4-ss**2)
    bb=(2+ss)/4
    true=aa*mp.exp(hh)/(1-aa+aa*mp.exp(hh))
    H=mp.log(bb/(1-bb)*(1-aa)/aa)
    ok(H>hh and bb>true, 'positive endpoint error')
    ok(abs(hh*(4-ss**2)-12*ss) < mp.mpf('1e-60'), 'exact step formula')

smp = mp.mpf(1)/mp.mpf(2)  # initial value a=1/4
check_a=(1-smp)/2
check_h=12*smp/(4-smp**2)
check_b=(2+smp)/4
ok(check_a == mp.mpf(1)/4 and check_h == mp.mpf(8)/5
   and check_b == mp.mpf(5)/8, 'additional rational case')

print('PASS:', checks, 'checks; exact Radau algebra and polynomial root exclusion; high-precision samples')
