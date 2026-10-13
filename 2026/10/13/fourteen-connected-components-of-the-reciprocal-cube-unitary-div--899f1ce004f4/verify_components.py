"""Exact finite comparisons for the range of the reciprocal-cube unitary divisor sum.

The mathematical proof additionally invokes Nagura's prime-gap theorem
and the standard complete-subsums lemma, neither of which is replaced
by this finite checker.
"""
from fractions import Fraction
from itertools import product


def primes_through(n):
    mark = bytearray(b"\x01") * (n + 1)
    mark[:2] = b"\x00\x00"
    for d in range(2, int(n ** .5) + 1):
        if mark[d]:
            mark[d * d : n + 1 : d] = b"\x00" * ((n - d * d) // d + 1)
    return [p for p in range(n + 1) if mark[p]]


def rational_factor(p, a):
    return Fraction(p ** (3 * a) + 1, p ** (3 * a))


def main():
    # For p < 29, rational lower bounds for the subsequent logarithmic factors.
    finite_witnesses = {
        11: (13, 17, 19),
        13: (17, 19, 23, 29),
        17: (19, 23),
        19: (23, 29, 31),
        23: (29, 31, 37),
    }
    proof_primes = set(primes_through(1000))
    for p, successors in finite_witnesses.items():
        assert p in proof_primes and all(q in proof_primes for q in successors)
        assert sum((Fraction(1, q ** 3 + 1) for q in successors), Fraction()) > Fraction(1, p ** 3)
        assert all(q > p for q in successors)

    # Nagura supplies p_next < 6p/5 for each prime p >= 29.
    assert Fraction(125, 91) > 1 + Fraction(1, 29 ** 3)

    # If P denotes prod_{p>=11} (1+p^-3), the rigorous enclosure is
    # P_B <= P <= P_B / (1-1/(2 B^2)); sum_{n>B} n^-3 <= 1/(2B^2).
    B = 1000
    small_primes = primes_through(B)
    P_lo = Fraction(1)
    for p in small_primes:
        if p >= 11:
            P_lo *= rational_factor(p, 1)
    P_hi = P_lo / (1 - Fraction(1, 2 * B * B))
    assert P_lo < P_hi

    cutoff = {2: 4, 3: 2, 5: 2, 7: 2}
    assert all(P_lo > rational_factor(p, cutoff[p]) for p in cutoff)

    options = {p: ['H'] + list(range(1, cutoff[p])) for p in cutoff}
    candidate_intervals = []
    for choices in product(*(options[p] for p in (2, 3, 5, 7))):
        lo, up = Fraction(1), Fraction(1)
        for p, a in zip((2, 3, 5, 7), choices):
            if a == 'H':
                up *= rational_factor(p, cutoff[p])
            else:
                lo *= rational_factor(p, a)
                up *= rational_factor(p, a)
        code = ''.join(map(str, choices))
        candidate_intervals.append((lo, up, code))

    candidate_intervals.sort(key=lambda entry: entry[0])
    assert len(candidate_intervals) == 32
    components = []
    for lo, up, code in candidate_intervals:
        if not components:
            components.append([lo, up, code, code, 1])
            continue
        c = components[-1]
        if lo <= P_lo * c[1]:
            # Overlap valid for the true value of P >= P_lo.
            c[4] += 1
            if up > c[1]:
                c[1] = up
                c[3] = code
        else:
            # Separation valid for the true value of P <= P_hi.
            assert lo > P_hi * c[1], f"P enclosure insufficient: {code}"
            components.append([lo, up, code, code, 1])

    expected = [
        ('HHHH', '2HH1'), ('2H1H', '2H11'), ('H1HH', '31H1'),
        ('H11H', '3111'), ('21HH', '21HH'), ('21H1', '21H1'),
        ('211H', '211H'), ('2111', '2111'), ('1HHH', '1HH1'),
        ('1H1H', '1H11'), ('11HH', '11HH'), ('11H1', '11H1'),
        ('111H', '111H'), ('1111', '1111'),
    ]
    assert [(c[2], c[3]) for c in components] == expected
    assert sum(c[4] for c in components) == 32
    for i in range(len(components)-1):
        assert components[i + 1][0] > P_hi * components[i][1]
    assert len(components) == 14

    print('EXACT_CERTIFICATE_OK: finite_kakeya_cases=5, prime_gap_ratio=6/5, '
          'prime_cutoffs=' + str(cutoff) + ', candidate_intervals=32, connected_components=14')
    print('P lower/upper (rigorous rational bounds):',
          f'{float(P_lo):.14f}', f'{float(P_hi):.14f}')
    for j, c in enumerate(components, 1):
        print('%02d %-4s %-4s %.12f %.12f %d' %
              (j, c[2], c[3], float(c[0]), float(P_hi * c[1]), c[4]))

if __name__ == '__main__':
    main()
