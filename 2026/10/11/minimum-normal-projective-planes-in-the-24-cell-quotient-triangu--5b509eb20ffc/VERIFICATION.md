---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: Reconstructed the published 12-vertex triangulation from its four symmetry generators and three facet seeds. The resulting order-24 action gives 48 tetrahedra, 96 triangles and 60 edges. Independent GF(2) row reduction gives ranks 48 for cocycle equations and 11 for vertex coboundaries, hence dim H^1(F2)=1 and 2048 representatives in its nonzero coset. Independent exhaustive enumeration reproduces exactly the ten weights 21:60, 23:132, 25:144, 27:240, 29:360, 31:408, 33:400, 35:240, 37:60, 39:4. Reconstructed local 1|3/2|2 tetrahedral cuts, with 36 minimum cocycles of disk profile (20 triangles,10 quadrilaterals) and 24 of (18,11); read the submitted checker’s connectedness and chi=1 tests and the proof of the converse for arbitrary normal RP2 using mod-2 intersection parity and Poincare duality. Weight>=support gives the universal lower bound, equality requires exactly one intersection on active edges, hence no missing multi-normal representatives. Finite enumeration is genuinely exhaustive on this one triangulation; it does not establish claims for arbitrary triangulations.

## originality

PASS

PASS best-of-knowledge: The Köhler-Lutz primary 2005 classification gives this exact vertex-transitive 24-cell quotient, incidence structure and symmetry group but does not report normal RP2 intersection systoles or the full nonzero H^1 cochain weight enumerator. A directly related Resultary record for the identical complex classifies shortest essential integral H1 triangular loops (64 in 4 orbits), a different primal invariant that does not imply the dual cocycle minimum or 60 projective planes. Normal-surface dualization itself is standard and not claimed new; the exact 21 bound, 60 minimizers, orbit decomposition and local disk profiles are the additional exact findings. Historical unindexed normal-surface computations remain a risk.

## value

PASS

PASS: A precise optimal normal projective-plane weight and complete minimizer/orbit classification for a natural highly symmetric triangulation of RP3 is a motivated triangulation-dependent normal-surface/coding-theoretic invariant, not merely a renamed topology fact. The weight enumerator and normal disk profiles distinguish configurations invisible to the previously known shortest H1 layer. It supplies an exact benchmark for normal-surface enumeration and cosystolic optimization; no invariance under changes of triangulation is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
