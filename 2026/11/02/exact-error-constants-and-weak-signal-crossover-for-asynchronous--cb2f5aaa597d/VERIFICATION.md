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

Before the first hub activation, each activated leaf displays its fixed bit, independently of the clock history. The signed neighbor margin for the hub's first declaration can only increase once leaves copy that declaration; a remaining tie is broken by the same private bit, so the hub is locked. All leaves eventually update. Conditional on hub time T, the number K of distinct observed leaves is binomial at parameter U=1-exp(-mu T); U has density rho(1-u)^(rho-1). Integrating gives the claimed beta-binomial weights, including uniform K for rho=1. Conditional erroneous consensus is a strict binomial left tail plus the stated tie term. Appending one private vote to an even sample gives e_{2j}=e_{2j+1}=b_j, including j=0. For fixed k, m times its weight tends to rho; the adjacent-weight products are uniformly bounded on k<=m/2, and the conditional tails admit a fixed-bias exponential bound. The contribution above m/2 remains negligible after multiplication by m. The negative odd sites of the biased +/-1 walk have expected visit numbers (q/p)^r/(p-q), with q=1-p: the probability of ever hitting -r is (q/p)^r and the one-step escape probability upon a visit is p-q. Summing the odd-site series and using the even/odd pairing gives the factor 2rho p(1-p)/(2p-1)^2. For p_m=1/2+alpha/sqrt(m), condition on U and couple the Bernoulli observation indicators to get K/m→U; at U>0, triangular-array binomial normal approximation gives the stated limit for both tie and strict-majority cutoffs, and bounded convergence applies. The equal-rate formula follows by u=y^2 and integration by parts and extends at alpha=0 via the integral. For large alpha, split at u=1/2 to bound the possibly singular beta-endpoint contribution exponentially, and use v=4alpha^2u on the other part and the integral of Phi(-sqrt(v)) equal to 1/2. The drop b_j-b_{j+1}=(p-q) binom(2j+1,j)(pq)^(j+1) follows by adding two votes. For m>=2 the probability of K>=2 decreases strictly with the hub rate, giving strictness for interior p; m=1 has identical e_0,e_1. The finite formula also covers p=1/2 and p=1, outside the strictness assertion. VERIFICATION.md and verify_star.py describe finite checks only; the audit does not rely on a rerun of that script.

## originality

PASS

The supported distinct claim is the quantitative characterization of wrong terminal consensus in the initially silent model: exact unequal-rate probability, sharp fixed-signal constant, and critical beta/Gaussian profile. Credit the first-announcement mechanism, qualitative correct consensus on stars at equal rates, and classical probability ingredients as prior.

## value

PASS

The star is a benchmark for the role of unequal centrality and update timing in social learning. The exact terminal risk identifies the penalty from a fast hub; the leading constant removes a logarithmic gap in the benchmark, and the weak-signal law describes when even growing populations no longer drive error to zero. Together the two regimes give more than a routine restatement of the first-vote mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
