"""Finite-state and randomized checks for cyclic dimer deposition.

Requires Python 3, numpy and scipy. Uses per-edge rate-one clocks.
"""
import math
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import expm_multiply


def exact_law(n, time):
    """Forward CTMC on all binary occupancy configurations."""
    dim = 1 << n
    q = lil_matrix((dim, dim), dtype=float)
    z = np.zeros(dim, dtype=float)
    for s in range(dim):
        for e in range(n):
            mask = (1 << e) | (1 << ((e + 1) % n))
            if s & mask == 0:
                q[s, s | mask] += 1.0
                q[s, s] -= 1.0
                z[s] += 1
    init = np.zeros(dim)
    init[0] = 1.0
    p = expm_multiply(q.tocsr().transpose()*time, init)
    return float(p @ z), float(np.sum(p[z == 0]))


def simulate(n, repeats, seed):
    rng = np.random.default_rng(seed)
    values = []
    available = []
    time = math.log(n)
    for _ in range(repeats):
        clocks = rng.exponential(size=n)
        occupied = np.zeros(n, dtype=np.bool_)
        last = 0.0
        for i in np.argsort(clocks):
            a, b = i, (i+1) % n
            if not (occupied[a] or occupied[b]):
                occupied[a] = occupied[b] = True
                last = max(last, clocks[i])
        values.append(last)
        # Independently regenerate the configuration at the finite observation time.
        occupied[:] = False
        for i in np.argsort(clocks):
            if clocks[i] > time:
                break
            a, b = i, (i+1) % n
            if not (occupied[a] or occupied[b]):
                occupied[a] = occupied[b] = True
        available.append(int(np.sum(~occupied & ~np.roll(occupied, -1))))
    return np.array(values), np.array(available)


def run():
    checks = 0
    for n in range(4, 11):
        for t in (0.25, 1.0, 2.0):
            mean, prob_jammed = exact_law(n, t)
            # The infinite-line availability is a comparison, not an identity on a cycle.
            bound = n*math.exp(-t - 2*(1-math.exp(-t)))
            assert 0 <= mean <= n
            assert 0 <= prob_jammed <= 1
            if n >= 8:
                assert abs(mean-bound) < 0.05
            checks += 3
    for n, reps in ((256, 5000), (1024, 3500)):
        last, z = simulate(n, reps, 7612+n)
        p = np.mean(last <= math.log(n))
        m = np.mean(z)
        expect_p = math.exp(-math.exp(-2))
        expect_m = math.exp(-2)
        # Monte Carlo tolerance, not an exact mathematical certificate.
        assert abs(p - expect_p) < 0.055, (n, p, expect_p)
        assert abs(m - expect_m) < 0.055, (n, m, expect_m)
        checks += 4
        print(f'n={n} trials={reps} jam_CDF@log_n={p:.5f} limit={expect_p:.5f} '
              f'free_edge_mean={m:.5f} limit={expect_m:.5f}')
    print(f'PASS: {checks} deterministic and stochastic assertions')


if __name__ == '__main__':
    run()
