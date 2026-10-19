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

## Reproducibility
Run `python3 checker.py` in a directory with this file and the standalone checker. It computes 39,042 finite consistency diagnostics, including barrier equations and independently computed trigonometric derivatives. Infinite-time convergence, uniqueness, basin completeness and critical scaling are consequences of the fully written analytical arguments in RESULT.md, not tests of finite trajectories.

## Scope of verification
The worst-case threshold allows arbitrary bounded real inputs; the cat-map condition is sufficient only. An independent scientific review has not been performed.
