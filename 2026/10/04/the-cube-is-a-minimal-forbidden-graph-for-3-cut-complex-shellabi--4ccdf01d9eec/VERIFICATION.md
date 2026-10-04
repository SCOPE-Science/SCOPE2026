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
# Verification

The bundled `verify_cube_cut.py` is a standard-library replay from the cube adjacency relation. It reconstructs all disconnected three-sets, all cut-complex faces, and all cover relations rather than trusting stored counts.

It verifies 32 facets, 188 nonempty faces, face vector \( (8,28,56,64,32) \), and 640 Hasse covers. It constructs 91 discrete-Morse pairs and proves acyclicity by topologically sorting the completely oriented Hasse diagram. The only critical cells are one in dimension \(0\), one in dimension \(3\), and four in dimension \(4\).

It separately builds oriented simplicial boundary matrices and performs exact rational Gaussian elimination, obtaining boundary ranks \( (7,21,35,28) \) and Betti vector \( (1,0,0,1,4) \). These checks support the zero-degree attaching-map argument used in the proof.

For minimality, it verifies that deleting any at most two cube vertices leaves a connected graph, and it enumerates all 255 proper vertex subsets. For every resulting induced subgraph it searches for a shelling of the \(3\)-cut complex and then independently checks the returned order against the facet-intersection definition of shelling. Of these, 162 induced subgraphs have between four and seven vertices; smaller cases are also checked under the standard void/empty-face conventions.

The replay is finite and exhaustive for \(Q_3\). It does not certify any statement about higher hypercubes. A successful run ends with `VERIFY_OK`.
