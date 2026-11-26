---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

This pass applies to repairs/2/RESULT.md, not the frozen wording. As written over all n, the original's positive-limit premise is unattainable: it forces u_n-b_n to converge for b_n=log_2 n+log_2 log_2 n, whereas b_n has distinct lattice phases, and the original applies its theorem along subsequences anyway. The corrected theorem explicitly quantifies over arbitrary sequences of sizes tending to infinity, retains full-sequence tightness, fixes integer rounding in the coordinate truncation, and proves nonconvergence using sizes 2^(2^t) and floor(2^(2^t+1/2)). Rechecked the repaired claim: counts by length are squared positive-composition binomials, giving the stated hypergeometric law and an exponentially negligible noncentral contribution even to fixed factorial moments. In the central range the exact stars-and-bars ratio for O(log n) total size is uniformly the product of positive geometric(1/2) probabilities times 1+o(1). The coordinate tail bound with floor(T/2) makes the discarded part o(n^(-r)) for each fixed order r. The exact geometric-sum tail u*2^(1-u) times the asymptotic step count n/2 gives the stated intensity. Exchangeability, factorial moments, and moment determinacy give Poisson limits along each phase; rank events are the corresponding count events. Compactness of the intensities at rounded offsets gives tightness over all sizes; the two phases give different centered CDF values at every offset in (0,1/2). The original finite checker was inspected, not executed; it checks finite paths, not the limiting argument.

## originality

PASS

For the corrected claim, the distinct result is the joint growing-threshold exceedance law, with the log-log shift and lattice-phase fixed-rank laws, in the equal-coordinate simple-path model. The closest same-model primary paper gives fixed-size one-gap results and identifies the longest-gap problem for simple paths; the other inspected models do not supply the conditional moderate-gap estimates needed here. No priority certification is implied.

## value

PASS

The repaired theorem answers a longest-gap question specifically raised for simple jump paths, with the correct extra log-log centering and genuinely different lattice phases. The fixed-rank exceedance laws and control under the common-length constraint add more than a bound on the order of the maximum or a scalar analogy. The scope remains two equal starting coordinates and l1 gap sums, with no asserted expected-maximum asymptotic or convergence rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
