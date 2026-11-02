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

# Reproducibility and boundaries

The standalone `verify.py` uses only the Python standard library. Execute `python3 verify.py` to enumerate all labeled graphs of maximum degree at most two on one through five vertices, canonicalize their components, reconstruct every diamond conflict from the original edge set, test the explicit coloring and use exact backtracking to refute a smaller palette. It additionally tests 295 nonisomorphic path/cycle component profiles of orders one through ten, including backtracking lower checks through order seven.

The expected last line is `VERIFY_OK`. The checked output is:

```
ALL_LABELED_DEGREE_TWO_GRAPHS_N_LE_5_OK 305
UNLABELED_COMPONENT_PROFILES_N_LE_10_OK 295
VERIFY_OK
```

The all-order proof is the constructive case analysis in `RESULT.md`. Finite tests are not treated as proof for arbitrarily many vertices. No independent audit, external certification or machine-checked formal proof is represented by these checks.
