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

# Verification record

The critical derivation uses only exact identities and bounded convergence. The attached `verify.py` uses standard-library Python 3 and runs finite reproducibility checks, not mathematical certification of an infinite-time limit.

## Actual checks

Run `python3 verify.py`. It integrates the complete six-compartment dynamics and the scalar reduced equation for two vaccination susceptibilities, checking compartment mass, accumulated infection pressure, transformed infectious prevalence, and the two cumulative infection counts. It also computes the log-time crossover against its theoretical limit for three decreasing positive susceptibility gaps.

Successful execution prints: `VERIFY_OK: 2 full six-compartment trajectories, maximum exact-reduction residual 1.1e-12; three singular log-clock tests, final profile discrepancy 0.00216844` (the last digits may vary minimally by floating-point implementation).

## Limits

Finite time grids do not establish the infinite-time limits, universal exponents, or uniform parameter asymptotics. Those follow from the analytical inequalities and the dominated-convergence argument in `RESULT.md`. No independent audit has been performed.
