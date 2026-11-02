"""Finite certificate for a two-tortoise complexity identity on Thue-Morse factors.

No nonstandard dependencies. Run: python3 thue_second_verifier.py
The all-length implication is proved separately by factor-prefix inheritance,
parity synchronization, and the left-special lifting lemma.
"""

def substitute_blocks(power):
    zero, one = b"0", b"1"
    for _ in range(power):
        zero, one = zero + one, one + zero
    return (zero + zero, zero + one, one + zero, one + one)


def exact_factors(length):
    """All factors, not merely sampled factors, of a given length.

    If 2**k >= length, every length-length factor lies in two
    consecutive mu**k blocks. Every pair 00,01,10,11 occurs in TM.
    """
    k = (length-1).bit_length()
    pairs = substitute_blocks(k)
    return {w[p:p+length] for w in pairs
            for p in range(len(w)-length+1)}


def one_tortoise(w):
    i = w.find(b"1")
    return w if i == -1 else w[:i] + w[i+1:] + b"1"


def second_tortoise(w):
    return one_tortoise(one_tortoise(w))


def collision_fibres(factors, operation):
    groups = {}
    for w in factors:
        groups.setdefault(operation(w), []).append(w)
    return [frozenset(g) for g in groups.values() if len(g) > 1]


def one_pass_deficit(n):
    # Published one-step Thue-Morse identity, applicable for n>=10.
    assert n >= 10
    return 2 if bin(n-3)[2:].startswith("11") else 4


def certify_base():
    f18 = exact_factors(18)
    pairs = set(collision_fibres(f18, second_tortoise))
    expected = {
        frozenset((b"011001011001101001", b"101001011001101001")),
        frozenset((b"010110100110010110", b"100110100110010110")),
        frozenset((b"011010010110011010", b"100110010110011010")),
        frozenset((b"011001101001100101", b"100101101001100101")),
    }
    assert len(f18) == 52
    assert min(w.count(b"1") for w in f18) == 8
    assert pairs == expected, (pairs ^ expected)
    assert all(len(x) == 2 for x in pairs)
    # Both alternating length-five words are absent; every longer
    # Thue-Morse factor contains a doubled adjacent letter.
    f5 = exact_factors(5)
    assert b"01010" not in f5 and b"10101" not in f5
    # Adjacent source letters really comprise all four pairs.
    assert exact_factors(2) == {b"00", b"01", b"10", b"11"}
    f17=exact_factors(17)
    d117=len(f17)-len({one_tortoise(w) for w in f17})
    d217=len(f17)-len({second_tortoise(w) for w in f17})
    assert (d117,d217,one_pass_deficit(15)) == (2,5,2)
    return pairs


def certify_long_window():
    # This is a cross-check of the symbolic proof, not the reason its
    # all-length quantifier is true. At each n, exact_factors(n) is complete.
    counts = {4:0, 6:0, 8:0}
    for n in range(18,513):
        factors=exact_factors(n)
        d1=len(factors)-len({one_tortoise(w) for w in factors})
        d2=len(factors)-len({second_tortoise(w) for w in factors})
        expected=one_pass_deficit(n)+one_pass_deficit(n-2)
        assert d1==one_pass_deficit(n), (n,d1)
        assert d2==expected, (n,d2,expected)
        counts[d2]+=1
    assert counts=={4:237,6:20,8:238}, counts
    return counts


if __name__=="__main__":
    base=certify_base()
    counts=certify_long_window()
    print("TM_TWO_TORTOISE_VERIFY_OK")
    print("length18_factors=52, nontrivial_two_pass_fibres=4")
    print("length17_one_pass_deficit=2, length17_two_pass_deficit=5")
    print("lengths18_through512_two_pass_deficits", counts)
