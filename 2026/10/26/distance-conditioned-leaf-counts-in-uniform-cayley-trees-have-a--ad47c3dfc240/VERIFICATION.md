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

The analytic proof uses the matrix-tree theorem and exact conditional extension counts; it applies for every integer \(n\ge4\). To replay the finite checks, run `python verify_cayley_leaf_distance.py` with Python 3 in the folder containing this document and the verifier.

The checker exhaustively enumerates \(n^{n-2}\) Prüfer codes for each \(2\le n\le8\) (the largest has 262,144 trees), checks all possible marked distances and leaf positions, then tests exact rational forward differences and maximizers for \(4\le n\le150\), exact tie positions, and sample large-size limit values. It produces `PASS: 44755 deterministic checks; exhaustive Cayley trees n=2,...,8`. These tests are independent of the counting proof but do not certify an infinite statement. The bound in the proof supplies the uniform Taylor remainder; the limiting scale is not inferred solely from numerical examples.

Self-review: passed. Independent audit: not yet performed. Residual originality risk concerns implicit consequences of earlier general forest-enumeration identities.
