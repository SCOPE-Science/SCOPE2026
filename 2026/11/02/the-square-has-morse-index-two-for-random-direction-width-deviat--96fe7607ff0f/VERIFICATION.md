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
# Reproducibility and limitations

Run `python checker.py` with the dependency in `requirements.txt`. The exact symbolic computation starts with the independently written second-order absolute-projection correlation jet, reconstructs the four-variable Hessian at the square and verifies its characteristic polynomial and determinant. A second numerical routine evaluates each quadrilateral's width directly from the maximum and minimum projections of its four vertices, then compares central finite differences against the symbolic quadratic form along five directions and two scales.

Observed checker result: `EXACT_FOUR_PARAMETER_HESSIAN_AND_MORSE_SIGNATURE_PASSED`, `INDEPENDENT_DIRECT_SPHERICAL_QUADRATURE_PASSED`, `ALL_CHECKS_PASSED`.

The analytic kernel expansion establishes the cubic remainder and full universal result; finite quadrature is corroborative only. None of these checks constitutes an independent mathematical audit. Historical novelty is provisional; global minimization of the quadrilateral deviation functional is outside scope.
