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

# Verification record

Running `python3 verify.py` from this package produced:

```
PASS: exact-rational ULC diagnostics for five heterogeneous and four homogeneous models
PASS: first heterogeneous (1,2) failure at k=4, rational defect -17/360
LIMIT: finite diagnostics do not prove the classification or eventual strictness
```

The calculation uses finite exact rational sums, not floating-point approximations. The accompanying mathematical argument proves the all-parameter homogeneous result by log-concavity of Poisson cumulative probabilities and a synchronized-sum argument; the heterogeneous result follows from the dominant two-rate exponential correction to the maximum pmf. No external mathematical certification has been performed. Numerical or finite checks are not used as infinite proofs. The first failure index is not characterized uniformly for arbitrary rates.
