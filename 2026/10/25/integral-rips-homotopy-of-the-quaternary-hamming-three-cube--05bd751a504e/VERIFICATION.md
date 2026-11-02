---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For all real r>=0 in X={0,1,2,3}^3 with inclusive Hamming threshold, scale r<1 is 64 points; 1<=r<2 collapses 48 coordinate-line tetrahedra to a connected graph of 64 vertices and 144 edges, hence wedge^81 circles. At 2<=r<3, adjacency iff words agree in at least one coordinate, so VR is exactly Ind(K4 categorical product K4 categorical product K4). Independently enumerated all maximal cliques, obtaining precisely 508 facets equal to 12 coordinate planes, 64 radius-one Hamming balls and 432 parity tetrahedra. Their union enumerates exactly 830101 augmented faces; independent greedy matching has 414848 pairs and 405 unmatched tetrahedra. Topological sorting all 6539456 incidences checks acyclicity, yielding a CW model with one 0-cell and 405 3-cells, hence wedge^405 S3 integrally. r>=3 yields the full simplex. Persistence interval descriptions follow from these disjoint-degree stages. This proves finite (4,4,4), not general q.

## originality

PASS

The 405 sphere count is explicitly conjectured in Antolin Camarena-Carnero Bravo (Conjecture 26), so its numerical prediction is not new; the finite exhaustive homotopy proof of the (4,4,4) case is the assessed contribution. Proposition 25 covers a triple product with at least one factor K2, not all K4. Earlier published q=3 Hamming Rips computations yield 46 three-spheres and do not imply q=4. Goyal-Shukla-Singh work treats two-factor categorical complete-graph products; no proof of this three-factor case was identified in available primary material. Full text of the highly relevant 2023 product preprint was not obtained; this is a nontrivial priority risk, not asserted whole-document noncoverage.

## value

PASS

This case resolves a natural specified finite instance of a previously published higher-product independence-complex conjecture, via a nontrivial complete 830101-face discrete Morse certificate. The full four-stage Hamming Rips filtration and 405 exact integral sphere wedge are independent useful natural invariants; there is no claim to prove all alphabet sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
