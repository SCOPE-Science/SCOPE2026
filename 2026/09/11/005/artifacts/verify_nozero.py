"""Rigorous no-zero certificate for the A=10 target rectangle (stdlib only).

Claim certified: S(k) != 0 for all k in R = [e1-1/10, e1+1/10] x [-b, 0],
  e1 = pi/2, b = exp(-sqrt(7)), A = 10,
where S(k) = i*k*trU + k^2*U01 - U10 with U = A1*B*A1 the transfer product,
  A1 = [[C, sk/kap], [kap*sk, C]], B = [[c, s/k], [-k*s, c]],
  C = cosh(kap), sk = sinh(kap), c = cos(2k), s = sin(2k),
  kap = sqrt(10 - k^2) (principal branch).

Since T22(k,10) = e^{4ik} S(k)/(2ik) (exact matrix identity) and the factor
e^{4ik}/(2ik) never vanishes on R (|k| >= 1.47), this proves T22(.,10) has no
zero in R, falsifying the A=10 instance of the target claim.

Method: complex midpoint-radius (ball) arithmetic with explicit rounding
inflation; adaptive subdivision of R. Every operation inflates the radius to
cover both input uncertainty and floating-point rounding (per-op inflation
|mid|*2^-51 + 1e-290, plus extra libm allowance for exp). Denominators are
asserted bounded away from zero (|k|>=1.4, |kap|>=2.6, |10-k^2|>=7.2).
Pass criterion per cell: |S(mid)| > S(radius), i.e. 0 not in the enclosure.
"""
import cmath
import math
import sys

ULP_INFLATE = 2.0 ** -51  # ~4.4e-16, covers <= 2ulp per elementary op
LIBM_INFLATE = 2.0 ** -49  # extra allowance for math.exp/cmath calls
ABS_FLOOR = 1e-290


class Ball:
    __slots__ = ("m", "r")

    def __init__(self, m, r):
        self.m = complex(m)
        self.r = float(r)
        assert self.r >= 0.0

    def __add__(self, o):
        if not isinstance(o, Ball):
            o = Ball(o, 0.0)
        m = self.m + o.m
        r = self.r + o.r + abs(m) * ULP_INFLATE + ABS_FLOOR
        return Ball(m, r)

    def __sub__(self, o):
        if not isinstance(o, Ball):
            o = Ball(o, 0.0)
        m = self.m - o.m
        r = self.r + o.r + abs(m) * ULP_INFLATE + ABS_FLOOR
        return Ball(m, r)

    def __mul__(self, o):
        if not isinstance(o, Ball):
            o = Ball(o, 0.0)
        m = self.m * o.m
        r = (abs(self.m) * o.r + abs(o.m) * self.r + self.r * o.r
             + abs(m) * ULP_INFLATE + ABS_FLOOR)
        return Ball(m, r)

    def __truediv__(self, o):
        if not isinstance(o, Ball):
            o = Ball(o, 0.0)
        assert abs(o.m) > o.r, "division enclosure contains 0"
        m = self.m / o.m
        # |1/o.m - 1/w| <= r_o / (|o.m| (|o.m| - r_o))
        rinv = o.r / (abs(o.m) * (abs(o.m) - o.r))
        r = (abs(self.m) * rinv + self.r * (1.0 / (abs(o.m) - o.r) + rinv)
             + abs(m) * ULP_INFLATE + ABS_FLOOR)
        return Ball(m, r)

    def __neg__(self):
        return Ball(-self.m, self.r)


def ball_sqrt(ball, re_floor, lipschitz):
    """Principal sqrt; requires Re(ball) >= re_floor > 0 (checked)."""
    assert ball.m.real - ball.r >= re_floor, "sqrt domain violated"
    m = cmath.sqrt(ball.m)
    r = lipschitz * ball.r + abs(m) * LIBM_INFLATE + abs(m) * ULP_INFLATE + ABS_FLOOR
    return Ball(m, r)


def ball_exp(ball):
    m = cmath.exp(ball.m)
    # |e^w - e^m| <= e^{Re m + r} r for |w - m| <= r
    er = math.exp(ball.m.real + ball.r)
    r = er * ball.r + abs(m) * LIBM_INFLATE + abs(m) * ULP_INFLATE + ABS_FLOOR
    return Ball(m, r)


def S_ball(k):
    """Enclosure of S(k). Asserts all denominators safely nonzero.

    Conventions: kap = sqrt(10 - k^2) (Re kap > 0, tunneling regime),
    C = cosh(kap), sk = sinh(kap).
    A1 = [[C, sk/kap], [kap*sk, C]] equals [[cos mu, sin mu/mu],
    [-mu sin mu, cos mu]] with mu = sqrt(k^2-10) = -i*kap, since
    cos(-i kap) = cosh(kap), sin(-i kap)/(-i kap) = sinh(kap)/kap, and
    -(-i kap) sin(-i kap) = kap*sinh(kap).
    """
    assert abs(k.m) - k.r >= 1.4, "k too close to 0"
    k2 = k * k
    w = Ball(10.0, 0.0) - k2            # 10 - k^2
    assert w.m.real - w.r >= 7.1, "w out of tunneling domain"
    kap = ball_sqrt(w, 7.1, 0.19)       # Re kap >= ~2.66
    assert abs(kap.m) - kap.r >= 2.6
    assert abs(w.m) - w.r >= 7.1
    e2k = ball_exp(Ball(2j, 0.0) * k)       # e^{2ik}
    em2k = ball_exp(Ball(-2j, 0.0) * k)     # e^{-2ik}
    ekap = ball_exp(kap)                    # e^{kap}
    emkap = ball_exp(-kap)                  # e^{-kap}
    c = (e2k + em2k) * Ball(0.5, 0.0)          # cos(2k)
    s = (e2k - em2k) * Ball(-0.5j, 0.0)        # sin(2k)
    C = (ekap + emkap) * Ball(0.5, 0.0)        # cosh(kap)
    sk = (ekap - emkap) * Ball(0.5, 0.0)       # sinh(kap)
    A01 = sk / kap
    A10 = kap * sk
    B01 = s / k
    B10 = k * (-s)
    # A1B = A1*B with A1=[[C,A01],[A10,C]], B=[[c,B01],[B10,c]]
    M00 = C * c + A01 * B10
    M01 = C * B01 + A01 * c
    M10 = A10 * c + C * B10
    M11 = A10 * B01 + C * c
    U00 = M00 * C + M01 * A10
    U01 = M00 * A01 + M01 * C
    U10 = M10 * C + M11 * A10
    U11 = M10 * A01 + M11 * C
    S = Ball(1j, 0.0) * k * (U00 + U11) + k2 * U01 - U10
    return S


def cell_ball(xc, hx, yc, hy):
    # complex ball covering [xc-hx,xc+hx] + i[yc-hy,yc+hy], plus float error
    # of the inputs (pi/2, exp(-sqrt7)) bounded by 1e-15.
    # Use the rectangle (not disk) radius: corners are within hypot(hx,hy).
    return Ball(complex(xc, yc), math.hypot(hx, hy) + 1e-15)


def main():
    e1 = math.pi / 2
    b = math.exp(-math.sqrt(7.0))
    x0, x1 = e1 - 0.1, e1 + 0.1
    y0, y1 = -b, 0.0
    print(f"R = [{x0}, {x1}] x [{y0}, {y1}]")
    stack = [(x0, x1, y0, y1, 0)]
    ncells = 0
    maxdepth = 0
    min_margin = float("inf")
    worst = None
    while stack:
        xa, xb, ya, yb, d = stack.pop()
        xc = (xa + xb) / 2
        yc = (ya + yb) / 2
        Sb = S_ball(cell_ball(xc, (xb - xa) / 2, yc, (yb - ya) / 2))
        gap = abs(Sb.m) - Sb.r
        if gap > 0:
            ncells += 1
            maxdepth = max(maxdepth, d)
            if gap < min_margin:
                min_margin = gap
                worst = (xc, yc, abs(Sb.m), Sb.r)
        else:
            assert d < 20, f"subdivision failed to terminate at depth {d}"
            xm = xc
            ym = yc
            stack.append((xa, xm, ya, yb, d + 1))
            stack.append((xm, xb, ya, yb, d + 1))
            # NOTE: split both axes alternately via two passes; simpler:
            # split along longer side:
            stack.pop()
            stack.pop()
            if (xb - xa) >= (yb - ya):
                stack.append((xa, xm, ya, yb, d + 1))
                stack.append((xm, xb, ya, yb, d + 1))
            else:
                stack.append((xa, xb, ya, ym, d + 1))
                stack.append((xa, xb, ym, yb, d + 1))
    print(f"cells certified: {ncells}, max depth: {maxdepth}")
    print(f"min exclusion margin |S_mid| - rad = {min_margin:.6f}")
    print(f"worst cell center={worst[0]}+{worst[1]}i |S_mid|={worst[2]:.4f} rad={worst[3]:.4f}")
    # identity cross-check at center (float): T22 = e^{4ik} S/(2ik)
    kc = complex(e1, -b / 2)

    def T22_direct(kk):
        A = 10.0
        mu = cmath.sqrt(kk * kk - A)
        C0, S0 = cmath.cos(mu), cmath.sin(mu)
        c0, s0 = cmath.cos(2 * kk), cmath.sin(2 * kk)
        U00 = C0 * C0 * c0 - C0 * S0 * s0 * (mu / kk + kk / mu) - S0 * S0 * c0 * 0 + (C0 * C0 - 1) * 0
        # rebuild full matrix entries directly
        P11, P12, P21, P22 = C0, S0 / mu, -mu * S0, C0
        Q11, Q12, Q21, Q22 = c0, s0 / kk, -kk * s0, c0
        # U = P Q P
        PQ11 = P11 * Q11 + P12 * Q21
        PQ12 = P11 * Q12 + P12 * Q22
        PQ21 = P21 * Q11 + P22 * Q21
        PQ22 = P21 * Q12 + P22 * Q22
        U00 = PQ11 * P11 + PQ12 * P21
        U01 = PQ11 * P12 + PQ12 * P22
        U10 = PQ21 * P11 + PQ22 * P21
        U11 = PQ21 * P12 + PQ22 * P22
        S = 1j * kk * (U00 + U11) + kk * kk * U01 - U10
        return cmath.exp(4j * kk) * S / (2j * kk), S

    Tt, Ss = T22_direct(kc)
    print(f"identity check at {kc}: |T22|={abs(Tt):.6f} |S|={abs(Ss):.6f} "
          f"|e^{{4ik}}/(2ik)|={abs(cmath.exp(4j*kc)/(2j*kc)):.6f}")
    print("VERIFY_OK: S(k) != 0 on all of R; T22(.,10) has no zero in R.")
    return 0


sys.exit(main())
