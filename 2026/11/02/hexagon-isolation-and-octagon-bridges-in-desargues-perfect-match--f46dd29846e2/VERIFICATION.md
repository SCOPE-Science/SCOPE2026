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

# Reproducible checks

The package includes `verify_petersen_permutations.py` and `verify_generalized_petersen.py`. Both use only the Python 3 standard library and no downloaded input or random seeds. Run them separately:

```sh
python3 verify_petersen_permutations.py
python3 verify_generalized_petersen.py
```

The first checker lists every permutation supported by the Petersen adjacency relation, classifies its cycles, tests the action of all \(120\) permutations of the five labels, forms the flip graph by relative permutation cycles and searches from every configuration. It also certifies the six Petersen perfect matchings, complementary cycle counts and doubled-\(K_6\) incidence.

The second checker builds the generalized Petersen graph \(GP(10,3)\) directly as \(20\) labelled vertices and \(30\) edges, checks a concrete edge-preserving bijection to the bipartite Petersen double cover, enumerates every perfect matching by disjoint-edge recursion and tests each difference as a connected degree-two subgraph. Its all-source searches reproduce all the numerical claims. It also evaluates the permanent of the ten-by-ten Petersen biadjacency matrix exactly by the Ryser inclusion–exclusion formula, obtaining \(60\) without reference to the matching recursion. Its logic does not call the first checker or reuse the first checker's computed configuration table.

For a successful run, the scripts print, respectively, `PETERSEN_PERMUTATION_CYCLE_CLASSIFICATION_PASS`, `DESARGUES_S5_THREE_ORBITS_AND_HEX_OCTAGON_PASS`, `SIX_FROZEN_MATCHINGS_DOUBLE_K6_INCIDENCE_PASS`, `ALL_60_SOURCE_GEODESICS_PASS`, `GENERALIZED_PETERSEN_30_EDGE_EXHAUSTION_PASS`, `EXACT_RYSER_PERMANENT_60_PASS`, `INDEPENDENT_KNESER_DOUBLE_ISOMORPHISM_PASS`, `MATCHING_CYCLE_FLIP_COMPONENTS_AND_K6_PASS`, and `ALL_PAIRS_DISTANCE_AND_ECCENTRICITY_PASS`.

**Limits.** These checks are exhaustive for the explicitly fixed finite graph. They do not constitute independent scholarly audit, establish literature priority or prove any general-family extension.
