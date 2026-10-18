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

The proof reconstructs the Euler polynomial, its polar matrix, the full Fourier spectrum, and a prime-dependent exact integer witness to strict negativity. The equality cases in the integer proof are checked using primality; no finite search substitutes for the unbounded argument. The full real kernel and positive trace are proved analytically.

The accompanying `verify.py` uses only Python's standard library. It verifies the polar matrix against the defining difference formula, the Fourier eigenrelation, the cosine-sign factorization, and every allowed weight ratio for odd primes below \(200\). The run produced:

`VERIFY_OK primes=45 exact_negative_witnesses=2001 trigonometric_sign_cases=40016 exact_integer_polar_cases=34`

The comparison of trigonometric values uses finite-precision floating-point arithmetic, while the classification of signs and the negative-mode witnesses use integer comparisons. No computer algebra package or external service is needed to reproduce the checks. No independent audit has been performed. No assertion is made about the existence of Hilbert schemes realizing every character vector.
