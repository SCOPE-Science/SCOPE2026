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
# Checks and limits

The verification artifact `verify.py` computes graph distances and deformation formulas in exact rational arithmetic. It samples all ordered edge-label choices for two through five arms, a thirteen-point uniform coordinate grid, and five rational times. It checks output coordinates, monotone and exact affine distance, coordinate-presentation symmetry, compatibility with pole reversal, identity at time zero, fixed-point behavior at distance one, terminal maximal distance, shared-pole seams, and the signed action of all edge permutations for up to five arms.

The recorded output `verification_output.txt` is from executing the embedded program without external packages. Sampled fractions and finite arm counts are not exhaustive for a continuum or all integers. The universal mathematical verification rests on the exact piecewise formulas and boundary-seam proof in RESULT.md. Literature originality assessment is based on the cited inspected materials and cannot guarantee complete publication coverage.
