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

# Verification of the graph-prism fixed-space theorem

The exact proof is in RESULT.md. The critical independently checkable identity is that an independent set in a union of selected rungs uses at most one vertex in each rung and therefore corresponds bijectively to a subset of rung indices equipped with a proper two-coloring of its induced base graph. Maximizing selected rung count identifies the independent number with the largest induced-bipartite-subset cardinality. This proves the geometric fixed-space triangulation for every finite graph and threshold without extrapolating from computations.

The standalone script `verify_prism.py` is standard-library Python. It enumerates all rung-orbit subsets and directly recomputes induced independence numbers, rather than assuming the theorem's orbit criterion. It checks 73 (graph, threshold) instances spanning 20 bipartite base graph instances, plus the independent nonbipartite triangle boundary. It separately reconstructs all faces and computes reduced mod-two boundary ranks for two-row ladders of width two through six, at parameters two and three (ten cases). The observed command and output are:

```
python3 verify_prism.py
VERIFY_OK orbit_tests=73 bipartite_graph_instances=20 finite_homology_cases=10 nonbipartite_boundary=triangle
```

Finite checks do not independently establish an infinite-family theorem. Step 1 and Step 2 of RESULT.md establish the exact general correspondence, Step 3 derives the homotopy classification using standard skeleton properties and integral chains, and Step 4 invokes the published two-row grid ambient wedge theorem. The last step is a corollary of an externally stated homotopy result; it is not a fresh proof of that published result. No independent mathematical audit or external formal certification has been carried out.
