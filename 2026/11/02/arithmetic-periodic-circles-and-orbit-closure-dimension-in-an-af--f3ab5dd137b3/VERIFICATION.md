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

The theorem follows from a unimodular torus coordinate change, an explicitly iterated affine skew product, a character-kernel component count and Möbius inversion. Its measure-theoretic part follows by tracking Fourier modes under the Koopman isometry. None of the infinite assertions is inferred from finite data.

Run `python3 verify_affine_torus.py` with the standard Python library. The program uses exact fractions, not floating-point tolerances. It checks sample fixed-point congruences in the original coordinates, several rotation denominators, first-admissible primitive periods, elementary divisibilities, and positive arithmetic component counts. These tests are consistency checks of finite instances, not an exhaustive test of every forcing or period.

Limits: the analysis concerns the integer-matrix torus family and Haar-typical orbits. It does not concern digitized dynamics, arbitrary noninteger coefficient matrices, or a pointwise dense-orbit statement for every initial condition. No independent mathematical audit has been performed.
