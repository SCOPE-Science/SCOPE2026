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

Execute the standalone Python program `verification/verify.py`, requiring SymPy. It symbolically checks the identity between the source’s positive equilibrium equations and the corrected reduction, verifies the coefficients as exact polynomials, and independently reconstructs the source’s printed coefficients.

It evaluates the complete model’s two reaction rates exactly at the positive witness \((u,v)=(1,1/3)\), verifies both true and source polynomial factorizations, and confirms the paper’s polynomial roots lie outside the physically admissible \(u\)-interval. It separately reconstructs the positive roots using the source's numerical parameters (6.1).

The symbolic general elimination is proved in `RESULT.md`; approximations used to compare the numerical baseline are not an infinite-domain proof. The checker prints `VERIFY_OK` on success. The result assumes the printed reaction kinetics of equation (1.1) as the scientific object.
