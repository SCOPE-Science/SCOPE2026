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
# Verification of the three-dimensional lattice constant

Run `python3 verify_lattice.py` (Python standard library only). The checker uses exact fractions for the four positive norm facets, verifies the supporting-functional domination, the face-equality coefficient identities, all three vertices of the extremal parameter triangle, and the previously exhibited extremizing pair. Expected output:

`LATTICE_SCHAFFER_EXACT_DOMINANCE_AND_EXTREMAL_TRIANGLE_OK`

The proof, rather than this finite checker, establishes the bounds for every nonnegative real coordinate triple and exhausts all possible normalized extremizing pairs. The known value \(\beta=15/11\) is taken from the cited primary source, not independently reproved. No external audit has been performed.
