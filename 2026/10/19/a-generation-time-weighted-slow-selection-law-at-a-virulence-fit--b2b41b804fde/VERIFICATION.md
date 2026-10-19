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
# Verification and reproducibility

Run `python verify.py` with Python 3, NumPy, and SciPy. It checks exact rational identities for equal transmission potentials, generation-time moments and example equilibria; verifies the expected Jacobian eigenvalue pattern at three interior equilibria; solves the full five-dimensional perturbed equations at four perturbation sizes; and compares their slow-time frequency at one fixed slow time with the unique implicit weighted-logarithm solution. These are supplemental finite checks, not exhaustive spectral certifications.

The analytic argument in RESULT.md provides the universal normal attraction, standard finite-dimensional invariant-manifold limit, and reduced drift formula. The rate convergence is asserted on bounded slow-time intervals for an endemic initial condition, not at arbitrary unbounded physical times or through eventual extinction of the disadvantaged strain.
