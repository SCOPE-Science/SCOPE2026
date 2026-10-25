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

# Verification instructions and limits

Run `python3 verify_cycle_fixed.py` with Python 3.9+ and only the standard library. The test enumerates actual edge orbits under 19 distinct explicit permutation cycle types, verifies cycle-support multiplicities, compares complete orbit-face polynomials to the independent factorial formula, reconstructs exact reduced simplicial homology over the field with two elements for 15 even-cycle factors, and checks directed acyclicity and the critical-face count for the prescribed matching on 3,366 enumerated faces.

Expected final line:

`CYCLE_ORBIT_FIXED_SPACE_CHECKS_OK 19 cycle_types 15 even_component_mod2_cases 3366 acyclic_matched_faces`

These finite tests do not prove the theorem for all permutations. The general proof comes from orbit classification and the acyclic fiber-matching argument supplied in `RESULT.md`. The test does not independently verify integral homotopy type or bibliographic originality. No independent mathematical audit is represented by this file.
