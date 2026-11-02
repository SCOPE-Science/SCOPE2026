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

The standalone `VERIFY_CHECK.py` was run with `mpmath` precision set to 50 decimal digits and passed 336 high-precision finite assertions across dimensions 1–4, three choices of weight and frequency, and degree/partial-product samples. It checks the gamma-ratio eigenvalues, an independently evaluated truncated infinite product, positivity, strict ordering, first-order coefficient, binomial block multiplicity and the normalized singular-value constant.

The finite product was truncated at 20,001 factors and compared to the exact ratio with an explicit finite tolerance, not treated as an equality or infinite proof. The singular-value and logarithmic asymptotics are verified by the analytic gamma-product expansion and exact block counting in `RESULT.md`; a finite checker cannot certify their limits. Full-text historical-priority comparison was not possible for a related 2020 radial Toeplitz paper. Independent audit has not been performed.
