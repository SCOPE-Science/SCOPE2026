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

The theorem concerns the fixed graph \(GP(10,2)\). Both supplied programs use only the Python standard library and compute exact integers, edge sets, adjacency matrices, and graph isomorphisms. They enumerate rather than sample.

Checks performed:

```
python3 verify_cycle_dfs.py
python3 verify_matching_alt.py
```

The first program enumerated all rooted nonreversing Hamiltonian cycles with exhaustive recursion and checked \(435\) unordered pairs, the thirty-vertex exchange graph, all-source distances, the antipodal orbit quotient, the Petersen triangle incidence graph, and the full double-cover adjacency. It also verified there are no simple four- or six-cycles in the base graph.

The second program enumerated all thirty-six perfect matchings by exact recursive branching on the smallest unmatched vertex. Exactly thirty complementary two-factors are Hamilton cycles and six are not. It independently reconstructed all eight-edge switches and the antipodal quotient, checked an explicit graph isomorphism to the Petersen graph modeled as disjoint two-subsets of a five-element set, and verified the lifted graph.

Outputs from the saved scripts:

```
DFS_EXHAUSTIVE_PASS cycles=30 eight_switches=60 degree=4 diameter=4
ANTIPODAL_QUOTIENT_PASS orbits=15 edges=30 triangles=10 derived_Petersen=10
CANONICAL_DOUBLE_COVER_PASS 30 vertices 60 edges Petersen_line_double_cover
SHARP_THRESHOLD_PASS lower_bound=8 connected_at=8
INDEPENDENT_EXACT_COVER_PASS perfect_matchings=36 cycles=30 remaining_2_factors=6
PETERSEN_ISOMORPHISM_PASS quotient_triangles=10 Kneser5_2_verified=1
SHEET_LIFT_PASS 8_switch_graph=double_cover_line_Petersen
```

The packaged `certificate.json` supplies the full thirty-cycle edge-mask census, involution, edge adjacency, quotient and explicit \(KG(5,2)\) labeling. Its graph labeling follows the indexing convention in `RESULT.md`.

Limitations: This is a complete finite computation for one twenty-vertex graph, not an infinite proof or an external audit. The two algorithms share the stated definition of the base graph but use different complete combinatorial enumerations. Bibliographic originality is subject to additional human review.
