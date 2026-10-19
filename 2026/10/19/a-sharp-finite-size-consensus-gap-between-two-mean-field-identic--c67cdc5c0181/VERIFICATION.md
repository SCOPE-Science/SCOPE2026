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

The exact finite-state calculation uses the birth-death harmonic equation with boundaries at zero and full consensus, and applies the binomial and Vandermonde normalizations directly. The accompanying `verify_exit.py` is self-contained Python 3 code using only the standard library.

Execution: `python3 verify_exit.py`.

Observed result: 4305 assertions passed. The exact-rational checks cover every population size from 3 through 39 and all interior states for both panel sizes. Independent high-precision-style log-gamma probability-mass summations at populations 101, 401, 1601 and 6401 corroborate convergence to the analytical maximal gap and the critical majority scale. The analytical Stirling and monotonicity arguments, not finite numerical tests, establish the claims for all population sizes and the large-population limit.

Scope of checks: the program does not simulate random trajectories, certify a publication-priority claim, or establish any result for different update rules or graph topologies. Independent external audit remains unperformed.
