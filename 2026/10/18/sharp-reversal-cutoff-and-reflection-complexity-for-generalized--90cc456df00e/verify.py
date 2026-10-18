"""Finite consistency checks for generalized Thue–Morse reversal theorem.

All infinite mathematical assertions are established by the accompanying proof,
not by these finite checks.
"""

def symbol(index, modulus):
    return index.bit_count() % modulus


def verify_difference_classes():
    for modulus in range(3, 64):
        differences = set()
        for d in range(modulus):
            differences.add((1, d, 1))
            differences.add((0, 1, d))
            differences.add((d, 1, 0))
        for u, v, w in differences:
            assert ((-w) % modulus, (-v) % modulus, (-u) % modulus) not in differences


def verify_pair_construction():
    for modulus in range(3, 35):
        for first in range(modulus):
            for second in range(modulus):
                k = (first - second) % modulus
                r = (second - 1) % modulus
                q = (1 << r) - 1
                m = (1 << (k + 1)) * q + (1 << k) - 1
                assert (symbol(2*m+1, modulus), symbol(2*m+2, modulus)) == (first, second)


def verify_finite_factors():
    # Fixed finite prefixes are explicitly not claimed to contain all factors
    # for arbitrary moduli or arbitrary lengths.
    for modulus in range(3, 9):
        symbols = tuple(symbol(i, modulus) for i in range(1 << 15))
        for length in range(1, 13):
            factors = {symbols[i:i+length] for i in range(len(symbols)-length+1)}
            classes = {min(w, w[::-1]) for w in factors}
            if length >= 3:
                assert len(classes) == len(factors), (modulus, length)
            elif length == 2:
                assert len(factors) == modulus**2
                assert len(classes) == modulus*(modulus+1)//2
            else:
                assert len(factors) == len(classes) == modulus
            if length == 3:
                assert len(factors) == 2*modulus**2-modulus
            if length == 4:
                assert all(w[::-1] not in factors for w in factors)


if __name__ == "__main__":
    verify_difference_classes()
    verify_pair_construction()
    verify_finite_factors()
    print("PASS: difference families, constructive pairs, bounded factor enumerations")
