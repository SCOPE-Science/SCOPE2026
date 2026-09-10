"""Exact (stdlib-only) verification for lane-517 Gap certificate.

Checks, with exact Fraction arithmetic:
  H(4/3), H(2), H''<0 on [4/3,2]        (piece A: s in [3/8,1/2])
  S(8/5), S(2), S''<0 on [8/5,2]        (piece B: s in [1/2,5/8])
  threshold 11 > 808/75 = (32/3)*1.01, margin 17/75
plus a dense float scan of P(s) over the scope.
"""
from fractions import Fraction as F

def main():
    ok = True
    # ---- Piece A: H(u) = 7u^5 - 32u^4 + 240u - 192, u in [4/3,2] ----
    def H(u): return 7*u**5 - 32*u**4 + 240*u - 192
    def Hpp(u): return 140*u**3 - 384*u**2  # = 28u^2(5u-96/7) <0 for u<=2<96/35
    a, b = F(4,3), F(2)
    assert H(b) == 0, H(b)
    assert H(a) == F(13696,243), H(a)          # > 0
    assert H(a) > 0
    # H''(u) = 28u^2(5u - 96/7... ) ; increasing in u (H'''=420u^2-768u=84u(5u-64/7)>0
    # on [4/3,2]? check H''(2) = 140*8-384*4 = 1120-1536 = -416 <0, and H'' increasing
    # since H'''(u)=84u(5u-9.14..)>0 there. Verify monotonic bound rigorously:
    assert Hpp(b) == -416
    # H'''(u) = 420u^2 - 768u = 12u(35u-64); zero at u=64/35~1.829? careful!
    # So H'' decreases then increases; bound its max by max(H''(4/3),H''(2)) since H'' convex
    # (H''''=840u-768>0 on [4/3,2] as 840*4/3=1120>768). Check:
    assert H(a) is not None
    import math
    H2a = F(140)*a**3 - F(384)*a**4 if False else (140*a**3 - 384*a**2)
    print("H''(4/3) =", H2a, "=", float(H2a))
    print("H''(2)   =", Hpp(b))
    assert H2a < 0 and Hpp(b) < 0
    # H''''(u)=840u-768 >= 840*4/3-768 = 352 > 0 so H'' convex -> max at an endpoint <0
    assert F(840)*a - 768 > 0
    print("H concave on [4/3,2]: OK; H(4/3)=13696/243>0, H(2)=0 -> H>=chord>=0")

    # ---- Piece B: S(t) = 3t^4-4t^3-64t^2+128t-16, t in [8/5,2] ----
    def S(t): return 3*t**4 - 4*t**3 - 64*t**2 + 128*t - 16
    def Spp(t): return 36*t**2 - 24*t - 128
    c, d = F(8,5), F(2)
    assert S(d) == 0, S(d)
    assert S(c) == F(17648,625), S(c)
    assert S(c) > 0
    # S''(t)=36t^2-24t-128 increasing for t>=1/3; max at t=2: -32 <0
    assert Spp(d) == -32
    assert Spp(c) == F(36*64,25) - F(24*8,5) - 128
    print("S''(8/5) =", Spp(c), "=", float(Spp(c)), "; S''(2) =", Spp(d))
    assert Spp(c) < 0 and Spp(d) < 0
    print("S concave on [8/5,2]: OK; S(8/5)=17648/625>0, S(2)=0 -> S>=chord>=0")

    # ---- Threshold ----
    assert F(11,1) > F(808,75)
    margin = F(11,1) - F(808,75)
    assert margin == F(17,75), margin
    print("threshold: 11 > 808/75, margin 17/75: OK")

    # ---- Exact endpoint products ----
    # s=3/8: V=17/24, V*=3824/243
    assert F(4)*F(3,8)+7 == F(17,2)          # 4s+7 = 17/2
    V38, Vs38 = F(17,24), F(3824,243)
    assert V38*Vs38 == F(8126,729)
    assert V38*Vs38 >= 11
    # s=1/2: V=3/4, V*=44/3, P=11
    assert F(3,4)*F(44,3) == 11
    # s=5/8: V=7/8, V*=?
    V58 = F(7,8)
    # t=8/5: V* = t(3t^3-16t^2+128)/12
    t = F(8,5)
    Vs58 = t*(3*t**3-16*t**2+128)/12
    print("P(3/8) =", V38*Vs38, "=", float(V38*Vs38))
    print("P(1/2) = 11")
    print("P(5/8) =", V58*Vs58, "=", float(V58*Vs58))
    assert V58*Vs58 >= 11

    # ---- Dense float scan (non-rigorous sanity; proof is the chord bounds) ----
    def Pf(s):
        if s <= 0.5:
            t = 1/s
            return ((4*s+7)/12)*(16-(4-t)**4/12)
        else:
            t = 1/s
            return (s+0.25)*(t*(3*t**3-16*t**2+128)/12)
    N = 2001
    m = min(Pf(0.375 + (0.625-0.375)*i/(N-1)) for i in range(N))
    print("float scan min P =", m)
    assert m >= 11 - 1e-9
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
