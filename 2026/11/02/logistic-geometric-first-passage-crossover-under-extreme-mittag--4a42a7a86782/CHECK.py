#!/usr/bin/env python3
"""Numerical checks of logarithmic-rate and spectral first-passage formulas.

No simulation or finite computation is used as proof of the limiting law.
Requires only Python 3 standard library. Run: python3 CHECK.py
"""
import math


def sigmoid_survival(kappa):
    """Limit of P(rate below the log threshold): q=1/(1+exp(-kappa))."""
    return 1.0 / (1.0 + math.exp(-kappa))


def midpoint_integral(f, a, b, n=24000):
    h = (b - a) / n
    return sum(f(a + (k + 0.5) * h) for k in range(n)) * h


def log_rate_tail(alpha, z):
    """P(alpha*log(rate)>z), source Mittag-Leffler integral representation."""
    ez = math.exp(z)
    coeff = math.sin(math.pi * alpha) / (math.pi * alpha) * ez
    c = math.cos(math.pi * alpha)
    def integrand(r):
        # r is always positive under midpoint integration.
        return math.exp(-r ** (1.0 / alpha)) / (r*r + 2.0*r*ez*c + ez*ez)
    return coeff * midpoint_integral(integrand, 0.0, 5.0, 24000)


def spectral_survival(alpha, x0, tau, periods, nodes=30000):
    """Exact survival at t=periods*tau via the spectral identity.

    Continuous-time simple symmetric walk with half-line absorption,
    Poisson jumps of total intensity rate, iid Mittag-Leffler rates
    drawn at every multiple of tau.
    """
    assert isinstance(x0, int) and x0 >= 1 and periods >= 0
    step = 1.0 / nodes
    total = 0.0
    for j in range(nodes):
        p = (j + .5) * step
        theta = math.pi * p
        kernel = math.sin(x0 * theta) / math.tan(theta / 2.0)
        s = tau * (1.0 - math.cos(theta))
        total += kernel / (1.0 + s**alpha)**periods
    return total * step


def main():
    assertions = 0
    def check(cond, msg):
        nonlocal assertions
        assertions += 1
        if not cond:
            raise AssertionError(msg)

    for x0 in (1, 2, 3, 5, 10, 20):
        value = spectral_survival(.3, x0, 1.0, 0)
        check(abs(value-1) < 1.0e-7, ('spectral normalization', x0, value))

    for alpha in (.2, .1, .05):
        for z in (-.7, .0, .7):
            t = log_rate_tail(alpha, z)
            check(0 < t < 1, ('tail range', alpha, z, t))
            print('log-rate-tail', f'alpha={alpha:.3f}', f'z={z:.2f}', f'P={t:.9f}',
                  f'logistic={1-sigmoid_survival(z):.9f}')
        # The exact distribution approaches the logistic law when alpha -> 0.
        check(abs(log_rate_tail(alpha, .7) - (1-sigmoid_survival(.7))) < .12,
              ('log-rate convergence', alpha))

    kap = .64
    q = sigmoid_survival(kap)
    prev_err = [math.inf, math.inf, math.inf]
    print('kappa', kap, 'geometric survival q', f'{q:.9f}')
    for alpha in (.24, .18, .14, .10, .08):
        x0 = int(math.floor(math.exp(kap/(2*alpha))+.5))
        vals = [spectral_survival(alpha, x0, 1.0, m) for m in (1,2,3)]
        print('spectral', f'alpha={alpha:.3f}', 'x0='+str(x0),
              ' '.join(f'P(T>{m}tau)={v:.9f}' for m,v in zip((1,2,3),vals)))
        check(1.0 > vals[0] > vals[1] > vals[2] > 0, ('ordered survival', alpha))
        for i,m in enumerate((1,2,3)):
            error=abs(vals[i]-q**m)
            check(error < prev_err[i]+.006, ('convergence trend', alpha,i,error,prev_err[i]))
            prev_err[i]=error
    check(max(prev_err)<.06, ('small alpha spectral proximity', prev_err))

    # Opposite side of the crossover: x0 fixed, tau grows exponentially.
    kap = -.64
    q = sigmoid_survival(kap)
    tau=math.exp(-kap/.08)
    vals=[spectral_survival(.08,1,tau,m) for m in (1,2,3)]
    print('opposite-side', f'kappa={kap}', f'tau={tau:.3f}', vals,
          'limit', [q**m for m in (1,2,3)])
    check(all(abs(v-q**m) < .09 for m,v in zip((1,2,3),vals)),
          ('opposite crossover', vals, q))

    print('PASS',assertions,'checks')


if __name__ == '__main__':
    main()
