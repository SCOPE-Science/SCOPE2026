---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With PSD corrections the quadratic constraints imply the affine constraints; zero corrections at the unique affine optimum leave it feasible, so the shared objective has the same unique optimum on the nested set. For the indefinite model, y(1-x)≤0 includes the upper half-plane on the side x>1 and the lower half-plane on x<1, with x=1 unconstrained. Projection of (r,m) to y≤0 gives (r,0), a zero of the correction −xy, whereas (r,m) itself is strictly feasible in the quadratic model for r>1,m>0. The Euclidean distance between solutions is m and the objective gap is m²/2. At (r,0) the active normal is (0,1−r), so cancelling the objective gradient (0,−m) requires a negative multiplier; increasing y slightly is feasible and strictly improves the objective. The constant constraint Hessian has norm one and the base gradient is nonzero. The source's positive normalization floor and zero first-step smoothing leave the indicator at zero even as m grows, selecting SQP at that comparison.

## originality

PASS

The supported distinctive result is the indefinite, fixed-Hessian falsification of the zero-probe gap and stationarity certificate in the specified shared-objective models. The PSD nesting observation and the indicator are antecedent or elementary context, not separate originality claims.

## value

PASS

This is a motivated failure mode for a published adaptive diagnostic, not just a general caution about indefinite constraints: exact zero can coexist with unbounded error and failure even of model first-order stationarity while the Hessian norm stays fixed. The PSD case explains which structural protection is lost. Model comparisons, solver guarantees and algorithm convergence are correctly distinguished.

The dated certificate retains the supplied scientific assessment, sources and limitations.
