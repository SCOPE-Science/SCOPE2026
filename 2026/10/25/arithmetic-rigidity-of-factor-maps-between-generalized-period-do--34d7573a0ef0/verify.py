#!/usr/bin/env python3
"""Finite exact checks for the generalized period-doubling factor theorem.
The theorem itself is proved analytically; this script tests its key explicit models.
"""

def val2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def substitution_word(q, stages):
    w = [0]
    for _ in range(stages):
        w = [v for a in w for v in (0, (a + 1) % q)]
    return w


def arithmetic_word(q, length):
    return [val2(n + 1) % q for n in range(length)]


def finite_window(q, exponent, radius=21):
    c = 1 << exponent
    return tuple(val2(n + c) % q for n in range(-radius, radius + 1))


def test():
    for q in range(2, 13):
        w = substitution_word(q, 12)
        assert w == arithmetic_word(q, 4096), ('substitution', q)

    for q in range(2, 13):
        for r in range(2, 13):
            reductions = {(t + j * q) % r for j in range(r) for t in (0,)}
            assert (len(reductions) == 1) == (q % r == 0), ('divisibility', q, r)
            l0 = 36 + (-36 % q)
            l1 = l0 + q
            assert finite_window(q, l0) == finite_window(q, l1)
            if q % r:
                assert finite_window(r, l0) != finite_window(r, l1)
            else:
                assert finite_window(r, l0) == finite_window(r, l1)
                assert tuple(t % r for t in finite_window(q, l0)) == finite_window(r, l0)

    for q in range(2, 13):
        for r in range(2, 13):
            if q % r != 0:
                continue
            wq = substitution_word(q, 13)
            wr = substitution_word(r, 13)
            assert [x % r for x in wq] == wr, ('factor', q, r)
            for length in (1, 2, 3, 5, 8, 13, 21):
                def language(w, n):
                    return {tuple(w[i:i+n]) for i in range(len(w)-n+1)}
                assert {tuple(x % r for x in v) for v in language(wq,length)} == language(wr,length)
    print('VERIFY_OK substitution_alphabets=11 q_r_pairs=121 reduction_pairs_checked')


if __name__ == '__main__':
    test()
