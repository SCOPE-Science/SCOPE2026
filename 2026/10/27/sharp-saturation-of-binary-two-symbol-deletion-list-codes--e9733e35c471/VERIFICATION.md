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

The mathematical proof establishes the result for every integer source length \(n\ge3\) and every list size \(L\ge1\). In particular, the two separate incidence bounds and the four disjoint three-output classes establish the universal bound and strict pre-saturation obstruction. Explicit class-based constructions attain the bound at and beyond the threshold.

Run `python3 check.py`. The checker uses only the Python standard library and reports:

```
PASS enumerated_words 4088 construction_cases 240 exact_DP_cases 40
```

These are complete finite checks only over their stated ranges. The infinite statement follows from the symbolic argument, not from extrapolation. The exact integer dynamic program is distinct from the construction and directly optimizes finite signature-class populations for small parameters. The checker does not establish priority in the literature or an independent audit.
