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

# Reproducible checks and boundaries

Run `python3 verify_flower_snark.py` (only Python 3 standard library). The exact run checked the canonical graph6 isomorphism and emitted:

```
VERIFY_OK_FLOWER_SNARK_INDEPENDENCE_HOMOTOPY_AND_FULL_DIHEDRAL_CHARACTER
GRAPH_N_M 20 30 UNIQUE_5_CYCLE (5, 6, 7, 8, 9)
F_VECTOR (20, 160, 660, 1510, 1923, 1310, 450, 75, 5) FACES 6113
MORSE_PAIRS 3054 HASSE_COVERS 29610 ACYCLIC_VERTICES 6113
CRITICAL_DIMS {0: 1, 5: 1, 4: 3} CRITICAL_FIVE_TO_FOUR {2: -1, 0: 1}
HOMOTOPY_WEDGE_TWO_S4
AUTOMORPHISM_GROUP_D10_ORDER 20
H4_TRACES_ROTATIONS (2, 0, 2, 0, 2, 0, 2, 0, 2, 0)
H4_TRACES_REFLECTIONS (2, 0, 2, 0, 2, 0, 2, 0, 2, 0)
H4_Q_MODULE_TRIVIAL_PLUS_ROTATION_SIGN
```

Every face is enumerated from the exact graph adjacency test; a complete directed-Hasse topological sort verifies acyclicity. The signed projection recursively eliminates all matched four-faces before computing the remaining integral attaching degree. A unit entry in that boundary is sufficient for the sphere cancellation, in view of the absence of other critical dimensions. The graph-automorphism group has been bounded and its twenty elements enumerated. Signed Lefschetz calculations are performed for every element, not a selection of conjugacy classes. This is a finite result about \(F_5\); the code does not prove an infinite-parameter statement. The group representation is classified over \(\mathbb Q\), not as a direct-sum decomposition of \(\mathbb Z[D_{10}]\)-lattices. Independent scientific audit is not performed.
