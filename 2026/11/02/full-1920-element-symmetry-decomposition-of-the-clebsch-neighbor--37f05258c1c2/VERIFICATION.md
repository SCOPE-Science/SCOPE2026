---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Rebuilt the even-vector Cayley model, 352 faces with f-vector (16,80,160,80,16), and four boundary ranks (15,65,64,16) using exact modular elimination and dimension-saturating chain inequalities. An independently written group-action computation enumerated all 1920 signed simplicial Lefschetz traces, finding character sum 0 and squared sum 5760. Fourier projection onto the three translation-dual orbits of sizes 1,5,10 identifies wedge^2 U5 (dim 6), epsilon4 tensor U4 (induced dim 15), and sign3 (induced dim 10); their Clifford little-group irreducibility and dimensions exhaust b2=31. Rational transfer after barycentric subdivision gives acyclic reduced G-quotient; no integral assertion is inferred.

## originality

PASS

The same Clebsch neighborhood complex is already known non-equivariantly to be a wedge of 31 two-spheres. The full 1920-element homology character, three nonisomorphic rational constituents and vanished invariant subspace are not fixed by that homotopy type. Applicable primary neighborhood-complex theory provides the construction, not the group representation. A different exact character calculated under an alias remains possible.

## value

PASS

The 5-regular Clebsch graph is a canonical strongly regular symmetric graph. Computing its complete equivariant rational H2 and quotient invariants distinguishes group actions invisible to the already known Betti numbers, a naturally motivated finite structural classification rather than a recomputation of homology rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
