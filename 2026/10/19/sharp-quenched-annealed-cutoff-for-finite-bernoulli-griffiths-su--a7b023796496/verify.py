"""Standalone checks for finite Bernoulli rare-region survival identities.

Run with: python verify.py
These finite checks corroborate, but do not substitute for, the proof.
"""
import itertools
import math
import random


def lengths(word):
    ans, count = [], 0
    for bit in word:
        if bit == 0:
            count += 1
        else:
            if count:
                ans.append(count)
            count = 0
    if count:
        ans.append(count)
    return ans


def survival(word, beta, reduced_time):
    n = len(word)
    return sum(m / n * math.exp(-reduced_time / m**beta)
               for m in lengths(word))


def exact_mean(n, p, beta, reduced_time):
    q = 1 - p
    inner = sum(
        (m / n) * (p*p*(n-m-1) + 2*p)*q**m
        * math.exp(-reduced_time/m**beta)
        for m in range(1, n)
    )
    return inner + q**n * math.exp(-reduced_time/n**beta)


def rates(p, beta, u):
    a = -math.log1p(-p)
    xi = 1.0/a
    yc = (beta*u/a)**(1/(beta+1))
    y = min(yc, xi)
    fa = a*yc + u/yc**beta
    fq = a*y + u/y**beta
    return fa, fq, xi**beta/beta


def run_checks():
    checks = 0
    # Full exact enumeration over every binary word, including endpoint runs.
    for n in range(2, 13):
        words = list(itertools.product((0, 1), repeat=n))
        for p, beta, reduced_time in [(0.2, 1.0, 0.2),
                                       (0.35, 3.0, 41.0),
                                       (0.75, 0.75, 5.0)]:
            expectation = 0.0
            for word in words:
                prob = math.prod((p if b else 1-p) for b in word)
                value = survival(word, beta, reduced_time)
                assert -1e-15 <= value <= 1+1e-15
                checks += 1
                expectation += prob*value
            assert abs(expectation - exact_mean(n, p, beta, reduced_time)) <= 3e-12
            checks += 1
        for p in (0.12, 0.35, 0.9):
            # At time zero the total weighted loss-free volume is the
            # fraction of loss-free sites, whose exact expectation is 1-p.
            assert abs(exact_mean(n, p, 1.5, 0) - (1-p)) < 2e-12
            checks += 1

    # Direct calculus identities for the saddle and cutoff branches.
    for p in (0.02, 0.2, 0.65):
        for beta in (0.5, 1.0, 2.0, 3.0):
            a = -math.log1p(-p)
            xi = 1/a
            uc = xi**beta/beta
            for ratio in (0.1, 0.5, 1.0, 1.5, 2.0, 10.0):
                u = ratio*uc
                fa, fq, critical = rates(p, beta, u)
                expected_fa = (beta+1)*(a**beta*u/beta**beta)**(1/(beta+1))
                expected_fq = expected_fa if u <= uc else 1+u/xi**beta
                assert math.isclose(critical, uc, rel_tol=1e-12)
                assert math.isclose(fa, expected_fa, rel_tol=1e-11)
                assert math.isclose(fq, expected_fq, rel_tol=1e-11)
                assert fq >= fa-1e-12
                if ratio > 1.0:
                    assert fq > fa+1e-9
                checks += 5

    # Deterministic, seeded finite samples, not a proof of convergence.
    rng = random.Random(7602026)
    for n in (100, 1000, 3000):
        word = tuple(rng.random()<0.18 for _ in range(n))
        for beta in (1.0, 3.0):
            for u in (0.3, 2.0, 6.0):
                reduced_time = u*math.log(n)**(beta+1)
                value = survival(word, beta, reduced_time)
                assert math.isfinite(value) and 0 <= value <= 1
                assert value <= survival(word, beta, 0)+1e-14
                checks += 2

    print(f"PASS: {checks} deterministic assertions and exact enumeration checks")


if __name__ == '__main__':
    run_checks()
