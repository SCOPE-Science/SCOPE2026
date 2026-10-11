---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The proof reconstructs exactly. Same-class twins are mutually maximally distant. Distinct classes on the same bipartition side are not mutually maximally distant because a vertex in the larger neighborhood difference witnesses distance three from the lower class. A cross pair is mutually maximally distant exactly for an inversion of the canonical order. Hence the strong resolving graph has class cliques and exactly those inversion cross edges. Any independent set uses at most one vertex per class; if its largest selected B-index is q and smallest selected A-index is r, then q is at most r, so size is at most p+1, with equality only at one cut q=r=t and with all eligible classes represented. Complements give every strong metric basis and the stated count. The K2 boundary is correctly separated. The packaged exhaustive checker is consistent with this proof through order nine and is not needed for the infinite argument.

## originality

PASS

Originality passes. The broad distance-hereditary paper supplies an efficient recursive algorithm, and the chain-graph paper treats ordinary metric and restricted-threshold dimension. Neither inspected source states the chain-specific mutually-maximally-distant relation, the closed strong-dimension formula, or the complete minimum-basis classification. The new content is the exact strong-resolving graph and its unique-cut maximum-independent-set structure.

## value

PASS

Strong metric dimension is a natural shortest-path invariant with hard general computation. The theorem turns a natural graph class into an exact canonical structure and classifies every minimum basis, not just its cardinality. The product-sum enumerator also retains information that the scalar dimension forgets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
