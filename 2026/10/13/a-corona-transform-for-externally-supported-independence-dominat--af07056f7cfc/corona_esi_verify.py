"""Independent finite checks of externally supported independent-set enumerators of leaf coronas.

Run with Python 3 and networkx: python corona_esi_verify.py
The general identity is proved separately; exhaustive tests are not a proof.
"""
from collections import Counter
from math import comb
import networkx as nx


def multiply(p, q):
    out = Counter()
    for a, ca in p.items():
        for b, cb in q.items():
            out[a + b] += ca * cb
    return out


def power(p, k):
    out = Counter({0: 1})
    for _ in range(k):
        out = multiply(out, p)
    return out


def formula(base, m):
    n = base.number_of_nodes()
    a = Counter({j: comb(m, j) for j in range(1, m + 1)})
    b = Counter({j: comb(m, j) for j in range(1, m)})
    result = Counter()
    for z in range(1 << n):
        nz = 0
        for v in range(n):
            if z >> v & 1:
                for w in base.neighbors(v):
                    nz |= 1 << w
        q = (nz & ~z).bit_count()
        r = n - q - z.bit_count()
        result.update(multiply(power(a, q), power(b, r)))
    return +result


def direct(base, m):
    n = base.number_of_nodes()
    order = n * (m + 1)
    neigh = [0] * order
    for u, v in base.edges():
        neigh[u] |= 1 << v
        neigh[v] |= 1 << u
    for v in range(n):
        for j in range(m):
            w = n + m * v + j
            neigh[v] |= 1 << w
            neigh[w] |= 1 << v
    whole = (1 << order) - 1
    out = Counter()
    for s in range(1 << order):
        nmask = 0
        rem = s
        while rem:
            bit = rem & -rem
            rem -= bit
            nmask |= neigh[bit.bit_length() - 1]
        if nmask & s:
            continue
        outside = whole & ~(nmask | s)
        rem = nmask
        while rem:
            bit = rem & -rem
            rem -= bit
            if not neigh[bit.bit_length() - 1] & outside:
                break
        else:
            out[s.bit_count()] += 1
    return +out


def domination_poly(base):
    n = base.number_of_nodes()
    full = (1 << n) - 1
    closed = [1 << v | sum(1 << w for w in base.neighbors(v)) for v in range(n)]
    out = Counter()
    for s in range(1 << n):
        seen = 0
        for v in range(n):
            if s >> v & 1:
                seen |= closed[v]
        if seen == full:
            out[s.bit_count()] += 1
    return out


def main():
    profiles = 0
    vertex_subsets = 0
    identity_m1 = 0
    extremal_checks = 0
    for h in nx.graph_atlas_g():
        n = h.number_of_nodes()
        if not 1 <= n <= 6:
            continue
        base = nx.convert_node_labels_to_integers(h)
        max_m = 3 if n <= 4 else 2 if n == 5 else 1
        for m in range(1, max_m + 1):
            got = direct(base, m)
            expected = formula(base, m)
            assert got == expected, (n, m, list(base.edges()), got, expected)
            profiles += 1
            vertex_subsets += 1 << (n * (m + 1))
            if m == 1:
                dp = domination_poly(base)
                assert got == Counter({n - k: c for k, c in dp.items()})
                identity_m1 += 1
            if m >= 2:
                maxdiff = max(
                    sum(1 for w in range(n) if w not in zs and any(base.has_edge(v, w) for v in zs)) - (m - 1) * len(zs)
                    for mask in range(1 << n)
                    for zs in [{v for v in range(n) if mask >> v & 1}]
                )
                assert max(got) == (m - 1) * n + maxdiff
                extremal_checks += 1
    print('ALL CHECKS PASSED')
    print(f'unlabeled_base_graph_corona_profiles={profiles}')
    print(f'full_vertex_subsets_enumerated={vertex_subsets}')
    print(f'single_leaf_domination_reversal_checks={identity_m1}')
    print(f'weighted_differential_extremal_checks={extremal_checks}')
    print('graph_orders=1..6; independent direct ESI-definition enumeration')


if __name__ == '__main__':
    main()
