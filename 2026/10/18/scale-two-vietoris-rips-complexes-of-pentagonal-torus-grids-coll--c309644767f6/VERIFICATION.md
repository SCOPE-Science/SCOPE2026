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

For n>=7, the graph-metric radius-two clique is wholly in a column A_j, one of 5n middle-column distance-two facets B_ij with endpoints (i,j-1),(i,j+1) and three middle rows, or a unit-square tetrahedron C_ij. The unique middle column when n>=7 prevents additional mixed facets. Six explicitly ordered free codimension-one pairs in each B, then two free pairs in each C, give exactly 30n+10n=40n elementary collapses. The remainder is a 5-by-n square-triangulated torus with each of n full meridian four-simplices attached along its five-edge meridian. Replacing each contractible four-simplex attachment by a meridian disk up to homotopy and killing one primitive generator in the torus presentation yields S1 wedge n S2. Counting Z faces (5n,20n,20n,5n,n) and reversing 40n pairs yields original (5n,30n,55n,35n,6n). The argument is uniformly combinatorial, not extrapolated from n=7.

## originality

PASS

Best-of-knowledge PASS: Adams et al study square C_m square C_m and C5 square C5, not the rectangular C5 square Cn for n>=7; already published width-four torus has n copies of S3 rather than n S2. Neither implication supplies the claimed uniform collapse or dimension shift.

## value

PASS

A complete all-n>=7 homotopy classification and elementary collapse for the natural previously untreated width-five graph-metric rectangular torus at the first nontrivial radius; explicit f-vectors and n-dependent free H2 rank enable comparison across torus widths and persistence. The difference from width four (S3 spheres) and large square tori (torus) is substantive topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
