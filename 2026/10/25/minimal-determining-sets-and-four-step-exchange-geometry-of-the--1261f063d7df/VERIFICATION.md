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

For the 16-vertex Cayley graph on F_2^4 with five directions summing to zero, every nonzero difference has a unique representation with one or two directions, giving Aut(G)=F_2^4⋊S_5. Given one anchored selected vertex, its pointwise stabilizer is trivial iff all five direction-incidence columns are distinct. Exhaustively evaluating all 2^16 vertex subsets by this elementary criterion, and separately by explicit action of all 1920 automorphisms, yields precisely 560 minimal 4-sets and 192 minimal 5-cycles; the two independent complete methods classify all candidates including converse. BFS from every one of 560 optimal bases yields connected 5920-edge exchange graph, every eccentricity 4, degrees 20 or 28, and the two printed layer profiles. Independent reimplementation recovered the same exhaustive invariants. As the universe is fixed finite, exhaustive enumeration is a proof, not an extrapolation.

## originality

PASS

Boutin develops determining sets and exchange behavior for graph families; Bailey–Cameron translates to group base size, and Clebsch graph tables give automorphism group and graph invariants. No inspected stronger theorem/classification or database entry determines this exact complete inclusion-minimal Clebsch census together with all-base four-step exchange geometry; risks of unindexed finite tables or complement nomenclature remain.

## value

PASS

The 16-vertex five-regular Clebsch graph is a canonical highly symmetric strongly regular graph. Its complete minimal pointwise-base census reveals two different minimal cardinalities (nonmatroidal) yet a connected radius/diameter-four optimum exchange graph, supplying a motivated exact natural combinatorial reconfiguration invariant rather than arbitrary small-instance arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
