---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For fixed a,b>=2, summing opposite-class isolation-indicator covariances yields ab[h_m((a-1)(b-1))-h_m((a-1)b)h_m(a(b-1))], where h_m(s)=C(s,m)/C(ab,m). Exact ratio factorization has factors 1-t/((R-t)(C-t)); the t=1 factor proves negativity for 2<=m<=J, while J<m<=min(R,C) has zero joint and positive marginals and m>min(R,C) has a vanishing marginal. Thus the strict sign interval is precisely 2<=m<=ab-max(a,b); the other values vanish. Bernoulli covariance is ab*p*(1-p)^(a+b-1)>0, and with-replacement endpoints make X and Y independent. Expanding the log product for a~alpha*n,b~beta*n,m~gamma*n gives fixed-edge limit -gamma^2*exp(-gamma*(1/alpha+1/beta))/(2*alpha*beta), and Bernoulli covariance/n tends to gamma*exp(-gamma*(1/alpha+1/beta)). Independent exact edge-subset enumeration checked all m for three small rectangles; finite checks do not prove the general or limit formulas.

## originality

PASS

Best-of-knowledge PASS, qualified: exact all-m fixed-distinct sign boundary and sparse constant appear beyond inspected binomial and replacement sources; the Bernoulli and replacement special cases are not claimed as historically new.

## value

PASS

Cross-class isolate covariance is an intrinsic bipartite random-network observable. Equal expected edge counts across standard sampling ensembles yield opposite covariance signs and different sparse scaling, quantified exactly rather than by arbitrary finite data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
