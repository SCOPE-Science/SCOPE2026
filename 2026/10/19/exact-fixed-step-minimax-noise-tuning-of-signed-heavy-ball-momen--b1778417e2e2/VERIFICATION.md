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

The analytic proof establishes the infinite family and all boundary cases; no finite computation is treated as a proof of the quantifiers. `verify.py` independently solves discrete Lyapunov equations for test cases, compares direct endpoint maximization with interior curvature probes, and checks the closed-form momentum against numerical scalar minimizers on a deterministic grid. It also tests that a decreasing positive curvature interval yields the claimed factor-two restriction cost. No independent audit has occurred.
