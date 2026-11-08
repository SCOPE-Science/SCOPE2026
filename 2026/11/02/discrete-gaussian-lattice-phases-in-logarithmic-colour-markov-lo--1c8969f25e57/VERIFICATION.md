---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Summing each directed edge variable including loops in eight-weight two-predicate Markov logic network yields exact P(M_n=m) proportional to binom(n,m)c11^(m^2)c00^((n-m)^2)(c10*c01)^(m(n-m)). On boundary c10*c01=c00^2 and c11<c00 this becomes binom(n,m)exp(-a m^2), a>0. The Lambert saddle x=W(2an)/(2a) solves log(n/x)=2ax; Stirling local expansion at floor(x)+j yields exp(-a(j-theta)^2) with uniformly summable Gaussian tails from decreasing adjacent exact ratios, proving total-variation phase approximations and theta prefactor. Full phase subsequences follow x_{n+1}-x_n->0. Independently directly computed binomial distributions for n=200,1000,10000,100000 at a=.4,log2,1.5, checking decreasing TV and partition relative error, plus very large n x~95 asymptotic convergence; finite checks corroborate not prove limits. Colour reversal gives the dual boundary; claims do not extend off the exact critical surfaces.

## originality

PASS

Best-of-knowledge qualified originality: the exact published model/theorem comparisons below do not establish an earlier dominating theorem for the narrow stated new remainder. Related prior methods and components explicitly credited; uninspected specialized literature risks remain.

## value

PASS

Natural stochastic fluctuation refinement of a newly identified logarithmic minority regime: gives the order-one discrete-Gaussian law, all lattice phases, explicit theta oscillation and no single centered limit. These facts matter for inference about rare colours and exact partition asymptotics; coarse logarithmic concentration and standard Gaussian CLT cannot substitute for them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
