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

Run `python verify_calibration.py` with Python 3 standard library. The program checks the saddle-point dynamic-coordinate variance recursively and by an exact rational geometric series for 256 parameter choices; verifies strict positivity of the step-doubling indicator; tests the finite-grid optimal noise variance against the exact Bhattacharyya formula and perturbed scales; checks high-precision asymptotic constants; and bisects the unimodal spectral critical point and the unequal-rate matching partners.

Observed check output: `VERIFY_OK 894`. The script also prints critical spectral rate, the two limiting variance scales and the nonzero terminal Bhattacharyya mismatch. Reproduction checks are finite, except for arbitrary-precision arithmetic of particular limiting expressions; the universal conclusions are proven analytically in RESULT.md.

Checks do not cover floating-point robustness of a complete solver, non-diagonal perturbation covariances, the whole-trajectory calibration optimum, independent peer review, or any claims about novel numerical schemes.
