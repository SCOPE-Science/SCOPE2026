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

Correctness PASS for K=M(Petersen), where vertices are the 15 Petersen edges and faces are pairwise disjoint-edge matchings. Freshly built complete simplicial chain groups with face vector (15,75,145,90,6); signed integer boundary ranks (14,61,79,6), and every nonzero Smith factor unit, prove reduced H2=Z^5 and reduced H3=Z^5. The general flag-cycle minimum-support theorem requires at least six vertices for nonzero H2, and at six support the carrier is an induced 3-crosspolytope boundary. Exhaustively inspected all binom(15,6)=5005 supports, found exactly110 incompatibility-perfect-matching octahedra. All eight-triangle join fundamental cycles have zero boundary. Enumerated all 120 S5 permutations, giving orbit sizes (10,60,40). Independent Smith reductions on matrices [D3|orbit cycles] have 84 nonzero factors and nonunit lists (2),(),(), proving exact integral quotients; one representative in each orbit is nonzero primitive with an 80-unit-factor augmented matrix. Source program also constructs seven conjugacy-type characters and rational representation identification; this character calculation was inspected but not independently replayed in this execution, so the latter rests on the explicit signed chain-action formula plus source certificate, not on novel rederivation of every 90×90 rational kernel.

## originality

PASS

Originality PASS, qualified. The existing published Petersen matching complex wedge type yields Betti ranks (5,5) but not shortest embedded homology carriers, their 110 count, three automorphism orbits, orbit index-two exception, or rational S5 characters. Adamaszek–Stacho already give the general flag cross-cycle minimal-support principle; that is used, not claimed new. Nearby Resultary records about Petersen two-matching, graph Morse, independence or 3-cut complexes refer to different simplicial objects.

## value

PASS

Scientific value PASS: the ordinary matching complex of the Petersen graph is a canonical, natural flag complex with nonzero H2 and high symmetry. Determining its minimum integral homology supports, all 110 carriers, and the distinct integral generation indices of the S5 orbits resolves natural geometric questions not implied by the known wedge-of-spheres result. The rational S5 decomposition adds precise equivariant homology information. This is an exact finite classification of motivated objects, not an arbitrary tiny numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
