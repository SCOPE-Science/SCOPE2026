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

Reduced closed walks of odd length m=g+2 are either injective m-cycles or g-cycles with one immediate backtrack; two disjoint backtracks would force cycle length <=g−2, violating girth. Square-freeness (at most one common neighbor for distinct vertices) makes each nontrivial cell a simplex with one variable coordinate, and injective m-cycles are isolated. Outside branches attach as free simplices and collapse onto a winding component of Hom(C_{g+2},C_g), a cycle of exactly gm homomorphisms per orientation. Thus 2*c_g S1 components and 2m*c_m singleton components; no higher homology. Independently enumerated complete homomorphism adjacency for C5, C7 (two values of g), 5-/7-cycle wedge and bridge, with predicted circle/isolated counts; finite samples confirm, not prove all H.

## originality

PASS

The classical Hom(C_m,C_g) cycle homotopy and square-free codomain point-or-circle theorems are already known, but the quantitative global formula in two consecutive cycle counts and explicit free collapse for arbitrary girth-g target are the assessed refinements. The highly relevant Fujii/Kimura/Nozaki and Matsushita PDFs were accessed and their theorems reviewed; priority still carries a risk from generic component algorithms.

## value

PASS

A single natural graph-Hom functor extracts the two shortest relevant odd cycle counts as Betti and component statistics, with an explicit canonical collapse. The all-graph-girth theorem is structural and offers a useful graph-homotopy/cycle-count correspondence beyond the already known point/circle dichotomy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
