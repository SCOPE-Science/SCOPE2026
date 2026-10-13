#!/usr/bin/env python3
"""Exact reproducibility checks for joint correlations of two nested-recursion sequences.

Requires only Python 3 standard library. The infinite theorem also uses the
algebraic root-location argument stated in RESULT.md; finite checks alone are
not an infinite proof.
"""

MORPH_1 = ('0112', '1230', '2301', '3023')
MORPH_2 = ('0132', '2310', '3201', '1023')
OUTPUT = (0, 1, 0, 1)
DIM = 16


def zeros(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]


def matmul(a, b):
    out = zeros(len(a), len(b[0]))
    for i in range(len(a)):
        for k, aik in enumerate(a[i]):
            if aik:
                for j, bkj in enumerate(b[k]):
                    out[i][j] += aik * bkj
    return out


def matvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def charpoly(a):
    # Faddeev--LeVerrier / Newton traces, integer and exact.
    n = len(a)
    cur = [[int(i == j) for j in range(n)] for i in range(n)]
    traces = []
    coeffs = [1]
    for k in range(1, n+1):
        cur = matmul(a, cur)
        traces.append(sum(cur[i][i] for i in range(n)))
        numerator = -sum(coeffs[k-j] * traces[j-1]
                         for j in range(1, k+1))
        assert numerator % k == 0, ('nonintegral characteristic coefficient', k)
        coeffs.append(numerator // k)
    return coeffs


def build_transfer():
    t = zeros(DIM, DIM)
    for a in range(4):
        for b in range(4):
            for digit in range(4):
                new_a = int(MORPH_1[a][digit])
                new_b = int(MORPH_2[b][digit])
                t[4*new_a+new_b][4*a+b] += 1
    return t


def automaton_output(n, morph):
    state = 0
    digits = []
    while n:
        digits.append(n % 4)
        n //= 4
    for digit in reversed(digits):
        state = int(morph[state][digit])
    return OUTPUT[state]


def sequences_nested(limit):
    a = [0] * limit
    b = [0] * limit
    if limit > 1:
        a[1] = b[1] = 1
    for index in range(2, limit):
        q, r = divmod(index, 4)
        if r == 0:
            a[index] = a[q]
            b[index] = b[2*q+b[q]]
        elif r == 1:
            a[index] = 1 - a[4*q]
            b[index] = 1 - b[4*q]
        elif r == 2:
            a[index] = a[2*q+1-a[q]]
            b[index] = b[2*q+1-b[q]]
        else:
            a[index] = 1-a[4*q+2]
            b[index] = 1-b[4*q+2]
    return a, b


def block_value(t_powers, prefix, h):
    a = b = 0
    digits = []
    while prefix:
        digits.append(prefix % 4)
        prefix //= 4
    for digit in reversed(digits):
        a = int(MORPH_1[a][digit])
        b = int(MORPH_2[b][digit])
    state = [0] * DIM
    state[4*a+b] = 1
    result = matvec(t_powers[h], state)
    return sum(((-1)**(OUTPUT[i//4]+OUTPUT[i%4])) * count
               for i, count in enumerate(result))


def prefix_value(t_powers, n):
    pos = total = 0
    for h in range(len(t_powers)-1, -1, -1):
        size = 4 ** h
        count = (n-pos) // size
        assert 0 <= count <= 3
        for _ in range(count):
            assert pos % size == 0
            total += block_value(t_powers, pos//size, h)
            pos += size
    assert pos == n
    return total


def main():
    t = build_transfer()
    expected = [1]
    for factor in ([1,-4], [1,-1], [1,3,4],
                   [1,-3,5,-12,16], [1]+[0]*8):
        expected = poly_mul(expected, factor)
    cp = charpoly(t)
    assert cp == expected, (cp, expected)
    assert matvec(t, [1]*DIM) == [4]*DIM
    signs = [(-1)**(OUTPUT[i//4]+OUTPUT[i%4]) for i in range(DIM)]
    assert sum(signs) == 0
    v = [1] + [0]*15
    powers = [[[int(i == j) for j in range(DIM)] for i in range(DIM)]]
    actual_s = []
    for k in range(13):
        if k:
            powers.append(matmul(t, powers[-1]))
        vec = matvec(powers[k], v)
        actual_s.append(sum(signs[i]*vec[i] for i in range(DIM)))
    assert actual_s == [1,4,4,12,-12,-12,44,-364,-364,-372,-2508,-2508,-6164]
    limit = 4**9
    a, b = sequences_nested(limit)
    for n in range(limit):
        assert a[n] == automaton_output(n, MORPH_1), ('first sequence', n)
        assert b[n] == automaton_output(n, MORPH_2), ('second sequence', n)
        if n + 1 < limit and n % 2 == 0:
            assert a[n] + a[n+1] == 1
            assert b[n] + b[n+1] == 1
    running = [0]
    for i in range(limit):
        running.append(running[-1] + (-1)**(a[i]+b[i]))
    for k in range(10):
        assert running[4**k] == actual_s[k], ('full block', k)
    # Independent random-but-reproducible aligned-block decomposition.
    seed = 1234567
    sample = {0,1,2,3,4,15,16,64,255,256,257,1024,4096,65536,limit}
    for _ in range(256):
        seed = (1103515245 * seed + 12345) % (2**31)
        sample.add(seed % (limit+1))
    for n in sorted(sample):
        assert prefix_value(powers, n) == running[n], ('partial block', n)
    print('VERIFY_OK',
          'transitions=64',
          'exact_charpoly_degree=16',
          'nested_vs_DFAO_indices='+str(limit),
          'full_block_levels=0..9',
          'transfer_levels=0..12',
          'aligned_prefix_checks='+str(len(sample)),
          'S8='+str(actual_s[8]),
          'S9='+str(actual_s[9]))


if __name__ == '__main__':
    main()
