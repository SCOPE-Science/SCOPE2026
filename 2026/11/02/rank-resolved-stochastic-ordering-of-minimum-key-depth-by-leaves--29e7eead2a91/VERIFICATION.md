---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The independent insertion ranks \(R_k\) are exactly uniform over \(\{1,\ldots,k\}\). The proof in `RESULT.md` checks all probability normalizations: an interior leaf event has probability \(1/3\), endpoint events have probability \(1/2\); conditional three-rank tail probabilities are listed explicitly, with strict stochastic order obtained after convolution with unaffected independent ranks. The covariance signs and aggregate formula are exact for every \(n\ge3\).

Run `python checker.py` using Python 3's standard library. It enumerates all \(n!\) insertion-priority permutations for each \(3\le n\le8\), checks every local leaf indicator's rank characterization, exact rational covariance and all integer upper tails; it separately performs exact triple counts through index eighty and exact global covariance sums for sizes below two hundred. These finite tests are reproducibility checks, not a substitute for the general analytic proof.

No independent audit has been performed. Historic priority has not been certified beyond the cited and inspected primary sources, especially for position-refined record/peak enumerations.
