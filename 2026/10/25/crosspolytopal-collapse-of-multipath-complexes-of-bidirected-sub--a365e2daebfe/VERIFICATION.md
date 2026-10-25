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
# Verification record

## Reproducible computation
Run `python3 verify.py` with Python 3 and its standard library. The code independently builds each bidirected, once-subdivided forest and exhaustively checks all multipath arc subsets, then rechecks the proposed domination removals and verifies the residual cross-polytope factorization. Recorded output:

`PASS forests 339 total_original_faces 226133 domination_face_checks 210764 largest_complex_faces 8119 total_graph_edges_across_tests 1049`

The listed instances comprise all labeled forests on two through five original vertices plus five selected six-vertex branching forests. The complete runtime algorithm and test construction are in the accompanying `verify.py`.

## Proof boundary
For all finite forests, the theorem relies on the induction in `RESULT.md`, not on finite enumeration. The local domination argument uses the original leaf and the inserted degree-two midpoint. Every deletion is an elementary simplicial collapse, preserving integral and simple homotopy type. The reversal sign comes from the absence of invariant nonempty faces and the Lefschetz trace formula. No higher-dimensional torsion conclusion is inferred from finite-field tests. The proof does not cover nonforests or arbitrary edge subdivisions.

## Review boundary
The scientific assessment is same-model only. An independent audit has not been performed, and literature indexing cannot rule out every independently discovered equivalent theorem.
