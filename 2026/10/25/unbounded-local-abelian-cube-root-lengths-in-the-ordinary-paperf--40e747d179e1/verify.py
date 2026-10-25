"""Reproduce finite checks for a paperfolding abelian-cube obstruction.

The unbounded statement is established by the accompanying symbolic proof;
these checks are finite and do not independently certify that induction.
"""


def odd_part(n):
    assert n > 0
    return n // (n & -n)


def paper_bit(i):
    """Zero-based binary word: 1 for odd_part(i+1) == 1 (mod 4)."""
    return int(odd_part(i + 1) % 4 == 1)


def recursive_paper_bit(i):
    if i % 2 == 0:
        return int((i // 2) % 2 == 0)
    return recursive_paper_bit(i // 2)


def limiting_sign(j):
    """One if odd_part(3*j+1) == 3 (mod 4), else minus one."""
    return 1 if odd_part(3 * j + 1) % 4 == 3 else -1


def main():
    size = 65536
    binary = [paper_bit(i) for i in range(size)]
    assert binary == [recursive_paper_bit(i) for i in range(size)]
    assert ''.join(map(str, binary[:16])) == '1101100111001001'

    # P is minus the signed prefix sum of the auxiliary limiting word.
    sig = [limiting_sign(i) for i in range(size)]
    p = [0]
    for s in sig:
        p.append(p[-1] - s)

    for n in range(size // 4):
        e = n % 2
        assert p[4*n] == p[n] + e
        assert p[4*n + 1] == p[n] + e + 1
        assert p[4*n + 2] == p[n+1] + e + 1
        assert p[4*n + 3] == p[n+1] + e

    assert min(p[1:]) >= 1
    special = set()
    for k in range(11):
        m = (2 * 4**k + 1) // 3
        if m > size:
            break
        special.add(m)
        assert p[m] == 1
        if 2 * m <= size:
            assert p[2*m] == 2*k + 2
    assert [i for i in range(1, size+1) if p[i] == 1] == sorted(special)

    for m in range(1, size//3):
        q = p[3*m] - 2*p[m]
        if m % 2 == 0:
            assert q <= 0
        elif m % 4 == 1:
            assert q <= -1
        else:
            assert q <= 1
        assert not (p[2*m] == 2*p[m] and p[3*m] == 3*p[m])

    ps = [0]
    for bit in binary:
        ps.append(ps[-1] + bit)
    for k in range(1, 9):
        start = 2 * (4**k - 1) // 3
        length = (4**k - 1) // 3
        assert start + length <= size
        assert all(2*binary[start+j]-1 == sig[j] for j in range(length))
        for m in range(1, length//3 + 1):
            counts = [ps[start+(j+1)*m] - ps[start+j*m] for j in range(3)]
            assert len(set(counts)) > 1
    print('VERIFY_OK paperfolding_arithmetic_and_recursive_generators=65536')
    print('VERIFY_OK auxiliary_prefix_recurrences=0..16383')
    print('VERIFY_OK positive_prefix_discrepancy_and_all_unity_indices=1..65536')
    print('VERIFY_OK triple_scale_inequality_and_abelian_cube_exclusion=1..21844')
    print('VERIFY_OK exact_prefix_dyadic_positions_and_cube_lower_bounds=k1..8')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
