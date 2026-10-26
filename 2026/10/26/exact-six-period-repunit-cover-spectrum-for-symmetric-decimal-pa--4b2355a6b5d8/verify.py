#!/usr/bin/env python3
"""Exact finite-state certificate for a six-period repunit cover."""
from math import gcd

MODULUS = 111111
PRIMES = (3, 7, 11, 13, 37)
DIGITS = (1, 3, 7, 9)
PERIOD = 6
EXPECTED = (60, 10121, 111, 10121, 60, 10101)
QUOTIENT_MODULUS = MODULUS // 3
ODD_THREE_NINE = {
    1: (10406, 11843),
    3: (2701, 6512, 10989, 16132),
    5: (28589, 32149),
}
# For odd t: each pair lists an m with no divisor of MODULUS
# for digit 1, respectively when q mod 3 is 1 and 2.
ODD_OBSTRUCTIONS = {
    1: {10406: (3, 1), 11843: (3, 3)},
    3: {2701: (2, 4), 6512: (5, 1),
        10989: (5, 1), 16132: (2, 1)},
    5: {28589: (3, 1), 32149: (2, 1)},
}

assert 3 * 7 * 11 * 13 * 37 == MODULUS
assert (10 ** PERIOD - 1) // 9 == MODULUS
assert all(pow(10, PERIOD, p) == 1 for p in PRIMES)


def gcd_cover(q, t):
    """Direct integer gcd, before periodic reduction to residues."""
    for digit in DIGITS:
        for m in range(1, PERIOD + 1):
            repunit = (10 ** m - 1) // 9
            padded = digit * repunit * (10 ** (t + m) + 1) + q * 10 ** m
            if gcd(padded, MODULUS) == 1:
                return False
    return True


def local_root_tables(t):
    """Independent CRT check: each prime has one admissible q residue."""
    rows = []
    for digit in DIGITS:
        for m in range(1, PERIOD + 1):
            table = []
            for p in PRIMES:
                power = pow(10, m, p)
                repunit = (10 ** m - 1) // 9
                constant = digit * repunit * (pow(10, t + m, p) + 1)
                root = (-constant * pow(power, -1, p)) % p
                assert (power * root + constant) % p == 0
                table.append((p, root))
            rows.append(tuple(table))
    return rows


def crt_cover(q, rows):
    return all(any(q % p == root for p, root in row) for row in rows)


def check():
    # Reduced CRT argument for the obstruction: digits 3 and 9 have no
    # prime-3 help when q is not divisible by 3. Exhaust all residues
    # modulo the product of the four remaining primes.
    for t in range(1, PERIOD + 1):
        reduced = [row[1:] for i, row in enumerate(local_root_tables(t))
                   if i // PERIOD in (1, 3)]
        survivors = [q for q in range(QUOTIENT_MODULUS)
                     if crt_cover(q, reduced)]
        if t % 2 == 0:
            assert survivors == list(range(0, QUOTIENT_MODULUS, 11))
        else:
            assert tuple(survivors) == ODD_THREE_NINE[t]
            for r in survivors:
                for residue in (1, 2):
                    q = next(r + j * QUOTIENT_MODULUS for j in range(3)
                             if (r + j * QUOTIENT_MODULUS) % 3 == residue)
                    m = ODD_OBSTRUCTIONS[t][r][residue - 1]
                    f = ((10 ** m - 1) // 9) * (10 ** (t + m) + 1) + q * 10 ** m
                    assert gcd(f, MODULUS) == 1, (t, r, residue, m)

    summaries = []
    for t in range(1, PERIOD + 1):
        rows = local_root_tables(t)
        found = []
        for q in range(MODULUS):
            a = gcd_cover(q, t)
            b = crt_cover(q, rows)
            assert a == b, (t, q, a, b)
            if a:
                found.append(q)
        assert len(found) == EXPECTED[t - 1], (t, len(found))
        assert all(q % 3 == 0 or (t % 2 == 0 and q % 11 == 0)
                   for q in found), t
        if t % 2 == 0:
            assert all(gcd_cover(q, t) for q in range(0, MODULUS, 11))
        excess = [q for q in found if q % 11]
        if t in (2, 4):
            assert len(excess) == 20 and all(q % 3 == 0 for q in excess)
        if t == 6:
            assert len(excess) == 0
        summaries.append((t, len(found), sum(q % 3 == 0 for q in found),
                          sum(q % 11 == 0 for q in found)))

    # Representative known symmetric-padding examples from the 2015 literature.
    assert gcd_cover(231 % MODULUS, 3)
    assert gcd_cover(420 % MODULUS, 3)
    assert gcd_cover(759 % MODULUS, 3)
    assert not gcd_cover(6363 % MODULUS, 4)  # Needs a longer cover.
    print("t, qualifying residues, divisible by 3, divisible by 11")
    for row in summaries:
        print(*row)
    print("VERIFY_OK: all 666666 residue states, two independent criteria")


if __name__ == "__main__":
    check()
