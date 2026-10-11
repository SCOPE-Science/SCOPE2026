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

Run `python3 verify.py` with Python 3.9 or later; no third-party dependencies are required. The verifier computes the projected-area Fourier polynomial and exact Grassmannian/Sphere Beta moments using rational arithmetic, verifies the two moment expansions through fourth order, verifies the quadratic and cubic cancellation and the strictly positive quartic coefficient, and checks the extrema of both curvature perturbation polynomials. A successful run prints `VERIFY_OK` and the coefficient as a reduced fraction.

The analytic proof in `RESULT.md` establishes the statements for all sufficiently small real parameter values, including the negative side. The script performs finite symbolic coefficient calculations, not exhaustive testing of an interval or independent verification of the complete proof. Optional external numerical quadrature at nonzero parameters was used only as a cross-check and is not required to reproduce the exact certificate. No independent scientific audit has been performed.
