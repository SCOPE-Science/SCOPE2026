from decimal import Decimal, localcontext

# High-precision checks of the exact closed form; the analytic proof is in RESULT.md.
with localcontext() as ctx:
    ctx.prec = 120
    three = Decimal(3).sqrt()
    C = Decimal(2) * three / Decimal(3)
    c = C - Decimal(1)
    for n in (1, 2, 3):
        h = Decimal('0.1') * (Decimal('0.01') ** (n - 1))
        s = (h ** 5) / Decimal(2)
        y3 = (C - (c * s).exp() - c * (-s).exp()) / C
        assert y3 < 0, (n, y3)
        print(f'n={n}, h={h}, y3={y3}')
