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
The analytic proof reduces the SVT recurrence exactly to independent scalar shrinkage recurrences under the matching observation hypothesis. It derives the activation index from the strict threshold test, proves persistent positivity after activation for every \(0<\delta<2\), and proves the \(\delta=1\) finite-settling formula. A nuclear/Frobenius norm argument separately identifies the unique finite-\(\tau\) regularized minimizer.

`verify.py` uses exact `fractions.Fraction` arithmetic. It checks multiple rational values of \(\tau\), \(\delta\), and \(s_j\), including \(\delta<1\), \(\delta=1\), and \(\delta>1\). It verifies the exact first-positive index, the geometric error recurrence, persistence of positivity, a multi-direction rank staircase, and the finite-settling formula. The packaged script returns `VERIFY_OK`.

These finite checks corroborate the recurrence implementation; they do not replace the all-parameter proof. No claim is made about floating-point roundoff or about observation patterns with shared rows or columns.
