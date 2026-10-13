#!/usr/bin/env python3
"""Check the distance spectrum of the binary equal-path multi-theta cycle codes."""
from collections import Counter
from math import comb


def multiply(a, b):
    c = Counter()
    for i, ai in a.items():
        for j, bj in b.items():
            c[i + j] += ai * bj
    return dict(c)


def power(a, r):
    out = {0: 1}
    for _ in range(r):
        out = multiply(out, a)
    return out


def distance_polynomial(r, ell):
    assert r >= 4 and r % 2 == 0 and ell >= 2
    s = ell // 2
    if ell % 2 == 0:
        u = [{s-d: 2 * comb(ell, s-d) for d in range(t, s+1)}
             for t in range(1, s+2)]
        b = dict(u[0])
        b[s] = comb(ell, s)
        out = Counter(power(b, r))
        for degree, coeff in power(u[0], r).items():
            assert coeff % 2 == 0
            out[degree] -= coeff // 2
        for t in range(1, s+1):
            for degree, coeff in power(u[t-1], r).items():
                assert coeff % 2 == 0
                out[degree + 2*t] += coeff // 2
            for degree, coeff in power(u[t], r).items():
                assert coeff % 2 == 0
                out[degree + 2*t] -= coeff // 2
    else:
        u = [{s-d: 2 * comb(ell, s-d) for d in range(t, s+1)}
             for t in range(s+2)]
        out = Counter()
        for degree, coeff in power(u[0], r).items():
            assert coeff % 2 == 0
            out[degree] += coeff // 2
        for t in range(s+1):
            for degree, coeff in power(u[t], r).items():
                assert coeff % 2 == 0
                out[degree + 2*t+1] += coeff // 2
            for degree, coeff in power(u[t+1], r).items():
                assert coeff % 2 == 0
                out[degree + 2*t+1] -= coeff // 2
    return dict(sorted((degree, int(coeff)) for degree, coeff in out.items() if coeff))


def graph_edges(r, ell):
    """Construct r internally disjoint u--v paths of ell edges each."""
    edges = []
    nxt = 2
    for _ in range(r):
        last = 0
        for j in range(ell):
            target = 1 if j == ell-1 else nxt
            if j < ell-1:
                nxt += 1
            edges.append((last, target))
            last = target
    return edges


def independent_graph_cycle_words(r, ell):
    edges = graph_edges(r, ell)
    result = set()
    for word in range(1 << len(edges)):
        degree = Counter()
        for k, (a,b) in enumerate(edges):
            if word & (1 << k):
                degree[a] ^= 1
                degree[b] ^= 1
        if all((x & 1) == 0 for x in degree.values()):
            result.add(word)
    return result


def expected_cycle_words(r, ell):
    patterns = set()
    full = (1 << ell) - 1
    for word in range(1 << r):
        if word.bit_count() % 2 == 0:
            patterns.add(sum((full << (i*ell)) for i in range(r) if (word >> i) & 1))
    return patterns


def exhaustive_distribution(r, ell):
    code = expected_cycle_words(r, ell)
    out = Counter()
    holes = Counter()
    radius = None
    for word in range(1 << (r*ell)):
        distances = [(word ^ c).bit_count() for c in code]
        minimum = min(distances)
        out[minimum] += 1
        holes[(minimum, distances.count(minimum))] += 1
    return dict(out), holes


def predicted_extremes(r, ell):
    s = ell // 2
    if ell % 2 == 0:
        return r*s, comb(ell, s)**r, 2**(r-1)
    return r*s + 1, 2**(r-1) * comb(ell, s)**r, r


def run():
    samples = [(4,2),(6,2),(4,3),(4,4),(4,5)]
    for r, ell in samples:
        assert independent_graph_cycle_words(r, ell) == expected_cycle_words(r, ell)
        formula = distance_polynomial(r, ell)
        brute, multiplicities = exhaustive_distribution(r, ell)
        assert formula == dict(sorted(brute.items())), (r, ell, formula, brute)
        assert sum(formula.values()) == 2**(r*ell)
        assert formula.get(0) == 2**(r-1)
        radius, count, nearest = predicted_extremes(r, ell)
        assert max(brute) == radius
        assert brute[radius] == count
        assert multiplicities[(radius, nearest)] == count
        assert sum(v for (d, n),v in multiplicities.items() if d==radius and n!=nearest)==0
        print(f'PATHS={r} LENGTH={ell} RADIUS={radius} DEEP_HOLES={count} NEAREST={nearest}')
    for r, ell in [(8,2),(10,3),(4,6),(6,7),(12,8)]:
        f = distance_polynomial(r, ell)
        radius, count, _ = predicted_extremes(r, ell)
        assert max(f) == radius and f[radius] == count
        assert sum(f.values()) == 2**(r*ell)
        assert f[0] == 2**(r-1)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
