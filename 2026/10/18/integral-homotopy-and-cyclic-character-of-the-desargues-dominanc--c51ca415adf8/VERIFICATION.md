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
# Verification of exact finite proof

Run `python3 verify_desargues.py` (Python 3.9+, no dependencies). This standalone code constructs the graph, all closed-neighborhood masks and all \(2^{20}\) candidate subsets, independently cross-checks the Desargues graph against the bipartite double cover of the Petersen graph, and verifies its complete face vector.

The checker constructs all 217103 deterministic vertex-toggle pairs and independently performs a topological sort of the entire oriented Hasse graph, processing all 434220 faces and 3663080 covering incidences; the remaining critical-cell vector is precisely one zero-cell and thirteen nine-cells. This is a genuine full acyclicity test. The code enumerates fixed simplices for all ten rotations, signs their induced vertex permutations and verifies the exact rational character \((13,-1,3,-1,3,-11,3,-1,3,-1)\).

Expected final stdout line: `ALL ASSERTIONS PASSED`. Successful execution verifies the fully specified finite combinatorial proof steps, not mathematical originality, human audit, generalization to other graphs, or an integral representation decomposition.
