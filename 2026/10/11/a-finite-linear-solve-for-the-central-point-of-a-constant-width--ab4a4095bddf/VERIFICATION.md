---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For nondegenerate paired-direction centrally symmetric U, determinant denominators [U_i,U_{i+1}] and [V_i,V_{i+1}] are nonzero by source duality. A double U-polygon has the closed half-edge coordinate E_U defined by two independent planar linear closure equations; dim(E_U)=n-2, including E_U={0} at n=2. Applying both source half-sum involute formulas gives a linear translation-equivariant F_U and an explicit unique decomposition F_U(R_Ux)=1 B_Ux+R_U(A_Ux). For any real x in E_U (not only source P), choose q>max_i |x_i|; P_i=R_Ux_i+qU_i and P_{i+n}=R_Ux_i-qU_i has successive positive edge coefficients q±x_i, is convex and of constant U-width, and has central equidistant R_Ux. Craizer–Martini Theorem 5.1 then implies F_U^k(R_Ux) converges to a point, so A_U^k x→0 for all x; finite dimension yields spectral radius(A_U)<1 and (I-A_U) invertible. Summing the exact affine recurrence with translation B_U gives O(P)=M_1+B_U(I-A_U)^(-1)r, with first-vertex anchoring and index relabel F_U(X)_{i+1}=Z_i crucial. Independent rational tests reconstructed nontrivial E_U for n=3,4,5, computed A_U,B_U, exact center invariance under one double involute, positive-width embedding, and converging numerical iterates. These finite tests are independent checks, not the all-polygon proof.

## originality

PASS

Best-of-knowledge original relative to the inspected mathematical statements. Craizer and Martini, arXiv:1406.3205, Theorem 5.1, prove convergence of double involutes and explicitly ask immediately thereafter for a direct method to obtain their central point. Their local involute identities are used as premises, but no translation-aware finite resolvent is given there. Craizer–Teixeira–Balestro, arXiv:1702.00522, make the double-evolute map linear on curvature-radius coordinates determining polygons only up to translation; this quotient does not determine the absolute center. The Arnold–Fuchs–Izmestiev–Tabachnikov–Tsukerman theory, arXiv:1510.07742, uses different perpendicular/angular-bisector evolutes and pseudo-Steiner points. Independent published-finding search retrieved the finding itself, not another record covering the center extraction. Generic (I-A)^(-1) algebra is classical; the specific geometric realization of all shape vectors and construction of B_U for this involute is the mathematical claim.

## value

PASS

The central point is a canonical exact geometric invariant of arbitrary convex polygons under the published Minkowski involute construction. Its direct determination is a concrete question immediately after the source convergence theorem. The proof replaces an infinite iterative limiting process by finitely many explicit determinant/half-sum operations and one (n-2)-dimensional solve, recovering the absolute translation omitted by radius-only operators. This is a structurally motivated, all-input method for the specific open central-point problem. The matrix-resolvent algebra by itself is routine; its mathematical value here is the geometric realization/contraction argument and the computable translation cocycle, not a claim to an independent general fixed-point theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
