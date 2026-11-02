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

# Reproducibility and scientific limitations

Run `python3 verify.py` with Python 3.9 or later. The standalone program requires only the Python standard library. It explicitly enumerates each partial signed monomial matrix with square equal to its support projection, multiplies every ordered pair, tests literal anticommutation, and compares the count with exact rational coefficients of `exp(5z+6z^2+2z^4)` in ground-set sizes zero through five. Successful output ends in `VERIFY_OK`.

The all-parameter generating function and joint-rank refinement are proved by the signed transitive-block classification in RESULT.md. Finite censuses are independent tests and not proofs of infinitely many cases. The result is for coefficients ±1 in characteristic other than two and does not imply a corresponding characteristic-two statement. Publication-priority risk from a broader monomial Clifford classification remains; independent validation is not performed.
