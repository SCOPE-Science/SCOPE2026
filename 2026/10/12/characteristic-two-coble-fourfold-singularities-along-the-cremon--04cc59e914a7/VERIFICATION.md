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

The exact verifier `artifacts/verify.py` reconstructs Dolgachev's characteristic-two weighted equation over \(\mathbb F_2\), differentiates it, and checks three explicit lifted singular curves through one Cremona–Richmond incidence point. It then extracts the normal quadratic form along a representative curve, verifies that the determinant of its polar form is \(t^2(t+1)^2\), and checks the incidence-point factorization \(Q_0=(w+x_0)(w+x_1)\).

The script also enumerates the \(15\) points and \(15\) lines of the smooth quadric \(Q(\mathbb F_2)\) and verifies that every point lies on exactly three of those lines and every line contains exactly three points. This finite enumeration checks the stated Cremona–Richmond incidence model only; it is not used as a substitute for the symbolic all-parameter proof of the generic transverse type.

The verification establishes the claim along the fifteen lifted curves. It does not compute a primary decomposition of the global Jacobian ideal, prove that there are no other ambient singular components, or construct a resolution.
