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

# Verification

A proof of the infinite-dimensional finding is given in `RESULT.md`. The reproducibility script `check.py` uses NumPy and SciPy to test finite Jacobi sections, exact one-defect formulas and first-coordinate derivatives, a nonconstant converging weight example, and two finite shadows of the long sign-block obstruction.

Run: `python check.py`.
Observed: `VERIFY_OK finite_section_checks=86 one_defect_cases=7 Frechet_directional_cases=3 alternating_block_sizes=2 infinite_proof_required=True`.

The key analytic steps not certified by finite tests are: compactness of the Jacobi tail difference, simplicity and isolation of the upper eigenvalue, uniform spectral-gap differentiation, and the two-sided infinite-block perturbation. These are explicitly proved in `RESULT.md`. Independent mathematical audit has not been performed.
