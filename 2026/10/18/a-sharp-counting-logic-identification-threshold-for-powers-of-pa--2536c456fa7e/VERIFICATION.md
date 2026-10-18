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

# Reproducibility and proof boundaries

The self-contained theorem and all cases are proved in RESULT.md. Execute `python3 verify.py` and `python3 verify_alt.py` in the same directory. The expected messages are `VERIFY_OK` and `ALT_VERIFY_OK`. Both scripts use Python 3 standard library only. One uses adjacency sets and linked signature refinement; the other separately constructs adjacency matrices and computes synchronized refinement classes.

The finite corroboration ranges are respectively \(1\leq k\leq24,\ 1\leq n\leq84\) and \(1\leq k\leq17,\ 1\leq n\leq74\). They establish no all-size enumeration and must not be mistaken for exhaustive proof beyond these bounds. The all-parameter proof uses the three low-order degree cells or, in the negative range, the stable two-vertex cells with matching-switch obstruction. Nonisomorphism is witnessed by an exact invariant: the number of triangles with one vertex from each of three intrinsic stable colour classes changes from two to zero.

Independent mathematical review: not performed.
