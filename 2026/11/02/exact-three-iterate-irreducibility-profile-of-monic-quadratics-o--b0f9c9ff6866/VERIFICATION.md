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

# Finite-field verification

The standalone `verify.py` script requires only standard Python 3. It constructs prime fields and polynomial-quotient realizations of four nonprime finite fields, enumerates every monic quadratic in each tested field, checks the first three critical-orbit character conditions, checks the pair and triple correlations in the proof, and compares the outcomes with all three exact formulas. A separate polynomial-arithmetic implementation verifies actual degree-2, degree-4, and degree-8 irreducibility by Rabin's gcd criterion over the prime fields of sizes 3, 5, 7, and 11.

Successful execution returned:

```
VERIFY_OK fields=14 coefficient_pairs=7190 direct_prime_iterates=4 degree_bound=8
```

The tested field orders were 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 9, 25, 27, and 49. The universal proof instead relies on Capelli's lemma, elementary norm identities, and complete quadratic-character-sum evaluations. Exhaustive finite tests do not certify all prime powers or later iterates. Independent validation has not been performed.
