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

The attached `separation_rank5_verify.py` is an exact finite-type oracle in the specified quaternary signature. It enumerates all distinct-tuple one-point extension types for circles with 1 through 16 points, verifies fifteen distinct empty-tuple types with the last two equal, checks the key two-point identity for gap pairs (6,7) and (7,7), and additionally tests 121 gap-truncation cases.

The general proof is not finite extrapolation. Four marks leave only a gap-positivity test, three marks reduce remaining two-round types to three-capped gaps, two marks reduce remaining three-round types to seven-capped gaps, and the verified pair identity forces one-point extension-type stabilization at 15 points. These statements are proved in RESULT.md and together cover all positive finite sizes.

The recorded output in `verification_output.txt` was generated from the exact embedded script. No code requiring privileged services or downloaded libraries is used. The formal proof has not been independently audited.
