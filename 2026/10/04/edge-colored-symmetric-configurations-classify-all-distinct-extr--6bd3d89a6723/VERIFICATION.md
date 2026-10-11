---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For two words of composition \(\llbracket1,\ldots,1\rrbracket\), if their supports intersect in \(r\) coordinates and agree in symbol on \(t\) of them, then \(d_H=2w-r-t\). Distance at least \(2w-1\) forces \(r+t\le1\), so supports meet at most once and no nonzero symbol repeats at a coordinate. Thus each coordinate is used by at most \(w\) words and incidence counting gives \(|C|\le n\). At equality, all point and block degrees are \(w\), producing a symmetric configuration \(n_w\); the symbols form a proper \(w\)-edge-coloring of its Levi graph. Conversely, König's line-coloring theorem gives such an edge-coloring for every \(w\)-regular bipartite Levi graph, and the resulting code has distance \(2w\) or \(2w-1\). The published \(n_6\) spectrum then gives equality exactly at \(n=31\) or \(n\ge34\), hence the threshold \(34\).

## originality

PASS

Chee--Dau--Ling--Ling's complete primary paper treats the exact same all-distinct weight-six family and explicitly leaves the \(n=33,34\) values undetermined, with only a threshold interval. Kaski--Östergård's complete primary paper independently gives the exact symmetric-configuration spectrum but does not state the coding correspondence. The audited two-way correspondence, including the symbol assignment as a proper Levi-graph edge-coloring and the König converse, is the missing bridge. Targeted Resultary and literature searches found no prior statement of that bridge.

## value

PASS

The correspondence resolves the only all-distinct total-weight-six gap explicitly left in the inspected coding table and converts the entire extremal equality layer into a classical configuration existence/classification problem. This is a motivated structural bridge with an exact threshold consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
