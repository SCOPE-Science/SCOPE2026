#!/usr/bin/env python3
"""Complete finite classification of systematic binary 4-by-8 three-PIR matrices.

All statements are for matrices [I_4 | P] with four distinguished message
coordinates and four parity coordinates. No third-party packages are needed.
"""
from collections import Counter
from itertools import combinations_with_replacement, permutations, product
from pathlib import Path

S = 4
UNIT = (1, 2, 4, 8)
ALL_PARITIES = range(16)
GROUP_PERMS = list(permutations(range(S)))
REQUESTS = list(combinations_with_replacement(range(S), 3))


def xor_sums(columns):
    """All subset sums, with a repeated column retained as a separate index."""
    sums = [0] * (1 << len(columns))
    for mask in range(1, len(sums)):
        low = mask & -mask
        sums[mask] = sums[mask ^ low] ^ columns[low.bit_length() - 1]
    return sums


def parity_test(columns):
    """Exact systematic three-PIR test using only nonempty parity subsets.

    The singleton {i} is one recovery set; any three disjoint recoveries
    can be replaced by a triple containing {i}. The other two have
    nonempty, disjoint parity-index sets and disjoint systematic supports.
    """
    sums = xor_sums(columns)
    for i in range(S):
        choices = [(m, sums[m] & ~UNIT[i]) for m in range(1, len(sums))
                   if sums[m] & UNIT[i]]
        if not any((a & b) == 0 and (u & v) == 0
                   for a, u in choices for b, v in choices):
            return False
    return True


def direct_test(columns):
    """Independently test three pairwise disjoint column-index recoveries.

    Uses all 256 subsets of the eight coordinates without a systematic
    singleton assumption or a parity-subset reduction.
    """
    sums = xor_sums(UNIT + tuple(columns))
    for i in range(S):
        eligible = [m for m in range(1, len(sums)) if sums[m] == UNIT[i]]
        if not any((a & b) == 0 and (a & c) == 0 and (b & c) == 0
                   for a in eligible for b in eligible if not (a & b)
                   for c in eligible if not ((a | b) & c)):
            return False
    return True


def minimal_recoveries(columns):
    sums = xor_sums(UNIT + tuple(columns))
    result = []
    for i in range(S):
        candidates = [m for m in range(1, 256) if sums[m] == UNIT[i]]
        minimal = [m for m in candidates if not any(q != m and (q & m) == q
                                                  for q in candidates)]
        assert minimal
        result.append(minimal)
    return result


def three_batch(columns):
    """All 20 multisets of three requests, each with disjoint recoveries."""
    recovery = minimal_recoveries(columns)
    for i, j, k in REQUESTS:
        if not any((a & b) == 0 and (a & c) == 0 and (b & c) == 0
                   for a in recovery[i] for b in recovery[j] if not (a & b)
                   for c in recovery[k] if not ((a | b) & c)):
            return False
    return True


def parity_rank(columns):
    pivots = {}
    for column in columns:
        v = column
        while v:
            pos = v.bit_length()
            if pos not in pivots:
                pivots[pos] = v
                break
            v ^= pivots[pos]
    return len(pivots)


def incidence_lemma(columns):
    """The sufficient pairwise-intersection condition of the 2015 source."""
    return (all(sum((col >> i) & 1 for col in columns) >= 2
                for i in range(S)) and
            all((columns[j] & columns[k]).bit_count() <= 1
                for j in range(S) for k in range(j + 1, S)))


def permutation_maps():
    return [[sum(((v >> i) & 1) << perm[i] for i in range(S))
             for v in ALL_PARITIES] for perm in GROUP_PERMS]


def canonical(columns, row_maps):
    """Orbit canonicalization under information and parity permutations."""
    return min(tuple(sorted(mapping[v] for v in columns)) for mapping in row_maps)


def validate():
    assert len(GROUP_PERMS) == 24 and len(REQUESTS) == 20
    for r in range(4):
        assert sum(parity_test(cols) for cols in product(ALL_PARITIES, repeat=r)) == 0

    # Independent full-space enumerations over precisely 16^4 matrices.
    valid_parity = [tuple(cols) for cols in product(ALL_PARITIES, repeat=S)
                    if parity_test(cols)]
    valid_direct = [tuple(cols) for cols in product(ALL_PARITIES, repeat=S)
                    if direct_test(cols)]
    assert valid_parity == valid_direct
    assert len(valid_direct) == 7800
    assert all(three_batch(cols) for cols in valid_direct)

    rows = permutation_maps()
    classes = Counter(canonical(cols, rows) for cols in valid_direct)
    assert len(classes) == 26
    assert sum(classes.values()) == 7800
    assert Counter(classes.values()) == {288: 12, 576: 6, 96: 4, 144: 3, 72: 1}
    assert all(576 % c == 0 for c in classes.values())

    # A separate, direct application of Burnside's lemma, not relying on
    # canonical representatives or class-size arithmetic.
    fixed_sum = 0
    for mapping in rows:
        for parity_permutation in GROUP_PERMS:
            fixed_sum += sum(
                tuple(mapping[cols[parity_permutation[j]]] for j in range(S)) == cols
                for cols in valid_direct
            )
    assert fixed_sum == 26 * 576 == 14976

    rank_count = Counter(parity_rank(cols) for cols in valid_direct)
    assert rank_count == {4: 4800, 3: 3000}
    assert Counter(parity_rank(rep) for rep in classes) == {3: 13, 4: 13}

    lemma_count = sum(incidence_lemma(cols) for cols in valid_direct)
    lemma_reps = sum(incidence_lemma(rep) for rep in classes)
    assert lemma_count == 456 and lemma_reps == 3
    assert 7800 - lemma_count == 7344

    # For every nonzero message u, the systematic [I|P] codeword has
    # Hamming weight at least three, independently of three-PIR recovery.
    for cols in valid_direct:
        for u in range(1, 16):
            weight = u.bit_count() + sum((u & v).bit_count() % 2 for v in cols)
            assert weight >= 3


    # Exactness, rather than merely the 3-PIR lower bound, for minimum distance.
    assert all(any(u.bit_count() + sum((u & v).bit_count() % 2 for v in cols) == 3
                   for u in range(1, 16)) for cols in valid_direct)

    table_path = Path(__file__).resolve().parent / 'orbit_representatives.tsv'
    lines = ['representative_parity_decimals\torbit_size\tstabilizer_order\tparity_rank\tincidence_lemma\tparity_columns_binary']
    for rep in sorted(classes):
        count = classes[rep]
        lines.append(
            ','.join(map(str, rep)) + '\t' + str(count) + '\t' + str(576 // count) +
            '\t' + str(parity_rank(rep)) + '\t' + str(incidence_lemma(rep)).lower() +
            '\t' + ','.join(format(v, '04b') for v in rep)
        )
    generated = '\n'.join(lines) + '\n'
    if table_path.exists():
        assert table_path.read_text(encoding='utf-8') == generated
    else:
        table_path.write_text(generated, encoding='utf-8')

    print('PIR_TEST_AGREEMENT systematic_matrices=65536 successes=7800')
    print('LOWER_LENGTH_CHECK r_le_3_successes=0')
    print('THREE_BATCH_CHECK successes=7800 request_multisets=20')
    print('ORBIT_CHECK orbits=26 fixed_sum=14976 group_order=576')
    print('INCIDENCE_LEMMA cases=456 classes=3 outside=7344')
    print('PARITY_RANK rank3=3000 rank4=4800')
    print('VERIFY_OK systematic_optima=7800 orbits=26 batch_all=true incidence_lemma=456 other=7344 burnside=26')

if __name__ == '__main__':
    validate()
