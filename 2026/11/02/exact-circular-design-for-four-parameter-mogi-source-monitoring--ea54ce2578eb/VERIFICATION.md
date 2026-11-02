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

Run `python check.py` using Python 3 and SymPy. The program differentiates the physical three-component displacement forward model with respect to the four parameters (source strength, depth and horizontal coordinates) rather than substituting the displayed Fisher matrix. It tests exact symbolic Fisher blocks for square and triangular networks, their determinant, an exact suboptimal angular example, the radial derivative factorization and the unique positive algebraic root. The program's successful execution was checked against the embedded source.

The proof of global angular optimality is the analytic rotational symmetrization and strict-concavity argument in `RESULT.md`. Finite checks do not certify the infinitely many possible station designs. The exact determinant is a local Gaussian information quantity; independent physical or observational validation has not been performed.
