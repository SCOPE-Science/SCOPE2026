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

# Reproducibility and limits

Run `python3 checker.py` in a standard Python 3 environment. The code constructs the sixteen-state transfer matrix directly from the local modal semantics and uses exact integer Newton identities to verify its characteristic polynomial. It separately enumerates all Boolean valuations on every cyclic frame with three through fourteen worlds, checks all fixed and period-two states, and checks the corresponding recurrence. The expected output is `ALL_CHECKS_OK`.

The general theorem is the symbolic transfer-matrix calculation and the formal trace/determinant identity, not the finite tests. No assertion is made for other neighbor sets, additional propositional variables, or primitive periods longer than two. No independent review has been performed.
