---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

The real frozen eight-file package includes the complete 90-facet list. Independently reconstructed (12,63,192,225,90) and every C(12,4)=495 potential 4-support. For a nonzero 2-cycle, support has >=4 vertices; on four vertices, every triangular face is needed and the cycle is the tetrahedral boundary up to scalar. All 153 missing tetrahedra with complete boundary survive nontrivially. Independent exact integer row/column unimodular reduction of the 63x192 d2 gives identity rank52 with zero residual, and within its primitive rank140 kernel the 140x225 d3 reduction gives identity rank136 with zero residual; H2(K;Z)=Z^4 with no torsion. The 153 integral H2 coordinates all have gcd=1, giving primitive classes; canonically mod orientation there are precisely 12 sign-classes, with multiplicities 16 nine times and 3 three times. Four specified representatives map to an integral basis. A separately written GF(2) bitset elimination yields ranks52/136, H2 dimension4, exactly 12 nonzero quotient classes with identical 16^9 3^3 counts; in the specified basis U=<e2+e3,e2+e4>, W=<e2+e3+e4,e1+e3> are complementary 2-planes with U\{0}:3, W\{0}:0, nine mixed:16. The map from 12 integral sign-classes to 12 distinct mod2 classes is injective, proving uniqueness of primitive integral minimum lift up to sign. Exact code was independently written from read facet list, not execution of opaque source verifier; finite exhaustive proof applies only to this labelled 12-vertex finite complex.

## originality

PASS

The complete 90-facet input table and published rank-four ambient homology predate the claim. They do not independently state or provide a published implication yielding the exact 153 essential induced tetrahedral sphere supports, primitive integral sign-class spectrum 16^9 3^3, the 12/15 mod-two support classification, the complementary two-plane U/W multiplicity rule, or uniqueness of primitive lifts among minimal carriers. Three actual Resultary semantic searches yielded the identical assigned Resultary record (excluded as non-independent priority), alongside analogous but distinct complexes. Lutz 2005 and Köhler–Lutz 2005 were inspected in their relevant primary full-text sections; the latter two same-topology examples have f=(12,66,204,240,96), unlike this 90-facet f=(12,63,192,225,90) object. A generic finite table encodes its derived invariants, but the claimed integral chain reduction and class-spectrum classification are not a listed prior theorem nor a mere naming/parameter substitution. Best-of-knowledge originality PASS with specific historical-census residual risk.

## value

PASS

The invariant is natural: minimum vertex support of a nonzero middle-dimensional simplicial homology class in a well-known small/vertex-minimal 4-manifold triangulation. All 495 four-vertex possibilities are classified, not a cherry-picked slice; the unusual 16^9 3^3 spectrum and U\oplus W pattern explain which rank-four mod-two homology classes have shortest carriers and how often. Integral primitivity and uniqueness of lifts add information unavailable from H2 rank, face vector, or simply listing missing tetrahedra. Such exact support-layer data are useful for computational topology benchmarks, comparisons of minimal triangulations and combinatorial systolic questions. The result is one finite object, not a universal classification; an unfinished census of larger support classes does not erase the independently useful first-layer classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
