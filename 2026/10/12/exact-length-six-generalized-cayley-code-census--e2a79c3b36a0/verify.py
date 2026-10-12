#!/usr/bin/env python3
from itertools import permutations
from collections import deque, Counter

N = 6
EXPECTED_MAXIMUM = 6
EXPECTED_LABELED_MAXIMA = 6000
EXPECTED_MAXIMAL_HIST = {4: 670320, 5: 82656, 6: 6000}
EXPECTED_LEFT_ORBITS = [120, 120] + [720] * 8
EXPECTED_NORMALIZED_MAXIMA = 50
EXPECTED_SUBGROUP_MAXIMA = 2
EXPECTED_GENERATOR_CYCLES = {
    (1, 2, 4, 6, 5, 3),
    (1, 3, 2, 6, 4, 5),
}


def compose(p, q):
    """Functional composition p o q in one-line notation, zero based."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return tuple(q)


def generalized_transpositions(n):
    e = tuple(range(n))
    out = set()
    for i1 in range(n):
        for j1 in range(i1, n):
            for i2 in range(j1 + 1, n):
                for j2 in range(i2, n):
                    phi = (
                        e[:i1]
                        + e[i2:j2 + 1]
                        + e[j1 + 1:i2]
                        + e[i1:j1 + 1]
                        + e[j2 + 1:]
                    )
                    if phi != e:
                        out.add(phi)
    return tuple(sorted(out))


def distance_from_identity(n, generators):
    e = tuple(range(n))
    dist = {e: 0}
    q = deque([e])
    while q:
        p = q.popleft()
        for g in generators:
            r = compose(p, g)
            if r not in dist:
                dist[r] = dist[p] + 1
                q.append(r)
    return dist


def compatibility_graph(perms, index, dist0):
    m = len(perms)
    adj = [0] * m
    for i, p in enumerate(perms):
        pinv = inverse(p)
        mask = 0
        for j, q in enumerate(perms):
            if i == j:
                continue
            rel = compose(pinv, q)
            if dist0[rel] >= 3:
                mask |= 1 << j
        adj[i] = mask
    return adj


def maximal_cliques(adj):
    n = len(adj)
    hist = Counter()
    maxima = []
    best_size = 0
    nodes = 0

    def rec(R, P, X):
        nonlocal best_size, nodes
        nodes += 1
        if not P and not X:
            s = R.bit_count()
            hist[s] += 1
            if s > best_size:
                best_size = s
                maxima.clear()
            if s == best_size:
                maxima.append(frozenset(i for i in range(n) if (R >> i) & 1))
            return

        union = P | X
        if union:
            z = union
            pivot = -1
            pivot_score = -1
            while z:
                bit = z & -z
                u = bit.bit_length() - 1
                score = (P & adj[u]).bit_count()
                if score > pivot_score:
                    pivot_score = score
                    pivot = u
                z -= bit
            cand = P & ~adj[pivot]
        else:
            cand = P

        while cand:
            vbit = cand & -cand
            v = vbit.bit_length() - 1
            rec(R | vbit, P & adj[v], X & adj[v])
            P &= ~vbit
            X |= vbit
            cand &= ~vbit

    rec(0, (1 << n) - 1, 0)
    return hist, best_size, maxima, nodes


def left_multiplication_maps(perms, index):
    maps = []
    for a in perms:
        maps.append(tuple(index[tuple(a[v] for v in p)] for p in perms))
    return maps


def left_orbits(maxima_set, left_maps):
    unseen = set(maxima_set)
    sizes = []
    while unseen:
        C = next(iter(unseen))
        orbit = set()
        for lm in left_maps:
            orbit.add(frozenset(lm[i] for i in C))
        if not orbit <= maxima_set:
            raise AssertionError("left multiplication failed to preserve maximum codes")
        sizes.append(len(orbit))
        unseen.difference_update(orbit)
    return sorted(sizes)


def is_subgroup(code, perms):
    ps = [perms[i] for i in code]
    S = set(ps)
    return all(compose(a, b) in S for a in ps for b in ps)


def cycle_tuple(p):
    seen = [False] * len(p)
    cycles = []
    for start in range(len(p)):
        if seen[start]:
            continue
        cyc = []
        x = start
        while not seen[x]:
            seen[x] = True
            cyc.append(x + 1)
            x = p[x]
        if len(cyc) > 1:
            cycles.append(tuple(cyc))
    return cycles


def canonical_generator_cycle(code, perms):
    gens = []
    for i in code:
        cyc = cycle_tuple(perms[i])
        if len(cyc) == 1 and len(cyc[0]) == 6:
            # A cyclic subgroup of order six has two inverse six-cycle generators.
            gens.append(cyc[0])
    if len(gens) != 2:
        raise AssertionError("expected exactly two six-cycle generators")
    return min(gens)


def main():
    perms = list(permutations(range(N)))
    index = {p: i for i, p in enumerate(perms)}
    e = tuple(range(N))
    eidx = index[e]

    gens = generalized_transpositions(N)
    assert len(gens) == 70

    dist0 = distance_from_identity(N, gens)
    assert len(dist0) == 720
    distance_hist = Counter(dist0.values())
    assert dict(sorted(distance_hist.items())) == {0: 1, 1: 70, 2: 469, 3: 180}

    adj = compatibility_graph(perms, index, dist0)
    degrees = {x.bit_count() for x in adj}
    assert degrees == {180}
    edges = sum(x.bit_count() for x in adj) // 2
    assert edges == 64800

    hist, maximum, maxima, bk_nodes = maximal_cliques(adj)
    assert maximum == EXPECTED_MAXIMUM
    assert len(maxima) == EXPECTED_LABELED_MAXIMA
    assert dict(sorted(hist.items())) == EXPECTED_MAXIMAL_HIST

    # Since the diameter is three, all distinct words in a maximum code are
    # automatically at generalized Cayley distance exactly three.
    for C in maxima:
        for i in C:
            for j in C:
                if i < j:
                    rel = compose(inverse(perms[i]), perms[j])
                    assert dist0[rel] == 3

    maxima_set = set(maxima)
    normalized = [C for C in maxima if eidx in C]
    assert len(normalized) == EXPECTED_NORMALIZED_MAXIMA

    subgroup_codes = [C for C in normalized if is_subgroup(C, perms)]
    assert len(subgroup_codes) == EXPECTED_SUBGROUP_MAXIMA
    generators = {canonical_generator_cycle(C, perms) for C in subgroup_codes}
    assert generators == EXPECTED_GENERATOR_CYCLES

    left_maps = left_multiplication_maps(perms, index)
    orbit_sizes = left_orbits(maxima_set, left_maps)
    assert orbit_sizes == sorted(EXPECTED_LEFT_ORBITS)

    print(
        "VERIFY_OK "
        f"generators={len(gens)} distance_hist=0:1,1:70,2:469,3:180 "
        f"vertices={len(perms)} edges={edges} degree=180 "
        f"maximal_cliques={sum(hist.values())} "
        "maximal_hist=4:670320,5:82656,6:6000 "
        f"maximum={maximum} labeled_maxima={len(maxima)} "
        f"normalized_maxima={len(normalized)} subgroup_maxima={len(subgroup_codes)} "
        "left_orbits=10 orbit_sizes=120x2,720x8 "
        "subgroup_generators=(1,2,4,6,5,3);(1,3,2,6,4,5) "
        f"bk_nodes={bk_nodes}"
    )


if __name__ == "__main__":
    main()
