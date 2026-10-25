---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The exact selected-coordinate recurrence u[k+1]=u[k]-alpha*Bernoulli(p)*u[k-1] is faithful to the stated additive, one-commit-old model; dependence across coordinates is irrelevant because E||e||^2 splits. Independently expanded the two 2x2 Bernoulli maps with SymPy: L(W)=W-d E11 and L^2(W)=W-d[[2,1],[1,1]], W=[[1,t],[t,1]], t=1/(1+alpha p), d=alpha p(2/(1+alpha p)-alpha). The latter decrement matrix is positive definite; positive-map iteration proves geometric mean-square decay for d>0, an invariant covariance at equality, and exponential augmented error for d<0. Its two rank-one deterministic starts imply an actual bad deterministic initial state. The global iff condition alpha+alpha^2 max_i p_i<2, strict minimum m>alpha^2/(2-alpha) for alpha<2, and the weaker mean-root criterion 0<alpha*p_i<1 follow. Independently checked 5/4 equal-collision vectors have squared collision 3/8 but opposing thresholds; finite checks do not replace the all-p proof.

## originality

PASS

Exact finite-dimensional mean-square stability of a one-step-delayed Bernoulli linear iteration is a specialization of general jump-system covariance theory. Its explicit scalar threshold, boundary witnesses, and row-diversity/equal-collision comparison were not found as stated mathematical consequences in the materially inspected Coleman treatment or ranked research records. We credit the general lifted spectral test and do not assert novelty of the method.

## value

PASS

A sharp, motivated concurrency surrogate isolates stale-self row collisions without row coherence, gives an exact minimum-diversity phase diagram and demonstrates that equal successive-row collision probabilities can mask opposite mean-square behavior. It also exposes a meaningful first-moment/MSE gap. The theorem is limited to iid sampling of an orthogonal identity system, not hardware scheduling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
