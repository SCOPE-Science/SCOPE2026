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

# Verification and reproduction

Run `python verify.py` with Python 3.9 or newer (standard library only). The deterministic checker reconstructs the two-stage Radau IIA rational stability map, validates the first seven exact Maclaurin coefficients, and evaluates **2,020 exact-rational finite-matrix entries** on cycles \(3\le n\le14\) at dimensionless timesteps \(h=1/10000\) and \(h=10^6\). For each matrix, it checks mass preservation, symmetry and translation invariance. It checks strict positivity at small \(h\) through nine vertices, a negative distance-five entry from ten through fourteen vertices, and positivity for all twelve tested sizes at the large sampled timestep.

The code also evaluates the derived complex-resolvent kernel at five representative positive timesteps and locates negative coefficients. Those floating-point diagnostics do **not** prove the infinitely-many-negative-coefficients theorem. Its all-timestep validity follows analytically from the nonreal decay root and the rational/irrational rotation argument in the result. Exact finite tests likewise do not establish claims covering arbitrarily many vertices or all timesteps.

Expected successful terminal output starts with `VERIFY_OK 2020 exact rational matrix entries` and lists five sampled negative-kernel locations.
