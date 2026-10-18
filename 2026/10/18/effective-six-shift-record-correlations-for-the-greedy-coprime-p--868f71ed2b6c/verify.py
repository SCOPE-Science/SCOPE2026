"""Exact finite residue certificate for two-point record densities.

Python 3 standard library. This script proves only the reported finite counts;
the infinite theorem uses primorial-copying and a separately proved tail bound.
"""
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
EXPECTED = {
    3: (30, 9, 8),
    4: (210, 62, 54),
    5: (2310, 681, 593),
    6: (30030, 8852, 7708),
    7: (510510, 150483, 131035),
    8: (9699690, 2859176, 2489664),
}

def records_upto(bound):
    r = 5
    result = []
    while r <= bound:
        result.append(r)
        for p in PRIMES:
            if (r - 1) % p:
                r += p - 1
                break
        else:
            raise ArithmeticError('prime table insufficient')
    return result

def check():
    limit = EXPECTED[8][0] + 1
    records = records_upto(limit)
    assert records[:10] == [5, 7, 11, 13, 17, 19, 23, 25, 29, 31]
    P = 1
    previous = None
    for n, p in enumerate(PRIMES[:8], 1):
        P *= p
        if n < 3:
            continue
        R = {r % P for r in records if PRIMES[n] <= r <= P + 1}
        C = sum((r + 6) % P in R for r in R)
        assert (P, len(R), C) == EXPECTED[n], (n, P, len(R), C)
        if previous is not None:
            old_period, old_residues = previous
            assert all(r % old_period in old_residues for r in R)
        previous = (P, R)
        print('stage', n, 'period', P, 'records', len(R), 'pairs_at_6', C)
    from fractions import Fraction
    upper = Fraction(2489664, 9699690)
    lower = upper - Fraction(23, 22 * 9699690)
    assert lower > Fraction(1, 4)
    assert upper < Fraction(3, 10)
    print('Q6 enclosure', lower, '< Q6 <=', upper)
    print('VERIFY_OK')

if __name__ == '__main__':
    check()
