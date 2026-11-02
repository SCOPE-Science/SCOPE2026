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
# Finite verification record

The two source files `verify.py` and `verify_subgroups.py` were run from their actual package directory using Python 3; their respective recorded outputs are `verification_output.txt` and `verification_subgroups_output.txt` and each ends with status `VERIFY_OK`.

`verify.py` checks all 65,536 binary four-by-four matrices. It checks binary Gaussian elimination against a 24-term determinant parity calculation, and graph reachability against absence of proper nonempty outgoing-closed subsets, throughout the entire universe. It independently compares the canonical-orbit histogram with a Burnside computation using the five cycle types. The total of 908 unrestricted perfect classes reproduces Wei–Zou's 2023 published result.

`verify_subgroups.py` enumerates all 30 actual subgroups of the symmetric group on four vertices, enumerates matrices invariant under each subgroup by orbits of its action on 16 cells, checks determinant parity and outgoing-closed subsets, and uses descending subgroup inclusion-exclusion to obtain exact stabilizer counts. It agrees with the direct method, including the absence of an exact alternating-group stabilizer.

Both verifiers are deterministic finite searches over completely specified spaces. Neither is a proof of a statement in higher dimensions or over other fields. There is no independent human audit or external proof-assistant certification.
