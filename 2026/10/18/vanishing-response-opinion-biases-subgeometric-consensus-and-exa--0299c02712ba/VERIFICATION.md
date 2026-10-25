---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Writing q_ij(s)=beta_ij(s)/s gives convex stochastic update with self-weight ≥1-theta>0. Old extrema remain bounds. Let b(r)=max_edge,max_|s|≤r |beta(s)|≤theta*r; then D_(t+1)≥D_t-2b(D_t)≥(1-2theta)D_t>0. Strong connectivity propagates strict drop from an old max (and rise from old min) in at most n-1 steps; compactness and continuity force limiting diameter 0. Flatness b(D_t)/D_t→0 proves adjacent diameter ratio→1 and Cesaro logarithmic mean gives subgeometric convergence. For d_(t+1)=d_t-2exp(-d_t^-alpha), letting y=d^-alpha gives Delta y=2alpha y^(1+1/alpha)exp(-y)(1+o(1)); H(y)=exp(y)/y^(1+1/alpha) has Delta H→2alpha, so H(y_t)~2alpha t, yielding three-term expansion and overshoot-controlled accuracy time. For analytic beta(s)=a s^m+O(s^(m+2)), reciprocal-power increments give m=1 geometric, m odd>=3 t^-1/(m-1). Examined exact-rational finite graph and scalar source checks, not treating finite runs as proofs.

## originality

PASS

The exact flat bias alpha=1 and qualitative slow convergence were ALREADY simulated by Alvim et al 2024; their consensus theorem covers convergence but not uniform ratio→1 for arbitrary heterogeneous flat biases or the three-term inverse-logarithmic law and accuracy time. The quantitative asymptotics may follow abstract scalar slowly varying iteration methods, but full model-specific theorem/comparison is not printed there.

## value

PASS

The result quantifies a real slow-convergence phenomenon in an explicit published consensus example and shows a structural obstruction to ANY uniform geometric decay under flat receptiveness on an entire class of finite strongly connected graphs, with sharp accuracy-cost scaling and analytic-versus-flat transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
