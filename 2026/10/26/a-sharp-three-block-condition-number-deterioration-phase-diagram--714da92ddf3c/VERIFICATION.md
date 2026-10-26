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

# Reproducibility
The embedded `VERIFY.py` requires Python 3.10+, NumPy, and SymPy. Reproduce using `python VERIFY.py` in the same directory. No network resources, external data, or additional project files are required.

The script verifies the exact two-block factorization, the discriminant and boundary-polynomial identities, a strictly positive certificate for the family-specific upper bound, and the exact three-by-three generalized characteristic polynomial. It then tests 1,800 independent reproducible random parameter configurations against directly assembled symmetric matrices and checks a four-term asymptotic witness sequence. On execution the script printed `VERIFY_OK: 1800 randomized matrix comparisons, 6 algebraic identities, exact witness and asymptotic sequence; last ratio=1.4998916236`.

The infinite claims are proved by the factorized identities and order comparisons in `RESULT.md`; floating-point tests only detect implementation or transcription mistakes within finite samples. The code does not test approximate or sketched preconditioning.
