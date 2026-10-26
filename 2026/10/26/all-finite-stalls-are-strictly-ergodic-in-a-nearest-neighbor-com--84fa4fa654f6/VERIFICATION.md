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

# Reproduction and limits

The included `verify.py` needs only Python 3 and its standard library. Execute `python3 verify.py` from the package directory; the expected first output line is `CHECKS_PASSED 1101`.

The script checks the unique-root equation at rational endpoints, high-precision eigenfunction recurrence residuals through twenty stall lengths, monotonicity of the computed spectral parameters, exact substitution word lengths against independent direct expansion, the published two-stall thirty-four-step count, the four-stall six-hundred/seven-hundred-step comparisons, the seven-stall thousand-step comparison, and the rational certificate proving the existence of a longer-step reversal by step seventy-two thousand.

The decisive universal proof is the explicit eigenfunction and the finite-rank decomposition in `RESULT.md`; a finite checker alone would not prove the theorem. Approximate-root residual tests are labeled numerical and are not used to deduce analytic exactness. No independent validation or external audit has been performed.
