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

The algebraic recurrence and all polynomial positivity certificates are re-created from scratch by running `python3 verify_bdf3.py`; no external library or downloaded database is required.

The program verifies 18 strict polynomial sign certificates for indices 4 through 21, four additional exact adjacent-ratio certificates for indices 20 and 21, and 285 positive Bernstein-basis rational coefficients in total. It also makes 52 independent generalized-binomial coefficient comparisons at four rational fractional orders, and exact calculations for the tail induction's two invariant-rectangle corner values and derivative inequality. The discriminant and the first three coefficients are checked exactly.

The infinite sign claim is **not** inferred from finite enumeration. It follows from the symbolic recurrence and the invariant ratio rectangle \([4/5,11/10]\) for all indices at least 22. The proof, including the explicit inequalities, appears in `RESULT.md`.

No independent mathematical review has been performed. Neither a particular fractional PDE scheme's stability nor a maximum principle follows solely from this coefficient-sign result.
