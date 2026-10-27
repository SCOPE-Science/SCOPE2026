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
# Computational and analytic checks

Run `python3 verify.py` using Python 3 standard library. The code independently generates all monotone unit-step maps using initial values and adjacent increments, filters for idempotency via composition, identifies their image intervals, and exhaustively tests pairwise commutation against interval intersection. It verifies all point-star families are commuting and cannot be enlarged while retaining commutativity, by their singleton idempotents. For ordered tuples it compares direct composition and common-product image ranks against the stated finite-difference convolution.

The parameter grid comprises \(1\le n\le9\) with \(m\in\{1,2\}\), \(1\le n\le7\) with \(m=3\), and \(1\le n\le5\) with \(m=4\): 30 configurations and 102,917 ordered candidate tuples. The successful exit line is `ALL_CONTRACTION_IDEMPOTENT_TUPLE_CHECKS_PASSED 30 102917`.

The mathematical proof supplies the unbounded-parameter justification. It uses a unique normal form for idempotent contractions, an explicit clipping-composition criterion, finite-interval Helly, endpoint-tuple counting, a rational generating function, and a fixed-tuple-length singularity/Riemann-sum asymptotic argument. Exhaustive finite tests alone do not prove any infinite theorem. No independent mathematical audit has been performed.
