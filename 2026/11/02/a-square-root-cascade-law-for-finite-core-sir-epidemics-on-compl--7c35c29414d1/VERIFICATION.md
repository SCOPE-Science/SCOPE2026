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

Sample independent infectious durations and directed exponential first-contact delays, opening a directed edge when contact precedes recovery; infected vertices equal graph reachability. For fixed core b and lambda_n→0,n lambda_n→∞, n lambda_n²→xi∈[0,∞], shared periphery paths yield conditionally independent core-arc counts Poisson(xi mu R_i), because simultaneous two-arc contributions vanish using only E[J]<∞. Core reachability converges; binomial uniform-over-2^b-core-subsets concentration proves X_n/(n lambda_n)⇒sum_{i∈C}R_i. For xi=∞ each core arc occurs whp; xi=0 none. b=2 with Exp(1) periods gives core2 prob c²/(1+c²) and Y=c(R1+B R2). Tagged-periphery argument yields exact finite binomial formulas; independently implemented rational finite-state CTMC recurrence matches these formulas for n=1..4 and lambda=1/3,1/2,2.

## originality

PASS

The epidemic-percolation directed graph representation is fully prior (Kenah and Robins). The asymptotic sparse two-step core-to-core Poisson directed cascade and joint peripheral scaling with fixed b are not the same statement as large within-community or persistent SIS results. Qualified PASS with historical multitype asymptotic coverage still possible.

## value

PASS

Sharp n^{-1/2} cross-core cascade scale and explicit mixture outbreak law are natural informative finite-core SIR limits, including non-exponential infectious times and exact finite two-core formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
