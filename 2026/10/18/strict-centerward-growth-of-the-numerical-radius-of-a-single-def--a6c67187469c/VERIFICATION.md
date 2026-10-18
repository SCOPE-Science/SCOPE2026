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

Run `python3 verify.py` in the extracted package. The script has no external dependencies and checks characteristic-polynomial continuants using exact rational arithmetic, plus the adjacent Chebyshev product identity and finite floating-point matrix eigenvalue comparisons via positive-definiteness bisection.

Expected output begins `VERIFY_OK exact_polynomial_checks= 1486 monotone_spectral_checks= 372`.

The polynomial checks cover specified rational weights across dimensions 4 through 24, and the spectral checks cover positive weights 1.01 through 3 in dimensions 4 through 16. The finite tests are not a proof of the all-dimensions or all-real-parameter theorem; that is supplied by the analytical proof in RESULT.md. All mathematical assumptions, including the strict endpoint condition, are documented there. Independent audit has not been performed.
