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
The theorem is proved analytically in `RESULT.md`. The critical steps are the positive even-power expansion, sharp power-sum extrema at fixed Euclidean norm, conversion to exact nested Euclidean balls, and support-function equality analysis. No finite enumeration establishes a quantified claim.

`verify.py` independently checks representative boundary radii, support values, strict intermediate directions, and radial inequalities. Replay output from the bundled verifier: `VERIFY_OK cases=35`.

Scientific limit: this concerns the support norm of the constant-energy body and does not assert saturation by eigenfunctions for arbitrary potentials.
