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

`verify.py` reconstructs the stated coordinate graph and verifies that it has 24 vertices, 36 edges, degree 3 at every vertex, and graph diameter 6. It then reconstructs the Rips clique complexes needed at scales 2, 3, and 4.

For scale 2, the verified acyclic matching has one critical 0-cell and nine critical 2-cells. For scale 3, it has one critical 0-cell and one critical 2-cell. At scale 4 the verifier enumerates 17,372 nonempty simplices and 93,480 Hasse covers, checks all 8,682 matched pairs and global acyclicity, and obtains critical counts 1, 5, 2 in dimensions 0, 4, 5. The signed integral Morse boundary from the two critical 5-cells to the five critical 4-cells is the zero matrix.

For scale 5, the verifier checks that the only missing edges are the twelve pairs of opposite coordinate vertices, so the clique complex is the boundary of the 12-dimensional cross-polytope. The graph diameter check gives contractibility at scale 6. The replay output ends with `VERIFY_OK`.

The computation proves only the graph-metric filtration described in the result; it does not verify Euclidean-metric or equivariant variants.
