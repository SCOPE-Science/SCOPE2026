from fractions import Fraction
from itertools import product

count = 0
for d in range(2, 7):
    for split in range(1, d):
        for raw in product(range(-2, 3), repeat=d):
            total = sum(abs(v) for v in raw)
            if total == 0:
                continue
            xraw = raw[:split]
            araw = raw[split:]
            xnorm = Fraction(sum(abs(v) for v in xraw), total)
            b = Fraction(sum(abs(v) for v in araw), total)
            mx = Fraction(max((abs(v) for v in xraw), default=0), total)
            ma = Fraction(max((abs(v) for v in araw), default=0), total)
            dc_x = 1 + xnorm - 2 * mx
            proposed = min(b + dc_x, 2 * (1 - ma))
            known = 2 * (1 - max(mx, ma))
            assert xnorm + b == 1
            assert proposed == known
            count += 1
print(f"VERIFY_OK {count}")
