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

Uses the explicitly credited type-B signed set-partition bijection of Buck et al. The zero block containing 1 has size b and contributes the first descent at 2b−1 if b≥2; each subsequent block with s_i positive/negative choices and q_i negative elements contributes descents at p+2q_i (if q_i>0) and at p+2s_i−1 (if s_i−q_i≥2). Choosing the remaining zero-block labels and each ordinary block from the smallest unused label yields precisely binom(n−1,b−1)∏ binom(n−a_{i−1}−1,s_i−1)binom(s_i−1,q_i); grouping by the stated Delta gives the exact N_n(T) for all n and T. A run composition corresponds bijectively to the set of cumulative descent positions. A memoized suffix DP over remaining labels, with O(r²) block choices per r, uses O(n³) arithmetic operations. Independent direct generation of all Stirling words by insertion of next adjacent maximum, testing original flattened condition, matched a separately computed signed-block formula for n=1..6 with totals 1,2,6,24,116,648 and 1,2,4,9,19,41 different descent profiles.

## originality

PASS

The type-B set-partition bijection and total run counts are explicitly due to Buck et al. (2023), and Shankar (2023) already gives the univariate descent-count generating function; neither exact position set nor arbitrary ordered run lengths appears as such in their inspected relevant theorems. Buck et al. list a related equal-run-length Open Problem 3 and solve some low-run cases, so those special cases are not asserted novel. A hidden multivariate refinement could still cover the formula.

## value

PASS

An exact positive position-resolved descent distribution and efficient prescribed-composition count is a natural, nontrivial refinement of the familiar univariate number-of-runs statistic for flattened Stirling permutations; it answers the all-equal-run problem for arbitrary d when d divides 2n, not solely a small numerical case. The known signed-partition bijection requires additional blockwise descent-location and multiplicity analysis; this is a usable enumerative formula of a canonical combinatorial family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
