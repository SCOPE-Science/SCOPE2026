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

Run `python verify_bistar.py` (Python 3, NumPy, SciPy). The program computes the proposed optimizer with exact rational coefficients for twelve pairs of leaf count and central-edge length. It independently solves unrestricted signed-coefficient linear programs for both hub extensions using an exact enumeration of sign functionals representing the real Lipschitz-free norm on the tree. It asserts agreement with the analytical formula to numerical linear-programming tolerance and prints `BISTAR_EXACT_FORMULA_LP_OK 12`. This is finite evidence; the unrestricted quantifiers are established by the symbolic proof in RESULT.md.

No independent audit has been performed.
