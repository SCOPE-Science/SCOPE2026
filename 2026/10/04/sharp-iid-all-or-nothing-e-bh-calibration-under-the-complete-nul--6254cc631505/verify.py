import math


def binom_tail(K, p, r):
    return sum(math.comb(K, j) * (p ** j) * ((1-p) ** (K-j)) for j in range(r, K+1))


def envelope(K, alpha):
    vals = [(r, binom_tail(K, r*alpha/K, r)) for r in range(1, K+1)]
    return max(vals, key=lambda x: x[1]), vals


def main():
    alpha0 = 1/(math.e**2 + 0.5)
    assert abs(alpha0 - 0.12675787666607524) < 1e-15
    for alpha in (0.01, 0.05, 0.10):
        assert alpha < alpha0
        for K in range(1, 201):
            (r, val), vals = envelope(K, alpha)
            assert r == 1, (alpha, K, r, val)
            target = 1-(1-alpha/K)**K
            assert abs(val-target) < 5e-13, (alpha, K, val, target)
            if K >= 2:
                assert all(v < target + 1e-14 for rr, v in vals if rr >= 2)
    a = 0.05
    expected = {
        10: 0.048889869534228136,
        20: 0.04883012474683324,
        100: 0.04878246975766576,
        1000: 0.048771764574954246,
    }
    for K, want in expected.items():
        got = 1-(1-a/K)**K
        assert abs(got-want) < 1e-15, (K, got, want)
    limit = 1-math.exp(-a)
    assert abs(limit-0.048770575499285984) < 1e-15
    assert limit < a
    print('VERIFY_OK')
    print('alpha0=', repr(alpha0))
    print('K100_alpha005=', repr(expected[100]))
    print('limit_alpha005=', repr(limit))

if __name__ == '__main__':
    main()
