#!/usr/bin/env python3
"""Exact finite-field verification of the rational linear spaces on a cyclic cubic fourfold."""
from collections import Counter
from itertools import combinations

N = 6

def b(a, c):
    return sum(((a >> i) & 1) * ((c >> ((i + 1) % N)) & 1)
               for i in range(N)) & 1

def cubic_at_binary(a):
    return sum(((a >> i) & 1) * ((a >> ((i + 1) % N)) & 1)
               for i in range(N)) & 1

def span(vectors):
    result = {0}
    for v in vectors:
        result |= {x ^ v for x in list(result)}
    return frozenset(result)

def linear_spaces(d):
    groups = set()
    for vectors in combinations(range(1, 64), d):
        u = span(vectors)
        if len(u) == (1 << d):
            groups.add(u)
    return groups

def coefficient_test(u):
    # The coefficients of a restricted cubic are B(e_i,e_j).
    # Testing all ordered pairs in the subspace is basis-independent.
    return all(b(v, w) == 0 for v in u for w in u)

spaces = {d: linear_spaces(d) for d in (1, 2, 3)}
assert [len(spaces[d]) for d in (1, 2, 3)] == [63, 651, 1395]
contained = {d: {u for u in spaces[d] if coefficient_test(u)} for d in spaces}
assert [len(contained[d]) for d in (1, 2, 3)] == [39, 75, 9]
assert all(cubic_at_binary(v) == 0 for u in contained[1] for v in u)

T = span([21, 42])
E = frozenset(v for v in range(64) if
              ((v >> 0) ^ (v >> 2) ^ (v >> 4)) & 1 == 0 and
              ((v >> 1) ^ (v >> 3) ^ (v >> 5)) & 1 == 0)
assert len(T) == 4 and len(E) == 16 and T & E == {0}
assert all(b(t, e) == b(e, t) == 0 for t in T for e in E)
assert (b(21, 42), b(42, 21)) == (1, 1)
null_E = {e for e in E if cubic_at_binary(e) == 0}
assert len(null_E) == 10

bases = [(5, 17), (10, 34), (27, 45),
         (5, 40), (10, 17), (20, 34)]
quadric_lines = {span(pair) for pair in combinations(null_E - {0}, 2)
                 if len(span(pair)) == 4 and all(cubic_at_binary(v) == 0
                                                 for v in span(pair))}
assert len(quadric_lines) == 6
assert quadric_lines == {span(pair) for pair in bases}
assert all(b(*pair) == 0 for pair in bases[:3])
assert all(b(*pair) == 1 for pair in bases[3:])

expected_planes = {span([w, a, c]) for w in T - {0} for a, c in bases[:3]}
assert expected_planes == contained[3]

points, lines, planes = [contained[d] for d in (1, 2, 3)]
plane_contains_line = Counter(sum(l <= p for p in planes) for l in lines)
plane_contains_point = Counter(sum(q <= p for p in planes) for q in points)
point_lines = Counter(sum(q <= l for l in lines) for q in points)
assert plane_contains_line == {1: 54, 3: 3, 0: 18}
assert plane_contains_point == {1: 27, 3: 12}
assert point_lines == {5: 27, 7: 9, 9: 3}
intersections = Counter()
for p, q in combinations(planes, 2):
    common = p & q
    intersections[{1: -1, 2: 0, 4: 1}[len(common)]] += 1
assert intersections == {-1: 18, 0: 9, 1: 9}
assert all(sum(l <= p for l in lines) == 7 for p in planes)

# An independent coefficient test: expand F(sum_i u_i*v_i)
# over F4 and compare polynomial coefficient words of degree 3.
def gf4_mul(a, c):
    r = 0
    for i in range(2):
        if (c >> i) & 1:
            r ^= a << i
    if r & 8:
        r ^= 0b1100  # x^3 = x(x+1) for x^2+x+1=0
    if r & 4:
        r ^= 0b111  # x^2 = x+1
    return r

def f4_at(v):
    r = 0
    for i in range(6):
        r ^= gf4_mul(gf4_mul(v[i], v[i]), v[(i+1) % 6])
    return r

def basis_of(u):
    result = []
    generated = {0}
    for x in sorted(u):
        if x not in generated:
            result.append(x)
            generated |= {v ^ x for v in list(generated)}
    return result

# Evaluate at every point of P^2(F4) in all nine asserted planes.
for plane in planes:
    basis = basis_of(plane)
    assert len(basis) == 3
    for a in range(4):
        for c in range(4):
            for d in range(4):
                if a == c == d == 0:
                    continue
                coords = []
                for j in range(6):
                    bit = lambda z, v: z if (v >> j) & 1 else 0
                    coords.append(bit(a, basis[0]) ^ bit(c, basis[1]) ^ bit(d, basis[2]))
                assert f4_at(coords) == 0

print('VERIFY_OK: 39 F2-points, 75 F2-lines, 9 F2-planes; plane grid and incidences exact')
