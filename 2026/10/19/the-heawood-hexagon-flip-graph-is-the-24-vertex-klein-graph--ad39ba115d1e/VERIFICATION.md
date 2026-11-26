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

The cyclic incidence model has exactly one common line per pair of points, so there is no 4-cycle. The symmetric difference of matchings is a disjoint union of even alternating cycles. Having four shared edges leaves six in the difference and is therefore equivalent to one hexagon flip. A read-only independent reconstruction backtracked all 24 matchings, used overlap-four adjacency, checked all 576 entries against the frozen matrix and supplied bijection, and reproduced every rooted distance, intersection number, and the eight antipodal classes with one neighbor in each other class. Three pairwise disjoint matchings use all 21 edges, and every one-factorization gives such a triple. For a public reference independent of the inaccessible cited matrix endpoint, I also reconstructed Dejter's Klein graph from the 24 oriented cycles in Theorem 2, Section 3's pairing of oppositely oriented 2-arcs, and Corollary 4. An explicit computed bijection preserves all adjacency entries between this historical construction and the reconstructed flip graph. Replay: python3 /workspace/replay_checks.py 4. The count eight is of unordered partitions, not labeled edge colorings.

## originality

PASS

The 24-vertex Klein graph, its parameters, the Heawood matching count, and the factorization count are prior background. The supported distinct claim is the identification under the all-hexagon matching adjacency, with the distance rule in terms of original matching overlaps. The closest checked historical construction is on Coxeter cycles, not matchings; its missing matching correspondence is a substantive step. Three later Resultary records overlap strongly, two nearly verbatim at the level of the theorem. Their relative catalogue timing does not establish provenance or constitute evidence of earlier coverage of the frozen claim.

## value

PASS

A canonical move graph on Heawood perfect matchings realizes a second well-studied graph, and the count of shared matching edges directly answers shortest-move questions. The antipodal fibers give a structural interpretation of the graph's known cover in terms of actual one-factorizations. This is a meaningful finite identification, not simply re-measuring the known Klein parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
