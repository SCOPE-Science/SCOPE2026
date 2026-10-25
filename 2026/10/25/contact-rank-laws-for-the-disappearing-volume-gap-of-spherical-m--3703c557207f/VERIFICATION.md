---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The analytic derivation supplies the proof. Its essential verified steps are the sphere-plus-convex-set erosion identity, farthest-vertex domination near the critical dilation, an anisotropic blow-up, and a beta-integral coefficient calculation. The planar shielding cutoff is obtained by maximizing the shorter-vertex constraint on the longer-vertex two-disk lens; equality and strict sharpness are treated separately.

Run `python verify.py` with SciPy available. The checker uses direct one-dimensional quadrature of the rhombus cavity, compares against a separately evaluated two-disk formula across the predicted threshold, and checks normalized critical-area limits for unequal and equal rhombi. It also checks the three-dimensional lens coefficient and a full-rank polar coefficient. Its completed run printed `PASS: 20 quadrature/asymptotic checks and rank-3 coefficient check`.

Numerical quadrature is not an infinite-dimensional certificate: it does not enumerate arbitrary polytopes, and it is not the basis for the exponent theorem. The big-O constant depends on the fixed polytope and may diverge as shorter vertices approach the circumradius. Originality is subject to residual uncertainty in historical erosion and ball-intersection literature. Independent review has not occurred.
