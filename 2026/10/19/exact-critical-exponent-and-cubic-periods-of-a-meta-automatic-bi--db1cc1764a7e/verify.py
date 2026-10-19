#!/usr/bin/env python3
"""Exact finite factor certificates for an automatic infinite word.

Python 3 standard library only. The mathematical reduction from infinite
repetitions to these finite factor tests is given in RESULT.md.
"""

MU = ((0, 1, 1, 2), (1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 2, 3))
CODE = (0, 1, 0, 1)
MAXIMAL_PERIODIC_LENGTHS = (2, 10, 6, 10, 10, 26, 14, 18, 17, 18, 18, 26, 20, 36)


def expand(word, steps):
    for _ in range(steps):
        word = tuple(symbol for x in word for symbol in MU[x])
    return word


def exact_adjacent_pairs():
    """Least closure of internal adjacent pairs under substitution boundaries."""
    letters = {0}
    while True:
        more = letters | {b for a in letters for b in MU[a]}
        if more == letters:
            break
        letters = more
    pairs = {(x, y) for a in letters for x, y in zip(MU[a], MU[a][1:])}
    while True:
        more = pairs | {(MU[a][-1], MU[b][0]) for a, b in pairs}
        if more == pairs:
            break
        pairs = more
    return letters, pairs


def exact_factors(length, pairs, binary=False):
    """Exact set of length-L factors, recording starting positions modulo 4.

    Every length-L factor fits in two adjacent 4**k substitution blocks
    whenever 4**k >= L. Every such block pair actually occurs.
    """
    steps = 1
    while 4 ** steps < length:
        steps += 1
    result = {}
    for a, b in sorted(pairs):
        full = expand((a, b), steps)
        if binary:
            full = tuple(CODE[x] for x in full)
        for start in range(len(full) - length + 1):
            block = full[start : start + length]
            result.setdefault(block, set()).add(start % 4)
    return result


def maximum_periodic_length(word, period):
    count = 0
    best = 0
    for i in range(len(word) - period):
        if word[i] == word[i + period]:
            count += 1
            best = max(best, count + period)
        else:
            count = 0
    return best


def main():
    letters, pairs = exact_adjacent_pairs()
    expected = {(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),
                (2,1),(2,2),(2,3),(3,0)}
    assert letters == {0, 1, 2, 3}
    assert pairs == expected
    print('ALPHABET=4 ADJACENT_PAIRS=10')

    state15 = exact_factors(15, pairs)
    assert len(state15) == 100
    assert all(len(phases) == 1 for phases in state15.values())
    binary29 = exact_factors(29, pairs, binary=True)
    assert len(binary29) == 186
    assert all(len(phases) == 1 for phases in binary29.values())
    print('PHASE_WINDOWS state_length=15 factors=100 binary_length=29 factors=186')

    overlap_tests = 0
    for p in range(1, 14):
        for factor in exact_factors(2*p+1, pairs):
            overlap_tests += 1
            assert any(factor[j] != factor[j+p] for j in range(p+1)), (p, factor)
    print('STATE_OVERLAP_PERIODS=1..13 CHECKED_FACTORS=' + str(overlap_tests))

    factor85 = exact_factors(85, pairs, binary=True)
    assert len(factor85) == 592
    maxima = tuple(max(maximum_periodic_length(f, p) for f in factor85)
                   for p in range(1, 15))
    assert maxima == MAXIMAL_PERIODIC_LENGTHS, (maxima, MAXIMAL_PERIODIC_LENGTHS)
    print('BINARY_FACTORS_LENGTH_85=' + str(len(factor85)))
    print('PERIODS_1_TO_14_MAXIMAL_LENGTHS=' + ','.join(map(str, maxima)))

    prefix = expand((0,), 8)
    projected = tuple(CODE[x] for x in prefix)
    assert projected[2:12] == (1,0)*5
    # Independent direct-prefix inclusion for the three finite languages.
    for length, full_set in ((15, state15), (29, binary29), (85, factor85)):
        seq = prefix if length == 15 else projected
        checked = {seq[i:i+length] for i in range(len(seq)-length+1)}
        assert checked == set(full_set), (length, len(checked), len(full_set))
    print('INDEPENDENT_PREFIX_FACTORS=15,29,85 EXACT_MATCH')
    print('FIFTH_POWER_WITNESS_AT_ZERO_BASED_POSITION_2=1010101010')
    print('ALL_FINITE_CERTIFICATES_PASSED')


if __name__ == '__main__':
    main()
