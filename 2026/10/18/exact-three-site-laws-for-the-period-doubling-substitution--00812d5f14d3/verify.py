"""Independent finite dyadic checks of the stated period-doubling triple law.

Run: python3 verify.py. Uses only the Python standard library.
Finite checks support, but do not replace, the Haar-measure proof.
"""
from fractions import Fraction
from itertools import product


def v2(q):
    q = abs(q)
    assert q > 0
    return (q & -q).bit_length() - 1


def correlation2(h):
    assert h != 0
    return Fraction(1) - Fraction(4, 3 * (1 << v2(h)))


def correlation3(a, b):
    assert a and b and a != b
    vs = sorted((v2(a), v2(b), v2(a - b)))
    assert vs[0] == vs[1] < vs[2]
    m, t = vs[0], vs[2]
    return Fraction(1, 3) - Fraction(4 * ((-1) ** m), 3 * (1 << t))


def joint_probability(a, b, signs):
    s0, sa, sb = signs
    return (Fraction(1) + Fraction(s0 + sa + sb, 3)
            + s0 * sa * correlation2(a)
            + s0 * sb * correlation2(b)
            + sa * sb * correlation2(a - b)
            + s0 * sa * sb * correlation3(a, b)) / 8


def dyadic_signs(K):
    modulus = 1 << K
    result = []
    for n in range(modulus):
        x = (n + 1) % modulus
        j = K if x == 0 else v2(x)
        result.append(1 if j % 2 == 0 else -1)
    return result


def check():
    assert correlation3(1, 2) == Fraction(-1, 3)
    assert correlation3(1, 4) == 0
    assert correlation3(2, 4) == Fraction(2, 3)
    assert correlation3(1, 8) == Fraction(1, 6)
    assert correlation3(2, 8) == Fraction(1, 2)
    comparisons = 0
    probabilities = 0
    for a in range(-16, 17):
        for b in range(-16, 17):
            if 0 in (a, b) or a == b:
                continue
            p = [joint_probability(a, b, signs) for signs in product((-1, 1), repeat=3)]
            assert sum(p) == 1
            assert all(Fraction(0) <= z <= Fraction(1) for z in p)
            probabilities += len(p)
    for K in (9, 11, 13):
        vals = dyadic_signs(K)
        N = len(vals)
        for a in range(1, 20):
            for b in range(a + 1, 20):
                avg3 = Fraction(sum(vals[i] * vals[(i + a) % N]
                                    * vals[(i + b) % N] for i in range(N)), N)
                # Only residues with one translated argument equal to 0 mod 2^K
                # can differ from the actual Haar-sign process: measure <= 3/2^K.
                assert abs(avg3 - correlation3(a, b)) <= Fraction(6, N), (K, a, b)
                comparisons += 1
        for h in range(1, 20):
            avg2 = Fraction(sum(vals[i] * vals[(i + h) % N]
                                for i in range(N)), N)
            assert abs(avg2 - correlation2(h)) <= Fraction(4, N), (K, h)
            comparisons += 1
    for m in range(0, 8):
        for t in range(m + 1, 13):
            # Three offsets realizing the valuation tree (m,m,t).
            a, b = 1 << m, 1 << t
            assert correlation3(a, b) == Fraction(1, 3) - Fraction(
                4 * (-1) ** m, 3 * (1 << t))
            comparisons += 1
    print("VERIFY_OK: %s exact dyadic/valuation comparisons, %s exact joint-word probabilities"
          % (comparisons, probabilities))


if __name__ == "__main__":
    check()
