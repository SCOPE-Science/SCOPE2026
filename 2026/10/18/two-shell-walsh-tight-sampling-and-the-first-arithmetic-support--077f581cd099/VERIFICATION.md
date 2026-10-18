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

The included `check.py` uses only the Python standard library and computes exact rational (never floating-point) Walsh Grams for all admissible pairs through dimension eight. It checks all parity/divisor regimes through ten, enumerates every odd dimension three through fifty-one with exact binomial coefficients, and verifies the polynomial identity used in the infinite improvement proof by integer polynomial multiplication. `check_output.txt` records the actual successful run. The general theorem is established in `RESULT.md` by algebra, not by extrapolation. The first public date is that of the motivating 2020 article, not a publication date for this result. Independent validation has not been performed.
