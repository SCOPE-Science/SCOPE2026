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

The independent scripts `verify_types.cpp` and `verify_types.py` use the exact rank-type recursion. The C++ calculation fixes the first tuple element by a cyclic automorphism and enumerates all remaining choices. The independent Python calculation uses no group-action reduction and enumerates all ordered triples and their fourth-vertex extensions. `reproduce.sh` checks that the two results agree for every crown size from 2 through 15, that there are six pairwise distinct root classes among sizes 2 through 7, and that sizes 7 through 15 have a common type.

The finite output is reproduced in `verification_output.txt`. The complete recurrence, including repeated vertices and all atomic pair-comparison relations, is implemented in both files. The separate infinite-tail proof is mathematical: a color-preserving clockwise-gap strategy with thresholds 2, 5, 11, 23 after the first of four moves. Therefore computation is used only for the finite boundary \(2\le n\le12\).

The programs do not establish broader families or independent validation. Exhaustive bibliographic priority has not been established.
