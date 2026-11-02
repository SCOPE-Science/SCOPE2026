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

# Independent numerical consistency checks, not a proof replacement

Run `python verify.py` with Python 3.11 or later and no third-party modules. The supplied verifier was run from the source code embedded with this finding. It completed 149 deterministic checks of profile normalization, positivity and monotonicity; numerical quadrature versus exact loss and derivative costs; comparisons against explicit admissible alternative pulses; and full two-quadrature drive and damped coherent-amplitude ODE calculations at three distinct loss budgets.

Universal global minimization, uniqueness and the sharp transitions depend on the analytic Poincaré energy-defect identities written in `RESULT.md`. The finite computations do not constitute a proof of an infinite-dimensional control claim. Exact laboratory feasibility, publication priority and independent validation are not established by these tests.
