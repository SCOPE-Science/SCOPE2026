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

The supplied `curves_f5.txt` contains the 31 published source equations in order. From this directory run:

```
python census.py
python bitangent_crosscheck.py
```

The first script checks geometric evenness of the line-intersection divisor by exact squarefree polynomial factorization and the order at infinity. The second checks normalized binary quartic coefficients against all degree-two-form squares over the field of five elements. The second script independently verifies there are exactly 31 projective lines and prints the Fermat bitangents. Both scripts produced the same vector of 31 individual counts, same six-stratum histogram, same sharp value, and same maximizer. `verification_output.txt` records full outputs.

The finite computation is exhaustive because published work supplies all 31 isomorphism classes and there are exactly 31 rational projective lines over the field. Smoothness and source-list completeness are established in the cited original classification; they are not reproved by these scripts. The geometric-square criterion is independently justified in `RESULT.md`. No independent external audit has occurred.
