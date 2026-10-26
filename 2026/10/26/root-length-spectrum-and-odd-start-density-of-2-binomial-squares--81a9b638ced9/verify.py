#!/usr/bin/env python3
"""Reproduce structural and finite checks for 2-binomial squares in Thue--Morse."""
from itertools import product


def tbit(j):
    return j.bit_count() & 1


def morphic_prefix(n):
    s = '0'
    while len(s) < n:
        s = ''.join('01' if c == '0' else '10' for c in s)
    return [int(c) for c in s[:n]]


def signature(w):
    """Counts scattered subsequences of length at most two."""
    sig = (len(w), w.count(1))
    counts = []
    for a, b in product((0, 1), repeat=2):
        counts.append(sum(w[i] == a and w[j] == b
                          for i in range(len(w)) for j in range(i+1, len(w))))
    return sig + tuple(counts)


def compact_signature(w):
    return (len(w), sum(w), sum(i * b for i, b in enumerate(w)))


def verify():
    for n in range(9):
        classes = {}
        inverse = {}
        for w in product((0, 1), repeat=n):
            k = compact_signature(w)
            s = signature(w)
            if k in classes:
                assert classes[k] == s
            else:
                classes[k] = s
            if s in inverse:
                assert inverse[s] == k
            else:
                inverse[s] = k
    print('VERIFY_OK independent_binomial_signatures_all_binary_words_length_0_to_8')

    N = 1 << 15
    t = [tbit(i) for i in range(N)]
    assert t == morphic_prefix(N)
    ones = [0]
    ones_positions = [0]
    for i, v in enumerate(t):
        ones.append(ones[-1] + v)
        ones_positions.append(ones_positions[-1] + i*v)

    def compact_at(i, m):
        return (ones[i+m] - ones[i],
                ones_positions[i+m] - ones_positions[i] - i*(ones[i+m]-ones[i]))

    def square(i, m):
        return compact_at(i, m) == compact_at(i+m, m)

    def witness(h):
        """Explicit even-root construction, root length 2h."""
        if h % 2 == 0:
            return 0
        k = h.bit_length()
        while (k - (h-1).bit_count()) % 2:
            k += 1
        b = (1 << k) - h
        assert tbit(b) == 0 and tbit(b+h) == 1
        return 4*b+2

    for h in range(1, 257):
        m = 2*h
        i = witness(h)
        assert i + 2*m <= N and square(i, m), (h, i)
        u, v = t[i:i+m], t[i+m:i+2*m]
        assert signature(u) == signature(v), (h, i)
    print('VERIFY_OK every_even_root_length_2_to_512_has_independently_verified_explicit_witness')

    assert square(1, 1)
    assert square(11, 3)
    for m in range(5, 260, 2):
        assert not any(square(i, m) for i in range(N-2*m+1)), m
    print('VERIFY_OK no_odd_root_length_5_to_259_in_prefix_32768')

    for a in range(6000):
        i = 2*a+1
        expected = tuple(t[a:a+4]) in ((0, 0, 1, 1), (1, 1, 0, 0))
        assert square(i, 3) == expected, (a, i)
    for a in range(6000):
        assert square(2*a+1, 1) == (t[a] != t[a+1])
    print('VERIFY_OK exact_odd_position_criteria_for_roots_1_and_3_checked_6000_each')

    for m in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):
        valid = sum(square(i, m) for i in range(N-2*m+1))
        assert (valid > 0) == (m % 2 == 0 or m in (1,3)), (m, valid)
    print('VERIFY_OK initial_spectrum_and_full_factor_checks')
    c3 = sum(square(i, 3) for i in range(N-6+1))
    print(f'CHECK observed_odd_root_3_frequency={c3}/{N-5}; exact_limit=1/12')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
