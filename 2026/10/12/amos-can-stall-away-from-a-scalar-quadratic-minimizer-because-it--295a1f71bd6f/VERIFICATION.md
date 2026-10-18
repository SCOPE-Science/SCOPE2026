---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

At beta=0 and x>0 on scalar f(x)=lambda*x²/2, bias-corrected second moment is exactly g², normalized gradient is 1 and gamma_t=xi² c_t. The source-form positive branch gives b_(t+1)=b_t+xi² c_t(1+b_t), x_(t+1)=(1-r_t)x_t-s_t with r=xi² c_t d_t/2 and s=xi*eta*d_t. With p=sqrt(xi)/4 and b→∞, sqrt(b_(t+1))-sqrt(b_t)→xi^(7/4); by Cesàro sqrt(b_t)/t→xi^(7/4) and b/t²→xi^(7/2). Therefore r~4/(xi^4 sqrt(eta)t³), s~4 sqrt(eta)/(xi³ t²), both summable; r≤1/2 implies product P_inf>0 and finite X_star=Σs_k/P_(k+1). Variation of constants yields x_t→P_inf(x0-X_star)>0 for every x0>X_star, with branch positivity proven from partial sums. x0=X_star tends to zero; smaller positive x0 leaves positive branch. Independent recurrence replay for xi=eta=1 through 100000 steps gave b/t²≈0.999873, P≈0.1723603, partial X≈16.4041, x0=20 yields x≈0.6198. No convergence claim for default beta=.999.

## originality

PASS

The original Tian–Parikh Amos Algorithm 1 gives coupled update, c_t and d_t heuristics, but does not establish this exact deterministic strongly-convex nonstationary limit or state-dependent positive-branch threshold; it leaves convergence analysis open. General Adam, AdamW, AdOGD/RAdam step counterexamples returned by Resultary concern different optimizers and update laws, hence cannot imply a source-form Amos theorem. Best-of-knowledge no implication-equivalent Amos claim found.

## value

PASS

A concrete nonstationary limit on the simplest strongly convex objective is an algorithmic failure boundary for the exact published adaptive decay mechanism, particularly the independently generated t^-2 step mass. The result is not generic summable-step folklore because the coupled Amos buffer is analyzed explicitly, with a sharp x0 threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
