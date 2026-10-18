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

# Reproducibility and verification

The exact affine kernel and beta marginal are derived in `RESULT.md`. The supplied `CHECK.py` script independently computes the beta sign integral by numerical quadrature and confirms two algebraically distinct regularized-incomplete-beta expressions, the published uniform-volume specialization, and the dimension-uniform Gamma coupling bound on a parameter grid. It also samples representative large-dimension regimes. Its output is finite numerical consistency evidence, not a substitute for analytic proof.

Run: `python CHECK.py` using Python 3, SciPy, and NumPy. The script exits with an assertion error on a failed consistency check. The strict inequalities and the asymptotic statements for arbitrary positive parameter sequences follow from the displayed proof, not from finite testing. Full independent mathematical and bibliographic review has not been performed.
