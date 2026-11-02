---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For strictly positive a,b,c,d, the lifted history-state Markov chain is primitive with stationary pair law (u,1,1,v)/(u+v+2), u=(1−b)/a, v=c/(1−d). The strictly positive hitting recurrences for targets y=0,1 are solvable by one-step first-step equations; the eight solutions yield exact differences K00−K01=(a−b)²(1+c−d)/Δ and K11−K10=(c−d)²(1+a−b)/Δ with Δ=(1−b)(1−d)+ac+2a(1−d)>0. Thus four-history constancy forces a=b and c=d; in the converse the first-order random-target identity gives K=1+1/(a+1−c). The proof distinguishes positive return time from time-zero hits and four-history targets from one-symbol targets. Independently formed the four-state transition matrix and solved exact rational stationary and absorbing hitting linear systems in 21 sampled kernels; both squared gaps agreed. Only proof, not sample search, establishes all positive parameters.

## originality

PASS

Best-of-knowledge: primary same-object comparisons, alias/implication checks and published finding searches distinguish the assessed exact statement from covered components. Historical priority uncertainty is retained; failed search is not novelty proof.

## value

PASS

The exact nonnegative quadratic defect laws answer a natural full-history version of the stationary-target hitting-time constancy question, identify precisely when order-two memory remains detectable, and quantify the deviation. This is a complete small-alphabet structural classification rather than merely a numeric hitting-time example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
