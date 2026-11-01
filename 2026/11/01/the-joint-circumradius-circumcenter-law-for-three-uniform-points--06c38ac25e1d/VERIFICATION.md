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

# Verification of the circumradius–circumcenter density

The supporting `circumradius_geometry_verify.py` program was executed directly. It passed 26 exact/numerical comparisons, including (i) independently integrated ordered-angle determinant against the elementary function \(\Phi\) at representative arc half-angles; (ii) quadrature of \(\Pr(R<1)\) against the previously established value \(4-32/\pi^2\); (iii) the contained-circle probability \(2/5\); and (iv) quasi-Monte Carlo sampling of the original three points for an independent distributional check. The numerical values included \(\Pr(R<1)\approx0.757722123445\) and \(\Pr(R<1,\ R+S>1)\approx0.357722123445\).

These tests verify only specified identities at sampled parameters or by floating-point quadrature. They do not constitute an infinite-dimensional proof, do not exclude arithmetic error outside the tested values, and do not establish historical originality. The universal distributional claim is proved analytically by the circle-coordinate Jacobian and restricted-arc integral in `RESULT.md`. No independent expert review was performed.
