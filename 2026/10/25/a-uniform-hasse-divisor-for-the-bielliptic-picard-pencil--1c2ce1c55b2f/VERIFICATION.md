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

# Reproducibility and logical boundaries

Run `python3 verify.py` with a standard Python 3 interpreter. The checker forms coefficient polynomials by exact integer multinomial arithmetic, reduces them modulo each prime between 5 and 199, checks the claimed factor relations with nonzero constants, checks the Gegenbauer equation, and checks the coefficient polynomial's degree, squarefreeness, and nonvanishing at both excluded parameters.

The run completed with `VERIFY_OK` for all 44 primes in that range. This is a finite corroboration, not an exhaustive proof over infinitely many primes. The general argument is the coefficient calculation, Lucas congruence divisibility, recurrence uniqueness, and ordinary elliptic/Prym decomposition in `RESULT.md`. Numerical output does not determine any factorization degrees of the exceptional divisor over arbitrary finite fields. Neither independent mathematical validation nor an external audit has been performed.
