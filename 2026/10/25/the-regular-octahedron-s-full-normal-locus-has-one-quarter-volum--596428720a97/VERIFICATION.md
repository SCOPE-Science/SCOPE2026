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

For each of the eight facets, projecting y to the plane s·x=1 gives barycentric 3lambda_i=1+2s_i*y_i-s_j*y_j-s_k*y_k. Minimizing across sign choices and vertices gives precisely 1-||y||_1-||y||_infinity; strict positivity is equivalent to projections in all facet interiors. Edge normal-cone inequalities simultaneously reduce to ||y||_1+||y||_infinity<=1, and all six vertex normals occur throughout int(O). In strict interior of Sigma3 the 6+12+8 distinct base points give 26, and a boundary facet-edge collision prevents 26 at equality; outside some facet foot is inactive. Independently integrated the chamber 0<=z<=y<=x, 2x+y+z<=1 symbolically to 1/144; 48 chambers give vol Sigma3=1/3, while vol O=4/3, yielding exactly 1/4. Independently verified facet barycentric minima for representative rational interior, exterior and boundary points. No claim about other octahedra or full count distribution.

## originality

PASS

Best-of-knowledge PASS for the exact full-normal active region and uniform-volume fraction of a specific non-simple Platonic polyhedron. The materially inspected Nasonov–Panina–Siersma primary paper introduces the normal-count framework and studies general three-dimensional bounds and simple-polytope cases, not an explicit regular-octahedron active region or its volume. Other Resultary octahedral findings address projection width/diameter and moments, not normal concurrency.

## value

PASS

The exact 1/4 fraction measures the robustness of the maximal normal-concurrency locus under a natural uniform interior distribution, not merely its nonemptiness. The octahedron is a canonical non-simple polyhedron; complete identification of its 26-normal region gives a motivated, exact, independently checkable geometric invariant that can anchor average-count or perturbative studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
