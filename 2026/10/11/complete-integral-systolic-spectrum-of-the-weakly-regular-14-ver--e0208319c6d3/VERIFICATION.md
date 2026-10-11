---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The included `verify.py` reconstructs the 14-vertex cyclic complex from the published facet formula and uses only integer arithmetic and finite enumeration. It verifies \(f=(14,42,28)\), that every edge lies in two triangles, that all graph triangles are facets, and that there are no 4-cliques.

For homology, a spanning tree is collapsed. The remaining 29 edges and 28 triangle boundaries give an integral presentation. The verifier computes all 29 maximal minors exactly by fraction-free elimination, checks that the relation rank is 28 and that the gcd of the maximal minors is 2, and constructs a primitive cofactor vector annihilating every relation. The same relation matrix has rank 27 over \(\mathbf F_2\).

It then exhausts all simple three- and four-edge cycles. All 28 three-cycles are face boundaries. There are 77 four-cycles: 42 null, 21 representing the nonzero order-two class, and 14 with primitive infinite-order class. Finally it verifies that the 35 essential four-cycles are exactly the union of the translation orbits of \((0,1,7,6)\), \((0,1,7,8)\), and \((0,2,4,6)\), with orbit sizes 14, 7, and 14.

The calculation is exhaustive only for simple cycles of lengths three and four; it does not classify longer or non-simple cycles.
