---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For uniform set partitions, successor arcs and the ordinary covariance are explicitly defined. Independently enumerated all partitions of sizes 4–7 and reproduced Cov(K_n,X_n)=D_n/(4B_n²). Independently generated Bell numbers through B_803: the integer D_n is strictly negative at every n=4..235 and positive at every n=236..799. Verified 5B_801<801 B_800. The infinite tail uses a separate analytic argument: the Touchard recurrence preserves real negative zeros, hence K_n is a Poisson-binomial sum and its third cumulant has absolute value at most its variance; normalized Bell log-concavity bounds 5(B_{n+1}/B_n)<n+1 for n>=800, making the exact covariance identity strictly positive. Neither finite enumeration nor an observed sign switch alone would imply the tail.

## originality

PASS

The threshold n=236 is an exact all-integer sign classification of the joint block-count/crossing statistic, distinct from already published conditional crossing means and general shifted-Bell expressions. Kasraoui Theorem 2.3 supplies the fixed-block crossing formula; Chern–Diaconis–Kane–Rhoades supplies generic shifted-Bell statistical machinery and marginal distribution limits. Those statements give paths to calculating the covariance but do not directly give the unique global sign threshold with a positive infinite tail. Targeted Resultary and scientific literature comparisons uncovered no exact threshold theorem, without establishing absolute priority.

## value

PASS

Block count and crossing count are intrinsic structural observables of a uniformly random set partition. The reversal at the unexpectedly large exact boundary 236 explains how small-sample sign evidence can mislead; obtaining a global sign law needs an analytic tail bound beyond finite numerical statistics. This is a motivated, reusable qualitative dependence threshold rather than an arbitrary statistic substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
