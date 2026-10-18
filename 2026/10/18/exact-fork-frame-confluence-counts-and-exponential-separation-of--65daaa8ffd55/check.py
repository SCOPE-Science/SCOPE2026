"""Independent finite tests for FIK/IK rooted-fork confluence counts.

Run: python3 check.py
No external dependencies.  All bit positions are labeled: 0 is the root.
"""
from collections import defaultdict
from math import comb


def formula(k):
    """Closed sums obtained by row classification and inclusion-exclusion."""
    assert k >= 1
    base = 2 ** (k * (k + 1))
    f = base + (2 ** (k + 1) - 1) ** k
    f += 2 * sum(comb(k, j) * 2 ** (k * (k + 1 - j))
                 for j in range(1, k + 1))
    # Root has no arrows to leaves and has no loop.
    i = (2 ** k + 1) ** k
    # Root has a loop and no arrows to leaves.
    i += 2 ** (k * k) + sum(
        (-1) ** t * comb(k, t) * (2 ** (k - t) - 1) ** k
        for t in range(1, k + 1))
    # Root points to j>0 leaves: root loop absent/present.
    for j in range(1, k + 1):
        m = k - j
        no_loop = (2 ** m + 1) ** k
        with_loop = no_loop + sum(
            (-1) ** t * comb(m, t) * 2 ** (k * (m - t))
            for t in range(1, m + 1))
        i += comb(k, j) * (no_loop + with_loop)
    return f, i


def matrix_semantics(k, bitset):
    """Evaluate the ORIGINAL quantified frame axioms, no normal-form shortcuts."""
    n = k + 1
    def edge(x, y):
        return bool(bitset & (1 << (n*x + y)))
    def leq(x, y):
        return x == y or (x == 0 and y > 0)
    fc = all(
        any(edge(xp, zp) and leq(z, zp) for zp in range(n))
        for x in range(n) for xp in range(n) for z in range(n)
        if leq(x, xp) and edge(x, z))
    bc = all(
        any(edge(xp, zp) and leq(x, xp) for xp in range(n))
        for x in range(n) for z in range(n) for zp in range(n)
        if edge(x, z) and leq(z, zp))
    return fc, bc


def direct_all(k):
    f = i = 0
    for bits in range(1 << ((k + 1) ** 2)):
        fc, bc = matrix_semantics(k, bits)
        f += fc
        i += fc and bc
    return f, i


def separate_rows(k):
    """Independent dynamic count over actual row bitmasks, not closed sums.

    Each possible root row is considered. Leaf rows are individually scanned;
    an OR-mask state tracks leaf columns hit, including those from the root.
    """
    n = k + 1
    full_leaf = (1 << k) - 1
    out = []
    for include_bc in (False, True):
        count = 0
        for rootrow in range(1 << n):
            has_root_edge = bool(rootrow & 1)
            root_leaf = rootrow >> 1
            candidate = []
            for leafrow in range(1 << n):
                leaf_leaf = leafrow >> 1
                # Forward confluence against o<=each leaf.
                if has_root_edge and leafrow == 0:
                    continue
                if (leaf_leaf & root_leaf) != root_leaf:
                    continue
                # Backward confluence for leaf->o.
                if include_bc and (leafrow & 1) and leaf_leaf != full_leaf:
                    continue
                candidate.append(leaf_leaf)
            dp = {root_leaf: 1}
            for _ in range(k):
                nxt = defaultdict(int)
                for seen, ways in dp.items():
                    for row_leaf in candidate:
                        nxt[seen | row_leaf] += ways
                dp = nxt
            if include_bc and has_root_edge:
                # Backward confluence from o->o to every leaf target.
                count += dp.get(full_leaf, 0)
            else:
                count += sum(dp.values())
        out.append(count)
    return tuple(out)


def main():
    full_cases = 0
    for k in range(1, 4):
        observed = direct_all(k)
        expected = formula(k)
        assert observed == expected, ('quantified semantics', k, observed, expected)
        full_cases += 2 ** ((k + 1) ** 2)
    for k in range(1, 7):
        observed = separate_rows(k)
        expected = formula(k)
        assert observed == expected, ('row dynamic program', k, observed, expected)
        print('k=', k, 'FIK=', expected[0], 'IK=', expected[1])
    print('PASS: full quantified frame tests for', full_cases,
          'binary relations; independently counted rows for k=1..6')

if __name__ == '__main__':
    main()
