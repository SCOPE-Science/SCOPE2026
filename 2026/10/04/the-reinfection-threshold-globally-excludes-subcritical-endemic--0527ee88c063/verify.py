from fractions import Fraction as Q


def F(I, beta, B, La, alpha, mu, gamma, delta, theta, sigma):
    A = alpha + mu
    M = mu + alpha * sigma
    K = (gamma + mu) * (delta + mu + theta) / gamma
    return La * beta * (M + beta * sigma * I) / ((A + beta * I) * (mu + beta * sigma * I)) + delta * B * I / (mu + B * I) - K


def check(params):
    La, alpha, mu, gamma, delta, theta, sigma = params
    A = alpha + mu
    M = mu + alpha * sigma
    K = (gamma + mu) * (delta + mu + theta) / gamma
    H = K - delta
    P = mu * mu + alpha * alpha * sigma * sigma + alpha * mu * sigma * (1 + sigma)
    bs = A * mu * K / (La * M)
    Bs = bs * K * P / (delta * A * M)
    assert H > 0 and P > 0 and Q(0) < sigma <= 1
    C0 = H * P * P + A * delta * mu * sigma * (M - mu) * (M - A * sigma)
    C1 = M * bs * sigma * H * P
    assert C0 > 0 and C1 > 0
    for I in [Q(1,7), Q(2,3), Q(5,2), Q(9,1)]:
        D = (A + bs * I) * (mu + bs * sigma * I) * (mu + Bs * I)
        lhs = D * F(I, bs, Bs, La, alpha, mu, gamma, delta, theta, sigma)
        rhs = -I * I * K * bs * bs * (C0 + C1 * I) / (A * M * M * delta)
        assert lhs == rhs
        assert rhs < 0
        for rb, rB in [(Q(1,2),Q(1,2)), (Q(3,4),Q(4,5)), (Q(1,1),Q(2,3))]:
            beta = rb * bs
            B = rB * Bs
            assert F(I, beta, B, La, alpha, mu, gamma, delta, theta, sigma) <= F(I, bs, Bs, La, alpha, mu, gamma, delta, theta, sigma)
            assert F(I, beta, B, La, alpha, mu, gamma, delta, theta, sigma) < 0


sets = [
    (Q(13),Q(2),Q(3),Q(5),Q(7),Q(11),Q(2,3)),
    (Q(17),Q(5,2),Q(4),Q(9,2),Q(3),Q(8),Q(1,2)),
    (Q(19),Q(3),Q(2),Q(7),Q(5),Q(13),Q(1)),
]
for s in sets:
    check(s)
print('VERIFY_OK')
