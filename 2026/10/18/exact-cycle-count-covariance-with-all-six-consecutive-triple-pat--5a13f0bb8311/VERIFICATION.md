---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For every n≥3 and six consecutive length-three rank patterns, conditioning on prescribed distinct images at positions (t,t+1,t+2) leaves n−3 uniform path components; the number of disjoint cycles has conditional mean Z_closed+H_{n−3}. Complete fixed-cycle length 1,2,3 counts (binomial fixed-point sums, pair reversal possibilities, and exactly two possible 3-cycles) yield the displayed S_p polynomial vector. Subtracting (n−2)(H_n−H_{n−3})/6 gives six rational covariances (3n−2,3n−8,3n−8,4−3n,4−3n,10−3n)/(6n(n−1)), including exceptional sign n=3 for pattern321. The peak orientations 132/231 give difference (n−2)/(n(n−1)) and sum −2/(3n(n−1)); analogous valley. I independently enumerated full uniform S_n for n=3,…,7 and recomputed cycle+rank-pattern covariances as exact fractions for each pattern, all matching. The infinite n claim follows symbolic closed-cycle table formulas, not this bounded enumeration.

## originality

PASS

The six-by-one orientation-refined joint cycle/pattern vector is the candidate contribution. Prior peak-pattern grammar treats orientation without cycle markings; cycle-type/peak generating functions treat aggregate peak counts without distinguishing orientations. Aggregated peak covariance may be covered; the presented theorem must not claim it independently novel.

## value

PASS

Cycle count measures a global permutation decomposition, while consecutive triple patterns are natural local statistics. The six-type covariance classification gives a sharp and non-obvious sign pattern (including an n=3 boundary exception), and a cancellation mechanism in which oriented peak/valley contrast is O(1/n) but combined peak count is O(1/n²). This is a motivated dependence invariant beyond textbook marginal enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
