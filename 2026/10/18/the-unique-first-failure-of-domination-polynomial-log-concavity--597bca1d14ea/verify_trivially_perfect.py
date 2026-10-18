"""Exact certificate for the first non-log-concave trivially perfect domination polynomial.

Requires Python 3.9+ standard library only. Enumerates unlabelled rooted
shapes by multisets of smaller rooted shapes. Each shape represents its
ancestor-comparability graph. The graph recursion and the independent
vertex-subset check are both included.
"""

from functools import lru_cache
from math import comb

ROOTED_COUNTS = (1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842,
                 4766, 12486, 32973, 87811, 235381)
EXPECTED_WITNESS_POLYNOMIAL = (0, 1, 15, 230, 1205, 3615, 7378,
                               11080, 12735, 11410, 8005, 4368,
                               1820, 560, 120, 16, 1)


def order(shape):
    return 1 + sum(order(child) for child in shape)


@lru_cache(maxsize=None)
def rooted_shapes(n):
    """Every rooted unlabelled tree on n vertices, exactly once."""
    assert n >= 1
    if n == 1:
        return {()}
    candidates = [(k, shape) for k in range(1, n)
                  for shape in rooted_shapes(k)]
    candidates.sort(key=lambda pair: (pair[0], repr(pair[1])))
    answers = set()

    def partitions(remaining, first, selected):
        if remaining == 0:
            answers.add(tuple(selected))
            return
        for j in range(first, len(candidates)):
            k, shape = candidates[j]
            if k > remaining:
                break
            selected.append(shape)
            partitions(remaining - k, j, selected)
            selected.pop()

    partitions(n - 1, 0, [])
    return answers


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, p in enumerate(a):
        for j, q in enumerate(b):
            c[i + j] += p * q
    return tuple(c)


@lru_cache(maxsize=None)
def domination_coefficients(shape):
    """Polynomial via universal root and its disconnected child graph."""
    if not shape:
        return (0, 1)
    without_root = (1,)
    for child in shape:
        without_root = multiply(without_root, domination_coefficients(child))
    child_total = len(without_root) - 1
    result = list(without_root) + [0]
    for k in range(child_total + 1):
        result[k + 1] += comb(child_total, k)
    return tuple(result)


def logconcavity_violations(coeffs):
    return tuple(k for k in range(1, len(coeffs) - 1)
                 if coeffs[k] ** 2 < coeffs[k - 1] * coeffs[k + 1])


def adjacency_from_ancestors(shape):
    adjacency = []

    def visit(t, ancestors):
        vertex = len(adjacency)
        adjacency.append(0)
        for ancestor in ancestors:
            adjacency[vertex] |= 1 << ancestor
            adjacency[ancestor] |= 1 << vertex
        for child in t:
            visit(child, ancestors + (vertex,))

    visit(shape, ())
    return adjacency


def brute_domination_coefficients(shape):
    adjacency = adjacency_from_ancestors(shape)
    closed = [1 << i | neighbors for i, neighbors in enumerate(adjacency)]
    count = [0] * (len(adjacency) + 1)
    for subset in range(1 << len(adjacency)):
        if all(subset & neighborhood for neighborhood in closed):
            count[subset.bit_count()] += 1
    return tuple(count)


def chain(n):
    if n == 1:
        return ()
    return (chain(n - 1),)


def main():
    sizes = []
    witnessed = []
    tested = 0
    for n in range(1, 17):
        shapes = rooted_shapes(n)
        sizes.append(len(shapes))
        assert len(shapes) == ROOTED_COUNTS[n - 1], (n, len(shapes))
        bad = []
        for shape in shapes:
            coeffs = domination_coefficients(shape)
            assert len(coeffs) == n + 1
            assert coeffs[0] == 0 and coeffs[n] == 1
            if n <= 7:
                assert coeffs == brute_domination_coefficients(shape), (n, shape)
            if logconcavity_violations(coeffs):
                bad.append((shape, coeffs))
        tested += len(shapes)
        if n < 16:
            assert not bad, (n, bad[:1])
        else:
            assert len(bad) == 1, len(bad)
            witnessed = bad
        print('order=%02d rooted_classes=%06d failures=%d' %
              (n, len(shapes), len(bad)))
    shape, coeffs = witnessed[0]
    assert shape == (chain(5), chain(5), chain(5))
    assert coeffs == EXPECTED_WITNESS_POLYNOMIAL
    assert logconcavity_violations(coeffs) == (2,)
    assert brute_domination_coefficients(shape) == coeffs
    print('TOTAL_CONNECTED_CLASSES_TESTED=%d' % tested)
    print('UNIQUE_FIRST_WITNESS=K1_join_3K5')
    print('WITNESS_COEFFICIENTS=%s' % (','.join(map(str, coeffs))))
    print('INDEX_TWO_FAILURE: d2^2=225 < d1*d3=230')
    print('EXHAUSTIVE_CERTIFICATE_OK')


if __name__ == '__main__':
    main()
