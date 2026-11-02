---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For n>=2, H_n=K_{n,n} square K2 with arbitrary independent proper n-color horizontal factorizations on the two layers and one shared vertical color has 4n vertices and n+1 perfect-matching color classes M_c, each 2n edges. Connectivity of W union M_c forces |W|-|W cap M_c|>=2n-1. Sum across partitioning color classes yields n|W|>=(n+1)(2n-1), so |W|>=2n+1. Construct W as n-1 horizontal edges at a0 in layer0, n horizontal edges at b0 in layer1, plus vertical edges at a0 and b0. It has 2n+1 edges. Contracting vertical color gives a spanning double-star; for any horizontal perfect matching, layer1 is connected, layer0 has at most an isolated matched pair at b0 plus its main component, and the selected vertical edges connect both to layer1. Thus the formula holds uniformly for every permitted independent pair of factorizations, not only matched identical colorings.

## originality

PASS

Best-of-knowledge originality qualified by material actually accessed. The explicit factorization-independent upper construction is an additional implication absent from the inspected prior general component theorem. Relevant literature not wholly indexed or accessible; see source_inspections and residual_risks.

## value

PASS

The color-connecting wild number is a natural graph invariant and the general component obstruction alone leaves the upper bound open. The robust double-star construction supplies a sharp exact infinite-family formula even when horizontal one-factorizations differ across layers, a concrete extension outside known product hypotheses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
