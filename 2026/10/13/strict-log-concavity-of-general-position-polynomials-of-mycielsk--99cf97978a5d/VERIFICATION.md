---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For n≥2 each nonadjacent pair has distance two (in particular, an original reaches its own twin via another original and the root via another twin). Thus a forbidden triple is exactly an induced three-vertex path, and allowed induced subgraphs are unions of cliques. Without the root, if there are no originals any twins are allowed; with one original, its twin is optional and at most one other twin is allowed; with two or more originals, no paired twin and at most one other twin is allowed. With the root, either there is no twin and originals are arbitrary, or there is one twin and only its paired original is optional. These disjoint choices give the claimed polynomial, including the empty set. For k≥4, direct extraction gives binom(n+1,k)(2+k(n−k)/(n+1)); the weight is positive including at k=n+1 and strictly concave, so the product with the binomial row is strictly log-concave where all three indices are in this range. At k=1,2 the displayed differences are positive directly; at k=3 and 4 the stated translations n−2 and n−3 of the boundary quartics have positive coefficients. The k=4 comparison is only required for n≥4 and n=2 is checked separately by (1,5,10,5). Fresh direct shortest-path subset enumeration by all-pairs distances matched every coefficient for 2≤n≤6; this is finite corroboration only. Replay paths: RESULT.md §§1–4; the inspected verify.py and verify_output.txt describe a separate finite replay (use Python 3.10+ for int.bit_count, despite the 3.9 wording).

## originality

PASS

Pass for the full root-inclusive enumerator across the family together with its strict coefficient inequalities. Do not credit as new the root-free structural classification or its routine count, the known maximum and maximum-set uniqueness, or the n=2 enumerator alone. The strongest prior all-set theorem is specifically root-free, and the general polynomial papers inspected do not establish the claimed family-wide coefficient inequalities.

## value

PASS

For an established graph transformation and a standard invariant previously studied here mainly at its maximum, the full size distribution gives more information than the extremal number. The strict log-concavity theorem governs the whole distribution, including low-degree exceptions to the binomial-weight pattern, and adds a property not given by the general set criterion or maximum-size calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
