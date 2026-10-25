---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Conditioning on pi(i)=j in a uniform S_n gives E[I|pi(i)=j]-E[I]=-2(i-(n+1)/2)(j-(n+1)/2)/(n-1). The covariance against H_{n,t}=sum_i 1{|pi(i)-i|>=t} reduces to a diagonal-distance polynomial sum. Independently symbolic subtraction confirms c(n,t+1)-c(n,t)=(t-n)(2t^2+2nt-n^2+1)/[3n(n-1)]; exact summation of c(n,t) gives the previously published total-footrule covariance (n+1)(n^2+1)/30. Exhaustive independent rational permutation enumeration n=2,...,7 reproduced EVERY threshold (sum 21 cases); this is corroboration only. Each denominator positive and 2nt-n+t^2-t+1=n(2t-1)+t(t-1)+1>0; layer-cake increments prove strict nonconstant nondecreasing f positivity. The unique root alpha=(sqrt(3n^2-2)-n)/2 of the first-difference quadratic proves the exact threshold maximizers, including integer tie and n=2 boundary.

## originality

PASS

The new parameter is the full family of individual long-displacement indicator counts H_{n,t}; the joint inversion/total-footrule covariance has long been computed (Ekhad–Zeilberger 2021), but aggregating all threshold covariances loses the scale profile and cannot logically recover these terms. Jiang 2011 concerns asymptotic rank-metric relations and Dimitrov–Khare supplies a general combinatorial moment technology without an evaluated finite formula for this threshold family in the inspected passages. Original Ekhad–Zeilberger §7 full PDF explicitly gives (n+1)(n²+1)/30 but only for SUM of |displacements|. Direct conditioning supplies a new exact all-threshold law and its maximizing scale; possible general unindexed moment identities remain a residual risk.

## value

PASS

Counting displacements beyond t probes location-dependent rank disagreement at a resolvable scale, unlike classical summed Spearman footrule. Exact strictly positive covariance for ALL nonconstant monotone displacement penalties is an informative robust cone-wide dependency law, while a maximizing macroscopic threshold identifies the strongest scale. These facts are not a trivial rephrasing of the known total-footrule covariance. No stochastic positive association or correlation-maximization is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
