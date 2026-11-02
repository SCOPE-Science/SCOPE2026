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

# Reproducibility and limitations
Run `python verify.py` using Python 3. The checker calculates prime valuations of the binomial using independent Legendre factorial sums, compares with the predicted carry and first-failure criterion, checks the exact congruence-class census, and independently evaluates whole binomial divisibility for a small subset. It covers 12 prime-power configurations and 2,386 coefficients.

This is finite corroboration only: the proof of all primes and exponents is the arithmetic argument in RESULT.md. The self-review has passed; independent mathematical audit and independent certification were not performed.
