#!/usr/bin/env python3
"""Independent numerical checks for sticky-wall bound-time LDP.

Only standard-library modules are used. This is finite numerical evidence,
not a substitute for the proof of the infinite-time assertions.
"""
import math
import random
import statistics

ALPHA = 1.0
V = 1.0
X = 1.0
RESET = 1.0
GAMMA = 1.0
N_CHECK = 0


def check(cond, detail):
    global N_CHECK
    N_CHECK += 1
    if not cond:
        raise AssertionError(detail)


def h(s, sign):
    w = math.sqrt(s * (s + 2 * ALPHA))
    value = math.exp(-X * w / V)
    if sign == '+':
        value *= ALPHA / (s + ALPHA + w)
    return value


def hprime(s, sign):
    w = math.sqrt(s * (s + 2 * ALPHA))
    wp = (s + ALPHA) / w
    deriv = -X * wp / V
    if sign == '+':
        deriv -= (1 + wp) / (s + ALPHA + w)
    return h(s, sign) * deriv


def ph(s, sign):
    z = s + RESET
    f = h(z, sign)
    return z * f / (s + RESET * f)


def phprime(s, sign):
    z = s + RESET
    f = h(z, sign)
    fp = hprime(z, sign)
    n, d = z * f, s + RESET * f
    return ((f + z * fp) * d - n * (1 + RESET * fp)) / d**2


def pole(sign):
    low, high = 1e-12, RESET
    def fun(z):
        return RESET * (-math.expm1(math.log(h(z, sign)))) / z - 1
    assert fun(low) > 0 and fun(high) < 0
    for _ in range(80):
        mid = (low + high) / 2
        if fun(mid) > 0:
            low = mid
        else:
            high = mid
    z = (low + high) / 2
    q = RESET - z
    R = z * h(z, sign) / (1 + RESET * hprime(z, sign))
    return q, R


def sample_adsorption(sign, rng):
    x, d, elapsed = X, (-1 if sign == '-' else 1), 0.
    while True:
        dt = rng.expovariate(ALPHA + RESET)
        if d < 0 and x / V < dt:
            return elapsed + x / V
        elapsed += dt
        x += d * V * dt
        if rng.random() < RESET / (ALPHA + RESET):
            x, d = X, (-1 if sign == '-' else 1)
        else:
            d = -d


def main():
    rng = random.Random(20261027)
    all_results = {}
    for sign in ('-', '+'):
        q, R = pole(sign)
        eh = (1 - h(RESET, sign)) / (RESET * h(RESET, sign))
        occupancy = 1 / (1 + GAMMA * eh)
        check(q > 0 and q < RESET, 'unique physical pole range')
        check(R > 0, 'positive pole residue')
        check(abs(q - RESET * h(RESET - q, sign)) < 5e-14, 'adsorption survival root')
        check(abs(ph(0, sign) - 1) < 1e-13, 'Laplace normalization')
        check(abs(-phprime(0, sign) - eh) < 1e-12, 'mean from two independent identities')
        check(abs(1 / (1 - GAMMA * phprime(0, sign)) - occupancy) < 1e-12, 'mean occupation')

        for d in [1e-2, 1e-3, 1e-4]:
            check(abs(d * ph(-q+d, sign) / R-1) < 0.15, 'survival pole strength')
            check(phprime(-q+d, sign) < 0, 'negative Laplace derivative')
        for s in [0.0, 0.1, 0.3, 0.5, 1, 2, 4, 7, 10]:
            check(ph(s, sign) > 0 and ph(s, sign) <= 1.0000000000001, 'proper LT')
            check(phprime(s, sign) < 0, 'LT derivative')
            u = 1 / (1 - GAMMA * phprime(s, sign))
            check(0 < u < 1, 'tilted bound fraction')
            k = s + GAMMA * (1 - ph(s, sign))
            rate = k * u - s
            check(rate > -1e-12, 'nonnegative LDP')
            if s > 0:
                check(rate > 0, 'strict LDP off its minimum')

        for d in (1e-3, 1e-4, 1e-5):
            s = -q + d
            p = ph(s, sign)
            dp = phprime(s, sign)
            u = 1 / (1 - GAMMA * dp)
            k = s + GAMMA * (1 - p)
            I = k * u - s
            expected_coeff = 2 * math.sqrt(GAMMA * R)
            ratio = (q - I) / math.sqrt(u)
            check(abs(ratio / expected_coeff - 1) < 0.10, 'sqrt left-rate edge')

        # Compare exact positive-parameter Laplace transforms and means with
        # an independent, event-driven simulation without time discretization.
        samples = [sample_adsorption(sign, rng) for _ in range(60000)]
        mc_eh = statistics.mean(samples)
        check(abs(mc_eh / eh - 1) < 0.055, 'exact-event Monte Carlo MFPT')
        for s in (0.1, 0.3, 0.7, 1.3):
            emp = statistics.mean(math.exp(-s * t) for t in samples)
            check(abs(emp-ph(s, sign)) < 0.012, 'exact-event Monte Carlo Laplace transform')

        m = 0 if sign == '-' else 1
        C = math.exp(-(RESET + ALPHA) * X / V) * (1 if m == 0 else ALPHA / 2)
        tau = X / V
        for s in (8., 12., 16., 20., 30., 40.):
            f = ph(s, sign)
            check(abs(f / (C * s**(-m) * math.exp(-tau * s)) - 1) < 0.25,
                  'ballistic first-adsorption transform')
            eps = GAMMA * (-phprime(s, sign)) / (1 - GAMMA * phprime(s, sign))
            check(0 < eps < 1, 'stable complement occupation')
            # Evaluate gamma-I without cancellation.
            deficit = eps * (s + GAMMA) + (1-eps) * GAMMA * f
            L = math.log(1 / eps)
            predicted = eps / tau * (L - m * math.log(L))
            check(abs(deficit / predicted - 1) < 0.4,
                  'right-rate logarithmic / log-log asymptotic')
        all_results[sign] = {'survival_decay_q': q, 'residue_R': R,
                             'mean_bulk_excursion': eh, 'mean_bound_fraction': occupancy,
                             'MC_mean_bulk': mc_eh}

    for sign, values in all_results.items():
        print('orientation',sign,':', {k:round(v,10) for k,v in values.items()})
    print('PASSED', N_CHECK, 'checks; exact event-driven draws:', 120000)

if __name__ == '__main__':
    main()
