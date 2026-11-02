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

# Reproducibility

The result is finite. Run the two included programs with standard Python 3; no third-party modules, external files or network services are required.

```sh
python verify_matching.py
python verify_coloring.py
```

`verify_matching.py` enumerates the 105 matchings of eight vertices, constructs every exact-cover decomposition into seven factors, constructs the entire four-cycle switching graph, checks 960 isolated and 5,280 mobile states, and executes breadth-first search from **every** mobile state. It then verifies that the 30 minimum-eccentricity states are precisely all relabelings of the affine translation factorization.

`verify_coloring.py` independently enumerates normalized proper seven-edge-colourings, performs alternating four-cycle swaps on their symmetric colour tables and renormalizes the colours. It confirms all 6,240 states, 17,640 undirected transitions and all components. It checks that the six degree classes are the full relabeling orbits of the vertex symmetric group, so a BFS from each nontrivial orbit representative proves the complete eccentricity table.

Expected successful checks from the two actual executed packages:

```
MATCHING_EXACT_COVER_6240_AND_17640_EDGES_PASS
ALL_5280_SOURCE_DISTANCES_RADIUS9_DIAMETER11_PASS
AFFINE_30_CENTERS_AND_960_ISOLATES_PASS
LATIN_EDGE_COLORING_6240_INDEPENDENT_CENSUS_PASS
INTERCALATE_17640_EDGES_SIX_ORBITS_PASS
ONE_5280_COMPONENT_AND_RADIUS9_DIAMETER11_PASS
```

The two programs give separate finite exhaustive calculations, not independent scholarly review. No claim is made for general complete graphs, higher-order one-factorizations, or different move sets. Scientific priority remains conditional on the accessible literature.
