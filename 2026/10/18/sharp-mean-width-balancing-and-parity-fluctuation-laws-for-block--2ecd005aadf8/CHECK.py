"""Stand-alone arithmetic checks for Gaussian widths of block-parity polytopes.

This checker tests finite instances and asymptotic constants; universal statements
are established by the analytical arguments in RESULT.md, not by enumeration.
"""
import itertools
import math
import random


def gaussian_moment(m, order=1):
    # E[min(|G_1|,...,|G_m|)^order], by tail integration.
    assert order in (1, 2)
    n = 12000
    hi = 8.0
    dt = hi / n
    acc = 0.0
    for i in range(n + 1):
        t = dt * i
        q = math.erfc(t / math.sqrt(2.0))
        v = order * (t ** (order - 1)) * (q ** m)
        acc += (1 if i in (0, n) else (4 if i % 2 else 2)) * v
    return (dt / 3.0) * acc


def vertices(block_sizes):
    blocks = []
    for m in block_sizes:
        blocks.append([x for x in itertools.product((-1, 1), repeat=m)
                       if math.prod(x) == 1])
    return [sum(chunks, ()) for chunks in itertools.product(*blocks)]


def support_formula(block_sizes, direction):
    ans = 0
    i = 0
    for m in block_sizes:
        g = direction[i:i + m]
        i += m
        s = math.prod(1 if v > 0 else -1 for v in g)
        ans += sum(abs(v) for v in g)
        if s == -1:
            ans -= 2 * min(map(abs, g))
    return ans


def check():
    rng = random.Random(41729)
    profiles = [(3,), (4,), (5,), (6,), (3, 3), (3, 4), (4, 4),
                (3, 3, 3), (3, 6), (4, 5), (3, 4, 5)]
    trials = 0
    for profile in profiles:
        vec = vertices(profile)
        N = sum(profile)
        assert len(vec) == 2 ** (N - len(profile)), (profile, len(vec))
        assert all(sum(x[i] for x in vec) == 0 for i in range(N))
        assert all(sum(x[i]*x[j] for x in vec) == (len(vec) if i == j else 0)
                   for i in range(N) for j in range(N))
        for _ in range(16):
            g = [rng.choice((-5, -4, -3, -2, -1, 1, 2, 3, 4, 5))
                 for _ in range(N)]
            exact = max(sum(a*b for a, b in zip(v, g)) for v in vec)
            assert exact == support_formula(profile, g), (profile,g,exact)
            exact_negative = max(-sum(a*b for a, b in zip(v, g)) for v in vec)
            local_deficit = 2 * sum(map(abs,g)) - exact - exact_negative
            predicted = 0
            offset = 0
            for m in profile:
                h = g[offset:offset + m]
                offset += m
                H = math.prod(1 if a > 0 else -1 for a in h)
                small = min(map(abs, h))
                if m % 2:
                    predicted += 2 * small
                elif H == -1:
                    predicted += 4 * small
            assert local_deficit == predicted, (profile,g,local_deficit,predicted)
            trials += 1
    pm = {m: gaussian_moment(m) for m in range(2, 12)}
    assert all(pm[m-1] - 2*pm[m] + pm[m+1] > 0 for m in range(3, 11))
    assert all(pm[m] > pm[m+1] for m in range(2, 11))
    N = 9
    aN = math.sqrt(2)*math.gamma((N+1)/2)/math.gamma(N/2)
    def width(part):
        return 2 * (N*math.sqrt(2/math.pi)-sum(pm[m] for m in part)) / aN
    assert width((4,5)) > width((3,6))
    assert abs(width((4,5))-4.5944052212) < 2e-8
    assert abs(width((3,6))-4.5665987079) < 2e-8
    c = math.sqrt(2/math.pi)
    for m in (50, 100, 400, 1000):
        mu = gaussian_moment(m)
        m2 = gaussian_moment(m, 2)
        assert abs(m*mu - 1/c) < 4/m
        assert abs(m*m*(m2 - mu*mu) - 1/(c*c)) < 30/m
    print('PASS: {} exact support and directional-width tests; {} vertex covariance profiles; convexity, extremal width and asymptotic moments'.format(trials, len(profiles)))


if __name__ == '__main__':
    check()
