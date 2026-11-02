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

Run `python3 verify_stability.py` with Python 3 and no external dependencies. The script checks exact rational equality between independently enumerated local order patterns and edge-subset integration, then checks the forest recursion and path/cycle expressions. Expected output:

```
VERIFY_OK direct_profile_graphs= 9016 forest_dp_graphs= 3110 paths= 21 cycles= 19 realizable_three_pair_stable_refinements= 10054 out_of= 46656
```

The final test enumerates all \(46,656\) preference profiles for three matched pairs when every participant places all three opposite-side candidates in one top tie, and obtains stability probability \(10054/46656=5027/23328\). No finite test substitutes for the all-size analytical proof. No independent audit has been performed.
