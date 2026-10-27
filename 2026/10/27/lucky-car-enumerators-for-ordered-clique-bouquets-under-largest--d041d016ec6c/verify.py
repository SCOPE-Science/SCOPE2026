"""Standalone checks of increasing largest-neighbor parking on consecutive clique bouquets.
Only finite checks are made; the theorem's infinite assertion uses a separate proof.
Run: python3 parking_bouquets_verify.py
"""
from itertools import combinations_with_replacement, product
from math import comb


def build_graph(sizes):
    n = 1 + sum(sizes)
    adjacency = [set() for _ in range(n + 1)]
    p = 2
    for m in sizes:
        vs = range(p, p + m)
        for i in vs:
            adjacency[1].add(i)
            adjacency[i].add(1)
            for j in range(i + 1, p + m):
                adjacency[i].add(j)
                adjacency[j].add(i)
        p += m
    return adjacency


def park(preferences, adjacency, initial=()):
    occupied = set(initial)
    lucky = 0
    for pref in preferences:
        vertex = pref
        for _ in range(len(adjacency)):
            if vertex not in occupied:
                occupied.add(vertex)
                if vertex == pref:
                    lucky += 1
                break
            higher = [w for w in adjacency[vertex] if w > vertex]
            free = [w for w in higher if w not in occupied]
            if free:
                occupied.add(max(free))
                break
            if not higher:
                return None
            vertex = min(higher)
        else:
            raise AssertionError('non-increasing movement in an acyclic orientation')
    return lucky


def direct_poly(sizes):
    n = 1 + sum(sizes)
    g = build_graph(sizes)
    ans = [0] * (n + 1)
    for seq in combinations_with_replacement(range(1, n + 1), n):
        lucky = park(seq, g)
        if lucky is not None:
            ans[lucky] += 1
    return ans


def add(a, b):
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) for i in range(max(len(a), len(b)))]


def times(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    return result


def compose_poly(sizes):
    # Independent sum over number t of leaf positions left unoccupied by root-preferring cars.
    ans = [0, 1]
    msum = sum(sizes)
    for t in range(1, msum + 1):
        left = t
        coeffs = [0, 1]
        for m in sizes:
            active = min(m, max(left, 0))
            left -= active
            if active:
                local = [0] + [comb(active - 1, j - 1) for j in range(1, active + 1)]
                coeffs = times(coeffs, local)
        ans = add(ans, coeffs)
    return ans


def closed_poly(sizes):
    # Independent expansion of u + sum_j u^j(1+u)^{S_{j-1}}((1+u)^m_j - 1).
    n = 1 + sum(sizes)
    result = [0] * (n + 1)
    result[1] = 1
    prefix = 0
    for j, m in enumerate(sizes, 1):
        for k in range(prefix + m + 1):
            if j + k <= n:
                result[j + k] += comb(prefix + m, k)
        for k in range(prefix + 1):
            result[j + k] -= comb(prefix, k)
        prefix += m - 1
    return result


def test_local_cliques():
    checks = 0
    for m in range(1, 8):
        adjacency = [set() for _ in range(m + 1)]
        for a in range(1, m + 1):
            adjacency[a] = set(range(1, m + 1)) - {a}
        for t in range(0, m + 1):
            coeff = [0] * (t + 1)
            for seq in combinations_with_replacement(range(1, m + 1), t):
                lucky = park(seq, adjacency, range(t + 1, m + 1))
                if lucky is not None:
                    coeff[lucky] += 1
            expect = [1] if t == 0 else [0] + [comb(t - 1, k - 1) for k in range(1, t + 1)]
            assert coeff == expect, ('local_clique', m, t, coeff, expect)
            checks += 1
    return checks


def test_bouquets():
    comparisons = 0
    for M in range(1, 8):
        # Every ordered composition of M is checked.
        for marks in product((0, 1), repeat=M - 1):
            sizes = []
            current = 1
            for mark in marks:
                if mark:
                    sizes.append(current)
                    current = 1
                else:
                    current += 1
            sizes.append(current)
            a = direct_poly(sizes)
            b = compose_poly(sizes)
            c = closed_poly(sizes)
            assert a == b == c, ('bouquet', sizes, a, b, c)
            assert sum(a) == 1 + sum((2 ** sum(v - 1 for v in sizes[:j])) * (2 ** m - 1) for j, m in enumerate(sizes))
            comparisons += 1
    return comparisons


def test_swap():
    checks = 0
    for sizes in [(1, 3, 2), (2, 1, 4), (3, 2, 1, 2), (2, 5), (1, 4, 1, 3), (3, 2)]:
        for j in range(len(sizes) - 1):
            x = list(sizes)
            y = list(sizes)
            y[j], y[j + 1] = y[j + 1], y[j]
            px = closed_poly(x)
            py = closed_poly(y)
            # right side: u^(j+1)(1+u)^S[(1+u)^(a-1)-(1+u)^(b-1)]
            S = sum(v - 1 for v in x[:j])
            a, b = x[j], x[j + 1]
            direct = [0] * len(px)
            for k in range(S + a):
                if j + 1 + k < len(direct):
                    direct[j + 1 + k] += comb(S + a - 1, k)
            for k in range(S + b):
                if j + 1 + k < len(direct):
                    direct[j + 1 + k] -= comb(S + b - 1, k)
            assert [v - w for v, w in zip(px, py)] == direct, ('swap', x, y)
            checks += 1
    return checks


if __name__ == '__main__':
    l, b, s = test_local_cliques(), test_bouquets(), test_swap()
    print(f'VERIFY_OK local_prefix_clique_cases={l} exhaustive_ordered_compositions={b} exchange_checks={s}')
