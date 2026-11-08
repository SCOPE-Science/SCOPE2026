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

PASS: Affine normalization sets John ellipse to B² and transforms genuine centrally symmetric six-tangent polygons into three opposite normal pairs. The symmetric John criterion is 0<θ_i≤π/2 and Σθ_i=π; contact vectors doubled in angle have origin in their convex hull. Direct shoelace/support-line computations give |K|=2Σtan(θ_i/2) and |K°|=Σsin θ_i. The resulting separable S=2Σf(θ_i), f=tan(t/2)+sin(t)/2, extends continuously to a compact cap triangle. On the boundary θ1=π/2, θ2+θ3=π/2; tangent-addition and AM-GM show the maximum only at θ2=θ3=π/4, giving S=5√2−1. Interior constrained equal-first-derivative cases have either equal angles (S=7√3/2) or golden-ratio two-equal saddle with positive second derivative direction; neither exceeds the boundary. Equality representative K0 is square clipped on two opposite diagonal corners, area 4√2−2 and polar 1+√2. Florian (1995), main theorem, gives S≥6 and square-only equality; genuine hexagons cannot attain but a continuous admissible degenerating hexagon path realizes all intermediate S values. Taylor expansion at maximizing gaps gives positive linear coefficient 3√2/2−2 in η and quadratic coefficient 8−11√2/2 in δ² with the stated mixed remainder. Source symbolic verifier matches normal area formulas but universal conclusion rests on exact optimization, not numeric sampling.

## originality

PASS

PASS subject to historical caveat: Full 2026 Böröczky–Makai source gives universal upper 2 for any centrally symmetric John-normalized plane convex body, a weaker numerical bound than (5√2−1)/π; its equality theorem does not imply the sharper six-tangent polygon optimum. Florian 1995 original theorem and proof establish the polar area sum LOWER bound 6, not this upper maximum (indeed the 1995 article explicitly cites the earlier Aczél–Fuchs result). Published Resultary enclosing-parallelogram theorem treats a different hexagon functional. No specific prior sharp upper or its equality form found; a historical tangential-polygon extremal source could nevertheless exist.

## value

PASS

PASS: The result sharpens a recently published affine area-plus-polar inequality specifically for a natural John-contact hexagon family, identifies a surprising nonregular maximizing affine class, all attainable normalized values and sharp local first-/second-order stability. This is a motivated exact extremal geometry theorem, not an arbitrary constant calculation or restatement of universal bound2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
