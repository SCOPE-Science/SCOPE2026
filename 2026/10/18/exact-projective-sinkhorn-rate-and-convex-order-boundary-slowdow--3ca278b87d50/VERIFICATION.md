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

# Verification of discrete martingale Sinkhorn rate

The analytical proof in `RESULT.md` establishes the universal claim. Its critical steps are the exact KL row projection, reduction to a single endpoint-total parameter, full-cycle terminal rescaling, derivative bounds, conditional relative-entropy Hessian, and the convex-order boundary expansion.

`VERIFY.py` independently computes conditional exponential tilts by numerical root finding, forms each source-martingale row, and applies terminal column rescaling directly, then compares the resulting projective recurrence with the closed formulas. It probes arbitrary nonsymmetric positive initial terminal weights, symmetric source/terminal masses, target parameters on both sides of the starting state, the strict monotonicity/no-overshoot law, analytical local multiplier, and relative-entropy ratios. Its seeded run passed 15,316 individual finite checks. Run `python VERIFY.py` with Python's standard library.

Finite tests are not exhaustive and do not establish the universal results. The local asymptotic expansion is only asserted for fixed \(0<a<T<1\); the boundary coefficient is derived holding \(a\in(0,1)\) fixed. No external independent scientific audit or certification is asserted.
