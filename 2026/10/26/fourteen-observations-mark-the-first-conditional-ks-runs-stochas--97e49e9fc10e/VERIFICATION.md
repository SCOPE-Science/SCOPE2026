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

# Reproducible verification

Run `python3 verify_ks_runs.py` using Python 3 and the standard library. The checker independently tabulates the full joint law of the total number of runs and the integer-scaled KS maximum (i) by brute-force choice of plus positions and (ii) by an integer-valued dynamic recurrence. It checks all positive size pairs with total size through 14 modulo label exchange, and tests all conditional tail inequalities using integer cross products. It verifies the closed-form three-run and four-run probabilities of the unbounded counterexample family for 40 initial parameters and prints its counts. The analytical proof of that family, not its finite tests, establishes the universally quantified part. All previous historical results are referenced rather than independently certified. The comparison with certain older unavailable texts is provisional.
