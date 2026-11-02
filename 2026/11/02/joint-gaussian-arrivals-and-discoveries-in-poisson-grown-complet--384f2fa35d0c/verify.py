"""Stand-alone exact and numerical checks for Poisson-born complete-graph discovery.

Requires Python >=3.10 and standard library. Optional numpy stress test is separate.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import isclose

checks = 0

def check(cond, explanation):
    global checks
    assert cond, explanation
    checks += 1


def full_event_distribution(m0, beta, lam, nsteps):
    # Tuple: current number of vertices, current walker location, visited mask.
    state = {(m0, 0, 1): Q(1)}
    for step in range(nsteps):
        out = defaultdict(Q)
        for (m, w, seen), mass in state.items():
            out[(m + 1, w, seen)] += mass * Q(beta, beta + lam)
            for target in range(m):
                if target != w:
                    out[(m, target, seen | (1 << target))] += mass * Q(lam, beta + lam) / (m - 1)
        state = out
    ans = defaultdict(Q)
    for (m, w, seen), mass in state.items():
        ans[(m, seen.bit_count())] += mass
    return dict(ans)


def compressed_event_distribution(m0, beta, lam, nsteps):
    state = {(m0, 1): Q(1)}
    for step in range(nsteps):
        out = defaultdict(Q)
        for (m, d), mass in state.items():
            out[(m + 1, d)] += mass * Q(beta, beta + lam)
            p = Q(m-d, m-1)
            out[(m, d + 1)] += mass * Q(lam, beta + lam) * p
            out[(m, d)] += mass * Q(lam, beta + lam) * (1-p)
        state = out
    return {k:v for k,v in state.items() if v}


for m0 in (3, 4):
    for beta, lam in ((1, 1), (2, 3), (5, 1)):
        for events in range(8):
            a = full_event_distribution(m0, beta, lam, events)
            b = compressed_event_distribution(m0, beta, lam, events)
            check(a == b, f'Exact lumping m0={m0} beta={beta} lambda={lam} events={events}')
            check(sum(a.values()) == 1, 'Detailed probabilities normalize')
            check(sum(b.values()) == 1, 'Compressed probabilities normalize')

for m0 in (3, 4, 5):
    for beta in range(1, 6):
        for lam in range(1, 6):
            alpha = Q(lam, beta + lam)
            k = Q(lam, beta)
            rate = Q(beta * lam, beta + lam)
            for m in range(m0, m0 + 8):
                for d in range(1, m + 1):
                    aa = m - 1
                    rr = Q(d - 1) - alpha * aa
                    # Embedded generator with birth rate beta and discovery rate lambda*(m-d)/(m-1).
                    discovery_rate = Q(lam * (m - d), m - 1)
                    l_r = beta * (-alpha) + discovery_rate * 1
                    check(l_r == -Q(lam, aa) * rr, 'Exact linear drift of imbalance')
                    l_r2 = beta * ((rr - alpha)**2-rr**2) + discovery_rate * ((rr+1)**2-rr**2)
                    qv = discovery_rate + alpha**2 * beta
                    check(l_r2 == -Q(2*lam, aa)*rr**2 + qv, 'Exact quadratic drift')
            integral = 1 - Q(2, 1)/(k+1) + Q(1, 1)/(2*k+1)
            var_from_kernels = rate / (2*k+1) + alpha**2 * beta * integral
            var_closed = beta*k*(k**2+1)/(k+1)**3
            cov_from_kernels = alpha*beta*(1-Q(1, 1)/(k+1))
            cov_closed = beta*k**2/(k+1)**2
            check(var_from_kernels == var_closed, 'Gaussian variance algebra')
            check(cov_from_kernels == cov_closed, 'Gaussian cross-covariance algebra')
            check(beta*var_closed-cov_closed**2 > 0, 'Positive-definite covariance')

print(f'PASS: {checks} exact rational checks')
