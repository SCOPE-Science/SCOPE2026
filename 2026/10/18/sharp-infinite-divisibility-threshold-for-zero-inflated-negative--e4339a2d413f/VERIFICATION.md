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

The supplied standalone `verify.py` was executed with the available Python 3 standard library and completed without exceptions:

```
PASS: 126 rational parameter configurations; all log-PGF coefficients exact through order 85 (edge cases through 120).
```

For each rational parameter configuration, the coefficient recursion is exact in `fractions.Fraction`; it does not rely on floating-point to calculate the logarithmic coefficients. A floating-point trigonometric expression determines the expected side only for the nonboundary grid points; the decisive boundary configurations use exact rational weights and exact sign checks. The exact cases include shapes three and four at their proposed sharp boundaries, as well as parameters on both sides. Positive-side cases have no negative checked coefficients; specified negative-side cases do have one. The finite computation neither establishes infinite divisibility over an infinite range nor proves first-failure indices universally. Those conclusions rely on the numerator-root proof and Pringsheim's theorem in `RESULT.md`. No independent audit or certification is asserted.
