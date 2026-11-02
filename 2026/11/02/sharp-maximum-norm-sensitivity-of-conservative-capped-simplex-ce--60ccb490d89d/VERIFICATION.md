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
# Reproduction and verification

Run `python3 verify_limiter.py` from the directory containing this document. The verifier uses only the Python standard library and reports 2,528 successful checks on the preserved source version.

The checks include exact rational enumeration of all extreme zero-sum perturbations in dimensions 2 through 10 for every possible number of free coordinates, exact rational mass-preserving sharpness examples for dimensions 3 through 32 and three distinct masses per dimension, and independent floating-point clipping/shift projection calculations for randomly generated pairs with matching total mass. The code checks coordinatewise caps, total-mass preservation and the computed maximum-norm ratio.

The proof for unbounded dimension relies on the KKT affine formula, the analytic linear-program bound for each free-set size, the monotonicity across free-set sizes, and the exact strict-face witness. Finite computations provide reproducibility and sanity checks, not an all-dimension certificate. The theorem does not cover nonuniform cell volumes, unequal masses, or complete PDE timestep stability.
