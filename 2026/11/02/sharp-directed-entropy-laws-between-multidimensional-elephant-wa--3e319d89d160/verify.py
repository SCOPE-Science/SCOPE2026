"""Deterministic finite-history checks for multidimensional elephant-walk path divergence.

Run: python3 verify.py
Only finite checks are performed here. Asymptotic statements follow from the proof.
"""
import itertools
import math
from collections import defaultdict
from fractions import Fraction

CHECKS = 0
D = 4
ALPHAS = [Fraction(-1, 4), Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]


def check(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


def q(alpha, counts, k):
    return tuple(Fraction(1, D) + alpha * (Fraction(c, k) - Fraction(1, D)) for c in counts)


def second_moment_of_counts(counts, k):
    return sum((Fraction(c, 1) - Fraction(k, D)) ** 2 for c in counts)


def second_moment_recurrence(alpha, kmax):
    s = Fraction(D - 1, D)
    moments = {1: s}
    for k in range(1, kmax):
        s = (1 + 2 * alpha / k) * s + Fraction(D - 1, D)
        moments[k + 1] = s
    return moments


def count_dp(alpha, kmax):
    probs = {}
    for e in range(D):
        arr = tuple(1 if i == e else 0 for i in range(D))
        probs[arr] = Fraction(1, D)
    for k in range(1, kmax + 1):
        check(sum(probs.values(), Fraction()) == 1, ('normalization', alpha, k))
        s = sum((v * second_moment_of_counts(z, k) for z, v in probs.items()), Fraction())
        check(s == second_moment_recurrence(alpha, kmax)[k], ('second moment', alpha, k))
        for counts, p in probs.items():
            qq = q(alpha, counts, k)
            check(sum(qq, Fraction()) == 1, ('q sum', alpha, counts))
            check(all(z > 0 for z in qq), ('q positive', alpha, counts))
        if k == kmax:
            return probs
        new = defaultdict(Fraction)
        for counts, weight in probs.items():
            for e, v in enumerate(q(alpha, counts, k)):
                cp = tuple(z + int(i == e) for i, z in enumerate(counts))
                new[cp] += weight * v
        probs = dict(new)


def divergence(q1, q2):
    return sum(float(x) * math.log(float(x) / float(y)) for x, y in zip(q1, q2))


def chain_kl(alpha, beta, n):
    probs = {}
    for e in range(D):
        arr = tuple(1 if i == e else 0 for i in range(D))
        probs[arr] = Fraction(1, D)
    cumulative = 0.0
    for k in range(1, n):
        new = defaultdict(Fraction)
        for z, weight in probs.items():
            qa, qb = q(alpha, z, k), q(beta, z, k)
            cumulative += float(weight) * divergence(qa, qb)
            for e, qe in enumerate(qa):
                zp = tuple(v + int(i == e) for i, v in enumerate(z))
                new[zp] += weight * qe
        probs = dict(new)
    return cumulative


def direct_kl(alpha, beta, n):
    total = 0.0
    for seq in itertools.product(range(D), repeat=n):
        pa = Fraction(1, D)
        pb = Fraction(1, D)
        counts = [0] * D
        counts[seq[0]] += 1
        for k in range(1, n):
            pa *= q(alpha, tuple(counts), k)[seq[k]]
            pb *= q(beta, tuple(counts), k)[seq[k]]
            counts[seq[k]] += 1
        total += float(pa) * math.log(float(pa) / float(pb))
    return total


def main():
    print('Multidimensional elephant-walk path-divergence finite verifier')
    for alpha in ALPHAS:
        count_dp(alpha, 9)
    for a, b in [(ALPHAS[0], ALPHAS[2]), (ALPHAS[2], ALPHAS[3]),
                 (ALPHAS[3], ALPHAS[4]), (ALPHAS[4], ALPHAS[0])]:
        for n in range(2, 7):
            lhs, rhs = chain_kl(a, b, n), direct_kl(a, b, n)
            check(math.isclose(lhs, rhs, rel_tol=2e-12, abs_tol=5e-13),
                  ('chain vs direct KL', a, b, n, lhs, rhs))
            check(lhs > 0, ('KL positive', a, b, n))
    for alpha in ALPHAS:
        s = second_moment_recurrence(alpha, 200)
        for k in range(1, 201):
            check(s[k] > 0, ('positive second moment', alpha, k))
            if alpha == Fraction(1, 2):
                h = sum((Fraction(1, j) for j in range(1, k + 1)), Fraction())
                check(s[k] == Fraction(D - 1, D) * k * h,
                      ('critical harmonic identity', k))
    for a, b in [(Fraction(-1, 4), Fraction(1, 2)),
                 (Fraction(1, 4), Fraction(3, 4)),
                 (Fraction(3, 4), Fraction(0))]:
        for k in [100, 300, 1000, 10000]:
            # Uniformity check: quadratic expansion in small empirical imbalance.
            delta = (Fraction(1, 1), Fraction(-1, 1), Fraction(0), Fraction(0))
            qa = tuple(Fraction(1, D) + a * v / k for v in delta)
            qb = tuple(Fraction(1, D) + b * v / k for v in delta)
            approx = D * float((a - b) ** 2) * sum(float(v*v) for v in delta) / (2*k*k)
            error = abs(divergence(qa, qb) - approx)
            check(error <= 50 / k**3, ('Taylor cubic bound', a, b, k, error))
    print(f'PASS: {CHECKS} deterministic assertions')
    print('Finite checks do not certify the n→infinity asymptotic conclusions.')


if __name__ == '__main__':
    main()
