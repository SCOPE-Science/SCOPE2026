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

The submitted `checker.py` uses Python's standard library only and can be executed with `python3 checker.py`. It enumerates all equivariant orbit-parameter choices for \(m=2,3,4\), verifies every one of the five preconditional axioms together with conditional identity, semicomplementation and double-negation inflation on all subsets, and directly compares the surviving binary-operation tables to the theorem's normal forms. It independently checks recurrence counts against explicit admissible-row enumeration through \(m=8\).

Observed outputs: full brute-force symmetric expansions for \(m=2,3,4\) number \(2,4,13\), with exact set equality; recurrence totals through \(m=8\) are \(2,4,13,55,261,1310,6802\); final checker line `ALL_CHECKS_OK`.

The all-size classification uses the mathematical proof in `RESULT.md`, not finite tests or probabilistic extrapolation. The checker does not explore arbitrary non-equivariant operations for larger carriers, and does not certify bibliographic priority or provide independent validation.
