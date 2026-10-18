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

# Reproduction of finite checks
Run `python3 check.py` from this package. The script enumerates every subset of the eight possible one-variable depth-one truth vectors, computes its true affine hull as a bit mask, verifies an independent partition by all affine existential tests, and counts the hull dimensions. It finds 96 distinct depth-two successor hulls and the sharp affine dimension 4. It computes the depth-one counts for one through three variables and directly checks 12,288 rooted instances across all directed graphs on three labelled worlds and all valuations of the one variable.

Expected final line: `AFFINE_DEPTH_VERIFY_OK`. The proof of the general finite-depth theorem appears in `RESULT.md`; finite enumeration only certifies the exhaustively bounded census and tests of the theorem on finite examples. No assertion of external or independent audit is made.
