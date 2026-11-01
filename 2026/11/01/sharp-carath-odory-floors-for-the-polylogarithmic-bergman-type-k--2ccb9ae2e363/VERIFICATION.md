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

The proof covers every nonnegative real parameter. It uses convergent fractional-power integrals, sharp geometric Möbius-transform bounds, elementary gamma/zeta identities, and a fixed-sector Riemann-sum asymptotic. No finite numerical computation is used to infer a universal conclusion.

The included `CHECK.py` may be run with Python 3 and mpmath installed:

```sh
python CHECK.py
```

It should produce three diagnostic `POLYLOG_..._OK` lines. These check representative exponents, complex interior samples and the boundary approach, not all uncountably many exponents; they are sanity tests and do not certify the analytic theorem. Exact identities at the integer endpoints are written directly in RESULT.md.

A self-review covered correctness, comparisons with known zero and kernel literature, and mathematical value. No independent audit or independent validation has been performed; the incomplete inspection of Fornberg–Kölbig (1975) is a residual originality limit.
