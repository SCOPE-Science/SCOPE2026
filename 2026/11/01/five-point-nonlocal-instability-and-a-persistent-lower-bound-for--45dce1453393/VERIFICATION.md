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
The accompanying `verify_convex5.py` uses only the Python standard library and rational Gaussian elimination. It enumerates all faces at sample sizes two through five, checks every orthogonal projector and row norm, verifies the strict primal/dual KKT witness, checks larger-dimensional face embedding, and independently tests the tridiagonal continuant inverses. It reports 420 rational assertions passed.

The proof separately establishes that every face is realized on a full-dimensional open input region and that all pieces control the global Lipschitz constant; the arithmetic checks alone cannot establish these global statements. The infinite alternating-curvature lower bound is obtained analytically from a limiting Green kernel and geometric domination, not by finite extrapolation. No independent validation has been performed.
