---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For each n>=2 and real 0<t<=2, the finite vertex metric has only hub-edge, spoke, and leaf-pair distances. All dual unit-ball constraints reduce to |s|<=t and |x_i|<=1, |x_i-s|<=1; each leaf-leaf bound <=2 is redundant. For s>=0, fiber x_i in [s-1,1]; for s<=0, [-1,s+1]. An interior leaf can perturb independently. When hub 0<s<t (or -t<s<0), choosing opposite small hub perturbations and moving the appropriate active leaf endpoints gives a nontrivial midpoint decomposition. At s=0, any corner x_i=+/-1 forces each midpoint summand hub to have a fixed sign while their average is zero; hence both hubs zero. At s=+/-t all endpoint choices are extreme by the active hub constraint. Therefore vertices are exactly three 2^n layers for 0<t<2 and two singleton boundary layers plus 2^n zero-layer corners when t=2. Polar duality between Lip_0 and finite Lipschitz-free balls transfers vertices to facets: 3*2^n vs 2^n+2. The excluded t=0 collapses two distinct metric points. Independently solved complete rational active-inequality intersections for n=2,3 and t=1/4,1,7/4,2, recovering exactly 12/6 and 24/10 vertices, respectively.

## originality

PASS

The t=1 unweighted book and t=2 redundant-edge bipartite graph counts are previously known and not claimed new. The surviving claim is a continuum 0<t<2 of one-edge weighted metric polytope vertex classifications including t<1, and a sharp facet jump at exactly t=2. Primary unweighted symmetric-edge-polytope results and three semantically close published metric families were compared by the actual parameter constraints; none logically specializes to the entire one-hub-edge path.

## value

PASS

Facet count and dual potential classification are canonical finite-dimensional Lipschitz-free geometry invariants, and an exact parameter-induced combinatorial transition at a redundant-edge boundary is mathematically motivated. It is not a mere unweighted graph recount: a full open interval of nongeneric metrics has a rigid facet spectrum and sharply loses 2^{n+1}-2 facets at its endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
