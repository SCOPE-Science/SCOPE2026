---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

A successful origin attempt at u has density e^(-2u) du. Given its success, both half rays are conditionally independent with occupancy parameter q_t(u)=1-(1-u)e^(u-t) at sites +/-2. Normalized U-density is 2e^(-2u)/(1-e^(-2t)); integrating z_t(U)=(1-U)e^(U-t) and z_t(U)^2 gives 2t/(e^(2t)-1) and 2(t-t^2+t^3/3)/(e^(2t)-1). Covariance is exactly Var(q_t(U))>0 since q_t is strictly increasing on (0,t). Independent symbolic integration and positivity numerical samples agree. Infinite-volume local dependence follows factorial decreasing-priority path tail; t=1 gap table is mathematically implied by known pairs and NOT original.

## originality

PASS

Best-of-knowledge originality supported by comparisons of exact statements, same-object sources and published Resultary records; material limitations and possible unindexed equivalences explicitly retained. Equivalent discrete Page–Rényi parking/random-greedy independent-set formulations have same single and pair laws. The new interior-time triple conditional probability is a third-order joint statistic, not a function of pair marginals alone.

## value

PASS

A strict positive conditional dependence law at every nonterminal time reveals correlation induced solely by shared selection time even though conditional half-lines are independent. Exact three-location transient law extends known one/two-point statistics and has natural dynamics significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
