"""Deterministic numerical checks for a polylogarithmic Dirichlet-mean inversion.

Run: python verify.py  (requires mpmath >= 1.3)
This verifies finite evaluations only; the universal claims have analytic proofs.
"""
import mpmath as mp
mp.mp.dps = 65


def H(k, z):
    w = 1 / z
    return (1 + mp.polylog(k-2, w) / mp.polylog(k-1, w)) / (2*z)


def density(k, x):
    if k == 2:
        q = mp.log((1-x)/x)
        return 1/(2*x*(1-x)*(q*q + mp.pi**2))
    z = mp.mpc(x, mp.mpf('1e-45'))
    return -mp.im(H(k, z))/mp.pi


def cond_positive(z):
    # Under the positive component, T=log((1-X)/X) has
    # Cauchy density 1/(T^2+pi^2).
    def f(t):
        x = 1/(1+mp.exp(t))
        return 1/(z-x)/(t*t + mp.pi**2)
    return mp.quad(f, [-mp.inf, -3, 0, 3, mp.inf])

checks = 0
for z in [mp.mpf('1.4'), mp.mpf('2.3'), mp.mpf('4.7')]:
    lhs = H(2, z)
    rhs = 1/(2*z) + cond_positive(z)/2
    assert abs(lhs-rhs) < mp.mpf('1e-52'), (z, lhs, rhs)
    checks += 1

for r in [1, 2, 3]:
    def integrand(t):
        x = 1/(1+mp.exp(t))
        return x**r/(2*(t*t+mp.pi**2))
    actual = mp.quad(integrand, [-mp.inf, -3, 0, 3, mp.inf])
    # Exact M_2 relation from product uniform moments.
    expected = [mp.mpf('1')/4, mp.mpf('5')/24, mp.mpf('3')/16][r-1]
    # Third moment from logarithmic derivative: S(y)=1+y/2+y²/3+y³/4 +...;
    # coefficient E[X^3] = (3/2)*(1/4-1/6+1/24)=3/16
    assert abs(actual-expected) < mp.mpf('1e-52'), (r, actual, expected)
    checks += 1

# Positive continuous densities on the interior, with universal left-end profile.
for k in range(2, 7):
    for x in ['0.00001', '0.01', '0.2', '0.5', '0.8', '0.99']:
        assert density(k, mp.mpf(x)) > 0, (k,x)
        checks += 1
    x=mp.mpf('1e-24')
    ratio=density(k,x) * 2*x*mp.log(1/x)**2/(k-1)
    assert abs(ratio-1)<mp.mpf('0.12'),(k,ratio)
    checks+=1

for k in range(3, 7):
    eps=mp.mpf('1e-8'); x=1-eps
    expected=mp.log(1/x)**(k-3)/(2*mp.factorial(k-3)*mp.zeta(k-1))
    ratio=density(k,x)/expected
    assert abs(ratio-1)<mp.mpf('0.004'),(k,ratio)
    checks+=1

print('PASS:',checks,'numerical checks; polylog transform, first moments, density positivity and endpoint asymptotics.')
