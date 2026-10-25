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

The origin lies inside the 3D convex hull, so min_{|u|=1} support_P(u) equals its smallest origin-to-facet distance. For generic nonaligned delta the complete facets are top/bottom n-gons and 2n alternating triangles; for aligned delta their side triangles combine into n rectangles. The top/bottom planes have distance h; an upper-edge/lower-vertex face has outward normal proportional to (1,0,r(t-c)/(2h)) and distance D=hr(c+t)/sqrt(4h²+r²(t-c)²). The minimum is min(h,D). Exact positive squaring shows D>=h iff h²<=ct/(1+ct). On the post-switch branch D² is unimodal, with its critical x0=(t-c)/(2+t-c), strictly below switch x*=ct/(1+ct) because c+(2c-1)t>0 for c>=1/2. Hence the min support rises until x* and decreases afterward; at x* its value is sqrt(ct/(1+ct)). This increases strictly with t, whose unique maximum is at half-step delta=pi/n. Independent 3D SciPy convex hull calculations verified all facets/minimal origin support for 140 different (n,delta,h) choices against the exact formula; only symbolic facet and derivative arguments prove all-n result.

## originality

PASS

Best-of-knowledge distinct final theorem after comparison of equivalent objects, broader implications and exact accessible primary statements; not a historical priority guarantee. A small-N antipodal conjectural optimum or classical regular octahedron is not a proof of the formula for all n>=3 and continuously varying h,delta. The exact facet distances and unique regime switch genuinely add the quantified classification.

## value

PASS

A natural structured spherical-code problem obtains a complete two-parameter covering-radius law, sharp competing polar/lateral hole transition, and unique height/twist optimization at every n. It explains why covering-optimal antiprisms are generally not edge-uniform and why two-ring designs retain a pi/4 limiting cover radius; not merely one small numeric polyhedron.

The dated certificate retains the supplied scientific assessment, sources and limitations.
