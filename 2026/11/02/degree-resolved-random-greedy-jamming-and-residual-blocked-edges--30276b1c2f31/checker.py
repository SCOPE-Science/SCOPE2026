"""Exact, independent finite checks for degree-resolved random-greedy adsorption on Cayley trees.

Run with Python 3 using only the standard library. All comparisons are rational.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, permutations
from math import factorial


def prufer_edges(seq, n):
    deg = [1] * n
    for v in seq:
        deg[v] += 1
    edges = []
    for v in seq:
        u = next(j for j in range(n) if deg[j] == 1)
        edges.append((u, v))
        deg[u] -= 1
        deg[v] -= 1
    u, v = (j for j in range(n) if deg[j] == 1)
    edges.append((u, v))
    return edges


def exact_root_occupancy(edges, n):
    neighbor = [0] * n
    for u, v in edges:
        neighbor[u] |= 1 << v
        neighbor[v] |= 1 << u
    full = (1 << n) - 1

    @lru_cache(None)
    def recurse(mask):
        if not (mask & 1):
            return F(0)
        count = mask.bit_count()
        ans = F(0)
        for v in range(n):
            if not (mask >> v) & 1:
                continue
            if v == 0:
                ans += F(1)
            elif not (neighbor[v] & 1):
                remaining = mask & ~(1 << v) & ~neighbor[v]
                ans += recurse(remaining)
        return ans / count

    return neighbor[0].bit_count(), recurse(full)


def add(x, y):
    z = x.copy()
    for monomial, coefficient in y.items():
        z[monomial] = z.get(monomial, F(0)) + coefficient
    return {k: v for k, v in z.items() if v}


def multiply(x, y, cutoff):
    out = {}
    for (i, j), a in x.items():
        for (k, ell), b in y.items():
            if i + k > cutoff:
                continue
            key = (i + k, j + ell)
            out[key] = out.get(key, F(0)) + a * b
    return {k: v for k, v in out.items() if v}


def scalar(x, a):
    return {k: a * v for k, v in x.items() if a * v}


def theoretical_mass(n):
    cutoff = n - 1
    T = {(k, 0): F(k ** (k - 1), factorial(k)) for k in range(1, cutoff + 1)}
    S = T.copy()
    power = {(0, 0): F(1)}
    for k in range(1, cutoff + 1):
        power = multiply(power, T, cutoff)
        shifted = {(i, j + k): a for (i, j), a in power.items()}
        S = add(S, scalar(shifted, F((-1) ** k, k)))
    masses = []
    power = {(0, 0): F(1)}
    scale = F(factorial(n), n ** (n - 1))
    for d in range(n):
        if d:
            power = multiply(power, S, cutoff)
        coefficient = sum((a / F(j + 1) for (i, j), a in power.items() if i == cutoff), F(0))
        masses.append(coefficient / factorial(d) * scale)
    return masses


def theoretical_degree_weighted(n):
    # H'(t)= t(1+log(1+t))/(1+t). Lagrange inversion.
    harm = F(0)
    total = F(0)
    for j in range(n - 1):
        if j:
            harm += F(1, j)
        total += F((-1) ** j) * (1 - harm) * F(n ** (n - 2 - j), factorial(n - 2 - j))
    return F(factorial(n - 1), n ** (n - 1)) * total


def check():
    assertions = 0
    for n in range(2, 8):
        mass = [F(0) for _ in range(n)]
        tree_count = n ** (n - 2)
        for seq in product(range(n), repeat=n - 2):
            d, p = exact_root_occupancy(prufer_edges(seq, n), n)
            mass[d] += p
        mass = [v / tree_count for v in mass]
        theory = theoretical_mass(n)
        for d in range(n):
            assert mass[d] == theory[d], (n, d, mass[d], theory[d])
            assertions += 1
        measured_weighted = sum((d * p for d, p in enumerate(mass)), F(0))
        predicted_weighted = theoretical_degree_weighted(n)
        assert measured_weighted == predicted_weighted, (n, measured_weighted, predicted_weighted)
        assertions += 1
        print(f'n={n}, expected root occupation={sum(mass)}, expected degree*occupation={measured_weighted}, blocked-blocked expected={n-1-n*measured_weighted}')
    # A second algorithm enumerates complete priority orders and counts edges
    # with neither endpoint accepted; it does not use the root recursion.
    for n in range(2, 7):
        blocked_total = 0
        for seq in product(range(n), repeat=n - 2):
            edges = prufer_edges(seq, n)
            neighbor = [set() for _ in range(n)]
            for u, v in edges:
                neighbor[u].add(v)
                neighbor[v].add(u)
            for order in permutations(range(n)):
                chosen = set()
                for v in order:
                    if not (chosen & neighbor[v]):
                        chosen.add(v)
                blocked_total += sum(u not in chosen and v not in chosen for u, v in edges)
        empirical = F(blocked_total, n ** (n - 2) * factorial(n))
        predicted = F(n - 1) - n * theoretical_degree_weighted(n)
        assert empirical == predicted, (n, empirical, predicted)
        assertions += 1
    print(f'PASS: {assertions} exact coefficient, root-recursion, and direct-priority assertions')


if __name__ == '__main__':
    check()
