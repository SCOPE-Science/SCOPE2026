"""Finite exact checks for the dyadic multiplicative-coset moment theorem.

Execute with Python 3. No external dependencies. Verification enumerates all
multiplicative subgroups and all cosets for each modulus 4,...,1024.
"""
from collections import Counter


def all_subgroups(a):
    modulus = 1 << a
    units = tuple(range(1, modulus, 2))
    visited = set()
    subs = []
    for t in units:
        h = frozenset(pow(t, k, modulus) for k in range(1 << (a - 1)))
        if h not in visited:
            visited.add(h)
            subs.append(h)
    # A subgroup containing -1 need not be cyclic; add all <-1,g>.
    for h in tuple(subs):
        j = frozenset(h | frozenset((-x) % modulus for x in h))
        if j not in visited:
            visited.add(j)
            subs.append(j)
    return subs


def check():
    subgroups_checked = 0
    cosets_checked = 0
    for a in range(2, 11):
        modulus = 1 << a
        units = set(range(1, modulus, 2))
        subs = all_subgroups(a)
        expected_count = (3*a - 4) if a >= 3 else 2
        assert len(subs) == expected_count, (a, len(subs), expected_count)
        subgroups_checked += len(subs)
        for h in subs:
            size = len(h)
            pending = set(units)
            defects = []
            half_counts = []
            while pending:
                u = min(pending)
                coset = {(u*x) % modulus for x in h}
                assert coset <= pending
                pending.difference_update(coset)
                defects.append(sum(coset) - modulus*size//2)
                half_counts.append(sum(x < modulus//2 for x in coset))
                cosets_checked += 1
            balanced = (-1 % modulus) in h
            if balanced:
                assert all(d == 0 for d in defects), (a,h,defects)
                continue
            j = size.bit_length()-1
            assert size == 1 << j and j <= a-2
            L = modulus//size
            # Trivial graph U_j (identity coset is all 1 mod L).
            is_U = all(x % L == 1 for x in h)
            if is_U:
                expected = [size*(r-L//2) for r in range(1,L,2)]
            else:
                assert j >= 1
                expected = [-modulus//2]*(L//4) + [modulus//2]*(L//4)
            assert sorted(defects) == sorted(expected), (a,size,h,defects,expected)
            assert all(d != 0 for d in defects)
            half_balanced = all(c == size//2 for c in half_counts)
            should_half_balanced = (j >= 1) if is_U else (j >= 2)
            assert half_balanced == should_half_balanced, (a,h,half_counts)
    print(f'PASS: {subgroups_checked} subgroups and {cosets_checked} cosets, moduli 2^2 through 2^10.')


if __name__ == '__main__':
    check()
