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

Under the definition in RESULT.md:26–30, a peak left of x has strict improvement interval (2p−x,x) clipped to [0,1]; a peak right of x has the reflected interval, and a peak at x has none. Mixed-side coalitions cannot block. At fixed x the intervals on either side are nested; adding all voters no less extreme than the extremal restriction's required side (the first j on the left, or j through n on the right) preserves the intersection and reduces the blocking threshold. The nonblocking inequalities are [min{x,2(x−p_j)}]_+<=q_j and [min{1−x,2(p_j−x)}]_+<=r_j. Each threshold is nonnegative, so solving the min inequalities with weak signs gives the precise stated upper and lower cuts, including equality and wrong-side indices. For j<=k the j-th lower cut is at most p_j<=p_k, which is at most the k-th upper cut. For j>k the lower cut is at most 1−r_j<=q_k, at most the upper cut. Clipping therefore preserves nonemptiness for all epsilon>=0, including zero. Sorting costs O(n log n); scanning the cuts costs O(n). Sorting, each clipped cut, and the min/max aggregations are nonexpansive for the sup norm, so the Hausdorff distance of the two intervals is bounded by the largest labeled displacement. A common peak gives the singleton core at epsilon=0, and moving it attains equality. Analytic replay: RESULT.md:34–70. The frozen exact-rational checker and its verification notes were inspected, not rerun; the finite comparisons do not prove the real-parameter statement.

## originality

PASS

The supported distinct contribution is the complete continuum line formula together with its sharp perturbation result. The general strict blocking predicate, qualitative existence bounds, finite algorithms and convexity of a fixed matching's tied-winner set are credited. Neither qualitative nonemptiness alone nor fixed-matching convexity suffices for novelty here. No stronger statement giving these exact continuum cuts and stability was established from inspected sources.

## value

PASS

The complete interval and endpoint scan describe all admissible alternatives rather than a chosen witness. They make the unrelaxed case explicit and quantify the worst-case effect of errors in estimated peaks with the exact constant. This is a natural spatial preference domain, not an arbitrary restriction of the alternative space, and the result does not overclaim robustness to other measures or metrics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
