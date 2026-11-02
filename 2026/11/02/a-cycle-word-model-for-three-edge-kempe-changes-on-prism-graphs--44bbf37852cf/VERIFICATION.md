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

Both self-contained verification scripts use only the Python standard library. Run from their common directory:

```
python verify_reduction.py
python verify_odd_cycles.py
```

`verify_reduction.py` imports `verify_direct.py` and enumerates every named proper edge colouring and every full alternating Kempe cycle for each prism with rim size three through twelve. It independently constructs face-word states and their proposed neighbors, tests identical state sets and actual neighbor equality for every state, and outputs `PRISM_CYCLE_REDUCTION_PASS`.

`verify_odd_cycles.py` checks five distinct valid states and each successive legal adjacency in the padded explicit five-cycle families for every rim size five through sixty; it outputs `FIVE_CYCLE_ALL_TESTED_5_TO_60_PASS`. These are finite checks; the all-size correctness rests on the face-potential correspondence, run/cycle classification, preserved prefix boundary conditions, and the published triangle-exclusion theorem. Independent scholarly audit remains unperformed.
