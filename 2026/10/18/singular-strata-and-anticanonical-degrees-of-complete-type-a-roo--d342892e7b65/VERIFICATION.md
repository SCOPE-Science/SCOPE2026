---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For any n>=4 over an algebraically closed field of arbitrary characteristic the source uses the face fan, not the normal fan, of P=conv(e_i-e_j) in the saturated root lattice sum z_i=0, dimension n-1. Every proper face is indexed by disjoint nonempty top and bottom index sets A,B of a linear functional and spans the incidence vectors of K_{|A|,|B|}. Its cone has |A||B| primitive rays and rank |A|+|B|-1. It is simplicial precisely when one side is singleton, and such a star-tree incidence set extends to an integral root-lattice basis, so is smooth. Every nonsmooth cone contains a minimal 2x2 square cone, giving exactly 6*C(n,4) irreducible reduced singular components of dimension n-4. At each minimal square cone the saturated four-index root sublattice and remaining quotient coordinates w_c=e_c-e_b give the product fan of n-4 copies of P1, hence component (P1)^(n-4). Four rays have primitive parallelogram relation and the transverse completed ring is K[[u,v,s,t]]/(uv-st), the ordinary threefold node. The root polytope is reflexive and terminal because its only lattice points are 0 and roots and the polar has integral 0/1 vertices. The anticanonical polar face dual to the square cone is a unit (n-4)-cube, inducing O(1,...,1), so each component has degree (n-4)! and reduced singular support total degree 6*C(n,4)*(n-4)!=n!/4. Independent complete enumeration of disjoint two-by-two pairs for 4<=n<=8 recovers counts 6,30,90,210,420 and exact degrees 6,30,180,1260,10080; all n rests on cone and lattice proofs.

## originality

PASS

Best-of-knowledge original portion is the complete all-n minimal-singular-cone/component classification with product geometry, local conifold and polar-derived anticanonical degrees; classical full type-A faces, Gorenstein terminality, smoothness obstructions are excluded.

## value

PASS

The full type-A root polytope is a standard natural terminal toric Fano family. Its reduced singular locus has a complete, uniform K2,2-indexed component geometry, a canonical node transverse singularity and an exact anticanonical cycle degree in every dimension. These intrinsic geometry and intersection-theory data go substantially beyond the known binary smoothness obstruction or tiny face enumeration and can serve later toric intersection and deformation calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
