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

Forest orientations extend by topological order, directed cycle labelling blocks shattering; hence VC is graphic rank. For cactus, free bridge directions and independent cycle blocks factor as product concept classes, each cycle lacking exactly its two coherent orientations and having Ldim length-1. A depth-4 diamond witness tree is in actual certificate/diamond_tree.json; independent full acyclic-orientation Littlestone recurrence on 18 diamond hypotheses gives Ldim4, and on 46 K2,3 orientations gives Ldim5. Subdivision encodes the old edge plus a free edge bit while preserving acyclicity, increasing Ldim and rank by one. Every noncactus contains theta and can attach a spanning forest freely; product/projection lower bound adds rank of attached forest. The universal conclusion is analytical, not extrapolated from small graphs.

## originality

PASS

Best-of-knowledge new cactus iff criterion and universal theta obstruction for adaptive (Littlestone) shattering, while Kozma–Moran static VC-rank equality is explicitly established prior work. General COM sample compression is not an Ldim equality result.

## value

PASS

A natural sharp structural graph boundary distinguishing static and online edge orientation learning, with minimal diamond obstruction, triangle-free K2,3 witness and unbounded disjoint-union gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
