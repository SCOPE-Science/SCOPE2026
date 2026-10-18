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

# Verification and limits

The proof checks all real points of least period two, with the exact assumptions \(a=b>0\), \(c>a/4\), \(\mu=-4\), and \(\varepsilon>0\). Its two independent scalar equations after eliminating the exchange relation give an exhaustive conic, not a finite numerical enumeration.

Exact Jacobian determinants, the tangent unit multiplier, and the two-step trace establish the full characteristic polynomial. At \(\Delta=0\) or \(\Delta=-4\), only algebraic eigenvalue multiplicities are claimed; no Jordan or nonlinear normal-form conclusions are assumed. The square-root branch \(d>0\) parametrizes each primitive two-cycle exactly once and excludes the fixed endpoints.

Run `python3 check_exact.py` to check the two-cycle exchanges and characteristic polynomial by exact rational arithmetic in three quadratic number fields, with no third-party packages. Expected stdout: `VERIFY_OK`. This finite reproducibility check corroborates but does not replace the universal proof.

Closest established work already recognizes nonisolated period-two families and generic volume-preserving spectral categories; novelty is limited to the exact parameterized transverse polynomial and threshold. The full text of the 1998 predecessor was not inspected. Independent audit and independent validation have not been performed.
