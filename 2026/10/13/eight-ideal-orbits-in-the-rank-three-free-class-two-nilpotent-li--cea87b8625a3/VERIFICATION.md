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

Run `python3 verify.py` from the folder containing the accompanying script. It uses only the Python standard library and reconstructs the complete subspace sets for the two prime fields. Expected terminal marker: `VERIFY_OK`.

Over \(\mathbb F_2\), the script searches 2825 distinct reduced-row-echelon subspaces in dimension six, detects 45 ideals, and forms eight automorphism orbits with sorted cardinalities \(1,1,1,7,7,7,7,14\). Over \(\mathbb F_3\), it searches 56632 subspaces, detects 94 ideals, and forms eight orbits with sorted cardinalities \(1,1,1,13,13,13,13,39\). The independently rebuilt orbit action uses elementary basis changes, diagonal scalings, and the central shear subgroup. All computations were replayed against the included script prior to packaging.

The calculations exhaust the indicated two prime-field instances only. They do not test arbitrary extension fields or establish that an infinite-field-uniform classification follows from finite enumeration. The general proof is supplied in RESULT.md. No independently performed audit or external mathematical validation is represented here.
