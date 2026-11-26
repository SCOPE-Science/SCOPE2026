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

Each depth-d tree needs 2^d distinct concepts and 2^(d−1) in each root branch. The positive branch has at most k starts on a path; the two cyclic branches have k and n−k. For the path lower bound, retain 2^d consecutive starts and query vertex 2^(d−1)−1, which splits them in half since that half has size at most k. For the cycle, the query k−1 partitions starts into contiguous blocks of lengths k and n−k, from which one retains 2^(d−1) consecutive starts in each branch. Midpoint queries bisect each retained block recursively: the clockwise distance from a start on the first half is less than k, and from a start on the second half it is at least n−(block size−1)>k on a cycle. Thus the floor thresholds and exact powers of two are attained, including the path singleton with dimension zero. For VC dimension on paths, an interval cannot label three ordered points 101. On two points their start intervals must overlap with both differences nonempty; a missed-by-both start is outside their union. Reflecting if needed makes it a start to the left, so the first query x is at least k and its start interval ends below m−1, forcing m≥k+2. The four stated starts for the pair k,k+1 realize all traces under this bound and k≥2. For cycles, three membership bits make at most six changes in total as the start goes around, hence at most six distinct traces (or one if constant). Adjacent points yield all four two-point traces iff both arc widths are at least two; the singleton/co-singleton boundaries have dimension one. The recorded finite enumeration is consistent with the proof but is not needed for its all-parameter conclusion.

## originality

PASS

The indicated contribution is the simultaneous all-parameter path and cycle classification, particularly the exact online ranks on both domains and the path static boundary. The earlier four-point translation theorem covers the cycle k=4 and, by label complementation, k=n−4 slices for n≥8, so those are not separate contributions. Two later-indexed records contain the exact path and cycle dimensions, respectively, as parts of richer theorems. This exact overlap is explicit; their November 8 records do not establish pre-existing coverage of the November 2 published record. An older exact all-width implication or exact table was not identified in the actual examined statements.

## value

PASS

The fixed-width path and cycle incidence families are natural domains for comparing static queries and adaptive membership. The exact finite-domain threshold is not supplied by counting concepts alone: it blends the root minority branch with how that branch can be recursively split. The path phase with VC dimension one and unbounded adaptive depth, and the distinct cyclic complement cutoff, are useful structural benchmarks. This judgment credits the full finite classification, not the easy interval ceiling or the previously known four-point slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
