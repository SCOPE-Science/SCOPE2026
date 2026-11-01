#!/usr/bin/env python3
"""Exact character certificate for the independence complex of KG(3,1).

Only Python's standard library is required.  Published rational Betti ranks
and the cross-polytope independence theorem are mathematical inputs; they are
not asserted to be reproved by this finite character certificate.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial

N = 7
TRIPLES = tuple(combinations(range(N), 3))
MASKS = tuple(sum(1 << i for i in a) for a in TRIPLES)
INDEX = {m: j for j, m in enumerate(MASKS)}


def partitions(n, upper=None):
    if n == 0:
        yield ()
        return
    for x in range(min(n, n if upper is None else upper), 0, -1):
        for tail in partitions(n - x, x):
            yield (x,) + tail


def permutation_of_type(mu):
    p = list(range(N))
    offset = 0
    for m in mu:
        for j in range(m):
            p[offset + j] = offset + (j + 1) % m
        offset += m
    assert offset == N
    return tuple(p)


def orbit_conflict_graph(p):
    """Vertices are admissible orbits of 3-subsets; edges signal disjoint triples."""
    visited = set()
    orbits = []
    for seed in MASKS:
        if INDEX[seed] in visited:
            continue
        orbit = []
        current = seed
        while INDEX[current] not in visited:
            visited.add(INDEX[current])
            orbit.append(current)
            current = sum(1 << p[i] for i in range(N) if current & (1 << i))
        if all(a & b for a, b in combinations(orbit, 2)):
            orbits.append(tuple(orbit))
    adjacency = [0] * len(orbits)
    for i in range(len(orbits)):
        for j in range(i):
            if any((a & b) == 0 for a in orbits[i] for b in orbits[j]):
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    return tuple(adjacency)


def independence_polynomial_at_minus_one(adj):
    size = len(adj)

    @lru_cache(maxsize=None)
    def evaluate(mask):
        if not mask:
            return 1
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            remaining -= bit
            if adj[bit.bit_length() - 1] & mask == 0:
                return 0  # An isolated vertex factors as (1-1).
        seed = mask & -mask
        component = seed
        fringe = seed
        while fringe:
            neighbors = 0
            todo = fringe
            while todo:
                bit = todo & -todo
                todo -= bit
                neighbors |= adj[bit.bit_length() - 1]
            fringe = neighbors & mask & ~component
            component |= fringe
        if component != mask:
            return evaluate(component) * evaluate(mask ^ component)
        vertex = max((i for i in range(size) if mask & (1 << i)),
                     key=lambda i: (adj[i] & mask).bit_count())
        bit = 1 << vertex
        return evaluate(mask ^ bit) - evaluate(mask & ~(adj[vertex] | bit))

    result = evaluate((1 << size) - 1)
    assert evaluate.cache_info().currsize < 200000
    return result


def permutation_sign(image_list):
    return -1 if sum(image_list[i] > image_list[j]
                     for i in range(len(image_list))
                     for j in range(i+1, len(image_list))) % 2 else 1


def trace_on_six_set_cycles(p):
    """Trace of Ind_{S6 x S1}^{S7}(sgn_6 x 1), via invariant subsets."""
    ans = 0
    for S in combinations(range(N), 6):
        if set(p[i] for i in S) == set(S):
            where = {i: j for j, i in enumerate(S)}
            ans += permutation_sign([where[p[i]] for i in S])
    return ans


def verify_orientation():
    """Top orientation of the six-point cross-polytope transforms by sign."""
    S = tuple(range(6))
    all_triples = tuple(combinations(S, 3))
    pairs = []
    used = set()
    for a in all_triples:
        if a in used:
            continue
        b = tuple(x for x in S if x not in a)
        used.add(a)
        used.add(b)
        pairs.append((a, b))
    assert len(pairs) == 10
    target = {a: (i, 1 if k == 0 else -1)
              for i, pair in enumerate(pairs) for k, a in enumerate(pair)}
    for p in permutations(S):
        pair_images = []
        orientation = 1
        for a, b in pairs:
            u = tuple(sorted(p[x] for x in a))
            v = tuple(sorted(p[x] for x in b))
            j, sign_u = target[u]
            j2, sign_v = target[v]
            assert j == j2 and sign_u == -sign_v
            pair_images.append(j)
            orientation *= sign_u
        orientation *= permutation_sign(pair_images)
        assert orientation == permutation_sign(p)
    return len(tuple(permutations(S)))


@lru_cache(maxsize=None)
def rim_hooks(shape, length):
    result = []
    for inner in partitions(sum(shape) - length):
        if len(inner) > len(shape) or any(inner[i] > shape[i] for i in range(len(inner))):
            continue
        boxes = {(i, j) for i, end in enumerate(shape)
                 for j in range(inner[i] if i < len(inner) else 0, end)}
        if len(boxes) != length:
            continue
        if any((i+1, j) in boxes and (i, j+1) in boxes and
               (i+1, j+1) in boxes for i, j in boxes):
            continue
        reached = {next(iter(boxes))}
        fringe = set(reached)
        while fringe:
            step = {(i+di, j+dj) for i, j in fringe
                    for di, dj in ((1,0),(-1,0),(0,1),(0,-1))}
            fringe = step & boxes - reached
            reached |= fringe
        if len(reached) == length:
            result.append((inner, (-1)**(len({i for i, j in boxes}) - 1)))
    return tuple(result)


@lru_cache(maxsize=None)
def character(shape, cycle_type):
    if not cycle_type:
        return int(not shape)
    return sum(sign * character(inner, cycle_type[1:])
               for inner, sign in rim_hooks(shape, cycle_type[0]))


def z_factor(cycle_type):
    z = 1
    for k, multiplicity in Counter(cycle_type).items():
        z *= (k**multiplicity) * factorial(multiplicity)
    return z


def hook_dimension(shape):
    boxes = {(i, j) for i, size in enumerate(shape) for j in range(size)}
    result = factorial(len(boxes))
    hooks = 1
    for i, j in boxes:
        hooks *= 1 + sum((u == i and v > j) or (v == j and u > i)
                         for u, v in boxes)
    return result // hooks


def main():
    assert len(TRIPLES) == 35
    assert verify_orientation() == 720
    classes = tuple(partitions(N))
    chi6 = {}
    chi9 = {}
    fixed_counts = {}
    for mu in classes:
        p = permutation_of_type(mu)
        quotient = orbit_conflict_graph(p)
        minus_one = independence_polynomial_at_minus_one(quotient)
        fixed_counts[mu] = (len(quotient), minus_one)
        chi9[mu] = trace_on_six_set_cycles(p)
        # The reduced Lefschetz number is -I(quotient;-1) = chi6 - chi9.
        chi6[mu] = -minus_one + chi9[mu]
    assert chi6[(1,)*7] == 29
    assert chi9[(1,)*7] == 7
    for shape in classes:
        assert character(shape, (1,)*7) == hook_dimension(shape)
    for a in classes:
        for b in classes:
            inner = sum(character(a, mu) * character(b, mu)
                        * factorial(7) // z_factor(mu) for mu in classes)
            assert inner == (factorial(7) if a == b else 0)
    decomposition = {}
    for shape in classes:
        numerator = sum(chi6[mu] * character(shape, mu)
                        * factorial(7) // z_factor(mu) for mu in classes)
        assert numerator % factorial(7) == 0
        multiplicity = numerator // factorial(7)
        assert multiplicity >= 0
        if multiplicity:
            decomposition[shape] = multiplicity
    expected = {(7,): 1, (4,3): 1, (2,2,2,1): 1}
    assert decomposition == expected
    assert sum(hook_dimension(shape)*m for shape,m in decomposition.items()) == 29
    assert all(chi9[mu] == character((2,1,1,1,1,1),mu) + character((1,)*7,mu)
               for mu in classes)
    print('VERIFY_OK ground_points=7 triple_vertices=35 S7_classes=15 orientation_tests=720')
    print('VERIFY_OK identity_I_minus_one=-22 H6_dimension=29 H9_dimension=7')
    print('VERIFY_OK Specht_H6=',decomposition,'Specht_H9=((2,1,1,1,1,1),(1,1,1,1,1,1,1))')
    print('VERIFY_OK all_class_traces=',[(mu,chi6[mu],chi9[mu]) for mu in classes])
    print('VERIFY_OK exact_character_orthogonality_and_dimensions')

if __name__ == '__main__':
    main()
