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

For fixed q>=3 and d coupon types, independent parallel uniform draws at synchronized size k have all-new probability (1-k/d)^q, all-old probability (k/d)^q; deleting geometric all-idle rounds yields survival a_q(u)=(1-u)^q/(1-u^q) and exact joint first-unequal round law with j laggards S(k-1)*binom(q,j)u^j(1-u)^(q-j)/(1-u^q). For k~x sqrt(d), log S(k-1)= -q x²/2+d^(-1/2)(q x/2-q x³/6)+ O_q((1+x^4)/d), uniformly on the Gaussian localization window. Mixed-hazard expansion gives local correction H=x/2-q x³/6 and Rayleigh density qx exp(-q x²/2), Gaussian tails justify summation. Gaussian moments give mean correction -1/(3q) (Euler-Maclaurin zero boundary) and two-laggard probability (q-1)/2 sqrt(pi/(2q)) d^(-1/2), higher laggards O(d^-1). For q=2 the pre-existing exact binomial product gives symmetric-bridge maximum and exact moments; no originality attached to old tie-break law. Independently checked 32 exact rational finite-stage models for d=2..9,q=2..5, and independently summed q=3,d=100000 to mean 228.712713 and P(J=2)=0.002287127; errors agree with the stated asymptotics. Finite checks are not the uniform asymptotic proof. Evidence: Source text in assigned RESULT.md §§Finding, Assumptions and scope, Proof, Verification, Relationship to prior work; repository Git tree ddb1d832a9eaf5f9f6666adf480119e83ccd972c

## originality

PASS

Best-of-knowledge novelty of the exact final quantitative claim, with classical proof mechanisms and expressly credited subcases excluded. Genuine broad/theorem and full-text comparison risks retained; inaccessible full texts alone do not dictate failure.

## value

PASS

The natural first loss of exact distinct-count synchronization in parallel coupon collection has a sharply quantified second-order departure index and probability of *two simultaneous laggards*, an event absent in two-player contests. The constant -1/(3q) and d^(-1/2) rare-event coefficient distinguish the general fixed-multiple-collector regime from the known two-player cancellation and terminal-completion statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
