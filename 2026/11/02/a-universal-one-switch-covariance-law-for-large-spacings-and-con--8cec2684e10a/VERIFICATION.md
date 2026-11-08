---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For m>=2 uniform X~Dirichlet(1,...,1), conditioning on X1>t yields the exact affine simplex slice te1+(1-t)Y and P(X1>t)=(1-t)^(m-1). Thus Cov(K_t,F_f)=m(1-t)^(m-1)(Phi_f(t)-Phi_f(0)). For C1 strictly convex f, Phi is strictly convex, Phi'(0)=-m Cov(Y1,f'(Y1))<0 because Y1 nondegenerate and f' increasing, and strict chord inequality gives Phi(1)>Phi(0). Strict convexity enforces exactly one positive crossing in (0,1) and negative/positive signs on either side. For f(x)=x², direct Dirichlet moments give Cov(K_t,Q)=(m-1)/(m+1)*t*(1-t)^(m-1)*((m+2)t-2), hence t*=2/(m+2). Pairwise exceedance probabilities yield Var(K_t)=mp(1-p)+m(m-1)(q-p²); fourth-order Dirichlet moments yield Var(Q)=4(m-1)/((m+1)^2(m+2)(m+3)). At t=c/m, c fixed, these yield Corr→c(c-2)/(2sqrt(e^c-1-c²)). Independently computed conditional quadratic moments and exact covariance for 156 rational (m,t) cases. The c limit is correlation only, not independence at zero.

## originality

PASS

Earlier spacing literature determines exceedance-count marginal/asymptotic behavior and Greenwood statistic moments, whereas the asserted theorem gives exact finite-sample mixed covariance for all differentiable strictly convex separable costs with exactly one sign change. The closest 1988 primary text was only partially accessible; lawful OA/arXiv did not yield readable complete text and authorized institutional retrieval reported vpn_disconnected. That inaccessible plausible source is a material priority risk, not a proof of coverage or reason to fail the current best-of-knowledge comparison.

## value

PASS

The unique sign crossing of exceedance-count dependence with every strictly convex additive spacing cost is a natural dependence invariant in goodness-of-fit spacing tests. The explicit Greenwood switch and nontrivial fixed-scale correlation supply meaningful finite and asymptotic calibration boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
