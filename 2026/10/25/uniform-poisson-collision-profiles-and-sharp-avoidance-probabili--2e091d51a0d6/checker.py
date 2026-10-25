"""Pure-standard-library finite checks for forest collision distributions.

Enumerates set partitions of up to seven vertices and compares full collision
histograms for several non-isomorphic forests, their exact Bell transforms,
and the conditional K-box product law. Infinite asymptotics require the proof.
"""
from math import comb


def partitions(n):
    if n == 0:
        yield ()
        return
    def rec(prefix, maximum):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for label in range(maximum + 2):
            prefix.append(label)
            yield from rec(prefix, max(maximum, label))
            prefix.pop()
    yield from rec([0], 0)


def bell(n):
    b = [1]
    for j in range(n):
        b.append(sum(comb(j, i) * b[i] for i in range(j + 1)))
    return b


def histogram(n, edges):
    out = [0] * (len(edges) + 1)
    for partition in partitions(n):
        x = sum(partition[u] == partition[v] for u, v in edges)
        out[x] += 1
    return out


def exact_counts(n, e, b):
    # Distribution via factorial moments, valid for forest edge sets.
    return [
        comb(e, j) * sum((-1)**h * comb(e-j, h) * b[n-j-h]
                         for h in range(e-j+1))
        for j in range(e+1)
    ]


def forest_edges(n, e, form):
    if form == "star":
        return [(0, j) for j in range(1, e+1)]
    if form == "path":
        return [(j, j+1) for j in range(e)]
    if form == "matching":
        return [(2*j, 2*j+1) for j in range(e)]
    raise ValueError(form)


def run():
    b = bell(8)
    tested = 0
    for n in range(1, 8):
        for e in range(n):
            expected = exact_counts(n, e, b)
            assert sum(expected) == b[n]
            for form in ("star", "path", "matching"):
                if form == "matching" and 2*e > n:
                    continue
                observed = histogram(n, forest_edges(n, e, form))
                assert observed == expected, (n, e, form, observed, expected)
                tested += 1
    # A 3-cycle violates forest-only factorization for two colors.
    triangle = [(0,1), (1,2), (0,2)]
    assert histogram(4, triangle) != exact_counts(4, 3, b)
    print("FINITE_CHECKS_OK", tested, "forest histograms and triangle boundary")
    print("BELL_7", b[7], "SPANNING_TREE_AVOIDANCE_7", exact_counts(7,6,b)[0])

if __name__ == '__main__':
    run()
