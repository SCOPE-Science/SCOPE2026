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

# Reproducible checks

The package includes `verify.py` and `verification_output.txt`. Run `python verify.py` in a standard Python 3 environment. It uses only the standard library; no additional input files or downloads are required.

The script constructs all labeled Prüfer trees for orders two through six and additional path, star, cycle, theta and barbell instances, for 1,467 cases. For each, it independently enumerates the exact Rips faces from pairwise squared-line-graph adjacency and the exact Čech faces from closed graph-radius-one ball supports. It asserts literal face-set equality, reconstructs every generator for every outside face, and checks a complete matching partitions those faces. It then deletes the pairs in the prescribed order, checking at every step that the lower face has exactly one surviving immediate coface, and confirms the resulting complex is the scale-one flag complex. Euler characteristics of the remainder are checked independently. The girth-six boundary test produces exactly two Rips-only triangles and verifies the octahedron-boundary face vector \((6,12,8)\).

Output records the case breakdown and ends with `VERIFY_OK`. These are finite tests, not a proof for graphs of unbounded size. The full mathematical justification and quantifiers appear in RESULT.md.
