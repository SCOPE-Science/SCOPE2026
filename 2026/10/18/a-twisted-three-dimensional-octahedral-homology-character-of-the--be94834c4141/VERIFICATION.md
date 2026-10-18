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

# Reproduction and checks

Run `python3 verify_cube_two_matching.py` with Python 3.10 or newer; the program uses only the standard library. It enumerates all 4096 candidate edge sets and tests two equivalent membership predicates; enumerates 1698 nonempty faces; constructs an acyclic nonaugmented discrete-Morse matching with 847 pairs, 7980 incidences and critical dimensions zero, five, five and five. It independently computes all mod-two boundary ranks and Betti numbers. It constructs all 48 cube automorphisms and checks, separately, their signed fixed-face and selected-orbit Lefschetz traces against the closed rational character formula. The tests count all 48 group elements rather than sampling conjugacy representatives.

The executable produces `Q3_TWO_MATCHING_EQUIVARIANT_VERIFIED` after all assertions succeed. This finite exhaustive certificate supports a nonequivariant integral homotopy result and a rational group-character result; it does not establish an integral equivariant module-isomorphism or independently certify priority. External independent mathematical assessment has not been performed.
