#!/usr/bin/env python3
"""Independent finite checks for circular two-block partition shattering.

Runs with Python 3.10+ and no third-party packages. Logical uses of the finite
computations and the all-size reduction are detailed in RESULT.md.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


def pairs(n):
    return tuple(combinations(range(n), 2))


def masks_from_cuts(n):
    """Distinct unordered pairs of cuts after n cyclic vertex positions.

    Concept bit 1 means endpoints are in different blocks.
    """
    queries = pairs(n)
    concepts = []
    for a, b in pairs(n):
        word = 0
        for i, (u, v) in enumerate(queries):
            # Exactly one of the two cuts lies on the forward arc u..v-1.
            if (u <= a < v) ^ (u <= b < v):
                word |= 1 << i
        concepts.append(word)
    assert len(set(concepts)) == comb(n, 2)
    return queries, tuple(concepts)


def masks_from_partition_labels(n):
    """Independent direct cyclic split construction, no parity formula."""
    queries = pairs(n)
    result = []
    for a, b in pairs(n):
        color = [0] * n
        for x in range(a + 1, b + 1):
            color[x] = 1
        word = sum((color[u] != color[v]) << i
                   for i, (u, v) in enumerate(queries))
        result.append(word)
    return queries, tuple(result)


def all_matchings(indices):
    """Enumerates every pairing, exactly (2k-1)!! on 2k points."""
    if not indices:
        yield ()
        return
    first = indices[0]
    for j in range(1, len(indices)):
        for rest in all_matchings(indices[1:j] + indices[j+1:]):
            yield ((first, indices[j]),) + rest


def chord_signatures_direct(matching):
    """Evaluate intervals of positions on endpoints using direct membership."""
    n = 2 * len(matching)
    seen = set()
    for a, b in combinations(range(n), 2):
        # Cut after a and b; one block is vertex interval a+1,...,b.
        bits = 0
        for j, (u, v) in enumerate(matching):
            if (a < u <= b) ^ (a < v <= b):
                bits |= 1 << j
        seen.add(bits)
    return seen


def chord_signatures_parity(matching):
    """Independent incremental parity walk around the 2k endpoints."""
    n = 2 * len(matching)
    partial = [0] * n
    w = 0
    for vertex in range(n):
        for j, (u, v) in enumerate(matching):
            if vertex == u or vertex == v:
                w ^= 1 << j
        partial[vertex] = w
    assert partial[-1] == 0
    return {partial[a] ^ partial[b] for a, b in pairs(n)}


def exact_vc(queries, concepts):
    for k in range(1, min(6, len(queries)) + 1):
        found = False
        for selected in combinations(range(len(queries)), k):
            signatures = {sum(((hypothesis >> q) & 1) << j
                              for j, q in enumerate(selected))
                          for hypothesis in concepts}
            if len(signatures) == 2 ** k:
                found = True
                break
        if not found:
            return k - 1
    return min(6, len(queries))


def ldim_and_tree(n):
    queries, concepts = masks_from_cuts(n)
    H = len(concepts)
    cols = tuple(sum(1 << h for h, c in enumerate(concepts) if (c >> q) & 1)
                 for q in range(len(queries)))
    @lru_cache(maxsize=None)
    def dim(state):
        m = state.bit_count()
        if m <= 1:
            return 0
        bound = m.bit_length() - 1
        best = 0
        for q, col in enumerate(cols):
            positive = state & col
            negative = state ^ positive
            if not positive or not negative:
                continue
            if min(positive.bit_count(), negative.bit_count()) < 1 << best:
                continue
            cand = 1 + min(dim(positive), dim(negative))
            best = max(best, cand)
            if best == bound:
                break
        return best

    def witness_tree(state, d):
        if d == 0:
            assert state
            return {"hypothesis_cut_indices": list(pairs(n)[(state & -state).bit_length()-1])}
        for q, col in enumerate(cols):
            one = state & col
            zero = state ^ one
            if one and zero and dim(one) >= d - 1 and dim(zero) >= d - 1:
                return {"query": list(queries[q]),
                        "zero": witness_tree(zero, d-1),
                        "one": witness_tree(one, d-1)}
        raise AssertionError("No depth certificate")

    d = dim((1 << H) - 1)
    cert = witness_tree((1 << H) - 1, d)
    def replay(node, constraints, depth):
        if depth == 0:
            a,b = node["hypothesis_cut_indices"]
            assert 0 <= a < b < n
            for q,val in constraints:
                u,v = queries[q]
                assert (((u<=a<v) ^ (u<=b<v)) == bool(val))
            return 1
        q = queries.index(tuple(node["query"]))
        return (replay(node["zero"], constraints + ((q,0),), depth-1)
                + replay(node["one"], constraints + ((q,1),), depth-1))
    leaves = replay(cert, (), d)
    assert leaves == 2 ** d
    return d, cert, dim.cache_info().currsize


def main():
    # Exact enumeration and independent cyclic-label implementation.
    for n in range(2, 17):
        q,c = masks_from_cuts(n)
        assert (q,c) == masks_from_partition_labels(n)
        assert len(c) == comb(n, 2)
    print("PAIR_CUT_MODEL_PASS n=2..16", flush=True)

    # All distinct-endpoint chord diagrams for five selected queries.
    hist = Counter()
    total = 0
    for matching in all_matchings(tuple(range(10))):
        s0 = chord_signatures_direct(matching)
        s1 = chord_signatures_parity(matching)
        assert s0 == s1
        hist[len(s0)] += 1
        total += 1
        assert len(s0) < 32
    assert total == 945
    assert max(hist) == 30
    assert hist == {16:42,19:120,21:186,22:50,23:45,24:220,
                    25:70,26:40,27:150,30:22}
    print("FIVE_CHORD_UNIVERSAL_OBSTRUCTION_PASS diagrams=945 max_signatures=30 histogram="
          + str(sorted(hist.items())), flush=True)

    # Four queried pairs on 7 cyclic vertices, with all 16 patterns realized.
    q,c = masks_from_cuts(7)
    support = ((0,2),(0,4),(1,3),(1,5))
    indices = [q.index(e) for e in support]
    witnessed = {sum(((h >> k) & 1) << j for j,k in enumerate(indices)) for h in c}
    assert witnessed == set(range(16))
    print("FOUR_QUERY_SHATTERED_WITNESS_PASS n=7 patterns=16", flush=True)

    # Confirm the exact small-size VC threshold independently by brute force.
    target = {2:0,3:1,4:2,5:2,6:3,7:4,8:4}
    for n,expected in target.items():
        q,c = masks_from_partition_labels(n)
        found = exact_vc(q,c)
        assert found == expected, (n,found)
    print("SMALL_VC_DIMENSIONS_PASS " + str(target), flush=True)

    # Exact adaptive dimensions by the recurrence, with replayed trees.
    dims = {}
    states = {}
    for n in range(2,17):
        d, tree, number = ldim_and_tree(n)
        dims[n] = d
        states[n] = number
    assert dims == {2:0,3:1,4:2,5:3,6:3,7:4,8:4,9:5,
                    10:5,11:5,12:6,13:6,14:6,15:6,16:6}
    print("SMALL_LITTLESTONE_DIMENSIONS_PASS " + str(dims), flush=True)
    assert dims[4] == 2 and dims[5] == 3
    print("FIRST_STRICT_GAP_PASS n=5 VC=2 Littlestone=3", flush=True)
    print("CIRCULAR_TWO_BLOCK_ALL_CHECKS_PASS", flush=True)

if __name__ == '__main__':
    main()
