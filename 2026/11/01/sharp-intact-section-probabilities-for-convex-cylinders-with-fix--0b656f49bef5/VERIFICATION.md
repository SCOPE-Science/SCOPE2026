---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For C=B×[-H/2,H/2], affine plane normal (sin θ v,cos θ) has conditional offset intervals L_hit=H cos θ+w(v)sin θ and L_intact=[H cos θ−w(v)sin θ]_+. Integrating against sin θ dθ dφ gives p=2〈F_H(w/2)〉/(H+πr) with F_H(x)=H/2−x arctan(H/(2x)). Cauchy perimeter gives 〈w/2〉=r, and F_H″(x)=4H³/(H²+4x²)²>0. Jensen yields lower envelope (H−2r atan(H/(2r)))/(H+πr) with iff w≡2r; planar zonoid representation q(v)=πr/2 ∫|cos(v−α)|dν and another Jensen give the upper envelope (sqrt(H²+π²r²)−πr)/(H+πr), strict for full-dimensional B and approached by thin rectangles. Strong Jensen over 0≤q≤πr/2 proves the stated width-variance remainder. For disk, E=sin θ and direct density integration yields the displayed normalized CDF and beta limits. The proof covers all compact convex bases with nonempty interior and all H>0; invariant conditional offset measure, not independent normalized offsets. Independent SymPy identity and square-base angular integration match, p≈0.084448543074 at H=2,r=1 between 0.08347679447 and 0.11331102324; finite/numeric checks are corroboration only.

## originality

PASS

Originality is best of knowledge after Resultary and published literature comparisons. IUR affine-plane sampling, Cauchy perimeter, zonoid representation and classical Jensen are prior tools; the inspected 2023 primary paper develops distributions of section area/chord length under an invariant model, not the event that no cap truncates a convex-cylinder slice. Dirksen treats central cylinder sections and maximum area, not affine-plane intactness with fixed base perimeter; oriented-cylinder model fixes orientation. No source inspected implies the sharp complete width envelopes and disk conditional eccentricity law. Unindexed or implicitly equivalent stochastic-geometry work remains a genuine risk.

## value

PASS

A natural stereological sampling model needs to distinguish cap-truncated sections from complete sections. The result gives an exact shape-optimized probability interval, identifies all constant-width minimizers and the unachieved degenerate supremum, and supplies a quantitative width-rigidity test and disk eccentricity distribution. These solve specific substantive distribution/extremal questions, not merely repeat Cauchy perimeter identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
