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

# Verification of the geometric subgroup fixed-space theorem

Run `python3 verify.py` with Python 3 and no external packages. The program independently enumerates the original colored faces fixed by each finite permutation subgroup, constructs the orbit-inflation cellular model, verifies its mod-two cellular boundary ranks, and compares signed direct normalizer traces with the abstract orbit-cycle formula. It checks 41 parameter/group cases, 3,014 fixed cells and 218 normalizer-character evaluations. Expected leading output: `VERIFY_OK cases= 41 invariant_cells= 3014 normalizer_characters= 218`.

**Proof boundary:** The program is a finite consistency check. The unrestricted topological conclusion rests on the full fixed-poset argument and published inhabited flabby inflation theorem in `RESULT.md`. It does not independently establish torsion-freeness for every parameter, enumerate all subgroups in unbounded degree, or perform any independent mathematical audit. No external certification is represented.
