"""Finite high-precision checks of the two ordered triangular stages."""
from decimal import Decimal as D, localcontext


def stage(a, b, s, x1, x2):
    """First two coordinates after exp(s*(a*G12+b*G23))."""
    u, v = (-a * s).exp(), (-b * s).exp()
    return u * x1, v * x2 + a / (a - b) * (v - u) * x1


with localcontext() as ctx:
    ctx.prec = 120
    alpha = D('0.5') + D(3).sqrt() / 3
    beta = 1 - alpha
    C = alpha - beta
    c = C - 1
    for n in range(1, 6):
        h = D(10) ** (1 - 2 * n)
        s = h ** 5 / 2
        x1, x2 = stage(beta, alpha, s, D(1), D(0))
        y1, y2 = stage(alpha, beta, s, x1, x2)
        y3 = 1 - y1 - y2
        closed = (C - (c * s).exp() - c * (-s).exp()) / C
        assert abs(y1 - (-s).exp()) < D('1e-115')
        assert abs(y2 - ((c * s).exp() - (-s).exp()) / C) < D('1e-115')
        assert abs(y3 - closed) < D('1e-115') and y3 < 0

        w1, w2 = stage(beta, alpha, s, *stage(alpha, beta, s, D(1), D(0)))
        reversed_y3 = 1 - w1 - w2
        reversed_closed = (C - (C + 1) * (-s).exp() + (-2 * alpha * s).exp()) / C
        assert abs(reversed_y3 - reversed_closed) < D('1e-115') and reversed_y3 > 0
        print(f'n={n} h={h} ordered={y3:.12E} reversed={reversed_y3:.12E}')
