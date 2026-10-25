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

# Reproducibility and checks

Run `python src/verify.py` using Python 3.9 or later. It uses only the Python standard library. In this package it printed:

`VERIFY_OK five_run_words_checked 80730 coefficient_range n=5..27`

The program enumerates every positive composition of each integer \(n\) into five parts for \(5\le n\le27\). The direct predicate tests all length-\(k\) factor windows against the length-\(k\) prefix, then compares with the run criterion. Independently, the generating-function coefficients are reconstructed from the explicit numerator and denominator polynomials by the linear recurrence for a rational power series, and compared with the direct counts. The counts for lengths \(5\) through \(11\) are \(1,2,7,13,27,44,75\).

All finite tests passed. No exhaustive assertion is made for lengths beyond \(27\); the all-length result relies on the mathematical proof in `RESULT.md`. The limiting density uses a symbolic pole-order argument and a second independent probabilistic derivation, not numerical extrapolation. No external audit or independent mathematical validation was performed.
