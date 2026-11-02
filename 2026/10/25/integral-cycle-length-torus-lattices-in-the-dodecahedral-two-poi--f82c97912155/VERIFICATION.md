---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Rebuilt GP(10,2) as 20-vertex 30-edge cubic graph. Standard two-particle discretized deleted product has (c0,c1,c2)=(190,540,375), and independently reconstructed all boundary incidences, obtaining rank ∂2=339 over F2 and F101 and ∂1∂2=0. Enumerated all 1168 unoriented simple cycles and all 823 vertex-disjoint pairs, with exactly twelve distinct length pairs. Each product-torus signed chain is an integral 2-cycle. The 36 disjoint pentagon-pair chains form a 375x36 matrix having a 36x36 integer minor determinant +1 in an independently selected row set; hence primitive in C2 and equal to ker∂2 by rational rank bound and primitive-kernel argument, proving integral H2=Z^36. All 823 tori were independently reconstructed in all 375 coordinates from this basis. Exact Smith normal forms for all twelve 36xm coordinate matrices reproduce each claimed quotient; e.g. (8,8) has 12 factors two and index 4096; (5,14) has Z^6⊕Z/2; (8,10) Z^17⊕Z/2; (9,9) Z^26. This is exhaustive for the fixed 20-vertex graph and relies on the standard deleted-product deformation equivalence, not on numerical approximation.

## originality

PASS

Important priority qualification: Barnett–Farber 2009 Theorem 6.1 states an *integral* free basis of ordered planar graph H2 via disjoint face-boundary tori, not merely a rational basis; ordered-vs-unordered descent might also yield the dodecahedral pentagon-pair integral basis, so that component cannot be claimed independently new without further comparison. The assessed original part is the exact twelve length-filtered integral Smith quotient spectrum, absent from the inspected planar-generation and rational dodecahedral representation results.

## value

PASS

Length-filtered torus lattices are geometrically canonical refinements of the natural H2 generators: same rational span can have index 1, 2, or 4096, and some length classes have reduced rank. The exhaustive 12-case Smith classification separates integral from rational geometric generation and is a useful precise invariant for a symmetric planar graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
