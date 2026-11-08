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

# Reproduction

Run `python verify_flex_quintic.py` in a Python 3 environment with SymPy. The verifier checks an exact quadratic Jacobian relation over the quadratic cyclotomic integer ring by polynomial reduction, the absence of linear syzygies by a full-column-rank certificate after reducing modulo seven, and the near-free Tjurina identity. Its final line is `FLEX_QUINTIC_VERIFY_OK`. The algebraic proof separately establishes the entire singularity basket, projective symmetry of line pairs and applicability of the near-free criterion. Modular full-rank is a valid characteristic-zero certificate because the coefficient matrix is integral and a nonzero reduced minor implies a nonzero integral minor. No independent audit or external validation has been performed.
