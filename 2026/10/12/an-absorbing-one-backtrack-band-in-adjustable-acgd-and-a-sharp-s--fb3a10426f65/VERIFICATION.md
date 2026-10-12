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

The quantified theorem is proved algebraically in `RESULT.md`. The verification script does not substitute finite tests for the proof.

The bundled script checks the exact default-parameter checkpoint transition with rational arithmetic, verifies that the initial scale requires two backtracks, proves by direct rational comparison that the eighth updated scale lies in the one-backtrack band, and recomputes the displayed iterate and objective contraction factors. It also samples rational scalings strictly inside the absorbing band and confirms exactly one backtrack and an unchanged checkpoint scale under the stated source rule.

The verification does not test multidimensional behavior, wall-clock cost, or global convergence beyond the scalar specialization claimed here.
