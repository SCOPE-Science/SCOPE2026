from math import comb, factorial


def alpha_numerators(n, m):
    N = n - m
    weights = [comb(n, k) * (m ** k) * (N ** (n - k)) for k in range(n + 1)]
    pref = []
    s = 0
    for w in weights:
        s += w
        pref.append(s)
    total = s
    out = []
    for i in range(1, m + 1):
        left = pref[m - i]
        right = total - pref[m + i - 1]
        out.append(left - right)
    return out


def condition_l1(a):
    m = len(a)
    return any(all(x >= 0 for x in a[:ell]) and all(x <= 0 for x in a[ell:])
               for ell in range(1, m + 1))


def condition_l2(a):
    s = 0
    for x in a:
        s += x
        if s < 0:
            return False
    return True


def check_grid():
    cases = 0
    for m in range(1, 31):
        for n in range(2 * m, min(8 * m, 180) + 1):
            a = alpha_numerators(n, m)
            assert condition_l1(a) or condition_l2(a), (m, n, a)
            cases += 1
    return cases


def check_endpoint_grid():
    cases = 0
    for m in range(3, 81):
        assert m ** (2 * m) > factorial(2 * m)
        for N in range(m + 1, min(6 * m, 300) + 1):
            lhs = comb(N + m, 2 * m) * (m ** (2 * m))
            rhs = N ** (2 * m)
            assert lhs > rhs, (m, N)
            cases += 1
    return cases


def check_ratio_sign_identity():
    cases = 0
    for m in range(3, 60):
        for N in range(m + 1, min(4 * m, 180) + 1):
            for i in range(1, m):
                left = m * m * (N - i) * (N + i + 1) - N * N * (m + i + 1) * (m - i)
                right = (N - m) * ((N + m) * i * (i + 1) - m * N)
                assert left == right
                cases += 1
    return cases


if __name__ == '__main__':
    c1 = check_grid()
    c2 = check_endpoint_grid()
    c3 = check_ratio_sign_identity()
    print('VERIFY_OK', c1, c2, c3)
