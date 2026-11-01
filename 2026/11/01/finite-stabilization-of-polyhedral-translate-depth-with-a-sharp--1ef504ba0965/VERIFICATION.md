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

The theorem follows from the analytic facet-clearance proof in `RESULT.md`, not from sampling. Reproduce deterministic exact-rational tests with `python verify_polyhedral_depth.py`. The program verifies 9,342 explicit polyhedral witness comparisons in dimensions two and three, plus four below-threshold rational sharpness witnesses. It does not exhaust uncountably many polytopes, scales, measures or query points. Independent audit has not been performed.
