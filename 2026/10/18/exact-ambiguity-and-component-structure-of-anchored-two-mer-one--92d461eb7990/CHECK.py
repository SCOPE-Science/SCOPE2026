"""Finite independent readout enumeration for the anchored two-mer channel.

All assertions concern small alphabets and lengths; the infinite theorem
is established by the separate combinatorial proof.
"""
from collections import defaultdict, Counter
from itertools import product
from math import comb


def compressed(w):
    return tuple(c for i, c in enumerate(w) if i == 0 or c != w[i - 1])


def runs(w):
    out = []
    for c in w:
        if out and out[-1][0] == c:
            out[-1] = (c, out[-1][1] + 1)
        else:
            out.append((c, 1))
    return tuple(out)


def walk_counts(q, k, a):
    c = [0] * q
    c[a] = 1
    for _ in range(k):
        c = [sum(c) - x for x in c]
    return c


def inspect(q, n, a, b):
    words = tuple(product(range(q), repeat=n))
    outer0 = (a + 1) % q
    outer1 = (b + 1) % q
    parents = defaultdict(set)
    run_data = []
    for ix, w in enumerate(words):
        z = (a,) + w + (b,)
        run_data.append(runs(z))
        full = ((outer0, a),) + tuple((z[j - 1], z[j]) for j in range(1, n + 2)) + ((b, outer1),)
        for deletion_position in range(1, n + 2):
            received = full[:deletion_position] + full[deletion_position + 1:]
            parents[received].add(ix)

    expected_hist = Counter()
    for k in range(n + 1):
        count = comb(n, k) * walk_counts(q, k, a)[b]
        expected_hist[k + 1] += count
    inconsistent = (n + 1) * (q - 1) * q ** (n - 1)
    expected_hist[1] += inconsistent

    histogram = Counter()
    actual_edges = set()
    for readout, pset in parents.items():
        consistent = all(readout[j][1] == readout[j + 1][0] for j in range(len(readout) - 1))
        if consistent:
            recovered = (readout[0][0],) + tuple(r[1] for r in readout)
            assert recovered[0] == outer0 and recovered[-1] == outer1
            middle = recovered[1:-1]
            assert middle[0] == a and middle[-1] == b
            assert len(pset) == len(compressed(middle)), (q, n, a, b, middle, pset)
        else:
            assert len(pset) == 1, (q, n, a, b, readout, pset)
        histogram[len(pset)] += 1
        ids = sorted(pset)
        actual_edges.update((u, v) for i, u in enumerate(ids) for v in ids[i + 1:])

    assert histogram == expected_hist, (q, n, a, b, histogram, expected_hist)
    expected_edges = set()
    for i, ri in enumerate(run_data):
        for j in range(i + 1, len(run_data)):
            rj = run_data[j]
            if tuple(c for c, _ in ri) == tuple(c for c, _ in rj) and sum(abs(x - y) for (_, x), (_, y) in zip(ri, rj)) == 2:
                expected_edges.add((i, j))
    assert actual_edges == expected_edges, (q, n, a, b, len(actual_edges), len(expected_edges))
    from_itinerary = sum(comb(k + 1, 2) * comb(n, k) * walk_counts(q, k, a)[b] for k in range(n + 1))
    assert len(actual_edges) == from_itinerary
    if n >= 3:
        closed_edges = n * (q - 1) * q ** (n - 3) * ((n - 1) * (q - 1) + 2 * q) // 2
        assert len(actual_edges) == closed_edges, (q, n, a, b, len(actual_edges), closed_edges)
    assert len(parents) == q ** (n - 1) * (1 + (n + 1) * (q - 1))
    return len(parents), len(actual_edges)


def main():
    tested = 0
    for q, highest in ((2, 9), (3, 6), (4, 5), (5, 4)):
        for n in range(1, highest + 1):
            for a in range(q):
                for b in range(q):
                    inspect(q, n, a, b)
                    tested += 1
            print(f"verified q={q} n={n}: all {q*q} ordered anchor pairs", flush=True)
    print(f"PASS: {tested} complete parameters, independent output and edge enumerations", flush=True)


if __name__ == '__main__':
    main()
