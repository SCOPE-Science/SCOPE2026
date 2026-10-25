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

# Verification scope

The proof is self-contained in `RESULT.md`. The accompanying standard-library Python program `verification.py` was run and returned `PASS: 2455 finite arithmetic and projection checks`.

The actual finite checks cover the transition identity for four pairs of semiaxes, matching chord-witness/affine-upper expressions at many scales, strict disagreement of that witness with the upper expression beyond the transition, and numerical comparison of the exact axial nearest-boundary formula against dense planar ellipse grids. Algebraic inequalities in the proof, rather than grid measurements, establish the result for all real scales and dimensions.

No independent mathematical review or exhaustive literature-priority certification has been performed. The middle interval of the nonround profile remains undetermined.
