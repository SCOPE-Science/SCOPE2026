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

Unrestricted exchange distance is |U∖T| by exchanging an edge of U∖T against an edge outside U in its fundamental cycle. Maximizing this distance from T gives the graphic rank of E∖T, since a maximal forest in E∖T extends to a spanning tree. A six-edge graph inside a graph of girth five has at most one cycle: the symmetric difference of two distinct cycles would be a nonempty even subgraph on at most two edges. For a pentagon the five external edges form a matching, since an off-cycle vertex with two pentagon neighbors would make a triangle or quadrangle; the other five vertices therefore form a pentagon, and deleting one edge of it leaves a path with five pendant edges. Deleting a chordless hexagon leaves its six vertices as leaves and leaves three internal edges on four vertices, which form a tree by triangle-freeness. Thus the complementary cycle census is 12·5+10. Independently reproduced by python3 /workspace/reproductions/petersen_exchange.py: the outer/inner pentagon construction is checked isomorphic to the disjoint-pairs labeling, nine-edge sets are filtered by connectivity, and all-source BFS is run over actual swap adjacency without using the distance formula. It obtained 2,000 connected vertices, eccentricity counts 70 at 5 and 1,930 at 6, complement-core split 60+10, and unordered coefficients (28140,222360,651080,748200,314220,35000), yielding 1,999,000 pairs and Wiener index 7,200,000. Separately, counting submasks of each tree reproduced all ten squared forest-extension moments, without the attached contraction routine. The exact finite computations cover the entire claimed graph.

## originality

PASS

The supported distinct contribution is the unrestricted central-tree classification and exact full unordered distance distribution. The known tree count and exchange-distance identity are explicitly excluded from novelty. The earlier pivot record has the same tree set but a different adjacency and different distance statistics. Its two scalar histograms already determine the Wiener sum by subtraction, so the Wiener index is not an independent originality contribution. They do not give the unrestricted histogram or the unrestricted eccentricity classification. The forest-support counts in a later Petersen shattering record are a material equivalent of the central-complement census once the rank criterion is supplied, but are later on the displayed dates. This is a bounded best-of-knowledge assessment, with the historical matroid manuscript an unresolved access risk.

## value

PASS

The Petersen graph is a canonical small symmetric graph, and the distance distribution and center structure of its unrestricted spanning-tree exchanges are natural invariants of that move system, not arbitrary selected instances. The cycle characterization explains the nonuniform eccentricities; the full exact histogram gives a usable benchmark for comparing unrestricted swaps with incident-edge pivots and for procedures using distances between trees. The previously implied first moment is not the basis of this value judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
