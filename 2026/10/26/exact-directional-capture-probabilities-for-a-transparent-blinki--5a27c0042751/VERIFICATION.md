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

# Reproducible checks

Run `python3 verify.py` with Python 3. The executable uses only the standard library. It reconstructs two independent algebraic representations: the closed forms and a 70-digit renewal resolvent from backward eigenmodes, over unequal gate switching rates, initial positions and reset rates. It tests probability bounds, mixture identities, strict reset monotonicity over sampled parameters, and asymptotic coefficients. It also simulates Brownian positions **only at exact exponential event times**, using the exact Brownian-bridge crossing probability on active-gate intervals, with fixed random seeds. The run passed 2346 assertions/comparisons. Monte Carlo events give empirical rather than deductive evidence; the infinite claims follow from the analytical proof in RESULT.md. Finite double-precision tests have finite tolerances; high-precision renewal calculation guards against cancellation in the small capture-probability regime.

No independent scientific audit was carried out.
