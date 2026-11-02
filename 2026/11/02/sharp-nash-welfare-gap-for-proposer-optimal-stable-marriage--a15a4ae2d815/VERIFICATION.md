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
# Verification scope

`VERIFY.py` is standalone Python 3 and requires only the standard library. Run `python3 VERIFY.py` beside the research note. It independently enumerates every strict complete preference profile with \(n=2\) and \(n=3\), every perfect matching and every candidate blocking pair. It reconstructs men-proposing deferred acceptance, evaluates integer-valued Nash products and rational product ratios, and checks the universal claimed upper bound. It counts 12 extremal three-pair profiles and reproduces the sharp ratio 8. It constructs sharp cyclic witnesses for sizes 2 through 9 and performs reproducible random checks for 1,000 four-pair and 150 five-pair profiles.

Expected successful output:

```
VERIFY_OK cyclic_sizes=2..9 exhaustive_2=16 exhaustive_3=46656
THREE_BY_THREE extremal_count=12 strict_gain_profiles=5424 max_product_ratio=8
SAMPLED_OK n4=1000 n5=150
```

The full-parameter mathematics is proved in `RESULT.md` using man-optimality, utility-ratio bounds, equality conditions and a labeled enumeration. Finite computations are tests, not an independent proof or full enumeration for larger markets. Independent external validation has not been conducted.
