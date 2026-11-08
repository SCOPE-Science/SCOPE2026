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

Let D={T(gX)<T(X)}. On D^c every sampled transform gives comparison success so P_M=1; on D the number of successes equals Bin(M,a), independent of X. On each length-l g-cycle invariance gives uniform X and at most l-1 directed strict score descents; therefore Pr(D)<=delta_L=1-1/L, attained by one descending cycle. Every grid threshold exactly has maximal rejection delta_L F_{M,a}(k-1), so M inequalities characterize universal validity. Lower-binomial CDF monotone in a gives interval of safe masses. Size-bias identity with Bin(M+1,a) proves strict safety at a=delta_L and continuity gives a_M,L<delta_L; LLN proves limit. Independent direct enumeration of maximal strict cyclic score orderings and all 2^M transformation strings for L=2..6, M=1..4 and a in {0,1/4,1/2,3/4,1} matched the exact rational formula; finite verification is not all-M proof.

## originality

PASS

Earlier arbitrary-distribution permutation tests use randomized reference; the audited theorem characterizes when the unmodified statistic itself is valid under a biased two-transform sampler.

## value

PASS

Nonuniform randomization is a practical validity concern in Monte Carlo permutation inference. The theorem gives a sharp universal all-threshold frontier and an exact resampling-budget reversal that separates fixed-origin tests from corrected random-reference schemes; these are substantive, reusable mathematical facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
