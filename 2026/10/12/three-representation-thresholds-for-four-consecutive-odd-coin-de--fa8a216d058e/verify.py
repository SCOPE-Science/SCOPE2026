"""Finite arithmetic checks of the three-representation threshold for four odd coins.

The unrestricted formula is proved separately; this script is supplementary.
"""

def ceil3(k):
    return (k + 2) // 3


def predicted_apery(a):
    u = ceil3(a + 2)
    v = ceil3(a + 3)
    return [
        a * (2 + u) if j == 0 else
        a * (2 + v) + 2 if j == 1 else
        a * (2 + u) + 4 if j == 2 else
        a * max(3, ceil3(j + 3)) + 2 * j
        for j in range(a)
    ]


def count_cap3(a, limit):
    c = [0] * (limit + 1)
    c[0] = 1
    for coin in (a, a + 2, a + 4, a + 6):
        for n in range(coin, limit + 1):
            c[n] = min(3, c[n] + c[n - coin])
    return c


def run():
    cases = 0
    residues = 0
    prethresholds = 0
    for a in range(9, 202, 2):
        m = predicted_apery(a)
        W = max(m)
        u, v = ceil3(a + 2), ceil3(a + 3)
        jmax = 1 if a % 3 == 1 else 2
        g = a * (1 + (v if jmax == 1 else u)) + (2 if jmax == 1 else 4)
        assert W - a == g
        assert [j for j, mj in enumerate(m) if mj == W] == [jmax]
        d = count_cap3(a, W + 2 * a)
        for j, threshold in enumerate(m):
            residue = 2 * j % a
            assert threshold % a == residue
            assert d[threshold] == 3, (a, j, threshold)
            for N in range(residue, threshold, a):
                assert d[N] < 3, (a, j, N, threshold)
                prethresholds += 1
            residues += 1
        assert d[g] < 3
        assert all(d[N] == 3 for N in range(g + 1, W + 2 * a + 1))
        cases += 1
    print('VERIFY_OK')
    print('odd_a_range=9..201')
    print('parameter_cases=', cases)
    print('apery_residues_checked=', residues)
    print('prethreshold_positions_checked=', prethresholds)
    print('upper_interval_for_each_case=g+1..max_apery+2*a')
    print('finite_check_is_not_infinite_proof=True')

if __name__ == '__main__':
    run()
