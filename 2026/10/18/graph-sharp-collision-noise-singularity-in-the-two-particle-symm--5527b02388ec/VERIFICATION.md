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

The standalone `verify.py` was executed with Python 3 and no third-party dependencies. It constructed exact-rational full two-particle generators, checked detailed stationary balance and centered Poisson solutions, and compared exact cycle and complete-graph formulas. It also compared weak-diffusion values with the killed pair-walk Green operator on representative connected graphs. Output: `PASS: 42 full-generator exact-rational and singular-limit tests`.

These finite examples check implementations and normalization. The analytical variational argument is needed for the arbitrary-graph result; the difference-equation proof establishes the all-cycle formula. No independent scientific audit has been performed. Tests do not establish novelty and do not justify extensions to unexamined model classes.
