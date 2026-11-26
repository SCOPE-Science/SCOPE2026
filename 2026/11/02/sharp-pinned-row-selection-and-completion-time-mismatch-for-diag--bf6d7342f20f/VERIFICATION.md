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

Each sampled coordinate is cleared forever and no other is changed; its survival probability after t iid draws is (1-p_i)^t. An initial unit error on a minimum-weight retained row attains the maximum for every t. If the least index retained is j, the rth selected index is at least j+r−1; replacing with the window preserves the numerator min(w) and weakly decreases the sum, strictly for a nonwindow if weights are strict. Inclusion-exclusion of missing coupons and summation of geometric tails give the CDF and expectation (including the empty-history convention 0^0=1 at t=0). Nonzero initial errors on all retained coordinates are necessary for that full coupon time to represent first solution time. Independently recomputed the four means by first-step recurrence, not inclusion-exclusion: for visited set U, E_U=(S+sum_{i not in U} w_i E_{U+i})/(sum_{i not in U} w_i), with E_R=0. In table order the outputs were 2593/360, 11057/1320, 937/105, 38677/5544. Comparing with 9/11, 11/13, 7/8 and 14/17 confirms the different unique optima. For 0<epsilon<1/2, epsilon²/(1+epsilon²)<1/5; pinning the largest weight minimizes the Frobenius residual but picks that smaller progress fraction. The stated divergent ratio is of 1−rho, not rho. Checked verify.py's finite coverage without executing it; the proof handles arbitrary weights, t and ties.

## originality

PASS

The diagonal exact window and disagreement with exact mean completion are distinct from the checked SCRK results and classical coupon formulas. Credit the existing unbounded Frobenius/progress phenomenon, including a prior nondiagonal rejected-proposal example; the diagonal exact time-uniform rate separation is a scoped refinement, not first discovery of the generic surrogate problem.

## value

PASS

There is a practical objective choice even for uncoupled coordinates: the exact rate-optimal window is cheap to find, and a rational witness proves it need not minimize mean full solution time. The unbounded relative progress loss clarifies when not to use the Frobenius proxy. No implication for noise, setup cost, or accepted updates is needed for this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
