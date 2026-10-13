import math


def source_values(r, beta):
    u = 1.0 / math.tanh(beta / 2.0)
    s = 0.5 * math.asinh(u * math.sinh(2.0 * r))
    C = math.cosh(2.0 * r)
    S = math.sinh(2.0 * r)
    direct = u * C * (u * math.exp(2.0 * r) - math.exp(2.0 * s))
    rational = u * C * (u * u - 1.0) / (u * C + math.sqrt(1.0 + u * u * S * S))
    return u, s, direct, rational


def h(z):
    A = (1.0 + z) ** 2 / (4.0 * z)
    B = (1.0 - z) ** 2 / (4.0 * z)
    if B == 0.0:
        return A * math.log(A)
    return A * math.log(A) - B * math.log(B)


def main():
    beta_c = math.log(2.0 + math.sqrt(3.0))
    assert abs(math.sinh(beta_c / 2.0) - 1.0 / math.sqrt(2.0)) < 1e-14

    for beta in (0.33, beta_c, 2.5, 5.0, 10.0):
        for r in (0.25, 0.75, 2.0, 3.0):
            u, s, direct, rational = source_values(r, beta)
            assert abs(direct - rational) <= 2e-10 * max(1.0, abs(rational))
            lower = (u * u - 1.0) / 2.0
            assert rational > lower
            q = math.tanh(s) ** 2
            if r > 0.0:
                for k in (1, 2, 5, 20):
                    finite_sum = sum((q ** n) / (math.cosh(s) ** 2) for n in range(k))
                    closed = 1.0 - q ** k
                    assert abs(finite_sum - closed) < 2e-13

    for beta in (0.33, beta_c):
        for r in (0.0, 0.5, 2.0, 5.0):
            u, s, direct, rational = source_values(r, beta)
            assert rational >= 1.0 - 2e-12

    for beta in (2.5, 5.0):
        u = 1.0 / math.tanh(beta / 2.0)
        a = 1.0 / (math.sqrt(2.0) * math.sinh(beta / 2.0))
        F_inf = (1.0 - a) ** 2
        C_beta = (u / 4.0) * (-math.log(1.0 - F_inf))
        for r in (4.0, 5.0, 6.0):
            _, s, _, R2 = source_values(r, beta)
            F = (1.0 - min(1.0, math.sqrt(R2))) ** 2
            q = math.tanh(s) ** 2
            L = math.log(1.0 - F) / math.log(q)
            assert abs(L / math.exp(2.0 * r) - C_beta) / C_beta < 2e-3

    for beta in (0.33, beta_c, 2.5):
        u = 1.0 / math.tanh(beta / 2.0)
        target = math.e / (4.0 * u)
        r = 6.0
        z = u * math.exp(-2.0 * r)
        ratio = math.exp(h(z)) / math.exp(2.0 * r)
        assert abs(ratio - target) / target < 2e-6

    print('VERIFY_OK')


if __name__ == '__main__':
    main()
