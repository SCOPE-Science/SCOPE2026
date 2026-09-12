"""Exact tilt-wall enumeration for the branch-fixed Kuznetsov class on a general
special Gushel-Mukai threefold. Stdlib only, exact Fractions arithmetic.

Setup: Pic(X) = Z*H, H^3 = 10, beta = -3/2.
  D(r,k) = 10*k + 15*r            (== H^2.ch1^beta)
  A(r,k,e) = e + 15*k + 45*r/4    (== H.ch2^beta), e = H.ch2 in (1/2)Z
  alpha^2(w|v) = (Av*Dw - Aw*Dv) / (5*(rv*Dw - rw*Dv))
  BG discriminant DH(r,k,e) = 100*k^2 - 20*r*e >= 0 (beta-independent).

Kuznetsov lattice (from HRR with H.c2(T) = 24, H.ch2(U^vee) = 1, ch3(U^vee) = -1/3):
  E in Ku(X)  <=>  e = -2*r - 4*k,  ch3 = -5*k/6.
Witness class v = [pr(O_x)], x in branch locus: (rv,kv,ev) = (5,-2,-2), ch3 = 5/3.
  Dv = 55, Av = 97/4, DH(v) = 600. Primitive since gcd(5,2) = 1.
"""
from fractions import Fraction as Q

BETA = Q(-3, 2)
H3 = Q(10)


def D_of(r, k):
    return H3 * Q(k) - BETA * H3 * Q(r)   # 10k + 15r


def A_of(r, k, e):
    e = Q(e)
    return e - BETA * H3 * Q(k) + (BETA * BETA / 2) * H3 * Q(r)


def Delta(r, k, e):
    return (H3 * Q(k)) ** 2 - 2 * H3 * Q(r) * Q(e)


def alpha2(v, w):
    rv, kv, ev = v
    rw, kw, ew = w
    Dv, Dw = D_of(rv, kv), D_of(rw, kw)
    Av, Aw = A_of(rv, kv, ev), A_of(rw, kw, ew)
    den = 5 * (Q(rv) * Dw - Q(rw) * Dv)
    if den == 0:
        return None
    return (Av * Dw - Aw * Dv) / den


def main():
    v = (5, -2, Q(-2))
    rv, kv, ev = v
    Dv = D_of(rv, kv)
    Av = A_of(rv, kv, ev)
    assert Dv == 55 and Av == Q(97, 4), (Dv, Av)
    assert Delta(*v) == 600
    # Ku relations
    assert Q(ev) == -2 * rv - 4 * kv

    print("v =", v, "Dv =", Dv, "Av =", Av, "Delta =", Delta(*v))

    # ---- Lemma 1: denominator never vanishes for 0 < Dw < Dv ----
    # G = 5(rv Dw - rw Dv) = 25(5m - 11rw); zero needs 5m = 11rw with 1<=m<=10.
    # 11 prime forces rw = 5k, m = 11k, k>=1, hence m>=11: impossible.
    bad_den = []
    for m in range(1, 11):  # Dw = 5m in (0, 55)
        Dw = 5 * m
        # (rw,kw): 10k+15r = 5m  <=> 2k+3r = m
        for rw in range(-12, 13):
            if (m - 3 * rw) % 2 != 0:
                continue
            kw = (m - 3 * rw) // 2
            if 5 * (rv * Dw - rw * Dv) == 0:
                bad_den.append((rw, kw))
    print("denominator-zero types with 0<Dw<Dv:", bad_den)
    assert not bad_den
    # G > 0 forces rw <= 4: 11rw < 5m <= 50.
    for m in range(1, 11):
        for rw in range(5, 400):
            assert not (0 < 5 * m - 11 * rw), (m, rw)

    # ---- Lemma 3 (negative-width: no G>0 wall with both discriminants, rw<=-1)
    # Fix (m, rw) with rw <= -1, G > 0. The ew-conditions are:
    #   Delta(w) >= 0:  ew <= 5kw^2/rw =: hi_w   [rw<0: upper bound!]
    #   Delta(u) >= 0:  eu <= 5ku^2/ru => ew >= ev - 5ku^2/ru =: lo_u,
    #     valid when ru = 5 - rw > 0 (true here since rw <= -1).
    # So need lo_u <= hi_w. But N := lo_u - hi_w > 0 always: exact check of
    # N > 0 over [-10^6,-1] x [1,10] below; asymptotically N ~ 45|rw|/4 -> +inf
    # (5kw^2/|rw| term dominates), so holds for all rw <= -1.
    for m in range(1, 11):
        for rw in list(range(-60, 0)) + [-10**3, -10**6]:
            if (m - 3 * rw) % 2 != 0:
                continue
            kw = Q(m - 3 * rw, 2)
            ku = Q(kv) - kw
            ru = rv - rw
            assert ru > 0 and rw < 0
            N = (ev - 5 * ku * ku / ru) - 5 * kw * kw / rw
            assert N > 0, (m, rw, N)
    print("width lemma: no G>0 wall with BOTH Delta(w),Delta(u)>=0 for rw<=-1.")

    # ---- Lemma 2: exact slope equality at beta=-3/2 has no half-integral solution ----
    # Exact wall needs Aw = Av*Dw/Dv = 97m/44; 97m/44 in (1/4)Z <=> 11 | m; m <= 10.
    exact_hits = []
    for m in range(1, 11):
        Aw_exact = Av * (5 * m) / Dv  # = 97m/44
        if (Aw_exact * 4).denominator == 1:
            exact_hits.append(m)
    print("m with exact-wall Aw in (1/4)Z:", exact_hits)
    assert not exact_hits

    # ---- Theorem: enumerate ALL BG-compatible half-integral walls, take max ----
    # A wall for v is cut out by a JH factor F that is tilt-STABLE of the same
    # slope: classical H-discriminant Delta(F) >= 0 for F AND, in the D > 0
    # sector, for the complementary quotient direction (both are semistable
    # factors of the JH filtration of a semistable object of class v; this is
    # the standard necessary condition used to bound numerical walls).
    # Both signs of G are enumerated. Completeness:
    #  * Lemma 1: G = 25(5m - 11rw) != 0 (11 prime, 1 <= m <= 10).
    #  * Width lemma (Lemma 3): no G>0 wall with both discriminants for rw<=-1.
    #  * Swap symmetry: alpha^2(u|v) = alpha^2(w|v) since F_u = -F_w, G_u = -G_w
    #    (as F_v = 0). So a G<0 wall at (m,rw) mirrors a G>0 wall at
    #    (m',rw') = (11-m, 5-rw); Lemma 3 kills rw' <= -1, i.e. rw >= 6.
    #    Hence only rw in {0,...,5} can carry walls: FINITE box, both signs.
    #  * Rank-0-only (single-discriminant) infinite tails (ew -> -inf giving
    #    unbounded alpha^2) are NOT genuine JH walls: the complementary
    #    quotient violates Delta >= 0 there. They are excluded by the
    #    both-discriminant condition, exactly as in the wall-bounding
    #    literature (both JH factors of a semistable object are semistable).
    G_of = lambda m, rw: 25 * (5 * m - 11 * rw)  # = 5(rv Dw - rw Dv)
    Aw_cap = lambda m: Av * (5 * m) / Dv
    C_of = lambda rw, kw: 15 * Q(kw) + Q(45, 4) * Q(rw)  # Aw = ew + C
    import math
    recs = []
    for m in range(1, 11):
        Dw = 5 * m
        for rw in range(0, 6):
            if (m - 3 * rw) % 2 != 0:
                continue
            kw = (m - 3 * rw) // 2
            ru, ku = rv - rw, kv - kw
            Du = D_of(ru, ku)
            if Du <= 0:
                continue
            G = G_of(m, rw)
            assert G != 0  # Lemma 1
            C = C_of(rw, kw)
            cap = Aw_cap(m)
            lo2, hi2 = -10**18, 10**18  # for E2 = 2*ew
            if rw > 0:
                hi2 = min(hi2, 2 * (5 * Q(kw) ** 2 / rw))  # Delta(w) >= 0
            elif rw < 0:
                lo2 = max(lo2, 2 * (5 * Q(kw) ** 2 / rw))
            # else rw = 0: Delta(w) = 100kw^2 >= 0 free
            if ru > 0:
                lo2 = max(lo2, 2 * (ev - 5 * Q(ku) ** 2 / ru))  # Delta(u)>=0
            elif ru < 0:
                hi2 = min(hi2, 2 * (ev - 5 * Q(ku) ** 2 / ru))
            # else ru = 0: Delta(u) = 100ku^2 >= 0 free
            if G > 0:
                # alpha^2 > 0 needs Aw < cap: E2 < 2(cap - C), strict
                hibound = 2 * (cap - C)
                hi2 = min(hi2, math.ceil(hibound) - (1 if hibound == math.floor(hibound) else 0))
            else:
                # alpha^2 > 0 needs Aw > cap: E2 > 2(cap - C), strict
                lobound = 2 * (cap - C)
                lo2 = max(lo2, math.floor(lobound) + (1 if lobound == math.ceil(lobound) else 0))
            lo2 = math.ceil(lo2)
            hi2 = math.floor(hi2) if not isinstance(hi2, int) else hi2
            if lo2 > hi2:
                continue
            assert hi2 < 10**17 and lo2 > -10**17
            for E2 in range(int(lo2), int(hi2) + 1):
                ew = Q(E2, 2)
                eu = ev - ew
                assert Delta(rw, kw, ew) >= 0 and Delta(ru, ku, eu) >= 0
                a2 = alpha2(v, (rw, kw, ew))
                assert a2 is not None
                if a2 <= 0:
                    continue
                recs.append((a2, rw, kw, ew, ru, ku, eu))
    print("BG-compatible half-integral walls (both factors) with alpha^2>0:", len(recs))
    recs.sort(key=lambda t: t[0])
    for r in recs[:8]:
        print("  a2=%s ~ %.5f  w=(%d,%d,%s) u=(%d,%d,%s)"
              % (r[0], float(r[0]), r[1], r[2], r[3], r[4], r[5], r[6]))
    print("  ...")
    top = recs[-1]
    print("TOP wall: a2=%s ~ %.5f  w=(%d,%d,%s) u=(%d,%d,%s)"
          % (top[0], float(top[0]), top[1], top[2], top[3], top[4], top[5], top[6]))
    assert top[0] == Q(13, 10)
    # Top value 13/10 is attained at two swap-orientations of the same wall:
    # G>0 factor w = (1,0,-7) [quotient (4,-2,5)] and its swap. Accept either
    # record orientation, then fix the G>0 representative for W3 below.
    assert {Q(top[3]), Q(top[6])} == {Q(-7), Q(5)}, top
    W3W = (1, 0, Q(-7))   # G>0 destabilizing factor class of the top wall
    W3U = (4, -2, Q(5))   # complementary quotient class
    assert D_of(*W3W[:2]) == 15 and Delta(*W3W) == 140
    assert D_of(*W3U[:2]) == 40 and Delta(*W3U) == 0
    assert alpha2(v, W3W) == Q(13, 10)

    # ---- Swap-symmetry cross-check: every G<0 record mirrors a G>0 record ----
    pos = {(r[1], r[2], r[3]) for r in recs if G_of(
        next(m for m in range(1, 11) if 5 * m == D_of(r[1], r[2])), r[1]) > 0}
    for r in recs:
        a2, rw, kw, ew, ru, ku, eu = r
        m = D_of(rw, kw) // 5
        G = G_of(m, rw)
        mu = D_of(ru, ku) // 5
        Gu = G_of(mu, ru)
        assert Gu == -G, (r, m, mu)
        assert alpha2(v, (ru, ku, eu)) == a2  # F_u=-F_w, G_u=-G_w
    print("swap symmetry verified on all records.")

    # ---- Tail-completeness: rw = 5 G>0 cells and rw in {0..5} G<0 cells ----
    # rw = 5: G > 0 needs m = 11 (outside 1..10); G < 0 cells at m' = 11 - m
    # mirror G > 0 cells at rw' = 0 (swap), already enumerated. rw >= 6: both
    # G > 0 (needs m >= 11 by 5m > 11rw >= 66) and G < 0 (swap partner rw' =
    # 5 - rw <= -1, empty by Lemma 3) are impossible. Verified:
    for m in range(1, 11):
        for rw in range(6, 600):
            assert not (0 < 5 * m - 11 * rw) or True  # G>0 needs m>=11: check
            if 0 < 5 * m - 11 * rw:
                raise AssertionError(("unexpected G>0 tail", m, rw))
    print("tail: no G>0 cells with rw >= 6 (any m in 1..10); G<0 there mirror")
    print("empty rw' <= -1 G>0 cells by Lemma 3. Box rw in {0..5} COMPLETE.")

    # ---- Wall semicircle (center c, radius R) for the top pair ----
    # nu_{b,a}(E) = (A(b) - (a^2/2) H^3 r)/D(b) with A(b) = e-10kb+5rb^2,
    # D(b) = 10k-10rb. Wall: F(b) - (a^2/2)*10*(rv Dw(b)-rw Dv(b)) = 0,
    # F(b) = Av(b)Dw(b)-Aw(b)Dv(b), G(b)/5 = rv Dw(b)-rw Dv(b) (degree <= 1).
    rw, kw, ew = W3W

    def DA(b, r, k, e):
        b = Q(b)
        return Q(10 * k) - Q(10 * r) * b, Q(e) - Q(10 * k) * b + Q(5 * r) * b * b

    def wall_height_sq(b, v, w):
        # a^2 of the (v, w) wall at tilt parameter b (None unless G > 0, a^2>0).
        Dv, Av = DA(b, *v)
        Dw, Aw = DA(b, *w)
        G = 5 * (Q(v[0]) * Dw - Q(w[0]) * Dv)
        F = Av * Dw - Aw * Dv
        if G <= 0:
            return None
        a2 = F / G
        return a2 if a2 > 0 else None

    assert wall_height_sq(BETA, v, W3W) == Q(13, 10)
    # semicircle endpoints: F(b) = -100b^2 - 330b - 140 (verified expansion:
    # Av(b) = -2+20b+25b^2, Dw(b) = -10b, Aw(b) = 5b^2-7, Dv(b) = -20-50b).
    disc = Q(330) ** 2 - 4 * 100 * 140
    assert disc == 52900 == 230**2
    b1, b2 = (Q(-330) - 230) / 200, (Q(-330) + 230) / 200
    assert (b1, b2) == (Q(-14, 5), Q(-1, 2))
    c = (b1 + b2) / 2
    assert c == Q(-33, 20)
    R2 = wall_height_sq(c, v, (rw, kw, ew))
    assert R2 == Q(529, 400)
    print("W3 semicircle: endpoints b1=%s b2=%s center c=%s R^2=%s R=23/20"
          % (b1, b2, c, R2))
    print("apex alpha = 23/20 = 1.15; section alpha^2 at beta=-3/2: %s" % top[0])

    print("CERTIFICATE_OK")


if __name__ == "__main__":
    main()
