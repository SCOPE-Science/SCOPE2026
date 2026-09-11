# Falsification of the stated unstable Moore-space Toda bracket on M^12

## Context
Recognized 2-primary unstable sphere/Moore program (Serre, Toda, Mahowald, Isaksen–Wang–Xu) where only narrow stems are known. The admitted target asked to decide the unstable Toda bracket T = <i_12, 2_12, eta_12 o sigma_13> on the mod-2 Moore space M^12 by Ext-plus-Moss: exhibit its Moss-converging detection class or the crossing differential / juggling obstruction.

## Definitions
- M^12 = S^12 ∪_2 e^13; i_12: S^12 → M^12 bottom-cell inclusion; 2_12: S^12 → S^12 degree-2.
- alpha = eta_12 o sigma_13: S^20 → S^13 → S^12 (|eta|=1, |sigma|=7, so |alpha|=8).
- Target conjunction: (G) T = <i_12,2_12,alpha> ⊂ pi_20(M^12); (F) T detected in Adams filtration s=4 by mu = <e_12,h0,h1h3>; with strict definedness / indeterminacy Z/2 / Moss convergence package.

## Result
The literal (pi_20, s=4) conjunction is FALSE, with two independent grading obstructions:
- (G) is impossible: <f,g,h> for W→X→Y→Z lies in [Sigma W, Z] (Toda 1963 Def. 1.1; Moss 1970 §1). Here W=S^20, Z=M^12, so <i_12,2_12,alpha> ⊂ [S^21, M^12] = pi_21(M^12), never pi_20. Off by one suspension. Stable check: 0+0+8+1=9 rel. bottom cell = absolute pi_21.
- (F) is impossible: for a_j in Ext^{s_j,t_j}, <a1,a2,a3> lies in Ext^{sum s −1, sum t} (May; Moss; cobar d preserves t). With e_12 in Ext^{0,12}, h0 in (1,1), h1h3 in (2,10): s = 0+1+2−1 = 2 ≠ 4, t = 12+1+10 = 23, stem 21 ≠ 20. Hence mu, if defined, lives in Ext^{2,23} = (stem 21, s=2).
- Either row alone falsifies the conjunction. Forced repaired address by the same data: (stem 21, s=2).

Null-composites for the corrected bracket's definedness: i_12 o 2_12 ≃ 0 by the cofiber S^12 → S^12 → M^12; 2_12 o alpha ≃ 0 in the Freudenthal stable range (12 > 8+1, pi_13(S^12) = Z/2 so 2·eta = 0).

## Proof / evidence
Theorem-level grading arguments plus replayable Ext-input corroboration:
- e_12 ∈ Ext_A^{0,12}(H^*(M^12),F2) (Hom_A sends x_12↦1, x_13↦0, compatible with Sq^1 x_12 = x_13).
- h0=[xi1], h1=[xi1^2], h3=[xi1^8] primitive cocycles; h1h3=[xi1^2|xi1^8] cocycle (d2=0) and E2-nonzero (full d1-image linear algebra in degree 10 shows non-membership).
- h0h1=0 via explicit d([xi1^3]+[xi2])=[xi1|xi1^2] with d[xi1^3]=[xi1^2|xi1]+[xi1|xi1^2], d[xi2]=[xi1^2|xi1]; hence h0·(h1h3)=0.
- e·h0=0 by Moore-module LES of 0→Σ^13→H→Σ^12→0: connecting δ(id) is the nontrivial Sq^1 extension class, hence an isomorphism F2→F2, so p^*=0.
- All cobar identities replay: `python3 output/artifacts/verify_target_grading.py` → VERIFY_OK (21 checks, stdlib only). Machine part corroborates Ext inputs; grading contradictions are proof-level.

## Limitations
Falsifies only the literal (pi_20, s=4) conjunction with named data. Does NOT decide the corrected bracket in pi_21 / Massey in (21,2): definedness details beyond degree, indeterminacy group, crossing differentials, Moss convergence/divergence, and juggling constraint p_*T are left open. No fallback work performed. Machine check covers only bidegrees used.

## Reproducibility
- `python3 output/artifacts/verify_target_grading.py` (stdlib only) → VERIFY_OK, 21 checks.
- By-hand steps: Toda degree (Toda Def. 1.1), Massey degree (May/Moss), LES e·h0=0, Freudenthal range.

## References
- H. Toda, Composition Methods in Homotopy Groups of Spheres (1963), Def. 1.1.
- R. M. F. Moss, Secondary compositions and the Adams spectral sequence (1970), §1 / Thm. 1.2.
- J. F. Adams, On the structure and applications of the Steenrod algebra; May, Matric Massey products; Isaksen–Wang–Xu stable stems (Ext charts); Freudenthal suspension theorem.
