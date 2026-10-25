---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

G=L(K5)=J(5,2) has 10 metric points, 30 edges, diameter 2, so the real 9-dimensional free unit ball is a symmetric edge polytope. At a polar vertex active ± incidence normals span dimension 9 iff tight-edge graph connected. Along a tight spanning tree differences are ±1 and normalization min f=0 gives integer f; graph diameter 2 gives f in {0,1,2}^10. Thus checking exactly 3^10=59049 candidate assignments is exhaustive, not sampling. Independently enumerated 1032 connected-tight admissible potentials, with tight edge-count multiplicities {12:110,14:300,16:330,18:280,20:12}, levels {2:922,3:110}. Independent S5×C2 orbit enumeration yielded 17 orbits of exactly stated sizes; the five maximum K4 stars distinguish S5 as all graph automorphisms. Every K4 star contributes at most 4 tight edges, so upper bound 20. Equality forces balanced 2+2 at all five K5 vertices; no simultaneous level 0/2 classes on 5 ground vertices; hence each color is spanning 2-regular, necessarily complementary Hamiltonian 5-cycles, 12 labeled maximizers. The equality proof does not depend solely on enumeration.

## originality

PASS

Best-of-knowledge originality judgment on this complete exact claim, based on statement-level comparison with primary mathematical literature and published research records, with limited full-text access flagged rather than interpreted as novelty proof.

## value

PASS

A canonical highly symmetric ten-point graph metric acquires a complete exact real transportation-ball facet-orbit classification and five distinct incidence strata; the sharp optimizer family is linked to complementary Hamiltonian cycles. Such a finite natural complete classification is independently useful as a computational/combinatorial benchmark, even without a formula for all J(n,2), and is not a mere generic recognition criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
