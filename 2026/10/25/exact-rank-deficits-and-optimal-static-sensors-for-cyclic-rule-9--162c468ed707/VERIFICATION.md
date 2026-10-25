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
# Verification

The analytic result is established in `RESULT.md` by reflection-span, quotient-orbit, and Möbius arguments. The standalone Python 3 standard-library verifier `verify.py` independently constructs each Rule-90 observation row by binary cyclic shifts and computes its rank using GF(2) elimination, without implementing the reflection-orbit proof in its rank calculation.

Execute `python verify.py`. The expected summary is:

```
VERIFY_OK exhaustive_sensor_sets=4079 census_checks=63 pair_horizon_checks=54 random_checks=1520
```

The exhaustive check considers all nonempty sensor subsets for every ring size from 3 through 11. The random check covers larger sizes through 127. The checker compares the full nullity formula, cardinality-stratified set census, and optimal horizon for observable two-sensor sets. Testing finitely many instances cannot independently establish the unrestricted theorem; historical priority has not been independently validated. Relevant inaccessible material is identified in `RESULT.md` and `REVIEW.md`.
