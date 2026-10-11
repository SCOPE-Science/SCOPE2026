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

# Reproducibility and checks

The accompanying `verify_normals.py` requires NumPy and SciPy and runs directly with Python 3. It reproduces twelve mean-value comparisons with separately integrated normal-map Jacobians; checks normal-root multiplicity for 4,408 randomly sampled interior points outside a narrow caustic strip; and checks both limiting coefficients against the exact formula. On the inspected packaged source the command `python verify_normals.py` printed `VERIFY_OK 4439 independent finite checks; direct Jacobian quadrature and normal-polynomial roots agree`.

A direct symbolic simplification also verified the claimed rational root of the ellipse–astroid crossing equation. Reproducibility checks establish neither mathematical originality nor correctness for all real parameters; the analytic proof is in `RESULT.md`. Floating-point methods are not intended for the discriminant set where normal roots coalesce. Independent audit has not been performed.
