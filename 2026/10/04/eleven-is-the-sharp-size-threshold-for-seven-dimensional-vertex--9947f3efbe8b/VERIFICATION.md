---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Read actual vertex/facet assignment proof and Jahn–Winter Theorems 6 and 7. Contraposition of their sufficient criterion yields a face F with both F and F^Delta having more vertices than facets. In dimension seven, dim(F)+dim(F^Delta)=6 and neither can have dimension ≤2; both therefore are three-polytopes. Euler and 2e≥3v show strict vertex excess requires at least six vertices, attained by a triangular prism (6v,5 facets). Four exterior vertices are necessary to extend an affine 3-face to dimension 7, so any obstruction has ≥10 vertices. For exactly ten, six on F and four exterior points must span independent affine directions, yielding the free join F bowtie Delta_3; then only four ambient facets contain F, contradicting at least six vertices of F^Delta. Hence ≥11 vertices; duality gives ≥11 facets. Triangular prism T joined to triangular bipyramid T^Delta is 7D with exactly 11 vertices and facets and Hall-face obstruction 6+6=12>11 (Jahn–Winter Theorem 6). Checked original verify.py arithmetic; independent proof confirms its non-computational structural step.

## originality

PASS

Full primary Jahn–Winter theorem establishes the first obstructed dimension and the face criterion, with cube/cross-polytope join witness at 14+14, but does not derive sharp size eleven. The claimed simultaneous extremal bound requires a new equality-case tetrahedral free-join exclusion, and the prism/bipyramid witness is smaller than the displayed prior example; full comparison finds no stronger covering theorem.

## value

PASS

Determining the exact smallest dimension-seven counterexample to a natural vertex–facet nonincidence matching property is a canonical finite extremal problem. The 11-by-11 obstruction plus global lower bound improves the 14-by-14 published template and isolates a sharp geometric boundary using a nonroutine equality-case free join lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
