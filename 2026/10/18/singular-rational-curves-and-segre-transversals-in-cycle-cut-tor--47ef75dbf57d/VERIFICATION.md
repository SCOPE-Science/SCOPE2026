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
# Reproducible mathematical checks

Run `python3 parity_cut_toric_verify.py` from the directory containing that standalone script. It uses only the Python 3 standard library. A successful run prints `VERIFY_OK` at the end and reports, for each \(n=4,5,6,7\), every face dimension count through a fixed vertex, the global number of edges, the local Segre-matrix shape, and its multiplicity.

Observed successful output on the packaged script:

```
n=4 vertices=8 edges=24 zero_vertex_faces=28 face_dim_counts=[(0, 1), (1, 6), (2, 12), (3, 8), (4, 1)] edge_local=rank_one_2_by_2 multiplicity=2 OK
n=5 vertices=16 edges=80 zero_vertex_faces=82 face_dim_counts=[(0, 1), (1, 10), (2, 30), (3, 30), (4, 10), (5, 1)] edge_local=rank_one_2_by_3 multiplicity=3 OK
n=6 vertices=32 edges=240 zero_vertex_faces=214 face_dim_counts=[(0, 1), (1, 15), (2, 60), (3, 80), (4, 45), (5, 12), (6, 1)] edge_local=rank_one_2_by_4 multiplicity=4 OK
n=7 vertices=64 edges=672 zero_vertex_faces=520 face_dim_counts=[(0, 1), (1, 21), (2, 105), (3, 175), (4, 140), (5, 63), (6, 14), (7, 1)] edge_local=rank_one_2_by_5 multiplicity=5 OK
VERIFY_OK
```

The checker independently generates even-parity vertices, intersects all incident facet-vertex sets, determines affine face dimensions by rational Gaussian elimination, tests the primitive integral ray spans with maximal minors in the *dual even-sum lattice*, and checks the edge-ray circuit and low-degree Segre semigroup Hilbert function. These are exhaustive finite checks only for the stated four dimensions. The universal theorem rests on the face-classification and monoid-isomorphism proofs in `RESULT.md`. No external or independent mathematical certification is asserted.
