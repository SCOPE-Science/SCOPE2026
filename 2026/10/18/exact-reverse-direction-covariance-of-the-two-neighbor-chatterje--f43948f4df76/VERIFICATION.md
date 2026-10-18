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

# Reproducibility verification

The companion `verify.py` runs with Python 3.10 or later and the standard library alone. The recorded execution returned:

```
PASS: 5915 exact assertions, independent exhaustive permutations for n=4..8
```

For each permutation it calculates the two right-neighbor score and the score of its inverse from scratch, yielding exact rational means, variances and cross-covariances. It reconstructs the edge-array orthogonal projections for integers \(4\le n\le40\) and checks the exact norm/inner-product identities. It checks the stated rational correlation inequalities for finite integers up to \(n=500\).

The analytical proof, not brute-force enumeration, establishes all parameter values and the unique sample-size maximum. No normal approximation, null simulation, or cross-paper priority certification is represented as a proof. Independent audit has not been performed.
