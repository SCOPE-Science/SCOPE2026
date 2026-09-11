# Real Abramovich–Bertram transfer at the fixed class (2,2): holds for all-real points, fails by defect −2 with a conjugate pair

## Context

The Hirzebruch surfaces F0 = P1 × P1 and F2 are deformation equivalent. The landmark complex Abramovich–Bertram (AB) relation (Abramovich–Bertram genus 0, Vakil all genera, Cooper Fock-space form §6.3) relates their genus-zero Severi degrees. At the canonical test parameter a=2, b=0 it reads N_F0(2C+2F) = N_F2(2C) + binom(2,1)·N_F2(2C−E), i.e. 12 = 10 + 2·1.

Whether this deformation invariance persists over the reals with Welschinger signs is a recognized benchmark for the real enumerative program: success would transfer F0 technology to F2, while sharp divergence would map the limits of real deformation invariance. The complex formula, its higher-genus extension, refined Block–Göttsche conjectures/relations, and del Pezzo real surgeries motivate but do not settle the signed fixed-class comparison, because specialization from complex or refined counts to Welschinger signs at fixed r requires sign analysis, and because F2 is non-del Pezzo (it carries a (−2)-curve), placing it outside del Pezzo-restricted real surgery theorems.

## Definitions

F0 bidegree (2,2) is class 2E+2F on Σ0 with polygon (d^t,d^b,l,r) = (2,2,(0,0),(0,0)). F2 main class is 2E+4F = 2C with C = E+2F on Σ2, polygon (0,4,(0,0),(2,2)). F2 correction class is E+4F = 2C−E on Σ2, polygon (2,4,(0),(2)). All three impose s = 7 point conditions, so dimensions match under the standard deformation identification.

Floor diagrams follow Brugallé–Mikhalkin arXiv:0812.3354 §3. A genus-0 diagram D of polygon Δ has complex multiplicity μ^C(D) = ∏ w(e)^2 over bounded edges. For a marking m and r conjugate point pairs, the r-real multiplicity μ^R_r(D,m) is Definition 3.8: r-pairs occupy positions {s−2k+1, s−2k+2}; Im(m,r) are pairs whose marks are non-adjacent; involution ρ swaps those pairs; r-reality means (D,m) ∼ (D,m∘ρ) via a diagram automorphism; even-weight bounded edges must meet m(Im); sign (−1)^{o_r} with o_r half the odd-divergence vertices in m(Im); weight product over bounded edges past position s−2r. Theorems 3.6/3.9: N(Δ,0) = Σ μ^C and W(Δ,r) = Σ μ^R_r over Aut-quotiented markings (markings counted up to diagram automorphism, Def. 3.4). The real structure is tautological; r = 0,…,3.

## Result

At the fixed genus-zero class pair F0 bidegree (2,2) / F2 main class 2E+4F with correction class E+4F and documented AB binomial coefficient 2, the Welschinger-signed floor-diagram counts are:

W_F0(r) = (8,6,4,2), W_F2(r) = (6,6,4,2), W_corr(r) = (1,1,1,1) for r = 0..3.

With RHS(r) = W_F2(r) + 2·W_corr(r) = (8,8,6,4), the defect D(r) = W_F0(r) − RHS(r) = (0,−2,−2,−2).

Hence the real AB relation HOLDS for all-real point conditions (r=0: 8 = 6 + 2×1) and DIVERGES by explicit nonzero defect −2 for every r ≥ 1, i.e. as soon as one conjugate point pair is present.

Per-diagram rows (Aut, marks, μ^C each, complex, W(r=0..3)): F0-A (w1) 2, 4, 1, 4, (4,4,4,2); F0-B (w1) 2, 4, 1, 4, (4,2,0,0); F0-C (w2) 4, 1, 4, 4, (0,0,0,0); F2-D (w1) 6, 6, 1, 6, (6,6,4,2); F2-E (w2) 24, 1, 4, 4, (0,0,0,0); F2-corr 48, 1, 1, 1, (1,1,1,1).

## Proof / evidence

Shape completeness is proved by divergence equations. Height is 2 for F0(2,2) and F2-main, so exactly 2 floors. For F0 with bounded-edge weight w, lower/upper stub counts bA,tA,bB,tB satisfy bA+bB=2, tA+tB=2, div A = bA−tA−w = 0, div B = w+bB−tB = 0: w=1 gives (1,0),(1,2) [type A] or (2,1),(0,1) [type B]; w=2 gives (2,0),(0,2) [type C]; w≥3 impossible. For F2-main: bA+bB=4, tA=tB=0, div A = bA−w = 2, div B = w+bB = 2: w=1 gives (3,1) [type D]; w=2 gives (4,0) [type E]. F2-correction is height 1, single floor with 4 bottoms and 2 tops, div +2. Complete: 3+2+1 shapes.

Implementation: every diagram is an explicit object (vertices with θ, edges with kind/weight/incidence); automorphisms by brute force; markings are linear extensions of the floor poset taken up to Aut; r-real multiplicity follows Def. 3.8 literally. Script `enumerate.py` writes `ledger.json`; `verify.py` re-runs the whole census live and asserts every number (VERIFY_OK, 18/18 checks, independently replayed in audit).

Calibration: complex F0(2,1)=1, F0(1,2)=1, Δ2-conics=1, F0(2,2)=4+4+4=12, F2-main=6+4=10, F2-corr=1 (the AB triple). Real gold standard: the full plane-cubic Δ3 table W=8−2r reproduced exactly with per-shape rows chain(2,1,0)=[5,5,5,3,1], w2-chain 0, fork=[3,1,−1,−1,−1] (totals [8,6,4,2,0]), validating adjacency, r-reality, even-edge killing, and signs including negative fork contributions.

Killing mechanism: the w=2 diagrams (F0-C, F2-E) contribute 4+4=8 complex curves but are killed (multiplicity 0) at every real r by the even-edge rule, while w=1 diagrams lose markings at different rates (F0-B drops 4→2→0; F2-D stays 6→6→4). Full per-marking audit trail with positions 1..7 is logged in the draft.

## Limitations

One fixed class pair (canonical a=2,b=0 AB case); genus 0; tautological real structure; floor-diagram (tropical) Welschinger counts via the Brugallé–Mikhalkin correspondence, which is used, not re-proved. No claim about other classes, higher genus, or non-tropical real structures. The uniform −2 defect for all r≥1 is a computed fact at this class, not a general theorem.

## Reproducibility

Run `python3 verify.py` in the artifact directory (requires `enumerate.py` alongside). It recomputes all diagrams, markings, Aut orders, complex totals, Δ3 calibration, target rows, and defect live and prints VERIFY_OK. Ledger values: F0-A n_reps 4 aut 2; F0-B 4/2; F0-C 1/4; F2-D 6/6; F2-E 1/24; F2-corr 1/48.

## References

[BM] E. Brugallé, G. Mikhalkin, Floor decompositions of tropical curves: the planar case, arXiv:0812.3354 (Thms 3.6/3.9, Defs 3.4/3.5/3.8, Table 1). [AB] A. Abramovich, A. Bertram, The formula 12=10+2×1 and generalizations. [Vak] R. Vakil, extension to all genera. [Coop] Y. Cooper, Fock-space approach to Severi degrees of Hirzebruch surfaces, arXiv:1709.01159 §6.3. [BG] L. Block, L. Göttsche, Fock spaces and refined Severi degrees, arXiv:1409.4868 Ex. 2.6(2). [Bous] P. Bousseau, Refined floor diagrams from higher genera and lambda classes, arXiv:1904.10311. [BW] E. Brugallé, K. Wickelgren, A quadratic Abramovich-Bertram formula, arXiv:2506.17854. [IKS] I. Itenberg, V. Kharlamov, E. Shustin, Welschinger invariants of real del Pezzo surfaces of degree ≥ 2, arXiv:1312.2921.
