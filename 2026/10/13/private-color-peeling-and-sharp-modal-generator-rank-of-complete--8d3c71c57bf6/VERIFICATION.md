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
# Reproducibility and limitations

Run `python3 verify.py` with Python 3 and only its standard library. Expected output:

```
VERIFY_OK exhaustive_support_cases 19607 rank_bruteforce_cases 274 sharp_depth_cases 13 direct_boolean_closures 600
```

The support tests compare an independently implemented modal successor-type refinement with the peeling quotient for every tuple of one to five nonempty subsets of a three-color palette. Rank tests brute-force all supports for small size vectors and palette sizes at most four. The depth family is tested for 2 through 14 parts. Random tests use direct Boolean-algebra closure and allow repeated colors within a part. These computations do not establish the general theorem; it is proved in `RESULT.md`. Independent external audit was not performed.
