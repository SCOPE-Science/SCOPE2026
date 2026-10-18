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

Run `python verify.py` using Python 3 and SymPy. Successful output starts with `VERIFY_OK` and reports the three tested finite fields. The script derives all six partial derivatives, checks the exact odd-characteristic affine elimination and the characteristic-two square-zero normal form, verifies the complete-intersection Hilbert polynomial and its conormal twist, enumerates finite-field projective singular-support points over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), and confirms the generic odd-characteristic Hessian rank over three prime fields.

The manuscript's scheme-theoretic statements for arbitrary algebraically closed fields are proved by its affine-chart derivations, complete-intersection argument, and global sheaf calculations. The finite tests alone would not prove the infinite assertions; the literature search alone cannot prove originality. The characteristic-zero literature cited for K3-carpet nonexistence is not applied to characteristic two. No independent audit has been performed.
