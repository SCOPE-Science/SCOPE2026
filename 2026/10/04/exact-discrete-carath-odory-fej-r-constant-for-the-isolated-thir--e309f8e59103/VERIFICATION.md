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

The theorem is proved symbolically in `RESULT.md`. `verify.py` is an independent finite corroboration. It checks all meshes \(6\le N\le5000\) against the factorized candidate and dual certificate, and for \(6\le N\le90\) independently enumerates active pairs of sampled inequalities to solve the two-variable linear program. Floating-point tolerances are used only in this corroborative calculation and are not part of the proof.
