"""Reproduce the exact census of forth-up/forth-down-confluent rooted-star frames.

Run with Python 3.9 or later: python verify.py
No nonstandard Python packages are required.
"""

from collections import Counter
from itertools import permutations
from math import factorial, gcd, prod


def cycles(permutation):
    """Cycles of a permutation represented by a tuple of images."""
    seen = set()
    result = []
    for i in range(len(permutation)):
        if i in seen:
            continue
        block = []
        while i not in seen:
            seen.add(i)
            block.append(i)
            i = permutation[i]
        result.append(tuple(block))
    return result


def partitions(n, high=None):
    if n == 0:
        yield ()
        return
    if high is None:
        high = n
    for p in range(min(n, high), 0, -1):
        for rest in partitions(n-p, p):
            yield (p,) + rest


def centralizer_size(shape):
    return prod(k**v*factorial(v) for k, v in Counter(shape).items())


def closed_form_fixed(shape):
    c = len(shape)
    g = [sum(gcd(x, y) for y in shape) for x in shape]
    G = sum(g)
    return (2**c + prod(2**(1+x)-1 for x in g)
            + 2**c*(prod(1+2**x for x in g)-2**G))


def labeled_formula(m):
    return (2**m + (2**(m+1)-1)**m
            + 2**m*((1+2**m)**m-2**(m*m)))


def orbit_formula(m):
    total = sum(factorial(m)//centralizer_size(shape) * closed_form_fixed(shape)
                for shape in partitions(m))
    assert total % factorial(m) == 0
    return total//factorial(m)


def image_mask(mask, perm):
    out = 0
    for index in range(len(perm)):
        if mask & (1 << index):
            out |= 1 << perm[index]
    return out


def directly_confluent(rows):
    """Literal quantifier checks, using 0 as the root and 1..m as leaves."""
    n = len(rows)
    for upper in range(1, n):
        # The only nontrivial order comparisons are 0 <= upper.
        for v in range(n):
            if rows[0] & (1 << v):
                if not any((rows[upper] & (1 << w)) and (v == 0 or w == v)
                           for w in range(n)):
                    return False
            if rows[upper] & (1 << v):
                if not any((rows[0] & (1 << w)) and (w == 0 or w == v)
                           for w in range(n)):
                    return False
    return True


def transform_relation(rows, leaf_perm):
    n = len(rows)
    full = (0,)+tuple(1+x for x in leaf_perm)
    moved = [0]*n
    for source, row in enumerate(rows):
        moved[full[source]] = image_mask(row, full)
    return tuple(moved)


def brute_census(m):
    n = m+1
    mask = (1 << n)-1
    permlist = list(permutations(range(m)))
    count = 0
    classes = set()
    for encoded in range(1 << (n*n)):
        rows = tuple((encoded >> (i*n))&mask for i in range(n))
        if not directly_confluent(rows):
            continue
        count += 1
        classes.add(min(transform_relation(rows, sigma) for sigma in permlist))
    return count, len(classes)


def independent_fixed_count(leaf_perm):
    """Enumerate invariant root rows and independent invariant leaf-row choices.

    This uses the original confluence quantifiers, not the normal-form formula.
    """
    m = len(leaf_perm)
    n = m+1
    full = (0,) + tuple(1+x for x in leaf_perm)
    leaf_cycles = cycles(leaf_perm)
    count = 0
    for root_row in range(1 << n):
        if image_mask(root_row, full) != root_row:
            continue
        choices = 1
        for cyc in leaf_cycles:
            cycle_length = len(cyc)
            count_here = 0
            for candidate in range(1 << n):
                row = candidate
                for _ in range(cycle_length):
                    row = image_mask(row, full)
                if row != candidate:
                    continue
                # Apply the two source/target confluence clauses directly.
                valid = True
                for v in range(n):
                    if (root_row >> v) & 1:
                        if not any(((candidate >> w) & 1) and (v == 0 or v == w)
                                   for w in range(n)):
                            valid = False
                            break
                    if (candidate >> v) & 1:
                        if not any(((root_row >> w) & 1) and (w == 0 or w == v)
                                   for w in range(n)):
                            valid = False
                            break
                if valid:
                    count_here += 1
            choices *= count_here
        count += choices
    return count


def check():
    # Two independent approaches: raw 0/1 matrix enumeration and cycle-type sum.
    for m in (1,2,3):
        raw = brute_census(m)
        expected = (labeled_formula(m), orbit_formula(m))
        assert raw == expected, (m,raw,expected)
    # A third route enumerates fixed relations directly under each relabeling.
    for m in range(1,6):
        by_type = {}
        for sigma in permutations(range(m)):
            shape = tuple(sorted((len(c) for c in cycles(sigma)), reverse=True))
            actual = independent_fixed_count(sigma)
            expected = closed_form_fixed(shape)
            assert actual == expected, (m,sigma,actual,expected)
            by_type[shape] = actual
        assert by_type[tuple([1]*m)] == labeled_formula(m)
    print('m | labelled | isomorphism classes')
    for m in range(2,7):
        print(m, labeled_formula(m), orbit_formula(m))
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
