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

# Verification and limits

The derivation first solves the two-type Moran birth--death recurrence with population size three and then evaluates the four favorable outgoing transitions from the unique three-allele interior state. The symbolic verification uses SymPy to check the first-step identity and the exact variance-factorized difference as identities in free variables. It also checks exact differences for two distinct background dispersions with the same mean.

Run `python verify.py` in this directory with Python 3 and SymPy installed. Successful execution prints `VERIFY_OK`. Its separate finite-state implementation enumerates all seven nonabsorbing three-individual allele configurations, constructs the exact rational Markov absorption system and solves it by Gauss--Jordan elimination for seven rational fitness triples. This is an independent finite-chain cross-check of the analytic first-step formula.

The proof itself holds for all strictly positive real fitnesses and explicitly accounts for all transitions, so its generality is not inferred from finite experiments. No infinite-population, Wright--Fisher, weak-selection truncation, or nonconstant-fitness conclusion is established. A genuine independent external audit has not been performed.
