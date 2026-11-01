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

The proof identifies an explicit finite path of core states, verifies the branch choice for every state and parameter in the indicated interval, and proves stationary weights by detailed balance. The cited theorem on occupation-time limits is used only after all its stated finite-core hypotheses have been checked.

The standalone `core_path_checker.py` uses standard-library exact rational arithmetic, with no downloads or optional dependencies. Executing `python3 core_path_checker.py` checks sample rational parameters \(1/1000000\), \(1/1000\), \(1/192\), \(1/96\), \(1/48\), \(1/24\), \(1/17\), \(1/12\), \(1/9\), \(1/8\), and \(1/6\). Each case checks all finite path transitions and verifies exact stationarity and outer-core mass.

These checks do not establish the theorem over a continuum of parameters; the inequalities and path formulas in RESULT.md do. Neither the arcsine law nor uniqueness of any stationary law is reproved by the checker. Independent validation has not been performed.
