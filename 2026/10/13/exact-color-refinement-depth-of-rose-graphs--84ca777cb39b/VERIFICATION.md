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
The proof is uniform for every rose graph with at least two petals. The attached `verify.py` independently constructs rose graphs and implements ordinary color refinement.

It checks every nondecreasing petal-length tuple with two through five petals and every length from \(3\) through \(12\). For each tuple it verifies both the exact stabilization-depth formula and equality of the stable partition with the explicit automorphism-orbit partition.

The checker returns:

`VERIFY_OK depth_checks=2992 orbit_checks=2992 petals=2..5 lengths=3..12`

These finite checks are corroborative only. They do not replace the all-parameter clipped-distance proof in `RESULT.md`.
