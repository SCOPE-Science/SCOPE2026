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

# Reproducible exact-chain verification

Execute `python3 check_columns.py` and `python3 check_rows.py` in a directory containing both files. Each performs a complete, deterministic calculation using only the Python standard library, asserts the exact expected data, and prints `PASS`.

The two implementations enumerate all faces of both neighborhood complexes, rather than a bounded sample of an infinite family. The first builds simplex tuples from each complementary neighborhood, and performs column-echelon elimination using the most-significant pivot. The second traverses all nonempty sixteen-vertex masks and eliminates the transpose coboundary rows with the least-significant pivot. It uses an isomorphic alternate Shrikhande Cayley presentation; the coordinate-change matrix has determinant one modulo four. The independent constructions also check the strongly regular parameters directly.

Expected face vectors in degrees zero through eight are \((16,120,528,1292,1728,1296,576,144,16)\) and \((16,120,560,1332,1728,1296,576,144,16)\) for Shrikhande and rook respectively. Augmented boundary ranks are \((1,15,105,423,869,848,448,128,16)\) and \((1,15,105,453,879,848,448,128,16)\). For each degree, subtract the incoming and outgoing boundary ranks from the face count to obtain the complete reduced binary Betti vector.

The computation verifies finite-chain ranks over \(\mathbb F_2\) only. It neither establishes a homotopy equivalence nor excludes integral torsion or prior publication elsewhere.
