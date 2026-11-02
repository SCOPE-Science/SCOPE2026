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

`verify.py` is a standalone Python 3 standard-library checker. Actual execution printed:

```
PASS 12516 exact-rational and floating checks
```

It compares the exact reciprocal-holding-time objective against independent direct first-hitting-time sums for each starting state, verifies strict pair-averaging for unequal rates at the same total cost, and samples many price/size regimes to compare the analytic scalar optimizer with perturbed ratios and its high-price boundary. The check uses seeded pseudorandom input, rational arithmetic where stated, and approximate floating-point comparisons elsewhere.

The complete all-parameter correctness guarantee comes from the stationarity/first-passage identity, strict equal-price pairwise smoothing and monotone scalar derivative proven in `RESULT.md`. Sampling finitely many real parameters does not prove a universal statement or the absence of a published equivalent. In particular a near-zero exceptional rate must not be interpreted as an admissible zero-rate minimizer. No external independent mathematical audit or verification has been performed.
