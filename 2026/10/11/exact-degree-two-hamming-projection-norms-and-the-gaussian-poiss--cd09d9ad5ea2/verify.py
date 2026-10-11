#!/usr/bin/env python3
"""Exact rational checks for the degree-two Hamming projection boundary formula.

Independent row-kernel and binomial mass calculations for small parameters;
finite checks corroborate but do not replace the analytic proof.
"""
from fractions import Fraction
from math import comb, factorial, sqrt, exp, pi
from itertools import product


def value(n, q, d):
    s = (q - 1) * n - q * d
    return (s * s - (q - 2) * s - (q - 1) * n) // 2


def mass(n, q, d):
    if not 0 <= d <= n:
        return Fraction(0)
    return Fraction(comb(n, d) * (q - 1) ** d, q ** n)


def exact_norm(n, q):
    return sum((abs(value(n, q, d)) * mass(n, q, d) for d in range(n + 1)), Fraction(0))


def boundary_norm(n, q):
    bad = [d for d in range(n + 1) if value(n, q, d) < 0]
    assert bad and bad == list(range(bad[0], bad[-1] + 1))
    lo, hi = bad[0], bad[-1]
    m = lambda k: mass(n - 2, q, k)
    p = Fraction(q - 1, q)
    return 2 * comb(n, 2) * p * p * (m(lo-1) - m(lo-2) - m(hi) + m(hi-1))


def direct_row(n, q):
    base = (0,) * n
    acc = Fraction(0)
    for y in product(range(q), repeat=n):
        u = [q - 1 if y[i] == base[i] else -1 for i in range(n)]
        ker = sum(u[i] * u[j] for i in range(n) for j in range(i + 1, n))
        acc += Fraction(abs(ker), q**n)
    return acc


def poisson_profile(lam):
    from math import ceil
    probs = [exp(-lam)]
    for k in range(1, max(30, int(lam + 18*sqrt(lam) + 30))):
        probs.append(probs[-1] * lam / k)
    return sum(abs(k*(k-1)-2*lam*k+lam*lam)*p for k,p in enumerate(probs))/(2*lam)


def main():
    cases = 0
    for q in range(2, 18):
        for n in range(2, 74):
            assert exact_norm(n, q) == boundary_norm(n, q), (n, q)
            cases += 1
    explicit = 0
    for q in range(2, 7):
        for n in range(2, 6):
            if q ** n <= 10000:
                assert exact_norm(n, q) == direct_row(n, q), (n, q)
                explicit += 1
    from math import comb as C
    n, q = 10000, 4
    p= (q-1)/q
    # Stable float binomial recurrence about the mode.
    mode = int((n+1)*p)
    mass_mode = exp(__import__('math').lgamma(n+1)-__import__('math').lgamma(mode+1)-__import__('math').lgamma(n-mode+1)+mode*__import__('math').log(p)+(n-mode)*__import__('math').log(1-p))
    masses = [0.0] * (n+1)
    masses[mode] = mass_mode
    for k in range(mode, 0, -1): masses[k-1] = masses[k]*k/(n-k+1)*(1-p)/p
    for k in range(mode, n): masses[k+1] = masses[k]*(n-k)/(k+1)*p/(1-p)
    ratio = sum(abs(value(n,q,k))*masses[k] for k in range(n+1))/(n*(q-1))
    target = sqrt(2/(pi*exp(1)))
    assert abs(ratio - target) < .015
    for lam in [.05, .1, .33, .57]:
        assert abs(poisson_profile(lam) - lam*exp(-lam)*(2-lam)) < 1e-10
    # Sparse-alphabet normalization: Poisson crossover checked against
    # an independently accumulated Binomial(n, 1/q) match distribution.
    sparse = 0
    for lam in (0.2, 0.5, 0.8, 1.4):
        q_sparse = 1000
        n_sparse = int(lam * q_sparse)
        pm = 1 / q_sparse
        massj = (1-pm)**n_sparse
        total = 0.0
        for j in range(n_sparse+1):
            total += massj * abs(value(n_sparse, q_sparse, n_sparse-j))
            if j < n_sparse:
                massj *= (n_sparse-j)/(j+1) * pm/(1-pm)
        ratio_sparse = total/(n_sparse*(q_sparse-1))
        assert abs(ratio_sparse - poisson_profile(lam)) < 0.02, (lam, ratio_sparse)
        sparse += 1
    print(f'VERIFY_OK exact_parameters={cases} direct_rows={explicit} gaussian_n={n} gaussian_q={q} ratio={ratio:.12f} target={target:.12f} poisson_first_regime=4 sparse_crossover={sparse}')

if __name__ == '__main__':
    main()
