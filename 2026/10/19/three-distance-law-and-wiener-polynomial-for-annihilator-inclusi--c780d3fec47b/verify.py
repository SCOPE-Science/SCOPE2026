"""Finite-instance checks for an annihilator-inclusion distance theorem.

Only Python's standard library is required. Integer-residue rings are checked
using gcd/divisibility, not the valuation-counting argument in the theorem.
"""
from collections import Counter, deque
from itertools import product
from math import gcd, prod


def factors(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            m = 0
            while n % d == 0:
                n //= d
                m += 1
            result.append((d, m))
        d += 1
    if n > 1:
        result.append((n, 1))
    return result


def predicted(parameters):
    """Return counts of distances 1, 2, 3 and disconnected pairs."""
    r = len(parameters)
    size = prod(q ** m for q, m in parameters)
    units = prod(q ** (m - 1) * (q - 1) for q, m in parameters)
    nested = prod((q ** (2 * m + 1) + 1) // (q + 1)
                  for q, m in parameters)
    equal = prod(((q - 1) * q ** (2 * m) + 2) // (q + 1)
                 for q, m in parameters)
    n_vertices = size - units - 1
    comparable_ordered = nested - (units + 1) * size + units
    equal_valuation_ordered = equal - units ** 2 - 1
    assert (equal_valuation_ordered + n_vertices) % 2 == 0
    edges = comparable_ordered - (equal_valuation_ordered + n_vertices) // 2
    exceptional = (r == 2 and all(m == 1 for _, m in parameters))
    opposite = ((1 << (r - 1)) - 1) * units
    three = 0 if exceptional else opposite
    disconnected = opposite if exceptional else 0
    two = n_vertices * (n_vertices - 1) // 2 - edges - three - disconnected
    assert min(edges, two, three, disconnected) >= 0
    return n_vertices, (edges, two, three, disconnected)


def distance_census(vertices, related):
    adjacency = [set() for _ in vertices]
    for i in range(len(vertices)):
        for j in range(i):
            if related(vertices[i], vertices[j]):
                adjacency[i].add(j)
                adjacency[j].add(i)
    counts = Counter()
    for start in range(len(vertices)):
        distances = [-1] * len(vertices)
        distances[start] = 0
        queue = deque([start])
        while queue:
            at = queue.popleft()
            for new in adjacency[at]:
                if distances[new] == -1:
                    distances[new] = distances[at] + 1
                    queue.append(new)
        for end in range(start):
            counts[distances[end]] += 1
    assert not [d for d in counts if d > 3]
    return counts[1], counts[2], counts[3], counts[-1]


def check_integers(modulus):
    vertices = [a for a in range(1, modulus) if gcd(a, modulus) != 1]
    def related(a, b):
        da, db = gcd(a, modulus), gcd(b, modulus)
        return da % db == 0 or db % da == 0
    observed = distance_census(vertices, related)
    expected_n, expected = predicted(factors(modulus))
    assert (len(vertices), observed) == (expected_n, expected), (
        modulus, expected_n, len(vertices), expected, observed)
    return (modulus, expected_n, observed)


def check_valuation_model(parameters):
    """Check other residue-field sizes using the full valuation block graph."""
    vertices = []
    for valuations in product(*(range(m + 1) for _, m in parameters)):
        if all(v == 0 for v in valuations):
            continue
        if all(v == m for v, (_, m) in zip(valuations, parameters)):
            continue
        sizes = [(q - 1) * q ** (m - v - 1) if v < m else 1
                 for v, (q, m) in zip(valuations, parameters)]
        for index in range(prod(sizes)):
            vertices.append((valuations, index))
    def related(a, b):
        va, vb = a[0], b[0]
        return (all(x <= y for x, y in zip(va, vb)) or
                all(y <= x for x, y in zip(va, vb)))
    observed = distance_census(vertices, related)
    expected_n, expected = predicted(parameters)
    assert (len(vertices), observed) == (expected_n, expected), (
        parameters, expected_n, len(vertices), expected, observed)
    return (parameters, expected_n, observed)


def check_residue_product(orders):
    """Enumerate actual tuples of integer residue rings, including repeated primes."""
    all_elements = product(*(range(n) for n in orders))
    vertices = [x for x in all_elements if any(a != 0 for a in x) and
                any(gcd(a, n) != 1 for a, n in zip(x, orders))]
    def related(a, b):
        aa = [gcd(x, n) for x, n in zip(a, orders)]
        bb = [gcd(x, n) for x, n in zip(b, orders)]
        return (all(y % x == 0 for x, y in zip(aa, bb)) or
                all(x % y == 0 for x, y in zip(aa, bb)))
    observed = distance_census(vertices, related)
    parameters = [factors(n)[0] for n in orders]
    assert all(len(factors(n)) == 1 for n in orders)
    expected_n, expected = predicted(parameters)
    assert (len(vertices), observed) == (expected_n, expected), (orders, expected, observed)
    return (orders, expected_n, observed)


def main():
    integers = [4, 6, 8, 9, 10, 12, 16, 18, 20, 21, 24, 27, 28, 30,
                36, 40, 42, 45, 48, 54, 56, 60, 63, 72, 75, 84, 90,
                105, 120]
    additional = [
        [(4, 1), (2, 2)], [(4, 1), (8, 1)],
        [(4, 1), (8, 1), (2, 1)], [(4, 2)],
        [(4, 1), (4, 1), (4, 1)], [(2, 2), (4, 1)],
    ]
    products = [(4, 4), (4, 9), (2, 4), (9, 9), (2, 2, 2), (2, 3, 5), (4, 4, 2), (2, 8), (3, 9)]
    direct_products = [check_residue_product(t) for t in products]
    results = [check_integers(m) for m in integers]
    more = [check_valuation_model(p) for p in additional]
    print('INTEGER_RING_CHECKS', len(results))
    print('EXCEPTION_Z6', check_integers(6))
    print('Z4_TIMES_Z4', check_residue_product((4, 4)))
    print('INTEGER_DIRECT_PRODUCTS', direct_products)
    print('NONPRIME_FIELD_VALUATIONS', more)
    print('VERIFY_OK', len(results), 'cyclic rings,', len(direct_products),
          'direct products, and', len(more), 'nonprime-field valuation models')


if __name__ == '__main__':
    main()
