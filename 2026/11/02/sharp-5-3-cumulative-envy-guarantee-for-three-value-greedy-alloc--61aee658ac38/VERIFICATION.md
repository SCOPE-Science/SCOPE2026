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

The integer transition potential is displayed in RESULT.md and is checked independently in `VERIFY_CERTIFICATE.py`. The finite checker covers every greedy state and signed comparison state of magnitude at most eight, every next value in {1,2,3}, and both assignments. The proof separately covers every state with magnitude at least nine by a direct inequality, without relying on a finite cutoff.

A fresh exact dynamic-programming check computes the offline optimum over all signs for all 29,523 ordered sequences of length at most nine. It also verifies the explicit infinite-family formulas at 501 sample parameters. These checks are supplementary to the analytical potential proof. Originality is subject to the explicitly reported primary full-text access limitation; independent validation has not been performed.
