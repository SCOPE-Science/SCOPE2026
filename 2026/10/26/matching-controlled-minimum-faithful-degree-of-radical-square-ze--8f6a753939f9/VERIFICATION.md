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

# Reproduction and boundaries

Run `python3 verify.py` using the standard Python 3 library. The program tests all 81 two-vertex quivers with ordered arrow multiplicities zero, one or two; 120 seeded three-vertex cases; 60 seeded four-vertex cases; and all 625 two-vertex quivers with ordered arrow multiplicities zero through four. Its two independent finite combinatorial computations are exhaustive feasible-integer-profile search and maximum-matching search, and it constructs explicit basis matrix units for each tested optimum. The constructed arrow action maps have disjoint matrix-unit coordinates, all arrow composites vanish, and vertex idempotents remain linearly independent. The expected output is:

`VERIFY_OK_FAITHFUL_MATCHING 261 max2_quivers 625 max4_quivers`

The program checks finitely many quivers and their explicit matrix actions. It does not prove the universal theorem, enumerate all module isomorphism types, or constitute independent mathematical validation. The argument for arbitrary finite quivers and fields is the two-way dimension-inequality and matrix-unit construction in RESULT.md.
