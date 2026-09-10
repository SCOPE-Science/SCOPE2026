# Certified equinumeration of left Gog and GOGAm trapezoids at (n,k) = (6,3)

## Context

The Gog–Magog (alternating-sign-matrix vs totally-symmetric-self-complementary-plane-partition) bijection is an open problem since Mills–Robbins–Rumsey (1986). Biane–Cheballah (arXiv:1401.6516) introduced left Gog and GOGAm trapezoids and conjectured (Conj. 7.2) that they are equinumerous for all shapes, proving explicit bijections only for trapezoids with one or two diagonals. The three-diagonal family is the first open cell. Fischer (arXiv:1804.07054) derived constant-term formulas for Gog trapezoids and Lindström–Gessel–Viennot (LGV) determinants for Magog trapezoids as tools toward the conjectures, not equinumeration proofs.

## Definitions

- A Gog triangle of order n is a Gelfand–Tsetlin triangle with strictly increasing rows and bottom row 1,…,n (Biane–Cheballah Def. 3.1). Gog triangles of order n are in bijection with n×n alternating sign matrices; there are ASM(n) of them (1, 2, 7, 42, 429, 7436 for n = 1…6).
- A Magog triangle of order n is a Gelfand–Tsetlin triangle with diagonal caps X[j][j] ≤ j (Def. 4.1). Magog triangles encode TSSCPPs.
- A GOGAm triangle is a Gelfand–Tsetlin triangle whose image under the Schützenberger involution S (Berenstein–Kirillov operators, Sec. 2.3) is a Magog triangle; equivalently it satisfies inequality system (5.1).
- A left (n,k) Gog (resp. GOGAm) trapezoid is the array formed by the k leftmost NW–SE diagonals (entries with column index j ≤ k) of a Gog (resp. GOGAm) triangle of order n (Defs. 3.3, 5.3). G(6,3) and M(6,3) denote these sets at n = 6, k = 3.

## Result

For left Gog trapezoids G(6,3) and left GOGAm trapezoids M(6,3) of order n = 6 with exactly 3 diagonals:

|G(6,3)| = |M(6,3)| = N* = 4862,

certified by independent replayable brute-force generators on both sides plus an exactly agreeing LGV determinant evaluation. The general all-n three-diagonal claim is NOT claimed.

## Proof / evidence

Leg 1 (Gog side): `gen_gog(6)` backtracks all Gog triangles with bottom row fixed 1..6, strict rows, and GT interlacing X[i+1][j] ≤ X[i][j] ≤ X[i+1][j+1]. It yields 7436 triangles (= ASM(6)); every object passes the `is_gog` validator. Projection onto the 3 leftmost diagonals gives 4862 distinct trapezoids.

Leg 2 (GOGAm side): `gen_magog(6)` backtracks all Magog triangles (weak rows, diagonal caps), yielding 7436 (= ASM(6)); every object passes `is_magog`. The Schützenberger involution S (BK s_k operators) is verified involutive on the n = 4 Gog and Magog sets; all 7436 S-images of Magog(6) satisfy GOGAm inequality (5.1) via `is_gogam`. Projection onto 3 leftmost diagonals gives 4862 distinct trapezoids.

Corroborating census (independently replayed): left-projection counts agree on both sides at n = 4 (k = 1,2,3: 14/35/42), n = 5 (42/219/387), n = 6 (132/1594/4862).

Leg 3 (LGV determinant): Fischer Sec-4 LGV determinant for (m,n,k)-Magog trapezoids at P = Q = 1, summed over the 56 weakly increasing bottom rows, gives exactly 4862 at (0,6,3). The implementation is validated against brute-force right-trapezoid counts at (0,3,2) = 7, (0,4,2) = 35, (0,4,3) = 42, (0,5,2) = 219, (0,5,3) = 387; brute-force right-Gog(6,3) = 4862 independently.

The equality is therefore established by exhaustive enumeration (legs 1–2 alone suffice); the LGV value is a numerically agreeing third leg. The integer 4862 numerically equals Catalan C9; no combinatorial identification is claimed.

## Limitations

- The equality is computational (exhaustion over 7436 + 7436 triangles), not a bijective or analytic proof; the all-n three-diagonal conjecture stays open.
- GOGAm membership is certified via inequality (5.1), i.e. the paper's own S-image criterion.
- A supporting n = 7 census (76505 = 76505) mentioned in the draft is not part of this headline and was not independently replayed here.

## Reproducibility

Stdlib-only Python. From `output/`: `python3 artifacts/verify.py` replays generator validation vs ASM numbers, S involution + (5.1), left censuses, Sec-9.2 (n,2) certification, constant-term spot checks, LGV totals including (0,6,3), and recorded obstruction probes. Verification-critical files are copied to `output/artifacts/` (gen.py, gogam.py, lgv_cert.py, lgv2.py, verify.py). Audit independently reran all three headline legs and obtained 4862 = 4862 = 4862.

## References

- P. Biane, H. Cheballah, Inversions and the Gog-Magog problem, arXiv:1401.6516.
- I. Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids, arXiv:1804.07054.
- J. Bettinelli, A simple explicit bijection between (n,2) Gog and Magog trapezoids, arXiv:1512.03305.
- I. Fischer, M. Konvalinka, A bijective proof of the ASM theorem, Part II: ASM enumeration and ASM-DPP relation, arXiv:1912.01354.
