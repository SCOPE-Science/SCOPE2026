---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Under E_{vab}, exactly P_a=P_b=v are forced, and later attachment choices exclude each leaf from subsequent parent selections. Product telescoping gives probability 1/((n−1)(n−2)); two forced root indicators and two harmonic sums cancel a,b dependence, leaving 2*1[v=1]−1/(n−2)−1/(n−1). Summing all n choose 3 event indicators yields E[Z]=n/6 and Cov(R,Z)=(4n²−15n+12)/(6(n−1)(n−2)), positive for all integer n≥3. Independently enumerated parent vectors n=3..7 and 150 rational identities; this does not replace infinite proof.

## originality

PASS

The fixed-labelled sibling-leaf event and its root-degree regression distinguish a non-fringe pair-count from ordinary leaves, complete fringe cherry counts, or generic unlabeled motif asymptotics. The inspected sources do not entail the exact conditional response or covariance; best-knowledge only.

## value

PASS

The count Z is a natural higher-order terminal-clustering statistic in recursive trees, not the ordinary leaf count. The exact label-insensitive root-degree conditional response and mixed covariance with a nonzero 2/3 limit are usable all-size structural identities, rather than unmotivated small instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
