#!/usr/bin/env python3
import math

P = 0.6
MU = 0.5
C = 0.9
PRIOR_MEAN = 0.3

LO = MU * (1.0 - C)
HI = MU + C * (1.0 - MU)


def bernoulli_kl(p, q):
    return p * math.log(p / q) + (1.0 - p) * math.log((1.0 - p) / (1.0 - q))


def binom_pmf(n, k, p):
    return math.exp(
        math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
        + k * math.log(p) + (n - k) * math.log(1.0 - p)
    )


def expected_regret(n, kappa):
    total = 0.0
    mass = 0.0
    for k in range(n + 1):
        w = binom_pmf(n, k, P)
        q = (k + kappa * PRIOR_MEAN) / (n + kappa)
        q = min(HI, max(LO, q))
        total += w * bernoulli_kl(P, q)
        mass += w
    if abs(mass - 1.0) > 2e-11:
        raise AssertionError((n, kappa, mass))
    return total


def main():
    # Interior oracle: q=P corresponds to lambda=(P-MU)/(MU*(1-MU)).
    lam_star = (P - MU) / (MU * (1.0 - MU))
    left = -C / (1.0 - MU)
    right = C / MU
    assert left < lam_star < right

    # Exact score variance = negative curvature for Bernoulli P.
    vals = []
    for x, prob in [(0.0, 1.0 - P), (1.0, P)]:
        h = (x - MU) / (1.0 + lam_star * (x - MU))
        vals.append((h, prob))
    mean_h = sum(h * prob for h, prob in vals)
    j = sum(h * h * prob for h, prob in vals)
    assert abs(mean_h) < 1e-14
    assert j > 0.0

    ns = [200, 1000, 5000]
    final = {}
    for kappa in [0.0, 2.0, 10.0]:
        seq = []
        for n in ns:
            scaled = n * expected_regret(n, kappa)
            seq.append((n, scaled))
        final[kappa] = seq
        if abs(seq[-1][1] - 0.5) >= 0.01:
            raise AssertionError((kappa, seq[-1]))

    print('lambda_star', format(lam_star, '.12f'))
    print('J', format(j, '.12f'))
    for kappa, seq in final.items():
        print('kappa', format(kappa, '.1f'), ' '.join(f'n={n}:nR={v:.12f}' for n, v in seq))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
