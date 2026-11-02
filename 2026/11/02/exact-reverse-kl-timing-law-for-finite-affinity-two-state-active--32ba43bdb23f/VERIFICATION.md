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

The analytic proof establishes uniqueness, normalization, boundary behavior, and both asymptotic regimes for every fixed interior population pair. A standalone Python 3 standard-library checker, `verify_optimum.py`, independently recomputes two KL divergences and their derivatives numerically, optimizes by interval bisection, compares efficiency with neighboring times and the maximum-power time, and checks low- and high-cost predictions for six representative population pairs. Its 480 finite assertions passed. It is neither an exhaustive continuum scan nor an independent mathematical audit. Run with `python3 verify_optimum.py`.
