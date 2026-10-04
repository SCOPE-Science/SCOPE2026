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

The proof is analytic. The accompanying `verify.py` performs independent arithmetic checks of the formulas used in the statement.

It verifies exactly that the first-cell coefficient is \(8/105\), evaluates the exact polynomial cell-integral formula at high precision, confirms the convergent coefficient \(C\) lies in the stated decimal interval, and checks numerically that \(j^6c_j\) and the scaled energy tail approach the proved constants \(1/196830\) and \(1/984150\).

The numerical checks do not replace the infinite proof. Convergence of the series follows from the analytic \(O(j^{-6})\) bound, and the sharp correction follows from the uniform Taylor expansion \(c_j=rac1{196830}j^{-6}+O(j^{-7})\).
