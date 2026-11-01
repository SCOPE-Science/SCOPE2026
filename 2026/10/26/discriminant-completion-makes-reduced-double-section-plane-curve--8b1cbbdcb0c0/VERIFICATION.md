---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Rebuilt exact homogeneous degrees of A=F_x, H=L_z F_y−L_y F_z, T=2(F_xz F_y−F_xy F_z), N=3d−2, and both displayed annihilating Jacobian syzygies. Direct polynomial differentiation gives D=A²−4LF and D_z F_y−D_y F_z=AT−4FH. The Euler-plus-syzygy determinant equals −N²(2d−2)FD, a nonzero scalar multiple of the reduced defining equation. Saito determinant criterion therefore proves freeness in all degrees, with syzygy degrees d and 2d−3, not only finite d. Checked independent symbolic exact identities for d=3,4,5. For a smooth cubic p on it, the degree-two projection C→P¹ has precisely four distinct branch directions by characteristic-zero Riemann–Hurwitz (total simple ramification four); discriminant is squarefree and cubic cannot divide binary D.

## originality

PASS

A prior full-text free-curve construction considers special tangent arrangements and a point outside the original curve, with additional hypotheses. This theorem instead handles the full discriminant divisor of the residual quadratic through any high-multiplicity center and supplies a universal all-d explicit determinant; its on-cubic center corollary is not a corollary of the outside-center theorem. Other general eigenscheme or pencil freeness results warrant caution.

## value

PASS

The branch discriminant is the canonical collection of special directions for a double residual intersection from a high-multiplicity center. Adding those lines makes every reduced such curve free with explicit basis and exponents, uniformly in degree; the smooth-cubic any-center specialization is a natural geometric consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
