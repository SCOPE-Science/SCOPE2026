---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reconstructed the 28-vertex, 42-edge cubic Fano-triple model and independently enumerated induced matchings by vertex deletion: a chosen pivot is either unused, or paired with a unique surviving neighbor, in which case both closed neighborhoods are removed. This partitions the matchings without assuming a size bound. The histogram is (1,42,609,3808,10374,11172,4242,84), and all 84 maximum edge masks match the frozen certificate exactly. On these masks, pivoted Bron–Kerbosch gives 2478 maximal cliques, all of size four; taking all subcliques gives (1,84,1092,3528,2478). All degrees are 26. Independently extending all 168 images of a noncollinear ordered basis gives 168 distinct collineations and an orbit equal to the maximum-matching set. The seven-color classes partition the 42 edges and lie in the independently enumerated matching set. Six classes would all have size seven, impossible by the packing bound. Replay: python /workspace/reproduce_frozen.py 5. This certifies the fixed graph only; the source scripts and recorded outputs were inspected, not executed.

## originality

PASS

The certified contribution is the exact induced-matching and edge-disjoint packing geometry, not the already tabulated strong chromatic index. The strongest distinct catalogue overlap is a later, explicit classification of the identical 84 objects and their disjoint-pair count; it does not establish antecedent coverage of the packing-purity and clique census. No stronger earlier covering result was found in the inspected material.

## value

PASS

Enumerating natural extremal color classes on a canonical symmetric cubic graph resolves more than the numerical strong-coloring threshold: all small packings extend to the same size and no near-partition of five maximum classes exists. The orbit and complete pure clique census make this a reusable description of the obstruction to saturating the edge-count bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
