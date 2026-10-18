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

For K=[-1,1]^3 intersect ||x||_1<=2, each of the six rational centers ±(1,-1/4,-1/4), ±(1/4,1,-1/4), ±(1/4,1/4,1) lies on a square facet of boundary K; each pair difference has some coordinate absolute >=5/4 (antipodal at least 2), so centers are separated outside int K and translates K+2z_i touch K without overlapping interiors. The strict boundary-cover criterion reduces blocking to ∂K subset union_i(z_i+int K). The proposed polyhedral inset K_delta for delta=1/13 has |u_j|<=12/13 and sum|u_j|<=25/13, thus K_delta compactly within int K. Independently ran exact Fraction half-plane disjunctive polygon-clipping on six square and eight triangular facets for all six centers and 14 inset inequalities: every surviving complement branch is eliminated by sixth center on every facet; no random grid/tolerance was used. The complement uses >= violating inequalities, a conservative superset, and still empties, hence certifies the closed inset cover and strict blocking criterion. This proves only b(K)<=6, no matching lower bound.

## originality

PASS

Zong introduced blocking number and general translate-boundary characterization; Wang–Zhang treatment contains the boundary-cover equivalence and six-blocker statements for ℓ_p balls and other specific bodies, but full relevant article text inspected shows neither regular cuboctahedron nor its six rational centers. Published six-blocking regular truncated-octahedron construction is a combinatorially distinct body and does not transfer by affine invariance; cube/octahedron family illumination results concern a different invariant with no implication to six blocking. No earlier exact cuboctahedral six-center configuration or positive rational clearance was located in actual primary searches. Older unindexed translative blocking examples remain a specific risk.

## value

PASS

Regular cuboctahedron is an Archimedean solid and a canonical cube–octahedron intersection in geometric covering/packing. Its blocking number is a natural open-type convex-geometric invariant. An explicit interior six-translate blocking configuration with independent exact rational certificate and positive clearance answers a substantive upper-bound question; absence of a lower bound and nonoptimal clearance are correctly scoped, and no invented exact equality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
