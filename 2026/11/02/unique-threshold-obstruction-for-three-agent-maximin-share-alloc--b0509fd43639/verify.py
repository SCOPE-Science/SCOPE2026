#!/usr/bin/env python3
"""Independent exhaustive finite check of a three-agent MMS partition obstruction.

Run with Python 3.9 or later. No external dependencies.
"""
from itertools import permutations, product


def partitions(m):
    """All unordered partitions of range(m) into three nonempty blocks."""
    result = set()
    for coloring in product(range(3), repeat=m):
        blocks = tuple(sorted(tuple(i for i, c in enumerate(coloring) if c == j)
                              for j in range(3)))
        if all(blocks):
            result.add(blocks)
    return sorted(result)


def rainbow(triple):
    return any(not (set(a) & set(b) or set(a) & set(c) or set(b) & set(c))
               for a, b, c in product(*triple))


def is_exceptional(triple):
    singles = [next((b[0] for b in part if len(b) == 1), -1)
               for part in triple]
    if any(sum(len(b) == 1 for b in part) != 1 for part in triple):
        return False
    if len(set(singles)) != 1:
        return False
    matchings = [tuple(sorted(b for b in part if len(b) == 2)) for part in triple]
    return len(set(matchings)) == 3


def canon(triple, m):
    signatures = []
    for perm in permutations(range(m)):
        mapped = tuple(tuple(sorted(tuple(sorted(perm[x] for x in block))
                                   for block in part)) for part in triple)
        signatures.append(min(tuple(mapped[i] for i in order)
                              for order in permutations(range(3))))
    return min(signatures)


def witness_value(part, bundle):
    return int(any(set(p).issubset(bundle) for p in part))


def check():
    sizes = {}
    for m in (3, 4):
        pp = partitions(m)
        for t in product(pp, repeat=3):
            assert rainbow(t), (m, t)
        sizes[m] = len(pp) ** 3
    pp = partitions(5)
    assert len(pp) == 25
    bad = [t for t in product(pp, repeat=3) if not rainbow(t)]
    assert len(bad) == 30, len(bad)
    assert sum(is_exceptional(t) for t in product(pp, repeat=3)) == 30
    assert all(is_exceptional(t) for t in bad)
    representatives = {canon(t, 5) for t in bad}
    assert len(representatives) == 1, len(representatives)
    robust_extensions_checked = 0
    for triple in bad:
        # The 0-1 threshold valuations have MMS exactly 1 for all agents.
        assert all(min(witness_value(part, set(block)) for block in part) == 1
                   for part in triple)
        assert not any(all(witness_value(triple[i],
                          {j for j, owner in enumerate(owners) if owner == i})
                          for i in range(3))
                       for owners in product(range(3), repeat=5))
        singleton = next(b[0] for b in triple[0] if len(b) == 1)
        for i in range(3):
            for mask in range(1, 1 << 5):
                extra = {j for j in range(5) if mask & (1 << j)}
                if singleton in extra or witness_value(triple[i], extra):
                    continue
                def augmented(j, bundle):
                    return witness_value(triple[j], bundle) or (j == i and extra <= bundle)
                assert any(all(augmented(j, {u for u, owner in enumerate(owners)
                                            if owner == j}) for j in range(3))
                           for owners in product(range(3), repeat=5))
                robust_extensions_checked += 1
    assert robust_extensions_checked == 720, robust_extensions_checked
    print("VERIFY_OK partitions_5=25 profiles_5=15625 "
          "obstructions=30 unlabelled_orbits=1 "
          f"profiles_3={sizes[3]} profiles_4={sizes[4]} "
          f"valuations_and_allocations_checked=30x243 "
          f"proper_acceptable_extensions_checked={robust_extensions_checked}")


if __name__ == '__main__':
    check()
