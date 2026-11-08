---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS. Rebuilt the Fano incidence geometry with point/line dot product over F2 and the magnitude-chain definitions. Verified chain counts C2=840,C3=2268,C4=1134 from length-4 distance compositions; each nonzero ∂4 column is supported on unique distance-two-shortening 3-chain in girth-6 graph, so distinct columns do not overlap and exactly 42 backtracking directed-edge chains lie in ker∂4: rank∂4=1092, with primitive direct-summand image. Checked explicit integral preimages for all 2-chain endpoint cases, giving ∂3 integral surjectivity and free rank 2268-840-1092=336. Character follows from equivariant exact chain sequences as χ(C3)-χ(C2)-χ(C4)+χ(ker∂4); independently enumerated all 168 GL3(F2) collineations and their 168 point-line correlations, recomputed fixed-tuple traces for every element, obtaining {trace 336:1, trace 0:335}. Maschke semisimplicity and uniqueness of rational characters imply the claimed regular rational module. The group universe is genuinely exhausted, not a random subsample. The finite computation is supplemented by the proof of integral surjectivity.

## originality

PASS

PASS best knowledge: full previously published Heawood and finite-plane records give mod-two or fieldwise endpoint-localized ranks, respectively. Neither determines the action of all 336 graph automorphisms. Related full Heawood symmetry representations found by Resultary are on matching/independence complexes, not this magnitude chain complex. A coincidence of dimension with |Aut(H)| does not imply a regular representation.

## value

PASS

PASS. The full rational 336-element symmetry character is a natural representation-theoretic refinement of a known scalar rank at the first girth-six off-diagonal magnitude-homology boundary. It determines all irreducible multiplicities and full-subgroup invariant dimensions, not a routine restatement of the numerical rank or an arbitrary code test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
