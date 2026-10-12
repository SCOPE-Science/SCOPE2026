"""Finite independent checks for bounded ternary-power permutation completions.
Python 3 standard library only. Test complete admissible six-item instances with small targets.
The mathematical NP-completeness proof is independent of these finite checks.
"""
from functools import lru_cache
from itertools import combinations_with_replacement


def transform(items, B):
    assert len(items) % 3 == 0 and sum(items) == len(items) // 3 * B
    assert all(4 * a > B and 2 * a < B for a in items)
    Q = 1
    while Q < B:
        Q *= 3
    C = Q - B
    P = 3 * Q
    transformed = tuple(3 * a + C for a in items)
    assert sum(transformed) == (len(items) // 3) * P
    assert all(4 * x > P and 2 * x < P for x in transformed)
    return P, transformed


def full_grouping(items, targets):
    """Exhaustive indexed-subset DP, *independent* of the proof's triples argument."""
    n = len(items)
    full = (1 << n) - 1
    subset_sums = [0] * (1 << n)
    for mask in range(1, 1 << n):
        bit = mask & -mask
        j = bit.bit_length() - 1
        subset_sums[mask] = subset_sums[mask ^ bit] + items[j]
    @lru_cache(None)
    def visit(rest):
        if rest == 0:
            return True
        low_bit = rest & -rest
        sub = rest
        while sub:
            if (sub & low_bit) and subset_sums[sub] in targets and visit(rest ^ sub):
                return True
            sub = (sub - 1) & rest
        return False
    return visit(full)


def fast_partition(items, target):
    """Separate recursive 3-partition search, not using admissible subset packing."""
    n = len(items)
    @lru_cache(None)
    def visit(indices):
        if not indices:
            return True
        a = indices[0]
        for i in range(1, len(indices)):
            for j in range(i + 1, len(indices)):
                if items[a] + items[indices[i]] + items[indices[j]] == target:
                    rest = tuple(t for t in indices if t not in (a, indices[i], indices[j]))
                    if visit(rest):
                        return True
        return False
    return visit(tuple(range(n)))


def make_witness(items, B):
    """Construct a permutation cycle by cycle from a valid triple partition."""
    P, lengths = transform(items, B)
    indices = tuple(range(len(items)))
    groups = []
    def solve(left):
        if not left:
            return True
        a = left[0]
        for i in range(1, len(left)):
            for j in range(i + 1, len(left)):
                b, c = left[i], left[j]
                if items[a] + items[b] + items[c] == B:
                    groups.append((a, b, c))
                    if solve(tuple(t for t in left if t not in (a, b, c))):
                        return True
                    groups.pop()
        return False
    if not solve(indices):
        return None
    starts = []
    p = 0
    for size in lengths:
        starts.append(p)
        p += size
    perm = [-1] * p
    for start, size in zip(starts, lengths):
        for t in range(size - 1):
            perm[start + t] = start + t + 1
    for grp in groups:
        for j, t in enumerate(grp):
            nxt = grp[(j + 1) % 3]
            perm[starts[t] + lengths[t] - 1] = starts[nxt]
    assert sorted(perm) == list(range(p))
    for start, size in zip(starts, lengths):
        for j in range(size - 1):
            assert perm[start + j] == start + j + 1
    visited = set()
    for i in range(p):
        if i in visited:
            continue
        j = i
        cycle = []
        while j not in visited:
            visited.add(j)
            cycle.append(j)
            j = perm[j]
        assert j == i and len(cycle) == P
    return P, perm


def check_fixed_exponent_dp():
    """Compare polynomial-for-fixed-K type-count DP against direct indexed partition."""
    from itertools import product
    K = 2
    sizes = tuple(3 ** j for j in range(K + 1))
    def count_dp(lengths):
        vals = tuple(lengths.count(i) for i in range(1, sizes[-1] + 1))
        @lru_cache(None)
        def visit(counts):
            if not any(counts):
                return True
            first = next(i for i, x in enumerate(counts) if x)
            def subset(i, rem, taking):
                if i == len(counts):
                    if rem == 0:
                        nxt = tuple(a - b for a, b in zip(counts, taking))
                        return visit(nxt)
                    return False
                low = 1 if i == first else 0
                for q in range(low, min(counts[i], rem // (i+1)) + 1):
                    if subset(i + 1, rem - q*(i+1), taking+(q,)):
                        return True
                return False
            for target in sizes:
                if target >= first + 1 and subset(0, target, ()):
                    return True
            return False
        return visit(vals)
    t = 0
    for n in range(1, 7):
        for lengths in combinations_with_replacement(range(1, 10), n):
            got = count_dp(lengths)
            want = full_grouping(lengths, set(sizes))
            assert got == want, (lengths, got, want)
            t += 1
    return t


def main():
    cases = 0
    yes = 0
    witness = 0
    for B in range(8, 49):
        choices = [a for a in range(1, B) if B < 4 * a and 2 * a < B]
        for items in combinations_with_replacement(choices, 6):
            if sum(items) != 2 * B:
                continue
            P, enlarged = transform(items, B)
            rhs = full_grouping(enlarged, {P, P // 3})
            lhs = fast_partition(items, B)
            assert lhs == rhs, (items, B, P, enlarged, lhs, rhs)
            cases += 1
            yes += bool(lhs)
            if lhs and witness < 15:
                assert make_witness(items, B) is not None
                witness += 1
    assert fast_partition((4,4,4,6,6,6), 15) is False
    assert fast_partition((4,5,5,5,5,6), 15) is True
    tests = check_fixed_exponent_dp()
    print(f"VERIFICATION_OK three_partition_instances={cases} positive={yes} constructed_permutation_witnesses={witness} fixed_exponent_DP_tests={tests}")

if __name__ == '__main__':
    main()
