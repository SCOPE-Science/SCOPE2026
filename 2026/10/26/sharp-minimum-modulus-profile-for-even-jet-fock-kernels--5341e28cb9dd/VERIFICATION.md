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

# Reproducibility and limits

The accompanying `verify.py` uses high-precision independent evaluation of the scalar exponential-polynomial identity. Run `python verify.py` with Python 3 and `mpmath`. It tests even orders 2, 4, 6 and 10 against finite penalties 0.1, 1, 10 and 100, checks an explicit complex polar grid inside and outside each closest-zero disk, and verifies derivative nonvanishing at each closest zero. It also verifies six high-order limiting profiles. All checks succeeded in the supplied environment. The script is only a finite consistency check, not an exhaustive search for other roots and not an independent proof. The exact complex-domain result rests on the two-line reverse-triangle and monotonicity argument in `RESULT.md`, plus coefficient normalization and Stirling expansion. Independent review is not performed.
