"""Triple-coincidence + census cross-consistency audit (exact arithmetic).

 (1) Triple coincidence at j=8 for gap g=1/4, K=1:
     Route A (stable-range MVN forcing): J(1/4)=8  [verify_uniform_washout]
     Route B (Chern-shadow worst over general pairs): maxwash=8  [general_pair]
     Route C (later-birth worst over all feasible (K,i)): 8  [later_birth]
     Recomputed here independently from closed forms; assert all equal 8.
 (2) Cross-consistency: Sec-16 trivial-target census (K=1: 64 designs) vs
     Sec-21 general-pair census restricted to mb=0 (trivial target).
     General mb=0 slice: pairs (ma,0) with S=ma>c=8 and feasible ra, i.e.
     exists ra with max(ma, 0-8)<=ra<=cap-8=23. Count them independently and
     assert the slice count equals ... (computed, then compared to 64 modulo
     the ta-degree of freedom: Sec-16 counts (m,t) with t free; Sec-21 counts
     (ma,mb) with ta existentially quantified. So slice count <= 64, and
     every slice member extends to >=1 Sec-16 design. Verify both directions
     of this refinement relation exactly.)
 (3) Sanity: total general K=1 pairs 327 >= trivial 64 (refinement adds
     Bott-carrying targets). K=2: 225 vs 55; K=3: 53 vs 3 (recomputed).

Prints VERIFY_OK. Stdlib only.
"""
from fractions import Fraction

def stage(j):
    N = 2 * (4 ** (j - 1))
    t = 3 ** j - 1
    D = 2 * t
    return N, t, D

def main():
    print("(1) triple coincidence at j=8:")
    # Route A: least j>=3 with (1/4)*N >= (D+1)/2
    JA = next(j for j in range(3, 50)
              if Fraction(1, 4) * stage(j)[0] >= Fraction(stage(j)[2] + 1, 2))
    # Route B: worst wash over S<=26, c=8: max over S in 9..26 of wash(S,8)
    def wash(S, c, i=3):
        j = i
        while not (S * 3 ** (j - i) < c * 4 ** (j - i)):
            j += 1
        return j
    WB = max(wash(S, 8) for S in range(9, 27))
    # Route C: worst over feasible (K=1, birth i<=7) with S=t_i, c=N_i/4
    WC = max(wash(stage(i)[1], stage(i)[0] // 4, i)
             for i in range(3, 10) if stage(i)[0] // 4 < stage(i)[1])
    print(f"  Route A (stable-range J): {JA}")
    print(f"  Route B (general-pair worst wash): {WB}")
    print(f"  Route C (later-birth worst wash): {WC}")
    assert JA == 8 and WB == 8 and WC == 8
    print("  triple coincidence at j=8 OK")

    print("(2) census refinement (K=1, c=8, cap=31):")
    c, cap = 8, 31
    # Sec-16 set: (m,t): m<=26, m+t+8<=31, m>t+8
    sec16 = {(m, t) for m in range(27) for t in range(32)
             if m + t + 8 <= 31 and m > t + 8}
    print(f"  Sec-16 designs: {len(sec16)}")
    assert len(sec16) == 64
    # Sec-21 mb=0 slice: ma with S=ma>8 and exists ra in [max(ma,-8), 23]
    slice21 = {ma for ma in range(27) if ma > 8 and max(ma, -8) <= 23}
    print(f"  Sec-21 mb=0 slice mas: {sorted(slice21)} (count {len(slice21)})")
    # refinement: projection (m,t)->m maps sec16 onto slice21
    proj = {m for (m, t) in sec16}
    assert proj == slice21, (proj, slice21)
    # every slice member has >=1 extension; count extensions per ma
    for ma in slice21:
        exts = [t for (m, t) in sec16 if m == ma]
        assert len(exts) >= 1
    print("  projection of Sec-16 onto ma == Sec-21 mb=0 slice. Refinement OK.")
    # general adds genuine new pairs (mb>0): count them
    gen_new = 0
    for ma in range(27):
        for mb in range(27 - ma):
            S = ma + mb
            if S > c and max(ma, mb - c) <= cap - c and mb > 0:
                gen_new += 1
    print(f"  general pairs with mb>0: {gen_new} (must be >0)")
    assert gen_new > 0
    assert len(sec16) + gen_new + len(slice21) == 64 + gen_new + len(slice21)
    # total general K=1 = 327 recomputed
    tot = sum(1 for ma in range(27) for mb in range(27 - ma)
              if ma + mb > c and max(ma, mb - c) <= cap - c)
    assert tot == 327, tot
    assert tot == len(slice21) + gen_new
    print(f"  total general K=1 = {tot} = slice({len(slice21)}) + new({gen_new}). OK")

    print("(3) K=2,3 totals recomputed:")
    for K, exp in [(2, 225), (3, 53)]:
        cK, capK = 8 * K, K * 32 - 1
        totK = sum(1 for ma in range(27) for mb in range(27 - ma)
                   if ma + mb > cK and max(ma, mb - cK) <= capK - cK)
        print(f"  K={K}: total={totK} (expect {exp})")
        assert totK == exp, (K, totK)
    # trivial censuses recomputed
    for K, exp in [(1, 64), (2, 55), (3, 3)]:
        cK, capK = 8 * K, K * 32 - 1
        triv = {(m, t) for m in range(27) for t in range(capK + 1)
                if m + t + cK <= capK and m > t + cK}
        assert len(triv) == exp, (K, len(triv))
    print("  trivial (64,55,3) and general (327,225,53) counts confirmed. OK")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
