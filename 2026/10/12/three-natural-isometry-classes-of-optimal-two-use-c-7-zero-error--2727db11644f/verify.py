#!/usr/bin/env python3
"""Exhaustive verification for maximum two-use C7 zero-error codes."""

from collections import Counter
from itertools import combinations
from hashlib import sha256

N = 7
VERTICES = [(i, j) for i in range(N) for j in range(N)]
INDEX = {v: k for k, v in enumerate(VERTICES)}


def cyclic_distance(a, b):
    d = abs(a - b) % N
    return min(d, N - d)


def build_compatibility():
    """Adjacency masks in the graph whose cliques are zero-error codes."""
    masks = []
    for a, (i, j) in enumerate(VERTICES):
        mask = 0
        for b, (k, ell) in enumerate(VERTICES):
            if a == b:
                continue
            confusable = cyclic_distance(i, k) <= 1 and cyclic_distance(j, ell) <= 1
            if not confusable:
                mask |= 1 << b
        masks.append(mask)
    return masks


COMPAT = build_compatibility()


def enumerate_target(target, collect=False):
    """Enumerate cliques of exactly target vertices without duplication."""
    solutions = []
    nodes = 0

    def rec(chosen, candidates):
        nonlocal nodes
        nodes += 1
        if len(chosen) == target:
            if collect:
                solutions.append(tuple(chosen))
            return 1
        if len(chosen) + candidates.bit_count() < target:
            return 0
        count = 0
        while candidates:
            if len(chosen) + candidates.bit_count() < target:
                break
            bit = candidates & -candidates
            candidates -= bit
            v = bit.bit_length() - 1
            count += rec(chosen + (v,), candidates & COMPAT[v])
        return count

    count = rec(tuple(), (1 << len(VERTICES)) - 1)
    return count, solutions, nodes


def group_permutations():
    """Natural isometries: independent D14 actions and coordinate interchange."""
    perms = []
    for ax in range(N):
        for sx in (1, -1):
            for ay in range(N):
                for sy in (1, -1):
                    for swap in (False, True):
                        perm = []
                        for x, y in VERTICES:
                            xx = (sx * x + ax) % N
                            yy = (sy * y + ay) % N
                            if swap:
                                xx, yy = yy, xx
                            perm.append(INDEX[(xx, yy)])
                        perms.append(tuple(perm))
    assert len(perms) == 392
    assert len(set(perms)) == 392
    return perms


GROUP = group_permutations()


def transform(code, perm):
    return tuple(sorted(perm[v] for v in code))


def canonical(code):
    return min(transform(code, perm) for perm in GROUP)


def distance_signature(code):
    """Invariant histogram of unordered coordinate-distance pairs."""
    points = [VERTICES[v] for v in code]
    hist = Counter()
    for p, q in combinations(points, 2):
        d1 = cyclic_distance(p[0], q[0])
        d2 = cyclic_distance(p[1], q[1])
        hist[tuple(sorted((d1, d2)))] += 1
    return tuple(sorted(hist.items()))


def fmt_code(code):
    return "{" + ",".join(f"({VERTICES[v][0]},{VERTICES[v][1]})" for v in code) + "}"


def main():
    count11, _, nodes11 = enumerate_target(11, collect=False)
    count10, maxima, nodes10 = enumerate_target(10, collect=True)

    assert count11 == 0
    assert count10 == 980
    assert len(maxima) == 980

    maxima_set = set(maxima)
    for code in maxima:
        assert len(code) == 10
        for u, v in combinations(code, 2):
            assert COMPAT[u] & (1 << v)

    classes = {}
    for code in maxima:
        classes.setdefault(canonical(code), []).append(code)
    assert len(classes) == 3

    data = []
    for rep, members in sorted(classes.items()):
        orbit = {transform(rep, perm) for perm in GROUP}
        stabilizer = sum(transform(rep, perm) == rep for perm in GROUP)
        assert orbit == set(members)
        assert len(orbit) * stabilizer == len(GROUP)
        data.append((rep, len(orbit), stabilizer, distance_signature(rep)))

    orbit_sizes = [x[1] for x in data]
    stabilizers = [x[2] for x in data]
    assert orbit_sizes == [392, 196, 392]
    assert stabilizers == [1, 2, 1]
    assert sum(orbit_sizes) == 980
    assert len({x[3] for x in data}) == 3

    census_text = "\n".join(
        ",".join(f"{VERTICES[v][0]}{VERTICES[v][1]}" for v in code)
        for code in sorted(maxima)
    ) + "\n"
    census_hash = sha256(census_text.encode("ascii")).hexdigest()
    assert census_hash == "7bedb501045012255db706cd7e32facf1e07891edeac480c48a721885fb0e3ab"

    print(
        "VERIFY_OK "
        f"vertices={len(VERTICES)} target11={count11} maximum=10 "
        f"labeled_maxima={count10} group={len(GROUP)} orbits={len(data)} "
        f"orbit_sizes={','.join(map(str, orbit_sizes))} "
        f"stabilizers={','.join(map(str, stabilizers))} "
        f"nodes11={nodes11} nodes10={nodes10} census_sha256={census_hash}"
    )
    for i, (rep, orbit_size, stabilizer, signature) in enumerate(data, 1):
        sig = ";".join(f"{a}{b}:{m}" for (a, b), m in signature)
        print(
            f"CLASS_{i} orbit={orbit_size} stabilizer={stabilizer} "
            f"signature={sig} representative={fmt_code(rep)}"
        )


if __name__ == "__main__":
    main()
