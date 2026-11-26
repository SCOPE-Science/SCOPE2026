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

With the unique c fixed first, every a-before-b pair in the remaining word contributes once for each rotation starting at or before that a, i.e. p_r times. Thus T is the displayed sum, and T/(a+b+1) is the averaged matrix entry. Subtracting the covariance term a^{-1} sum_{r<s}(s-r)(t_s-t_r) leaves a sum of identical pointwise quadratic bounds; the covariance vanishes exactly for constant t_r (automatic when a=1). Completing the square gives the stated nearest-integer rule with both tied choices allowed. If T is nonzero, the first a contributes b+t(b-t-1), at least b; equality requires t=0 or b-1 and all later a's after all b's. This gives both claimed words including their coincidence at b=1. Vanishing means there is no ordered ab pair, giving the claimed unique zero. The proof does not assert that the rest of the spectrum is contiguous. Independent replay: `cd /workspace && python3 review_replay.py 4` evaluated literal rotation counts on 3,418 necklaces in all 36 compositions 1<=a,b<=6 and checked the formula and entire extremizing sets. This bounded check corroborates the proof; the frozen script and its larger recorded run were inspected, not executed.

## originality

PASS

The average itself is established. The fixed-content singleton-marker maximum, all equality cases and the first positive value with its full level set are distinct from the inspected results, which concern binary averages/variance, ternary equivalence, or counts of rotation classes rather than the magnitude of this ternary entry.

## value

PASS

The first ternary scattered-subsequence entry beyond pair counts is a natural statistic not fixed by the composition. A single marker gives the simplest nontrivial fixed-content setting. Knowing when splitting the b-run is optimal, including ties, and knowing exactly which necklaces are invisible or produce the least nonzero signal gives useful structural information for distinguishing circular words. This is not merely evaluation of the average on a few test words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
