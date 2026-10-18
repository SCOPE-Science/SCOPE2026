"""Finite exact-arithmetic checks for alternating binary-digit Newman inequalities.
These tests do not replace the induction proof for all lengths and odd moduli.
"""

def alternating_digit_sum(n):
    value = 0
    sign = 1
    while n:
        if n & 1:
            value += sign
        sign = -sign
        n >>= 1
    return value


def complete_vector(q, k):
    f = [0] * q
    f[0] = 1
    for j in range(1, k + 1):
        direction = 1 if (j & 1) else -1
        f = [f[r] - f[(r - direction) % q] for r in range(q)]
    return f


def check():
    tested = 0
    for q in range(3, 32, 2):
        for k in range(0, 13):
            f = [0] * q
            f[0] = 1
            seen = [0] * q
            for n in range(1 << k):
                r = alternating_digit_sum(n) % q
                seen[r] += -1 if n.bit_count() & 1 else 1
                for residue, count in enumerate(seen):
                    sign = -1 if min(residue, q-residue) % 2 else 1
                    assert sign * count >= 0, (q,k,n,residue,count)
                assert seen[0] > 0
                tested += 1
            assert seen == complete_vector(q, k)
    for q in (3, 5, 7, 9, 11, 21, 51, 101):
        for k in range(0, 120):
            f = complete_vector(q,k)
            for r, v in enumerate(f):
                assert (-1 if min(r,q-r)%2 else 1)*v >= 0
            assert f[0] > 0
    print('PASS: exact prefix sign tests:', tested, 'integers, odd moduli 3..31')
    print('PASS: all complete-block vectors through 120 digits in eight moduli')

if __name__ == '__main__':
    check()
