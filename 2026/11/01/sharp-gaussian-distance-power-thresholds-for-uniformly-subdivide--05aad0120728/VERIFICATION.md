---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed Schoenberg equivalence (all t>0, not one fixed t), basepoint Gram from direct tree distances 1,2,3,4 and arm S_m action. The 2m×2m Gram is m−1 copies Q_p=D_p−O_p and one P_m,p=D_p+(m−1)O_p. For 1<p<2, D_p is positive definite and −O_p is positive definite by the explicit fractional-power integral Gram for functions 1−e^(−t),1−e^(−2t); hence Q_p≻0. The P block is [[A_m,B_m],[B_m,2^p A_m]] with determinant (2^(p/2)A_m−B_m)F_m. On [1,s_m] derivative inequalities make F_m strictly decreasing from positive to negative, so exactly one p_m; P PSD rank1 there, indefinite between p_m and s_m, then A_m≤0 rules out all p≥s_m. Negative-type fractional-power monotonicity gives every smaller p, including discrete p=0. Endpoint only one zero Gram eigenvalue so affine embedding dimension 2m−1, full 2m below. Increasing m subtracts a strictly positive 2×2 −O_p matrix and makes old null vector negative, giving p_{m+1}<p_m. Taylor at p=1 yields displayed c and O(m^-2). m=2 is a 5-point path with p=2 endpoint dim1. Independently reconstructed graph-distance Gram and computed smallest/next eigenvalue for m=3,4,8 at analytic roots: null within numerical precision, next >0.22.

## originality

PASS

Doust–Weston exact one-level star exponent is for m leaves at one edge, while this two-edge subdivision adds m intermediate vertices and three/four additional pair-distance regimes. Their negative-type gap bounds do not evaluate the subdivided star sharp root. Li–Weston supplies the general strictness theorem and Sánchez a general finite-metric determinant method with evaluated bicliques; neither gives this family equation, rank direction, strict arm-count law, or asymptotic. Resultary R4/R5 returned tree curvature/persistence and unrelated Gaussian metrics rather than a matching p-negative-type classification. Best-of-knowledge original, with possible older tree special cases risk.

## value

PASS

Uniform subdivision is a canonical operation on star trees, making the exact generalized-roundness/negative-type change from a known star exponent a natural structural question. The sharp all-Gaussian-scales threshold, unique rank-drop/equality vector, strict monotonicity in branch count, and nontrivial 1+c/m asymptotic add mutually reinforcing exact geometry. These are not automatically implied by tree 1-negative-type or a finite numerical census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
