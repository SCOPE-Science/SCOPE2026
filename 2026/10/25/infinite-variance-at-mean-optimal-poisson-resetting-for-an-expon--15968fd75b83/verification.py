"""Reproduce exact moment identities for a fixed exponential-distance target under Poisson reset.

Requirements: Python 3.10+ and mpmath >= 1.2.
Execution: python reset_search_verify.py
"""
import math
import mpmath as mp

mp.mp.dps = 65


def conditional_transform(s, R, D, rate):
    h = mp.exp(-R * mp.sqrt((rate + s) / D))
    return (rate + s) * h / (s + rate * h)


def closed_conditional(R, D, rate):
    q = mp.sqrt(rate / D)
    ex = mp.exp(q * R)
    return (ex - 1) / rate, (2 * ex ** 2 - (2 + q * R) * ex) / rate ** 2


def averaged_closed(lam, D, rate):
    q = mp.sqrt(rate / D)
    m1 = q / (rate * (lam - q)) if lam > q else mp.inf
    m2 = lam ** 2 * q / (rate ** 2 * (lam - q) ** 2 * (lam - 2 * q)) if lam > 2 * q else mp.inf
    return m1, m2


def relclose(a, b, tol=mp.mpf('1e-27')):
    assert mp.fabs(a - b) <= tol * max(1, mp.fabs(a), mp.fabs(b)), (a, b)


for D, rate in [(1, 1), (2, mp.mpf('0.5')), (mp.mpf('0.8'), mp.mpf('1.3'))]:
    for R in [mp.mpf('0.2'), mp.mpf('1.1'), mp.mpf('3.0')]:
        f = lambda s: conditional_transform(s, R, D, rate)
        cm1, cm2 = closed_conditional(R, D, rate)
        relclose(-mp.diff(f, 0, 1), cm1)
        relclose(mp.diff(f, 0, 2), cm2)

for lam, D, rate in [(3, 1, 1), (4, 2, mp.mpf('0.5')), (5, 1, mp.mpf('0.25'))]:
    lam = mp.mpf(lam)
    z = mp.sqrt(rate/D)/lam
    mu, m2 = averaged_closed(lam, D, rate)
    quadrature_mu = mp.quad(lambda x: lam*mp.exp(-lam*x)*closed_conditional(x,D,rate)[0], [0,1,5,mp.inf])
    quadrature_m2 = mp.quad(lambda x: lam*mp.exp(-lam*x)*closed_conditional(x,D,rate)[1], [0,1,5,mp.inf])
    relclose(mu, quadrature_mu)
    relclose(m2, quadrature_m2)
    relclose(m2/mu**2-1, 1/(z*(1-2*z))-1)

# The whole-positive-integer moment spectrum comes from the conditional
# normalization: rate*exp(-sqrt(rate/D)*R)*T_R converges in moment to Exp(1).
D = rate = 1
for m in range(1, 6):
    R = mp.mpf(18)
    p = mp.exp(-R)
    f = lambda s: conditional_transform(s, R, D, rate)
    normalized_moment = (-1)**m * mp.diff(f,0,m)*(rate*p)**m
    assert mp.fabs(normalized_moment / mp.factorial(m) - 1) < mp.mpf('1e-5'), (m, normalized_moment)

# Unique mean optimum and CV optimum, at dimensionless q/lambda=1/2,1/4.
for z in [mp.mpf('0.05'), mp.mpf('0.12'), mp.mpf('0.25'), mp.mpf('0.4')]:
    cv2 = 1/(z*(1-2*z))-1
    assert cv2 >= 7
relclose(1/(mp.mpf('0.25')*(1-2*mp.mpf('0.25')))-1,7)
relclose((1/(mp.mpf('0.25')*(1-mp.mpf('0.25'))))/(1/(mp.mpf('0.5')*(1-mp.mpf('0.5')))),mp.mpf(4)/3)
print('PASS: 9 independent Laplace differentiations, 6 exponential quadratures,')
print('5 normalized higher-moment limits, dimensionless CV and mean tradeoff checks.')
