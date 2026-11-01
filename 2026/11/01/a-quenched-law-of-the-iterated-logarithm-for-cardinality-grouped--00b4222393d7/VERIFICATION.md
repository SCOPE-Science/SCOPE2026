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

# Verification and scope

The exact-arithmetic checker `checker.py` was executed directly from its packaged source with Python 3 and produced:

```
PASS: 12002 exact assertions
```

It checks the subset-product/cardinality-parity identity through six binary inputs, Lucas parity through 1024, exact rational expectations and independence for finite rows, and sparse binary-count bounds. No external dependencies or files are necessary.

These assertions verify finite algebraic steps only. They do not establish almost-sure limits, independence for all time horizons, or historical novelty. Those conclusions are based on the complete analytical argument in `RESULT.md`, with the standard Kolmogorov law of the iterated logarithm and martingale functional central limit theorem clearly identified. Independent mathematical validation has not been performed.
