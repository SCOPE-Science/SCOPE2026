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

Run `python -m pip install -r requirements.txt` followed by `python verify.py`. The packaged replay passed 100 symbolic and exact-rational assertions, including exact comparison of full seven-state and reduced generators, Cramer identities, polynomial determinant factorization, mean advantage and short-time coefficients. Numerical grid checks are corroborative, not substitutes for the analytical all-parameter proof in RESULT.md. No empirical or independent validation has been performed.
