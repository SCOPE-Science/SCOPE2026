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

Affine normalization A=(0,0),B=(1,0),D=(0,1),C=(p,q) is valid when p,q>0,p+q>1; no pair of parallel sides precisely excludes p=1 or q=1. Schneider criterion z∈M_Q(u)⇒z∈Z_Q(u) reduces testing to four normal cones, with a midpoint singleton in each cone and four edge-normal middle segments. The four sign cases yield an excluded nonexposed midpoint and exclude all segment interiors by their second conflicting middle lines; barycentric coefficients in RESULT place the excluded corner strictly inside the triangle of the other three (positive and summing to 1). Schneider exposed-point lemma proves all three surviving vertices qualify. Rational polygon-union calculations for representative (p,q)=(2,2),(2,.8),(.8,2),(.7,.6) corroborate the table, not substitute for all-parameter cone analysis.

## originality

PASS

Schneider proves general existence and exposed-point tests for convexity points and develops polygonal middle hedgehogs; those results yield machinery but not the exact count for all nontrapezoid quadrilaterals. The four parameter cases and explicit midpoint triples add a complete low-complexity classification; independent rational tests support each region, not bibliographic novelty.

## value

PASS

The first generic asymmetric four-vertex polygon is a natural complexity threshold for reflection convexity. A complete affine-invariant classification with EXACT cardinality and explicit location of all convexity points sharpens Schneider’s general existence theorem and contrasts generic smooth-body infinitude, without claiming trapezoid boundary cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
