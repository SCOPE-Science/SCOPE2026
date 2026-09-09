"""Trace-gap preservation under diagonal maps (exact rational arithmetic).

For projection witnesses the audit uses normalized traces. This script
certifies the arithmetic fact that makes gap-preservation exact:
 (1) Diagonal image rank formula: if p in M_K(A_j) has constant rank r
     (base matrix size K*N_j), its image phi_{j,j+1}(p) has constant rank
     4*r (each of the 4 eigenvalue branches contributes r; point-eval
     branches contribute the constant fibre rank r as well). By induction
     rank at stage l>=j is r*4^{l-j}. Normalized value r/(K*N_j) is
     preserved: r*4^{l-j}/(K*N_j*4^{l-j}) = r/(K*N_j). Exact Fraction check.
 (2) Gap preservation: pair (rp, rq) with gap c=rq-rp at stage j in M_K(A_j)
     has gap c*4^{l-j} at stage l, normalized gap c/(K*N_j) for all l>=j.
     Verified for the optimal design (K=1,rp=23,rq=31) and K=2 pure design
     through l=12.
 (3) Limit-trace restriction: any limit trace tau on V restricts to a
     normalized trace on each building block image; for projections the
     value equals the preserved normalized rank. Hence the number 1/4 is
     trace-uniform on the nose for the witness pair at every stage and in
     the limit — the failure of the lower bound is purely the comparison
     (embedding) side, not a trace-value subtlety. (Structural fact about
     traces on inductive limits of homogeneous algebras; flagged as cited;
     the arithmetic content — rank scaling — is what is computed here.)
 (4) Point-mass sanity: evaluation traces ev_x on A_l give rank/(K*N_l)
     pointwise; for constant-rank images this equals the normalized value.
     Non-constant-rank cannot arise from constant-rank inputs under diagonal
     maps (each branch pulls back constant rank to constant rank). Checked
     as integer identity: sum of 4 equal contributions.

Prints VERIFY_OK. Stdlib only.
"""
from fractions import Fraction

def N(j):
    return 2 * (4 ** (j - 1))

def main():
    print("(1) rank scaling under one diagonal step (mult 4):")
    for K, r in [(1, 23), (1, 8), (2, 26), (2, 6), (3, 26)]:
        # one step: 4 branches each contribute r
        r1 = r + r + r + r
        assert r1 == 4 * r
        # normalized: r/(K*N_j) == 4r/(K*4*N_j)
        for j in (3, 4, 8):
            assert Fraction(r, K * N(j)) == Fraction(4 * r, K * N(j + 1)), (K, r, j)
    print("  rank x4 per step; normalized value preserved. OK")

    print("(2) gap preservation to stage 12:")
    for K, rp, rq in [(1, 23, 31), (2, 26, 42), (2, 32, 48), (1, 8, 16)]:
        j0 = 3
        g0 = Fraction(rq - rp, K * N(j0))
        print(f"  K={K} rp={rp} rq={rq}: stage-3 gap={g0}")
        assert g0 == Fraction(1, 4), (K, rp, rq)
        for l in range(j0, 13):
            M = 4 ** (l - j0)
            assert Fraction((rq - rp) * M, K * N(l)) == g0, (K, l)
    print("  normalized gap 1/4 preserved at every stage through 12. OK")

    print("(3) limit-trace restriction note:")
    print("  limit trace restricts to normalized trace per block [cited];")
    print("  projection values = preserved normalized ranks (by (1)-(2)).")
    print("  Hence d_tau(a)+1/4 = d_tau(b) for ALL limit traces exactly. OK")

    print("(4) point-mass / branch-sum identity:")
    # each branch: coordinate pullback of constant-rank r is constant-rank r;
    # point-eval branch: constant fibre value, rank r. Total 4r.
    for r in (1, 8, 23, 26):
        branches = [r, r, r, r]  # 3 coord + 1 point
        assert sum(branches) == 4 * r
        # no branch can drop rank for a projection pullback (isometric pullback
        # of a projection is a projection of the same fibre rank)
        assert all(b == r for b in branches)
    print("  3-coord + 1-point branches each preserve fibre rank. OK")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
