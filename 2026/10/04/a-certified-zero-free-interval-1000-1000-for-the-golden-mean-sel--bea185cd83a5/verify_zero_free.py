#!/usr/bin/env python3
"""Interval certificate for a finite zero-free range of the golden-mean self-similar Fourier transform.

Requires mpmath 1.3.0. The proof uses mpmath.iv outward interval arithmetic.
"""
from collections import deque
import mpmath as mp

R = 1000.0
DEPTH = 42
START_WIDTH = 0.1
MIN_WIDTH = 1.0e-7
mp.iv.dps = 30
iv = mp.iv
p = (iv.sqrt(5) - 1) / 2


def finite_product_box(a, b):
    """Enclose the depth-DEPTH matrix-product approximation F_N on [a,b]."""
    x = iv.mpf([a, b])
    A = iv.mpc(1, 0)
    B = iv.mpc(1, 0)
    for k in range(DEPTH - 1, -1, -1):
        y = x / (2 ** k)
        A, B = p * A + p * p * iv.exp(-iv.j * iv.pi * y) * B, A
    return A


def main():
    # supp(mu) subset [0,2/3] gives |F(t)-1| <= 4*pi*|t|/3.
    # Since 22/7 > pi, the rational bound below is safely larger.
    # The matrix M(t) has max-row-sum norm 1 because p+p^2=1.
    tail = iv.mpf(88) / 21 * iv.mpf(1000) / (2 ** DEPTH)

    pending = deque()
    j = 0
    while j * START_WIDTH < R:
        a = j * START_WIDTH
        b = min(R, (j + 1) * START_WIDTH)
        pending.append((a, b, 0))
        j += 1

    certified = 0
    splits = 0
    min_width = START_WIDTH
    min_margin_lower = float('inf')
    max_depth_seen = 0

    while pending:
        a, b, d = pending.popleft()
        z = finite_product_box(a, b)
        # Keep certification comparisons in interval arithmetic. A box is safe
        # if one coordinate is entirely farther from zero than the tail disc.
        margins = (
            z.real.a - tail,
            -z.real.b - tail,
            z.imag.a - tail,
            -z.imag.b - tail,
        )
        positive = [m for m in margins if m > 0]
        if positive:
            certified += 1
            min_width = min(min_width, b - a)
            # Diagnostic only; certification above did not convert endpoints.
            local = max(float(m.a) for m in positive)
            min_margin_lower = min(min_margin_lower, local)
            max_depth_seen = max(max_depth_seen, d)
            continue
        if b - a <= MIN_WIDTH:
            raise RuntimeError(
                f"uncertified interval [{a:.17g},{b:.17g}] at width {b-a:.3e}; "
                f"box={z}, tail={tail}"
            )
        m = (a + b) / 2.0
        pending.append((a, m, d + 1))
        pending.append((m, b, d + 1))
        splits += 1

    print(
        f"VERIFY_OK R={R:g} depth={DEPTH} leaves={certified} splits={splits} "
        f"tail_upper={float(tail.b):.17e} "
        f"min_margin_lower={min_margin_lower:.17e} "
        f"min_width={min_width:.17e} max_bisection_depth={max_depth_seen} "
        f"mpmath={mp.__version__} iv_dps={mp.iv.dps}"
    )


if __name__ == '__main__':
    main()
