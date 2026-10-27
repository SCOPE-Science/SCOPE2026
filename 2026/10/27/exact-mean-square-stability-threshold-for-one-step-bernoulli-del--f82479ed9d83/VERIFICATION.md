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

The analytic proof derives the second-moment matrix and its characteristic polynomial, then supplies an explicit positive-definite Lyapunov certificate in the strict stability region. The included `verify_threshold.py` checks exact rational instances at \(q=0\), \(q=1\), and \(q=1/2\), verifies the Lyapunov identity by exact arithmetic at those points, and checks a polynomial sign witness above the \(q=1/2\) boundary. These finite checks corroborate but do not replace the universal analytic proof. The theorem is limited to iid one-step-or-zero delays and deterministic quadratic gradients. The independent audit and external validation channels remain unperformed; no independent certification is claimed.
