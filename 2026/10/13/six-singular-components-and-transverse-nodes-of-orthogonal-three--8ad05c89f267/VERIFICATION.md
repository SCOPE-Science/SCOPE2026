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
# Verification

The exact polynomial equations and all quantifiers are in `RESULT.md`. The crucial dependency matrix is \(H=\begin{psmallmatrix}0&a&b\\a&0&c\\b&c&0\end{psmallmatrix}\), whose determinant is \(2abc\). Every nonzero pattern is handled in the proof. The projective degree calculation uses the degree-two isotropic quadric and the Segre polarization, not a numerical interpolation.

The included `CHECK.py` evaluates the defining equations, Jacobian rank, kernel quadratic Hessian and degree formula for ambient dimensions \(M=4,5,6,7\) using exact symbolic algebra. Its successful output is `EXACT_CHECK_OK`. It does not certify all dimensions or classify the non-generic intersections, and no external or independent audit has been performed.
