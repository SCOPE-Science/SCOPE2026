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

The complete original result is a finite-state, all-rule theorem with an exact reproducible calculation. Run `python verify.py --csv classification.csv` using Python 3 (no external dependencies). The program recomputes the exact shortest-word census for all 256 rules, verifies the sharp maximum, reproduces the full CSV byte-for-byte, and independently enumerates 32,256 output words/predecessor-tail sets through length six. It checks all reachable-subset successor closures, so a failure to reach a singleton establishes impossibility for all word lengths.

The independent direct enumeration covers only observations of lengths up to six; it cannot independently certify the negative infinite cases. Those cases are proved by the 15-state subset closure, backed by exact code and the de Bruijn path correspondence in RESULT.md. No stochastic simulations, floating-point approximations or timeouts are used.

This verification is part of the described proof/reproducibility process, not an external audit. The reported classification remains subject to independent mathematical and historical-priority review.
