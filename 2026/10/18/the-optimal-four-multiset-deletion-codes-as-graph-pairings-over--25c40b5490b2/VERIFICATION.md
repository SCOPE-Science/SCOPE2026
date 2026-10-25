---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The five multiplicity types (4),(3,1),(2,2),(2,1,1),(1,1,1,1) use, respectively, one (3) output; one (3) plus one oriented (2,1); two oriented (2,1); two oriented (2,1) plus one squarefree triple; four squarefree triples. Disjoint shadows give a+b<=q, b+2c+2d<=q(q-1) and f<=D(q,4,3), hence the known bound q+binom(q,2)+D. Equality forces all pure words, no (3,1), a maximum quadruple packing, and exact cover of every oriented double-single output. Absent pair-squares define even-degree graph H, while missing oriented arcs pair at each doubled center into distinct uncovered-support wedges. Conversely these necessary conditions give disjoint output shadows at all three types; hence the data classify all optimizers uniquely. For q even congruent 2 or 4 mod6, Steiner quadruple perfection leaves no uncovered triples; for q odd congruent 1 or 3 mod6, the parity lower bound and SQS(q+1) imply uncovered triples form a Steiner triple system, so an H edge would require the SAME unique uncovered triple to be assigned from both endpoints, forbidden. Direct independent q=6 construction with 3 quadruples and six-cycle wedges verified 24 codewords, 54 mutually disjoint three-multiset outputs and 6 mixed codewords. The existence theorem for SQS in the stated congruence classes is the credited classical input.

## originality

PASS

Best-of-knowledge distinct exact theorem after statement-level comparison: Full text of Zabokritskiy’s 2026 multiset-profile article could contain a sharper general equality-case theorem, not excluded by abstract-only material. Previously known ingredients are credited; no unsuccessful search is treated as novelty proof.

## value

PASS

Classifying ALL optimizers, rather than merely restating the established cardinality, is a natural mathematically useful equality-case problem. The graph H/even-degree/local neighbor-pairing parameterization exposes the precise freedom in missing pair-squares; Steiner quadruple systems force global rigidity in four infinite congruence classes, while the six-symbol mixed construction demonstrates the freedom is real in another class. These distinctions can matter for structural enumeration and selecting noncanonical code designs even when the optimum size is already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
