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

Exact finite certificates: run `python src/pencil_census.py`, `python src/orbit_and_base.py`, and `python src/independent_census.py` with `data/census.json` and `data/orbits.json` alongside. The first script uses exact Groebner tests and exhaustive linear subspace enumeration, the second derives full rational surface symmetry, degree-five eliminants and transversality, the third uses independent extension-field arithmetic through cubic degree to reproduce the curve and pencil census. These scripts were successfully replayed against the packaged data.

Correctness is supported by the proof of exhaustive reduction in RESULT.md; finite checks alone do not imply results outside the enumerated F3 parameter spaces. Prior equivalence may be incompletely indexed. Independent audit was not performed.
