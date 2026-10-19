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

# Verification notes

The universal proof is the six-step argument in RESULT.md. The fixed-line case is treated separately. The strict positivity of the first-coordinate multiplier, the signed strict monotonicity of the second coordinate and the square-summability of its reciprocal-square denominators hold for both signs of the initial coordinates and for every nonzero coupling.

The standalone Python standard-library program `verify.py` was executed successfully: **384,018** finite consistency assertions passed. These include exact-rational first steps, strict orbit monotonicity and numerical agreement of a dyadic finite difference and a signed tail coefficient across four parameter choices with both coupling signs. Finite tests are not proofs of convergence, completeness of the plane or novelty. No independent audit has been conducted.

Reproduce with `python verify.py` in the directory containing the files. No external data files or third-party packages are required.
