---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For n=2 only one matching; for n=4 all (3!)^4=1296 complete strict preference profiles and 3 perfect matchings/profile were independently exhausted with blocking-pair tests and rank-sum/max-regret reconstruction. Solvability counts exactly 48 with none, 1098 with one, 150 with two stable matchings. Among 1248 solvable cases E=G in 1176, E proper subset G in 48, G proper subset E in 24, no disjoint/nonnested cases. The displayed n=6 profile was independently tested against ALL 15 perfect matchings; precisely two stable choices attain (sum rank, worst rank)=(13,3) and (12,4), giving disjoint E and G. No 6-agent all-profile census is asserted.

## originality

PASS

The underlying stable-roommates criteria are standard; independently inspected Simola–Manlove and two highly close published Resultary records. Rank-maximal (lexicographic first-choice) is not egalitarian (sum rank), even when histogram counts 1176/48/24 coincide: the former has 24 R/G disjoint profiles whereas present E/G census has NO four-agent disjointness. The published stability-only orbit census gives 48/1098/150 but no objective comparison; stable marriage is different bipartite domain. Thus six-agent first E/G disjointness and precise four-agent relation are not covered by these sources. A source could still contain an unindexed explicit example.

## value

PASS

Sum-rank egalitarian welfare and worst-rank regret are two economically meaningful competing fairness objectives; the earliest size of forced incompatible stable choices is a natural structural boundary. The exact n=4 classification distinguishes disagreement from nonintersection and the six-person witness demonstrates a genuine Pareto trade-off, rather than merely reproducing 4-agent solvability counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
