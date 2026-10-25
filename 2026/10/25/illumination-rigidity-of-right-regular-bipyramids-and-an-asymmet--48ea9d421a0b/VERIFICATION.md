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

## Checks performed

`python3 verify.py` completed successfully using only the Python standard library:

```
EXACT_ANGULAR_OK n=3..140 cells=14764 integer_cover_n=3..12 optimizer_gcd=verified
FACETS_OK n=3..60 symmetric_heights=1/3,1,5 direction_tests=394632
ASYMMETRIC_EXACT_WITNESS_OK n=5 heights=1,3 directions=6 fractional=7/2
```

The angular arc-incidence tests and cyclic-block counts use exact integer arithmetic; the finite set-cover sweep runs through every subset state for each indicated \(n\). The radical witness inequality uses exact squares of positive integers. The facet-direction sweep uses ordinary floating-point trigonometry and excludes near-boundary values; it is independent diagnostic corroboration, not an exact certificate for arbitrary real parameters.

The infinite result depends on the explicit strict facet inequalities, pole/equator separation, cyclic block covers and fractional dual incidence bound proved in `RESULT.md`. Only the specified unequal-height pentagonal polytope is claimed. No independent external proof audit has been performed.
