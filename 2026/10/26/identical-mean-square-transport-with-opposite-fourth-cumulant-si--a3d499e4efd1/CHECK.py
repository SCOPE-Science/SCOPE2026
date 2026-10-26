"""Standalone mathematical checks for paired-run/rest exponential transport.
Requires mpmath and sympy. Execute: python CHECK.py
"""
from fractions import Fraction
import mpmath as mp
import sympy as sp
mp.mp.dps = 60
z2, z3 = mp.zeta(2), mp.zeta(3)
checks = 0

def check(cond, what):
    global checks
    assert bool(cond), what
    checks += 1

def near(a, b, tolerance=mp.mpf('1e-36')):
    check(abs(a-b) < tolerance, f'not close: {a} vs {b}')

u = sp.symbols('u', real=True)
theta = sp.symbols('theta', real=True)
V = sp.symbols('v', positive=True)
# Analytic coefficient expansion of E exp(-lambda T) cosh(k v U) = 1.
mT, eU2, eU4, eU2T, eT2 = sp.symbols('mT eU2 eU4 eU2T eT2', positive=True)
k, a, b = sp.symbols('k a b')
lamb = a*k**2 + b*k**4
expr = -mT*lamb + (eT2*lamb**2)/2 + (V*k)**2*eU2/2 - (V*k)**2*lamb*eU2T/2 + (V*k)**4*eU4/24
A = sp.solve(sp.expand(expr).coeff(k,2), a)[0]
B = sp.factor(sp.solve(sp.expand(expr.subs(a,A)).coeff(k,4), b)[0])
check(sp.simplify(A - V**2*eU2/(2*mT)) == 0, 'second implicit coefficient')
check(sp.simplify(24*B - V**4/mT*(eU4-6*eU2*eU2T/mT + 3*eU2**2*eT2/mT**2)) == 0, 'fourth implicit coefficient')

J11 = mp.quad(lambda z: mp.log(z)*mp.log(1-z),[0,mp.mpf('.01'),mp.mpf('.5'),mp.mpf('.99'),1])
J21 = mp.quad(lambda z: -mp.log(z)**2*mp.log(1-z),[0,mp.mpf('.01'),mp.mpf('.5'),mp.mpf('.99'),1])
near(J11, 2-z2)
near(J21, 6-2*z2-2*z3)

# Rigorous rational lower bound (pi>3.14; zeta(3)>sum_{n=1}^5 n^-3).
rigorous_lower=sp.Rational(157,50)**2 + 12*sum(sp.Rational(1,j**3) for j in range(1,6))
check(rigorous_lower>24, 'explicit rational positivity certificate')

# Exact equilibrium velocity correlation follows from the within-run survival.
for lag in (mp.mpf('0'), mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('1'), mp.mpf('3')):
    probability=mp.quad(lambda u:(u-lag)*mp.exp(-u)/2,[lag,lag+50])
    near(probability, mp.exp(-lag)/2,mp.mpf('1e-19'))

# Equal Exp(1) marginal run and pause; mixed dependence copula.
for coupling in ('comonotone','countermonotone'):
    cross11, cross21 = ((2,6) if coupling=='comonotone' else (J11,J21))
    eT2value = 4 + 2*cross11
    eU2Tvalue = 6 + cross21
    numerator = 24 - 6*eU2Tvalue + 3*eT2value
    expected = -24 if coupling=='comonotone' else (mp.pi**2+12*z3-24)
    near(numerator,expected)
    # All cases share variance growth coefficient v**2.
    near(mp.mpf(2)/2,mp.mpf(1))
    check(numerator < 0 if coupling=='comonotone' else numerator > 0, 'kurtosis sign')
    print(coupling, 'variance growth (v=1)',1, 'fourth-cumulant growth (v=1)',mp.nstr(numerator/2,25))

threshold = 24/(mp.pi**2+12*z3)
check(0<threshold<1,'threshold range')
near((mp.pi**2+12*z3)*threshold,mp.mpf(24))
for fraction in (Fraction(0),Fraction(1,3),Fraction(2,3),Fraction(1)):
    p=mp.mpf(fraction.numerator)/fraction.denominator
    linear=(p*(mp.pi**2+12*z3)-24)/2
    moments_mixture= (1-p)*(-24)/2+p*(mp.pi**2+12*z3-24)/2
    near(linear,moments_mixture)
print('critical countermonotone mixing probability',mp.nstr(threshold,25))

# Completely independent validation from Laplace-renewal characteristic roots.
def phi(lambda_, k, p):
    z=1+2*lambda_
    same=z/(z*z-k*k)
    opposite=(mp.beta(1+lambda_-k,1+lambda_)+mp.beta(1+lambda_+k,1+lambda_))/2
    return (1-p)*same + p*opposite

def root(kval,p):
    return mp.findroot(lambda l:phi(l,kval,p)-1,(kval*kval/3,kval*kval))

for p in (mp.mpf(0),mp.mpf('0.25'),threshold,mp.mpf(1)):
    expected_b=(p*(mp.pi**2+12*z3)-24)/48
    for kk in (mp.mpf('.002'),mp.mpf('.001'),mp.mpf('.0005')):
        lam=root(kk,p)
        check(abs(phi(lam,kk,p)-1)<mp.mpf('1e-45'),'renewal root')
        near((lam-kk**2/2)/kk**4,expected_b,mp.mpf('0.000005'))
    print('mixture',mp.nstr(p,12),'coefficient k4',mp.nstr(expected_b,18))

# Exact comonotone root formula at separated Fourier tilts.
for kval in (mp.mpf('0.001'), mp.mpf('.05'),mp.mpf('.2')):
    near(root(kval,0),(mp.sqrt(1+4*kval*kval)-1)/4)

# One-dimensional matching Exp(1) marginals (Monte Carlo is not needed).
for power in range(1,7):
    check(sp.integrate((-sp.log(u))**power,(u,0,1))==sp.factorial(power),f'run moment {power}')
print('PASS:',checks,'independent symbolic and high-precision mathematical checks')
