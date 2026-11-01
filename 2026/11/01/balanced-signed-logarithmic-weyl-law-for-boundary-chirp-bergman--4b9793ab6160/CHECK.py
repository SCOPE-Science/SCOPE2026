"""Finite checks of the beta moment, Tricomi reduction, and chirp asymptotics.

The assertions validate numerical and finite algebraic instances, not the
infinite-dimensional spectral theorem or the asymptotic error estimate.
"""
import math
import mpmath as mp

mp.mp.dps = 65
checks = 0


def require(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def exact_complex_moment(n, alpha, c):
    a = n + 1
    z = -1j * mp.mpf(str(c))
    return mp.exp(1j * c) * mp.gamma(a + alpha + 1) / mp.gamma(alpha + 1) * mp.hyperu(a, -alpha, z)


def leading_complex_moment(n, alpha, c):
    c = mp.mpf(str(c))
    alpha = mp.mpf(str(alpha))
    a = n + 1
    rho = alpha / 2 + mp.mpf('0.25')
    b = mp.sqrt(2*c)
    amplitude = mp.sqrt(mp.pi) * c**rho * a**rho * mp.exp(-b * mp.sqrt(a)) / mp.gamma(alpha+1)
    phase = b * mp.sqrt(a) + c/2 - mp.pi * rho/2
    return amplitude * mp.exp(1j * phase)


# Binomial expansion of the beta moment produces an independent exact finite
# exponential-integral representation for nonnegative integral alpha.
for alpha in (0, 1, 2):
    for c in (mp.mpf('0.7'), mp.mpf('1.3')):
        for n in range(0, 10):
            numer = mp.fsum((-1)**k * math.comb(n, k) * mp.expint(alpha+k+2, -1j*c) for k in range(n+1))
            beta = mp.beta(n+1, alpha+1)
            direct = numer / beta
            via_u = exact_complex_moment(n, alpha, c)
            require(abs(direct-via_u) <= mp.mpf('1e-45') * max(1, abs(via_u)),
                    f'moment identity n={n} alpha={alpha} c={c}')

# Large-a expansion: scaled relative errors stay bounded and shrink with n.
for alpha, c in ((-0.5, 0.8), (0, 1.0), (1, 1.3), (2, 0.6)):
    err = []
    for n in (30, 80, 180):
        exact = exact_complex_moment(n, alpha, c)
        leading = leading_complex_moment(n, alpha, c)
        relative = abs(exact/leading-1)
        require(relative < 6/mp.sqrt(n+1), f'leading chirp asymptotic n={n}, alpha={alpha}')
        err.append(relative)
    require(err[2] < err[0], f'decay of relative error alpha={alpha}')

# Real eigenvalues have the predicted sign well away from a phase crossing.
for theta in (0, 0.4, 2.1):
    for n in range(60, 116, 5):
        pred = mp.re(mp.exp(1j*theta)*leading_complex_moment(n, 0, 1.0))
        true = mp.re(mp.exp(1j*theta)*exact_complex_moment(n, 0, 1.0))
        amplitude = abs(leading_complex_moment(n, 0, 1.0))
        if abs(pred) > mp.mpf('0.65')*amplitude:
            require((pred > 0) == (true > 0), f'sign n={n} theta={theta}')

# This finite phase-distribution check illustrates the Weyl step only.
for c, theta in ((0.7, 0.0), (1.0, 0.2), (1.7, 1.3)):
    nmax = 300000
    b = math.sqrt(2*c)
    phi = c/2 - math.pi/8 + theta
    npos = sum(math.cos(b*math.sqrt(n+1)+phi) > 0 for n in range(nmax))
    require(abs(npos/nmax-0.5) < 0.025, f'finite phase fraction c={c}')

print(f'PASS: {checks} finite assertions (mpmath {mp.__version__}).')
