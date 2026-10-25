---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

At minimizing parallel supporting lines in the plane, either two integer vertices (distance ≥1) or a supporting primitive edge and an integer opposite support vertex give a nonzero integer determinant over the primitive edge norm, hence distance ≥1/sqrt(M(a,b)). For every maximizing positive primitive (p,q), modular inverse produces lattice (x,y) with p y−q x=1 inside [0,p]×[0,q] and strictly interior orthogonal projection to segment (0,0)−(p,q); distance equals 1/sqrt(M). Equalities force primitive maximal direction, determinant one, and projection contact; conversely those contacts attain the bound. A corner is primitive iff gcd(a,b)=1. For a=28t,b=36t, t≡1 mod21, gcd(a−1,b−1)=1; the top three candidates on each boundary side share nontrivial factors (4t/7/2 or 4t/3/2). Remaining side candidates are strictly inferior by differences 88t−7 and 40t−7. Independent exhaustive primitive searches for t=1,22,43 reproduced unique maxima (27,35),(615,791),(1203,1547), and determinant witness (10,13) at t=1.

## originality

PASS

Deza–Liu–Pournin prove exact minimum in a square [0,k]^2, and the general kissing-polytopes framework studies cubes. The rectangular parameter pair (a,b) is not reducible to the Euclidean square theorem by anisotropic affine coordinate normalization because Euclidean lengths are changed. The novel all-a,b primitive maximum identity, equality witness and infinite interior extremizers are not covered by the square formula itself.

## value

PASS

Replacing a square with an anisotropic integer rectangle is a natural variant of the established kissing-polytopes invariant. A complete optimal formula and equality conditions for all a,b reduce geometry to arithmetic, while an explicit infinite interior-extremizer family disproves naive side-boundary search. The distinction is substantive: Euclidean distance is not preserved by rectangular normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
