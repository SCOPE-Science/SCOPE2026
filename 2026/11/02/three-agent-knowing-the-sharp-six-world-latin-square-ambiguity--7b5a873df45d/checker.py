"""Exhaustive labelled six-world three-agent S5 observational-fiber census.

Run with Python 3.9 or later: python3 checker.py
Only the standard library is used. The finite census supplements the
symbolic reconstruction theorem; it does not prove its unbounded scope.
"""
from collections import Counter, defaultdict
from itertools import product


def set_partitions(n):
    """Enumerate each partition of {0,...,n-1} exactly once by induction."""
    if n == 0:
        yield ()
        return
    for part in set_partitions(n - 1):
        yield part + ((n - 1,),)
        for j in range(len(part)):
            yield part[:j] + (part[j] + (n - 1,),) + part[j + 1:]


def block_at_world(part, n):
    rows = [0] * n
    for block in part:
        mask = sum(1 << x for x in block)
        for x in block:
            rows[x] = mask
    return tuple(rows)


def minimal_observations(a, b, c):
    """Return locally irredundant three-generator signature or None."""
    out = []
    for x, y, z in zip(a, b, c):
        if (x & y) in (x, y) or (x & z) in (x, z) or (y & z) in (y, z):
            return None
        out.append(tuple(sorted((x, y, z))))
    return tuple(out)


def direct_someone_knows(a, b, c, subset):
    return tuple(((x & subset) == x or (y & subset) == y
                  or (z & subset) == z) for x, y, z in zip(a, b, c))


def unique_k33_signature(sig):
    """Check that the nine minimal blocks are edges of a labelled K(3,3)."""
    blocks = {mask for row in sig for mask in row}
    if len(blocks) != 9 or any(mask.bit_count() != 2 for mask in blocks):
        return False
    adj = [0] * 6
    for mask in blocks:
        u, v = (i for i in range(6) if (mask >> i) & 1)
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    for split in range(1 << 6):
        if split.bit_count() != 3 or not (split & 1):
            continue
        if all(adj[v] == (((1 << 6) - 1) ^ split) if (split >> v) & 1
               else adj[v] == split for v in range(6)):
            return True
    return False


def census(n):
    frames = [block_at_world(p, n) for p in set_partitions(n)]
    counts = defaultdict(int)
    for a in frames:
        for b in frames:
            for c in frames:
                signature = minimal_observations(a, b, c)
                if signature is not None:
                    counts[signature] += 1
    return len(frames), counts


if __name__ == '__main__':
    expected_bell = {1: 1, 2: 2, 3: 5, 4: 15, 5: 52, 6: 203}
    expected_signatures = {4: (1, 6), 5: (30, 180), 6: (825, 5010)}
    for n in range(1, 7):
        n_parts, counts = census(n)
        assert n_parts == expected_bell[n]
        if n < 4:
            assert not counts
        else:
            assert (len(counts), sum(counts.values())) == expected_signatures[n]
            distribution = Counter(counts.values())
            if n <= 5:
                assert distribution == {6: len(counts)}
            else:
                assert distribution == {6: 815, 12: 10}
                ambiguous = [sig for sig, size in counts.items() if size == 12]
                assert len(ambiguous) == 10
                assert all(unique_k33_signature(sig) for sig in ambiguous)
        print(f'n={n}: partitions={n_parts}, signatures={len(counts)}, '
              f'ordered_frames={sum(counts.values())}')

    # A direct six-world signature, with classes specified by bit masks.
    aa = (17, 6, 6, 40, 17, 40)
    bb = (3, 3, 12, 12, 48, 48)
    cc = (9, 34, 20, 9, 20, 34)
    target = minimal_observations(aa, bb, cc)
    assert target is not None
    _, classes = census(6)
    assert classes[target] == 12
    assert unique_k33_signature(target)
    all_blocks = sorted({mask for triple in target for mask in triple})
    cross_edges = [(i, j) for i in range(9) for j in range(i + 1, 9)
                   if (all_blocks[i] & all_blocks[j]) != 0]
    proper_colourings = sum(all(colours[i] != colours[j]
                               for i, j in cross_edges)
                            for colours in product(range(3), repeat=9))
    assert proper_colourings == 12
    for subset in range(1 << 6):
        from_blocks = tuple(any((mask & subset) == mask for mask in triple)
                            for triple in target)
        assert from_blocks == direct_someone_knows(aa, bb, cc, subset)
    print('six_world_K33_edge_colours=12; nontrivial_signatures=10')
    print('ALL_CHECKS_OK')
