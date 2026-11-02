---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Read RESULT.md, exact reduced Swiatkowski weight-three basis/differential construction, and full verify.py. The truncated tetrahedral graph has 12 vertices, 18 edges, four disjoint 3-cycles and natural full S4 symmetry. The weight-three top and next chain modules have 1760 and 4752 integral basis elements, no chain group above degree 3. I independently rebuilt the F2 differential columns and recomputed rank 1756, so rational top nullity is at most four. Four products of the three distinct triangles omitting one face are actual integral cycles with disjoint supports and unit coefficients, giving independent primitive rank four; the source checks all 96 signed action equalities and the independent F32003 rank 1756. A unit-coefficient coordinate from each ensures any rational combination representing an integral kernel chain has integral coordinates. Natural integral chain model => H3=Z^4 as the four-point permutation lattice. Any equivariant retraction onto its invariant diagonal line would multiply the generator by 4, impossible over Z.

## originality

PASS

An–Drummond-Cole–Knudsen supplies natural reduced Świątkowski chains for all graph braid spaces, but does not tabulate the 18-edge truncated tetrahedron weight-three H3 S4 lattice. Maciążek–Sawicki provides product-torus generators and universal presentations for specific wheel/bipartite graph families, not this integral symmetry module; its open full-text Sections 5.1 and 5.3–5.7 were checked. Drummond-Cole small-graph tables stop at nine edges. Resultary same-truncated-tetrahedron matching-complex result uses a different simplicial object. Exact finite rank and integral sign-positive S4 action remain non-implied by the general model.

## value

PASS

The truncated tetrahedron is a canonical four-face polyhedral graph, and the space of three unordered particles has four obvious geometric triple-torus candidates that need not generate the full top integral homology. The theorem proves completeness and gives their full positive S4 permutation lattice and an exact integral invariant-splitting obstruction, which Betti numbers or a rational character do not alone settle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
