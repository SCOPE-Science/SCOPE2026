---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

The definition is vertex subsets inducing maximum degree at most one, empty included. The three-way least-pivot recurrence partitions by exclusion, inclusion without a neighbor, or inclusion paired with a uniquely determined neighbor; every call strictly reduces W. Independently constructed both 16-vertex graphs from the literal adjacency definitions and exhaustively checked all 65,536 masks per graph, recovering coefficient vectors [1,16,120,384,528,144] and [1,16,120,384,544,240,32]. Exact common-neighbor counts (2 for every pair) and degree six substantiate (16,6,2,2) and equal spectrum; maximal sizes and multiplicities follow from exhaustiveness. No extrapolation to general graphs is made.

## originality

PASS

The comparison is between two specific cospectral SRGs under the degree-at-most-one dissociation invariant; independently published calculations of independence complexes compare only degree-zero sets and topological homotopy, not this polynomial. Published cubic-graph dissociation bounds concern valency three and do not imply these six-regular coefficient arrays. No known prior exact table was found; unindexed earlier counts remain a priority risk.

## value

PASS

A complete dissociation polynomial is a natural graph invariant, and this exact pair is the canonical smallest-class strongly regular cospectral counterpoint: the full arrays isolate the first degree of divergence and the distinct maximal allowable cardinalities. It gives an independently usable counterexample to determination by the SRG tuple, beyond a cosmetic graph renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
