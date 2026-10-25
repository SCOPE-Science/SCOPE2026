"""Independent finite diagnostics for Gaussian support of enriched rooted-tree chain polytopes.
Run: python3 verify.py . This checker does not certify the infinite-depth theorems.
"""
import math
import random


def number_of_vertices(b, h):
    return (b ** (h + 1) - 1) // (b - 1)


def dynamic_antichain_value(g, b):
    n = len(g)
    dp = [0.0] * n
    for v in range(n - 1, -1, -1):
        children = range(b * v + 1, min(b * v + b + 1, n))
        dp[v] = max(abs(g[v]), sum(dp[u] for u in children))
    return dp[0]


def brute_antichain_value(g, b):
    n = len(g)
    masks = [0] * n
    for v in range(1, n):
        ancestor = (v - 1) // b
        masks[v] = masks[ancestor] | (1 << ancestor)
    weights = [abs(z) for z in g]
    best = 0.0
    for subset in range(1 << n):
        value = 0.0
        valid = True
        for v in range(n):
            if subset & (1 << v):
                if subset & masks[v]:
                    valid = False
                    break
                value += weights[v]
        if valid and value > best:
            best = value
    return best


def recurse_sample(b, h, rng):
    if h == 0:
        return abs(rng.gauss(0, 1))
    leaves_choice = sum(recurse_sample(b, h - 1, rng) for _ in range(b))
    return max(abs(rng.gauss(0, 1)), leaves_choice)


def run():
    rng = random.Random(271828)
    count = 0
    for b, h, rounds in [(2, 1, 80), (2, 2, 55), (2, 3, 8), (3, 2, 15)]:
        n = number_of_vertices(b, h)
        for _ in range(rounds):
            g = [rng.gauss(0, 1) for _ in range(n)]
            x = dynamic_antichain_value(g, b)
            y = brute_antichain_value(g, b)
            assert math.isclose(x, y, rel_tol=1e-12, abs_tol=1e-12), (b, h, x, y)
            count += 1
    mu = math.sqrt(2 / math.pi)
    Phi = lambda z: (1 + math.erf(z / math.sqrt(2))) / 2
    M = 2 * math.exp(0.5) * Phi(1)
    rho = 2 * math.exp(0.5) * Phi(-1)
    assert 0 < rho < 1 and M > 1
    samples = 12000
    diagnostics = []
    for b in (2, 3, 4):
        means = []
        for h in (1, 2, 3):
            avg = sum(recurse_sample(b, h, rng) for _ in range(samples)) / samples / b**h
            means.append(avg)
        tail = M * b**(-2) * rho**(b**3) / (b - 1)  # certified bound for c_b-c_{b,2}
        diagnostics.append((b, tuple(round(x, 5) for x in means), round(tail, 8)))
    assert mu < 1
    print('VERIFY_OK exact_antichain_checks=', count, 'sample_based_profiles=', diagnostics)
    print('Finite diagnostics only; symbolic proofs of asymptotics are in RESULT.md.')


if __name__ == '__main__':
    run()
