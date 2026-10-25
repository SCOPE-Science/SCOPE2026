---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The Crofton motion-invariant line measure of lines hitting a convex polygon is its perimeter; a segment has hit measure twice its length. For adjacent sides AB and BC, their union of hit-line sets equals the hit-line set of triangle ABC almost everywhere; inclusion-exclusion gives joint measure |AB|+|BC|-|AC|. Thus normalized side lengths a_i=m_i/2 and two-step chords b_i=a_i+a_{i+1}-q_i, whose cosine law uniquely fixes all interior angles. Positive turns summing to 2pi plus vector closure with lengths a_i give a strictly convex closed polygon and are necessary/sufficient. Compact strict angle/side lower bounds imply inverse local Lipschitzness; equilateral lengths make m_i=2/n. Independently computed random convex polygon side incidence by angular quadrature; maximum error approximately 2.64e-9. This finite test corroborates only, not proves the full converse.

## originality

PASS

Cauchy-Crofton normalization, triangle inclusion-exclusion and law of cosines are classical individual tools. Harutyunyan–Ohanyan 2009 and Bäsel 2012 derive chord-length laws mainly for regular polygons, not labeled local-edge hit marginals plus adjacent joint-event inversion for all strictly convex polygons. Gates characterizes triangle/quadrilateral from richer whole chord-length distributions. The complete sparse inverse and global feasibility criterion are a distinct theorem on inspected evidence; residual older side-pair integral geometry priority remains.

## value

PASS

Identifying a labeled convex polygon from only local single-side and adjacent-pair Crofton hit probabilities is a sparse reconstruction problem with natural input observables. Explicit inverse, global feasibility and nondegenerate stability establish substantially more than routine side-length formulas, and the equilateral q-only reduction is a motivated special subclass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
