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

Run `python checker.py` in the directory containing RESULT.md and checker.py. The checker uses Python's standard-library exact fractions and SymPy for exact symbolic simplification; it performs six symbolic identities and 606 further exact assertions, reporting 612 total.

The symbolic conditions directly verify the equal elementary symmetric sums, the Vandermonde product difference, the common shifted second sum and the cleared-denominator identity for all formal variables. Exact rational periodic-orbit reconstruction checks one period return, the sample means and cubic difference, every circular autocorrelation in selected periods from one to eight, and strict saturated-response signs across rational test cases. The checker is reproducible and deliberately requires no numerical integration or external datasets.

The all-period autocorrelation theorem is established by the Fourier proof in RESULT.md, not by checking periods up to eight. The universal sign theorem is established by the symbolic factorization with strictly positive factors, not by a finite parameter grid. No external independent validation has been performed.
