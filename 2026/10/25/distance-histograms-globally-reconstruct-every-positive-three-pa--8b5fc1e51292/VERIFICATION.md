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

# Verification and reproducibility

The embedded `verify_theta_reconstruction.py` is stand-alone Python 3 and imports only the standard library. Running `python verify_theta_reconstruction.py` reproduces the exact rational polygon-clipping checks and seeded sampling comparisons. The observed output was:

```
EXACT_CASES 961
POSITIVE_ONSET_CASES 182
RANDOM_CHECKS [((1, 2, 5), '3', 0.046875, 0.0467909), ((1, 1, 5), '5/2', 0.1632653, 0.1619), ((1, 1, 1), '3/4', 0.3125, 0.3128273), ((2, 3, 3), '5/2', 0.078125, 0.0794909)]
ALL_CHECKS_OK
```

The reference program evaluates all path alternatives, not just the two endpoints' routes. Boundary equalities contribute zero probability. The strict threshold onset is tested at rational perturbations above the value derived in the proof. These computations verify the finite configurations only; no sampling claim is used to establish the theorem for arbitrary positive real lengths.

The complete proof is in `RESULT.md`. The closest general paper on distance distributions and metric graphs was accessible in abstract and citation form but not as an inspectable full-text manuscript; the originality assessment preserves that bibliographic uncertainty.
