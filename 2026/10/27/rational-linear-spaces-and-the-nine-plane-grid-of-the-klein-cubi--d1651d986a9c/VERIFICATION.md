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

# Reproducibility
Run `python3 verify.py` from the extracted package using Python 3's standard library. This enumerates precisely all vector subspaces of dimensions 1, 2 and 3, checks the ordered-coefficient condition for containment in the cubic, and asserts the counts and plane/line incidences. It also performs a separate direct cubic evaluation over the four-element field on every displayed rational plane, without assuming the coefficients criterion for this second test.

Observed result: `VERIFY_OK: 39 F2-points, 75 F2-lines, 9 F2-planes; plane grid and incidences exact`.

This finite exhaustive computation is a certificate for the finite claims at issue, while the accompanying mathematical argument derives the same classification structurally. It neither certifies a complete census over algebraic closures nor constitutes independent expert review.
