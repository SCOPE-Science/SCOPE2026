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

The nested-event representation X_(1)=1_{K=0}, X_(2)=1_{K<=1}, K~Bin(n,q), yields R_n=a(1-b)/[b(1-a)] exactly, with a=(1-q)^n and b=a+nq(1-q)^(n-1). Both fixed-n boundary values vanish. Under nq->c>0 the limiting squared correlation is F(c)=(exp(c)-1-c)/[(1+c)(exp(c)-1)]. The uniform escape bounds R<=1/(1+nq) for nq->infinity and R<=c/(2-c) for c=nq->0 exclude maximizing sequences at either boundary. Differentiation gives F' sign equal to 1+c+c^2-exp(c), whose unique positive zero is established from the change of sign of its second derivative; compactness and comparison at q=c*/n force every optimizer to that limit. Independent differentiation and finite maximization n=2,3,5,10,100,1000 corroborate localization, not an infinite proof.

## originality

PASS

The fully inspected package explicitly isolates the new n->infinity optimization. The 2021 discrete-parent article introduces the general finite-n setup and reports finite n<=9 numerical values; the 2022 two-draw paper and published Resultary three-point records do not imply the optimized two-atom growing-n Poisson threshold, on available statements. Best-of-knowledge only; full text of the 2021 article was not independently recoverable in this run.

## value

PASS

A sharp asymptotic extremal statistic and universal rare-event scale for adjacent binary order statistics, including an explicit transcendental constant, resolve a natural large-sample optimization not delivered by a finite-sample table. The distinction between Pearson and nonlinear maximal correlation is substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
