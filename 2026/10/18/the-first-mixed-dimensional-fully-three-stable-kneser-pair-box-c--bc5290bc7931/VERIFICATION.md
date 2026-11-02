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

The claim defines m>=6 graph vertices as unordered cyclic pairs at cyclic separation>=3, edges as disjointness, and N(G) as nonempty simplices sharing a graph neighbor. Reconstructed all face masks independently via a common-neighbor predicate rather than source facet-generation procedure. At m=6,7,8 respectively there are 3,7,12 vertices, 6,56,910 nonempty faces and f-vector at m8 (12,66,204,304,228,84,12). Reproduced source pivot-sweep greedy matching at all sizes and verified full directed Hasse graph acyclic (topological sort of all 6/56/910 faces); critical sets at m8 precisely (7), (0,1,5), (0,4,10), (1,3,6,8); 453 matched pairs. Independently computed exact integral signed Morse projection along matching and found all critical differentials zero. Morse complex at m8 has one 0-cell, no 1-cells, two 2-cells, one 3-cell. The 2-skeleton is S2∨S2, with pi2→H2 an isomorphism, so zero cellular attaching degree forces the 3-cell attaching map null; hence S2∨S2∨S3. At m6/m7 exactly one 0 and one 1 critical cell gives S1. Independent mod2 matrix eliminations yielded reduced b1=1 for m6,m7 and reduced (b2,b3)=(2,1) for m8. Nonequivariant transfer from N(G) to standard box complex is the existing Csorba theorem. Entire finite complexes exhausted, no extrapolation to m>8. Full Git tree recalculated from all nine actual Git blob identifiers; main and frozen repository manifests match.

## originality

PASS

Best-of-knowledge originality of the exact first mixed-dimensional m=8 open-neighborhood and nonequivariant box-complex type. Independent Resultary search, original stable-Kneser theorem full texts, and 2025 induced 2-independent/squared-cycle preprints were compared at the exact parameter and implication level. They identify nearby or equivalent graph constructions but their homotopy theorems exclude k=2 or final gap three, or address different complexes; no inspected result yields this wedge. The 2024 circular-complete article is inaccessible in full and its scope beyond the abstract remains a residual risk, not a negative proof. The general box/neighborhood equivalence is expressly prior. Published or unindexed equivalent calculations could still exist.

## value

PASS

The family of fully three-stable pair Kneser graphs is the next canonical stability boundary beyond the extensively studied two-stable Schrijver sphere theorem. The complete exact nonequivariant homotopy classification of the first three admissible sizes isolates m8 as the first mixed-degree obstruction within these sizes: two independent 2-spheres and one 3-sphere after two circles. Both the naturally motivated graph construction and its open-neighborhood/box-complex invariant precede the computation in primary literature; the mixed-degree integral attaching-map conclusion is not a textbook substitution or a known-table recomputation. This finite homotopy fact can be used as a precise benchmark and boundary for topological chromatic methods, without a paper-sized general theorem. It does not claim an infinite classification, a stronger equivariant invariant or that no other graph exhibits an earlier transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
