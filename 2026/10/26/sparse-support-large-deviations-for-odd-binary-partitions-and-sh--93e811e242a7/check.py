"""Finite cross-check of restricted binary-partition and semi-Pell identities.

Run: python3 check.py
This finite test supports, but does not prove, the stated asymptotic laws.
"""

def verify(limit=2048):
    # Independent coefficient calculation: each binary power is absent or
    # appears an odd positive number of times. W assigns weight 2 to each
    # occupied part size.
    counts = [0] * (limit + 1)
    weighted = [0] * (limit + 1)
    counts[0] = weighted[0] = 1
    power = 1
    while power <= limit:
        next_counts = counts[:]
        next_weighted = weighted[:]
        for multiplicity in range(1, limit // power + 1, 2):
            delta = power * multiplicity
            for n in range(delta, limit + 1):
                next_counts[n] += counts[n - delta]
                next_weighted[n] += 2 * weighted[n - delta]
        counts, weighted = next_counts, next_weighted
        power *= 2

    # Unrelated recurrence evaluation, without using partition enumeration.
    sf = [0] * (limit + 1)
    sp = [0] * (limit + 1)
    sf[0] = sf[1] = 1
    sp[1] = 1
    for n in range(2, limit + 1):
        if n % 2 == 0:
            sf[n] = sf[n // 2]
            sp[n] = sp[n // 2]
        else:
            sf[n] = sf[n - 1] + sf[n - 2]
            sp[n] = 2 * sp[n - 1] + sp[n - 2]
    for n in range(1, limit + 1):
        assert counts[n] == sf[n], (n, counts[n], sf[n])
        assert weighted[n] == 2 * sp[n], (n, weighted[n], sp[n])
    assert counts[0] == weighted[0] == 1
    print('VERIFIED:', limit, 'positive indices via independent odd-binary-partition coefficient DP and two recurrences')
    print('ODD SAMPLES:', [(n, sf[n], sp[n]) for n in (7, 31, 127, 511, 2047) if n <= limit])

if __name__ == '__main__':
    verify()
