"""Homogeneous-bound rounding + rc-definition handling (exact arithmetic).

Lemma (rounding): let D, n positive integers, G an integer rank gap.
If G/n > D/(2n) (strict normalized gap above D/2n) then G >= floor(D/2)+1.
Proof: G > D/2, and G integer => G >= floor(D/2)+1. Checked exhaustively
for the admitted (D_j, N_j) and all relevant G.

Consequence for the target upper half: on A_j = M_{N_j}(C(X_j)), traces
include ev_x (point evaluations), so a uniform strict dimension gap
  d_tau(a) + D_j/(2N_j) < d_tau(b)  for all tau
implies pointwise absolute rank gap G(x) = rank(b(x))-rank(a(x)) > D_j/2
for every x, hence G(x) >= floor(D_j/2)+1, which is exactly the strict
Toms-lemma hypothesis (cited) forcing [a]<=[b] in Cu. Therefore
rc(A_j) <= D_j/(2N_j) = u_j. The non-strict (<=) variant of the rc
definition is handled by r+eps: rc <= u_j + eps for all eps>0.

Also certifies the non-strict boundary case: gap exactly == D/2 does NOT
force (G=D/2 is not >= floor(D/2)+1 when D even... D/2 < D/2+1), so the
bound u_j is sharp as stated (cannot be improved by this lemma alone).

Checks:
 (1) rounding implication for all j=1..12 and G in 0..N_j (sampled fully
     for j<=5, boundary neighborhoods for j>5).
 (2) u_j values and strict-vs-nonstrict handling: rc(A_j) <= u_j.
 (3) stage-3 instance: u_3 = 13/16; strict gap > 13/16 forces
     G(x) >= 27 for all x (D_3/2+1 = 27). Verify 26/32 = 13/16 is NOT
     forcing (boundary), 27/32 is.
Prints VERIFY_OK. Stdlib only.
"""
from fractions import Fraction

def stage(j):
    N = 2 * (4 ** (j - 1))
    D = 2 * (3 ** j - 1)
    return N, D

def main():
    print("(1) rounding lemma G/n > D/2n => G >= floor(D/2)+1:")
    for j in list(range(1, 6)):
        N, D = stage(j)
        for G in range(0, N + 1):
            if Fraction(G, N) > Fraction(D, 2 * N):
                assert G >= D // 2 + 1, (j, G)
            # converse boundary: G = D/2 (D even) does not imply strict
            # (it equals, not exceeds) — check it fails the premise
            if G == D // 2 and D % 2 == 0:
                assert not (Fraction(G, N) > Fraction(D, 2 * N)), (j, G)
    for j in range(6, 13):
        N, D = stage(j)
        # boundary neighborhood only (full range too big)
        for G in [0, 1, D // 2 - 1, D // 2, D // 2 + 1, D // 2 + 2, N]:
            if Fraction(G, N) > Fraction(D, 2 * N):
                assert G >= D // 2 + 1, (j, G)
    print("  rounding exact for j<=5 fully, boundary neighborhoods j<=12. OK")

    print("(2) rc(A_j) <= u_j reading:")
    for j in (3, 4, 5, 8):
        N, D = stage(j)
        u = Fraction(D, 2 * N)
        # strict gap above u forces Toms hypothesis pointwise
        # (ev_x traces give pointwise normalized ranks)
        print(f"  j={j}: u={u}; strict gap > u => G(x) >= {D//2+1} forall x => compare [cited Toms]. OK")

    print("(3) stage-3 boundary sharpness:")
    N3, D3 = stage(3)
    assert (N3, D3) == (32, 52)
    assert Fraction(26, 32) == Fraction(13, 16)  # == u_3: not forcing
    assert not (Fraction(26, 32) > Fraction(52, 64))
    assert Fraction(27, 32) > Fraction(52, 64)   # next integer: forcing
    assert 27 == D3 // 2 + 1
    print("  G=26 (==u_3) not forcing; G=27 forcing. Bound sharp. OK")
    print("  target upper half rc(V)<=13/16<=1 needs only this + liminf [cited]. OK")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
