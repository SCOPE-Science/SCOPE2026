from itertools import combinations_with_replacement
from math import comb


def canonical_sequences(m, n):
    if m == 1:
        yield (n,)
        return
    for pre in combinations_with_replacement(range(1, n + 1), m - 1):
        yield tuple(pre) + (n,)


def build_adj(ds):
    m = len(ds)
    n = max(ds)
    adj = [set() for _ in range(m + n)]
    for i, d in enumerate(ds):
        for j in range(d):
            a = i
            b = m + j
            adj[a].add(b)
            adj[b].add(a)
    return adj


def is_total_dominating(adj, mask):
    return all(any((mask >> v) & 1 for v in adj[u]) for u in range(len(adj)))


def induced_connected(adj, mask):
    vertices = [u for u in range(len(adj)) if (mask >> u) & 1]
    if not vertices:
        return False
    allowed = set(vertices)
    seen = {vertices[0]}
    stack = [vertices[0]]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v in allowed and v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(vertices)


def hit_coeff(total, universal, k):
    if k < 0 or k > total:
        return 0
    avoid = comb(total - universal, k) if k <= total - universal else 0
    return comb(total, k) - avoid


def formula_coeffs(m, n, a, b):
    out = [0] * (m + n + 1)
    for k in range(m + n + 1):
        out[k] = sum(hit_coeff(m, a, i) * hit_coeff(n, b, k - i)
                     for i in range(k + 1))
    return out


graphs = 0
subsets = 0
for m in range(1, 7):
    for n in range(1, 7):
        if m + n > 11:
            continue
        for ds in canonical_sequences(m, n):
            adj = build_adj(ds)
            a_star = {i for i, d in enumerate(ds) if d == n}
            b_star = {m + j for j in range(ds[0])}
            brute = [0] * (m + n + 1)
            for mask in range(1 << (m + n)):
                tds = is_total_dominating(adj, mask)
                predicted = (any((mask >> u) & 1 for u in a_star) and
                             any((mask >> v) & 1 for v in b_star))
                assert tds == predicted, (m, n, ds, mask, 'criterion')
                if tds:
                    assert induced_connected(adj, mask), (m, n, ds, mask, 'connectivity')
                    brute[mask.bit_count()] += 1
                subsets += 1
            formula = formula_coeffs(m, n, len(a_star), len(b_star))
            assert brute == formula, (m, n, ds, 'coefficients', brute, formula)
            assert brute[2] == len(a_star) * len(b_star), (m, n, ds, 'minimum count')
            assert all(brute[k] > 0 for k in range(2, m + n + 1)), (m, n, ds, 'support')
            if len(a_star) == m and len(b_star) == n:
                expected = [0] * (m + n + 1)
                for k in range(m + n + 1):
                    expected[k] = sum(comb(m, i) * comb(n, k - i)
                                      for i in range(1, m + 1)
                                      if 1 <= k - i <= n)
                assert brute == expected, (m, n, ds, 'complete-bipartite specialization')
            graphs += 1

print(f'VERIFY_OK graphs={graphs} subsets={subsets} max_order=11')
