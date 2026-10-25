"""Reproduce finite numerical checks for the randomized implicit RK2 scalar moment law.

Requires Python 3.10+ and mpmath (pip install mpmath).  This is a numerical
cross-check; the full all-parameter argument is analytical in RESULT.md.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 45
checks = 0

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def moment(p, s):
    p, s = mp.mpf(p), mp.mpf(s)
    lower = 1 - s
    upper = 1 / (1 + s)
    if lower < 0:
        return (mp.quad(lambda r: (-r)**p / (1-r)**2, [lower, 0])
                + mp.quad(lambda r: r**p / (1-r)**2, [0, upper]))
    return mp.quad(lambda r: r**p / (1-r)**2, [lower, upper])

def bisect_root(p):
    low = mp.sqrt(2)
    high = mp.mpf(3)
    while moment(p, high) < 1:
        high *= 2
    for _ in range(82):
        mid = (low + high) / 2
        if moment(p, mid) < 1:
            low = mid
        else:
            high = mid
    return (low + high) / 2

# Independent exact-rational stage elimination (two formulations).
for s_n in range(1, 12):
    s = Fraction(s_n, 4)
    for j in range(12):
        tau = Fraction(j, 11)
        old = Fraction(3, 7)
        stage = old / (1 + s*tau)
        semi = old - s*stage
        implicit = (1-s*(1-tau))*old/(1+s*tau)
        direct = old*(1-s/(1+s*tau))
        check(semi == implicit == direct, 'scheme multiplier mismatch')

# The push-forward density integrates to one, and gives the correct inverse CDF.
for s in [mp.mpf('.1'), mp.sqrt(2), mp.mpf('2'), mp.mpf('4'), mp.mpf('25')]:
    lo, hi = 1-s, 1/(1+s)
    check(abs((1/(1-hi)-1/(1-lo))-1) < mp.mpf('1e-38'), 'density normalization')
    for j in range(1, 10):
        t = mp.mpf(j) / 10
        r = 1-s/(1+s*t)
        check(abs((1/(1-r)-1/s)-t) < mp.mpf('1e-38'), 'inverse distribution')

# The single minimizer sqrt(2) is independent of moment order.
for p in [mp.mpf('.2'), mp.mpf('.5'), mp.mpf('1'), mp.mpf('2'), mp.mpf('4')]:
    m0 = moment(p, mp.sqrt(2))
    for s in [mp.mpf('.5'), mp.mpf('1'), mp.mpf('1.3'), mp.mpf('1.5'), mp.mpf('2.5')]:
        check(moment(p,s) > m0, 'moment-minimum comparison')
    for s in [mp.mpf('.8'),mp.mpf('1.2'),mp.mpf('1.6'),mp.mpf('3')]:
        eps = mp.mpf('1e-5')
        fd = (moment(p,s+eps)-moment(p,s-eps))/(2*eps)
        exact = (abs(1-s)**p-(1+s)**(-p))/s**2
        check(abs(fd-exact) < mp.mpf('1e-7'), 'derivative formula')

# Cross-check p=1 and p=2 exact source-compatible formulas.
for s in [mp.mpf('2'),mp.mpf('3'),mp.mpf('4.03'),mp.mpf('6.2'),mp.mpf('9')]:
    f2 = 1 + s*s/(1+s)-2*mp.log(1+s)
    check(abs(moment(2,s)-f2) < mp.mpf('1e-38'), 'p2 expression')
    f1 = -1+2/s+2*mp.log(s)-mp.log(1+s)
    check(abs(moment(1,s)-f1) < mp.mpf('1e-38'), 'p1 expression')

ps = [mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2'),mp.mpf('4'),mp.mpf('10'),mp.mpf('100')]
roots = [bisect_root(p) for p in ps]
for p,r in zip(ps,roots):
    check(abs(moment(p,r)-1) < mp.mpf('1e-22'), 'root moment equality')
    check(moment(p,r*mp.mpf('.99')) < 1, 'stability inside')
    check(moment(p,r*mp.mpf('1.01')) > 1, 'instability outside')
    check(r>2, 'root exceeds 2')
for a,b in zip(roots,roots[1:]):
    check(a>b, 'strict ordering by p')
check(abs(roots[1] - mp.mpf('6.2182622375974')) < mp.mpf('2e-13'), 'p1 threshold')
check(abs(roots[2] - mp.mpf('4.0336104693577')) < mp.mpf('2e-13'), 'p2 threshold')
check(abs(roots[-1] - (2+mp.log(400)/100)) < mp.mpf('.003'), 'large-p expansion')

# The p->0 limiting logarithmic second moment and the p<1 beta limit.
for p in [mp.mpf('.1'),mp.mpf('.3'),mp.mpf('.6')]:
    beta_limit = mp.pi*p/mp.sin(mp.pi*p)
    check(beta_limit>1, 'beta limit >1')

print('PASS', checks, 'independent exact/numerical checks')
print('p and critical s:')
for p,r in zip(ps,roots):
    print(mp.nstr(p,6), mp.nstr(r,19))
