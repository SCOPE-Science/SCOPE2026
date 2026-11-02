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

Run `python3 verify_clique_bouquet_spread.py` in the directory containing the files. It requires only the Python standard library. The program performs three genuinely different finite checks: exhaustive signed active-count states, independently enumerated **labelled** integer-valued one-Lipschitz assignments, and direct exact-arithmetic phase/gap identities. The label-enumeration routine checks every assignment in \(\{-1,0,1\}\) subject to the actual clique edge constraints; it does not call the reduced-state routine.

Observed output:

```
EXACT_ALL_SIGNED_ACTIVE_COUNT_STATES_OK 203
DIRECT_LABELLED_INTEGER_LIPSCHITZ_POTENTIALS_OK 40 27726
EXACT_DOMINANT_PHASE_AND_SQUARE_LAW_OK 168
EQUAL_PETAL_PARITY_AND_GIANT_CLIQUE_LIMIT_CHECKS_OK
ALL_CLIQUE_BOUQUET_SPREAD_CHECKS_OK
```

All comparisons use exact integers. They do not certify infinitely many blade-size tuples; the analytic argument in RESULT.md is required for the universal claim. No independent external audit has been performed.
