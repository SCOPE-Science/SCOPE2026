---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The finite-period proof uses a smooth coordinate change to remove the first-order perturbation, then computes the variance of the second-order Fourier observable. Exact orthogonality and the signed-residue separation for all periods at least five give the coefficient. The period-four aliasing is checked separately.

The unchanged standalone `CHECK.py` tests the character identities using exact rational arithmetic at periods 5 through 20, distinguishes short-period aliasing, and solves representative nonlinear periodic-point equations numerically. The finite checks do not replace the analytic perturbation and all-period residue argument.
