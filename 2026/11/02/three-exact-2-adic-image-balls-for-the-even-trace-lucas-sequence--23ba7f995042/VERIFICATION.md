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

# Reproducibility of finite checks
Run `python3 VERIFY.py` using Python 3 standard library only.

The code generates the sequence modulo each dyadic modulus until the complete recurrence state returns to its initial state. Since the companion recurrence matrix has determinant one, this state walk is purely periodic; the collected set is the entire image modulo that modulus. The predicted set is independently generated from the three prescribed congruence balls. The script checks twelve parameters (both signs), all exponents from 1 through 11, and uses unrestricted integer arithmetic for the three valuation-distance identities on distinct indices.

Recorded result: `PASS 132 complete modular images, 13904 modular recurrence states, 25308 valuation-isometry comparisons`.

The program tests finitely many parameters and moduli. The proof in `RESULT.md` establishes the theorem for all eligible parameters and all powers of two. No independent audit has been performed.
