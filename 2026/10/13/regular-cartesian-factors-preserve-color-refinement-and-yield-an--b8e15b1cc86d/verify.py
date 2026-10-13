"""Finite computational checks for regular-factor color-refinement invariance.
These tests support but do not replace the proof for all finite graphs.
"""
from itertools import combinations


def path(n):
    return [set(j for j in (i - 1, i + 1) if 0 <= j < n) for i in range(n)]


def cycle(n):
    return [set(((i - 1) % n, (i + 1) % n)) for i in range(n)]


def complete(n):
    return [set(range(n)) - {i} for i in range(n)]


def disjoint(*factors):
    out = []
    for graph in factors:
        offset = len(out)
        out.extend({j + offset for j in neighbors} for neighbors in graph)
    return out


def product(g, h):
    a, b = len(g), len(h)
    return [set(u * b + j for j in h[v]) | set(w * b + v for w in g[u])
            for u in range(a) for v in range(b)]


def refinement(g):
    col = [0] * len(g)
    steps = [tuple(col)]
    for _ in range(len(g)):
        signatures = [(col[u], tuple(sorted(col[v] for v in g[u]))) for u in range(len(g))]
        ids = {sig: i for i, sig in enumerate(sorted(set(signatures)))}
        new = [ids[sig] for sig in signatures]
        if new == col:
            return steps
        col = new
        steps.append(tuple(col))
    raise AssertionError('nonterminating refinement')


def equal_partition(colors, signatures):
    return all((colors[i] == colors[j]) == (signatures[i] == signatures[j])
               for i in range(len(colors)) for j in range(i))


def verify():
    count = 0
    for size in range(2, 11):
        Gs = [path(size), cycle(size), complete(size)]
        for g in Gs:
            for h in [cycle(n) for n in range(3, 11)] + [complete(n) for n in range(2, 8)] + [disjoint(cycle(3), cycle(4))]:
                colors_g = refinement(g)
                colors_product = refinement(product(g, h))
                assert len(colors_g) == len(colors_product)
                b = len(h)
                for t in range(len(colors_g)):
                    sig = tuple(colors_g[t][i // b] for i in range(len(g) * b))
                    assert equal_partition(colors_product[t], sig)
                count += 1
    # The same color histograms for two nonisomorphic cylinder-like graphs.
    for m in range(2, 12):
        for n in range(6, 14):
            g = path(m)
            h = cycle(n)
            h2 = disjoint(cycle(3), cycle(n - 3))
            for a, b in zip(refinement(product(g, h)), refinement(product(g, h2))):
                assert sorted(__import__('collections').Counter(a).values()) == sorted(__import__('collections').Counter(b).values())
    print('PASS product_roundwise=', count, 'cylinder_counterparts=', 10 * 8)

if __name__ == '__main__':
    verify()
