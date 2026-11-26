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

Normalizing the orthogonal columns gives entries 1/sqrt(d) on disjoint blocks and row leverage 1/d. Identical-input joint sampling is uniform across rows, so each group has sampling probability 1/d. A sampled row from group j adds d*s_j^2/r in diagonal coordinate j. Normalizing by d^2, the weak-coordinate errors are at most (d-1)/d^2, including equality, because 0<=C_j<=r. The leading error is exactly |d*C_1/r-1| with C_1 binomial(r,1/d), giving the tail sum. Its integer acceptance set excludes 0, and the upper endpoint is below r since 1+epsilon<d. The kth and (k+1)st closed bands have a strict open gap exactly when (2k+1)*epsilon<1; actual budgets must lie on the grid r/d. For d=5 and epsilon=1/4, r=5,7,10 admit respectively {1}, the empty set, and {2}. For fixed epsilon and r_d/d approaching positive alpha, the admissible integer endpoints stabilize off the two stated boundaries and the binomial point masses converge to the Poisson masses. Under row-norm sampling the one-draw rescaled coordinate is d^2+d-1. Its error meets tolerance exactly for the leading group, whose sampling mass is d^2/(d^2+d-1). This also checks the d=2 boundary of the weak-error condition. The frozen verifier was read; these conclusions rely on the proof and exact witness, not a script execution.

## originality

PASS

The sampler and the binomial algebra are standard; the supported distinct claim is the explicit equal-leverage, stable-rank-to-one Gram example with reentrant zero-success sample budgets and its comparison to a one-draw norm sampler. The inspected related results use different estimators or targets, or give sufficient high-probability bounds rather than this exact phenomenon.

## value

PASS

The explicit all-nonzero-row family is a controlled counterexample to monotonic attainability in sample budget and to expecting uniformly good prescribed leverage sampling solely from near-one stable rank. Exact reentrant failure and the improving one-draw norm baseline diagnose different sensitivities of the two distributions. This is a finite-budget spectral Gram statement on the exhibited family, not a failure of general subspace embedding guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
