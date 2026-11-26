---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independent marking leaves the unmarked arrival-epoch queue stationary under the two-tag conditioning. With u=1-p, a=1/(1+rho p), d=1/(1+rho), b=1-d, the first tag has an Erlang(q+1,mu) sojourn given Q=q. If the gap to the known susceptible second tag is T, the later-mark avoidance factor is exp(-lambda p (D-T)_+); integrating its exponential first-arrival law gives (exp(-lambda p D)-p exp(-lambda D))/(1-p). Summing with the geometric Q law and u^Q yields the first marginal. At the second tag, if Q1>0, the first tag is exactly the newest predecessor, so its corresponding mark factor is u^(Q1-1), rather than u^Q1; if Q1=0 the factor is one. Its geometric marginal, memorylessness, and Erlang transform give (1-rho)(a+rho a^2/(1-rho ua)), the same s as the first marginal. For joint escape, every pre-first customer contacts the first tag and every post-second arrival before the second departure contacts the second tag. There is no untagged intervening arrival, and any post-second contact of the first tag is included because FCFS orders their departures, even if their visits are disjoint. Thus j=a E[u^Q a^Q1]. Before the second arrival, the independent potential-completion clock gives P(G=g)=b d^g and Q1=max(Q+1-G,0); summing the truncated geometric law gives E[u^Q z^Q1]=(1-rho)(d+bz/(1-rho uz))/(1-rho ud). Substitution at a gives j=as. Then j-s^2>0 since a-s=2p rho^2/((1+p rho)(1-rho+2p rho)); dividing by s(1-s) gives the correlation. The variance, ordered cells, and fixed-p heavy-traffic limit follow without boundary conditioning on null events. The source applies only to adjacent arrivals in the full stream, zero exposure threshold and no onward transmission. Inspected the frozen script and recorded 840 rational checks and three simulation comparisons, without executing them; those checks do not supply the stationary-law or contact-union arguments.

## originality

PASS

Pass for the exact two-tag, two-mark-conditioned joint law and dependence, not the original queue model, overlap calculus or one-tag escape probabilities. No equivalent statement or direct implication of that same paired result was found in the inspected primary and indexed material. This is a bounded comparison, not a priority guarantee.

## value

PASS

The adjacent pair is the first nontrivial dependence observable beyond a one-tag marginal in this stationary FIFO model. The joint calculation quantifies the exact error of an independence assumption for pair-count variance and shows that the rare-escape clustering does not vanish in heavy traffic. These are well-defined properties of the mathematical zero-threshold marked queue, not claims for longer lags or more general transmission mechanisms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
