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

# Verification record

Run with standard Python: `python3 VERIFY.py`. The checker constructs the orbit vectors directly from the explicit inequalities (no downloaded data, third-party libraries, or heuristic root solver). In the completed scientific review its output was:

`VERIFY_OK isotropic_orbits=65 exhaustive_bounded_character_cases=27 exceptional_oct=6`

The exact checker tests 65 coprime parameter triples in dimensions 2–6, including all endpoint types in the tested range, and bounded integer-character searches on 27 triples. It verifies that the orbit tensor sum acts as a scalar on the sum-zero space. It does not enumerate arbitrarily large integers or establish a universal root-free theorem. The mathematical proof in `RESULT.md` handles all permitted dimensions and integer parameters; the checker is supplemental.

The group-theoretic ingredient is the standard complete toric automorphism theorem, in particular the Demazure-root description of the identity component and the finite fan-symmetry complement. This claim has not undergone an independent mathematical audit.
