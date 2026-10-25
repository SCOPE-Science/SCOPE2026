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

# Reproducible verification

Run `python3 check_coxeter.py` in a directory with the embedded checker; it requires only the Python standard library. The checker rebuilds the 28 three-subsets that are not Fano lines and their cubic disjointness graph, verifies every shortest-path distance shell, and exhaustively enumerates every simplex at the two nontrivial thresholds. Its radius-two check confirms 112 free codimension-one faces and actual elementary collapses to the original graph, hence survival of the degree-one persistence module across radius two. Its radius-three check verifies all 10,896 faces, 5,404 disjoint matched pairs, critical-cell distribution and the acyclicity of the full directed Hasse diagram (a topological sort visits every face). Finally, the all-pairs diameter test establishes the radius-four full simplex.

Expected successful output:
```
radius 2: 112 certified collapses onto original 28-vertex 42-edge graph
radius 3: 10896 faces, 5404 disjoint matched pairs,
          Hasse DAG verified, one critical vertex and 87 critical four-cells
radius 4: full simplex; integral wedge and persistence classification PASS
```

The conclusion from an acyclic matching to a homotopy-equivalent CW complex uses the finite discrete-Morse theorem. The checker makes no inference from partial enumeration, sampling, machine floating-point calculations, or numerical homology alone. The result covers precisely the indicated graph and real radius ranges; it does not provide independent external validation or rule out all unpublished equivalent work.
