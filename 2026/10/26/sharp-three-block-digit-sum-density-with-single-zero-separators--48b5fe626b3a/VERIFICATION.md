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

Run `python verify.py` in the same directory. The standard-library checker uses exact fractions, not floating-point approximations. It verifies eight interpolation nodes for the polynomial identity (universal by multiaffinity), 216 exact transfer-matrix evaluations, and 27 independent exhaustive low-residue enumerations with the infinite upper-bit tail summed exactly. It also checks the strict two-block-bound counterexample.

The mathematical proof in RESULT.md establishes the carry identity, support degrees, maximal carry coefficient, geometric tail, and monotonicity. The enumerations alone are not proofs over unbounded block lengths. The existing literature already supplies the limiting constant; finite-block sharpness in the stated family is the additional claim. No independent mathematical validation is asserted.
