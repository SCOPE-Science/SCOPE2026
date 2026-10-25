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

The full-lattice STAB(P_n) facets x_i≥0 and x_i+x_(i+1)≤1 have primitive normals −e_i and e_i+e_(i+1), which become incidence vectors of a rooted path graph after alternating row signs. Total unimodularity shows simplicial normal cones are smooth. Every minimal dependent active ray set is a root-to-root graph cycle through indices p<q; its endpoint variables zero and all path edge sums one force alternating 0,1,0, giving a local three-coordinate rank-three nonsimplicial cone τ_j, 2≤j≤n−1. Each cone appears and every nonsmooth cone contains one, so the singular support has exactly n−2 irreducible orbit closures Y_j. Fixing x_(j−1)=0,x_j=1,x_(j+1)=0 splits the remaining stable-set face into independent paths, yielding X_(j−2)×X_(n−j−1), of codimension three. The primitive four-ray circuit dual semigroup has four Hilbert generators and equation uv−wz, hence conifold multiplicity two. Joint face intersections are nonempty exactly for nonconsecutive centers, and their toric orbit closures are irreducible, giving Ind(P_(n−2)); unimodularity identifies the singular and non-Q-factorial supports. Independently counted path vertices n=3..8 as 5,8,13,21,34,55 and singular fixed points 1,4,9,17,30,51; these finite checks corroborate, not prove, the all-n graphic-circuit argument.

## originality

PASS

PASS with residual priority risk. The inspected primary sources cover toric normality, chain/order-polytope equivalence and affine Hibi singular criteria, not a closed formula for the normal-fan projective singular components of all paths, their conifold transverse germs and exact independence-complex incidence. Separate same-batch even-cycle data do not logically imply this full path classification.

## value

PASS

A sharp infinite-family toric geometry classification identifies every irreducible reduced singular component, its dimension and product structure, local conifold model, and all higher intersections. For path stable-set polytopes these are natural geometric invariants useful in toric resolutions and adjacent graph families; the theorem is stronger than identifying individual small singular examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
