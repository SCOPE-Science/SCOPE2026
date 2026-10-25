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

For n≥3 over algebraically closed arbitrary-characteristic k, the affine lattice of crown-edge polytope P_n is saturated by integral transportation. The inequalities x_i,y_i≥0, sums=1 and x_i+y_i≤1 exhaust facets. Each edge vertex makes at most two h_i=1−x_i−y_i active, so a face with one diagonal facet has two arms and smooth generic interior unless contained in a row/column star; two active diagonal facets force a reverse-edge segment. The respective normal cones are nonsimplicial at row stars and reverse-edge segments, and all other cones are unimodular; hence the *reduced* singular support is exactly 2n row/column P^{n−2} plus C(n,2) reverse-edge lines. The transverse saturated generators (e_i,0),(e_i,1) give rank-one 2×(n−1) and 2×(2n−4) determinantal cones of multiplicity n−1 and 2n−4; coordinate supports give exact incidence. Does not assert global nonreduced singular scheme.

## originality

PASS

Best-of-knowledge original exact *all-n reduced singular component geometry*, intersections, and transverse types; general toric fan and graph edge-polytope criteria are credited, and Hilbert-series/degree/normality data of the same monomial model cannot imply this classification without new local work.

## value

PASS

A natural diagonal-free Segre embedding is an important basic toric statistical model; explicit singular support includes an unexpected reverse-edge stratum alongside star spaces, a genuine equidimensional-to-mixed-dimensional transition, and two exact transverse local singularity families. These are independently usable geometric invariants rather than a numerical tiny gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
