---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The only linear dependence among centered simplex vertices is Σ a_i=0, and R_Δ is centrally symmetric about zero. Its support h(u)=Σ max(0,u·a_i)=1/2 Σ|u·a_i|; the origin-centered inball is optimal by averaging the translates c+rB and −c+rB. For each pair (i,j), the d−1 remaining vertices are linearly independent; any unit u_ij normal to them leaves projections t_i=−t_j, giving h(u_ij)=|u_ij·(a_i−a_j)|/2≤||a_i−a_j||/2. Since r=min_{||u||=1} h(u), all edges obey 2r≤edge length≤diam≤1. Equality forces every edge to be unit, hence regular. Conversely, Živaljević 2013 Proposition 7 identifies the regular zonotope with intersections of edge-normal strips through a_i,a_j; for unit regular edge, each strip’s bounding hyperplane lies exactly 1/2 from the center, hence 1/2B⊂R_Δ. The inequality also gives all pairwise lengths≥1−ε in near equality. Independent singular-vector normal checks for random centered simplices d=2..9 reproduced special support identities; the exact proof is dimension free.

## originality

PASS

Živaljević gives the general Δ-zonotope and Makeev problem and a regular-simplex strip identity, but not the edgewise inradius bound or regularity rigidity across arbitrary generating simplices. Hausel–Makai–Szűcs address the regular universal cover and prove d=3, not diameter-constrained inradius optimization over all simplices. Bezdek’s fixed-inradius intrinsic-volume minimization is a different constraint/objective, and its original full text was unavailable; residual minimum-width folklore risk is recorded. Broader vertex-transitive zonotope radii indexed separately do not cover nonregular simplex generators, which are generally not vertex-transitive. The exact edgewise estimate passes best-of-knowledge originality.

## value

PASS

The unit Euclidean ball is the canonical diameter-one symmetric test body in Makeev’s universal-cover setup. Identifying the regular generator as the unique best inball container under the very same diameter constraint is a motivated structural extremal fact, not a routine normalization exercise. The inequality controls every generating edge individually and provides immediate near-extremal edge-length rigidity; it can be used to compare candidate generators before tackling universal covering, without claiming a new covering theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
