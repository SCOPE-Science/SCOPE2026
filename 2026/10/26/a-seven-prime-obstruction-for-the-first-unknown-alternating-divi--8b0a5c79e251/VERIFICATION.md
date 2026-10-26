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

# Reproducibility and proof limits

The exact rational threshold identities are reproduced in `verify.py` using `fractions.Fraction`. The checker also tests local factors for odd primes and exponents in a finite range, dyadic exponents through 89, and all integers through 100000. Run `python verify.py` from the same folder.

The mathematics is not predicated on checking infinitely many cases: monotonic prime-factor inequalities, the explicit closed formula for \(\beta(2^a)/2^a\), and the parity of \(\beta(p^e)\) cover all prime powers. Finite tests cannot certify the universal theorem independently. No independent mathematical audit has been performed.
