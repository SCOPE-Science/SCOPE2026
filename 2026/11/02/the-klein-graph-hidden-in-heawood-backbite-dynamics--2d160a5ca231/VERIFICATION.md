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

# Reproducibility of the finite Heawood backbite classification

Use Python 3.10 or later; both programs depend only on its standard library:

```text
python3 verify_paths.py
python3 verify_edges.py
```

`verify_paths.py` defines the Fano incidence graph with the cyclic difference set, explores every Hamiltonian path by backtracking from every vertex, identifies reversal pairs, enumerates all endpoint-to-interior backbites, and checks all 504 breadth-first shortest-path trees. It forms the suppressed multigraph, finds 56 vertex-disjoint simple-edge triangles, constructs the 56-vertex quotient, checks its girth and all-root distance shells, and enumerates 336 explicit incidence graph automorphisms. It verifies that the quotient's full directed-edge set is one orbit. Expected output:

```text
PATH_DFS_504_BACKBITE_672_RADIUS24_DIAMETER25_PASS
KLEIN_QUOTIENT_56_84_GIRTH7_DIAMETER6_ARC_TRANSITIVE_PASS
THREE_PATH_SYMMETRY_ORBITS_OF_168_PASS
```

`verify_edges.py` independently realizes the graph using dot-product orthogonality of nonzero binary triples, tests all 203,490 possible eight-edge complements of paths, and verifies connectivity of each candidate. It computes backbites as path edge-set changes rather than reordering path tuples, reconstructs the suppressed and contracted graphs, and checks all-root distances and girth. Expected output:

```text
EDGE_COMPLEMENTS_203490_EXHAUSTIVE_504_HAMILTON_PATHS_PASS
INDEPENDENT_BACKBITE_EDGES_672_DEGREE2_336_DEGREE4_168_PASS
QUOTIENT_56_CUBIC_GIRTH7_DIAMETER6_PASS
```

The classification of the 56-vertex arc-transitive nonbipartite cubic quotient as Klein graph F056B uses the published Foster census and its uniqueness classification. The verification establishes the hypotheses of that identification without importing the classification itself. No assertion of random-walk mixing time or of a result for arbitrary graphs is made. The displayed outputs were obtained from the packaged scripts before this review.
