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

The upper bound is realized by placing label 2 on one deleted matching pair and 0 elsewhere. For weight at most 3 there can be at most one label-2 vertex; every same-side vertex then lacks a label-2 neighbor and must be positive, which forces weight at least 4, with the n=3 boundary checked separately. At weight 4 there must be exactly two label-2 vertices and no label-1 vertices; they must lie in opposite parts, and the zero vertex paired with the opposite label-2 vertex forces the two indices to coincide. Thus the minimum is 4 and the minimum functions are exactly the n deleted-pair labelings. The inspected verifier independently exhausts all ternary labelings for n from 3 through 7 and matches both the optimum and the complete minimum-set classification; this finite check corroborates but does not replace the all-n proof.

## originality

PASS

The 2018 regular-graph paper supplies degree-based upper bounds and packing methods but no crown-graph equality or classification of all minimum functions. The 2019 algorithmic paper proves hardness on bipartite graphs and gives algorithms for cographs and other structured classes, but crown graphs are not covered there by an exact closed theorem and no crown formula was located in the full accessible article. Targeted Resultary searches returned related domination variants on crown graphs and Roman variants on complete multipartite graphs, not the same perfect-Roman crown statement. The submitted exact optimum together with the complete minimum-function classification therefore survives best-of-knowledge comparison.

## value

PASS

Crown graphs are a standard dense regular bipartite family, and perfect Roman domination is a natural exact invariant on them. The result gives both the optimum and every optimum, not merely another upper bound, and the deleted-pair structure is a reusable boundary example for perfect-Roman behavior on dense bipartite graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
