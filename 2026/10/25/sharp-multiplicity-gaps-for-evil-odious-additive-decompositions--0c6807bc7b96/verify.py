"""Reproduce finite checks for the sharp mixed evil-odious sum theorem.
The infinite theorem is proved separately by the binary recurrences.
"""

def convolution(nmax):
    c = [0] * nmax
    c[0] = 1
    for n in range(1, nmax):
        if n & 1:
            c[n] = -2 * c[n // 2]
        else:
            c[n] = c[n // 2] + c[n // 2 - 1]
    return c


def main():
    limit = 1 << 19
    c = convolution(limit)
    lower = []
    upper = []
    mersenne = []
    for n in range(limit):
        assert (n + 1 - c[n]) % 4 == 0
        r = (n + 1 - c[n]) // 4
        assert r >= 0
        if (n + 1) & n == 0:
            k = (n + 1).bit_length() - 1
            assert c[n] == ((-1) ** k) * (n + 1)
            assert r == (0 if k % 2 == 0 else (n + 1) // 2)
            mersenne.append(n)
        else:
            assert 5 * abs(c[n]) <= 3 * (n + 1)
            assert 10 * r >= n + 1 and 5 * r <= 2 * (n + 1)
            if 10 * r == n + 1:
                lower.append(n)
            if 5 * r == 2 * (n + 1):
                upper.append(n)
    assert lower == [10 * (4 ** k) - 1 for k in range(9) if 10 * 4 ** k - 1 < limit]
    assert upper == [5 * (4 ** k) - 1 for k in range(9) if 5 * 4 ** k - 1 < limit]
    assert mersenne == [(1 << k) - 1 for k in range(20)]

    # Independent direct digit parity / representation-count verification.
    brute_limit = 2049
    parity = [(-1) ** (n.bit_count() % 2) for n in range(brute_limit)]
    for n in range(brute_limit):
        direct_c = sum(parity[j] * parity[n-j] for j in range(n + 1))
        direct_r = sum(1 for j in range(n+1) if parity[j] == 1 and parity[n-j] == -1)
        assert direct_c == c[n]
        assert direct_r == (n + 1 - c[n]) // 4
    print('VERIFIED: 524288 recurrence cases, 2049 direct convolution and mixed-sum cases')
    print('VERIFIED: exact Mersenne exception pattern and all finite equality indices')

if __name__ == '__main__':
    main()
