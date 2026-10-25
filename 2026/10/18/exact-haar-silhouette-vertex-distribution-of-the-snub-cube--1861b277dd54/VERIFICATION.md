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

The result specifies the Archimedean snub cube as a 24-vertex convex hull over Q(τ), τ^3−τ²−τ−1=0 (two mirror enantiomorphs equivalent by reflection). It certifies 32 triangular plus 6 square supporting faces, 60 edges, and 31 distinct facet-normal great circles. Apparent contour edges occur iff adjacent outward facet normal scalar products with a generic u have opposite signs. Exact rational-field sign order and finite planar arrangement gives 762 distinct circle intersection nodes, 1608 arcs, 848 chambers (Euler F=2+1608−762), with section silhouette chamber counts (F9,F10,F11,F12)=(96,288,336,128). The spherical Gauss–Bonnet boundary angle sum for each chamber produces 18 distinct arccos(sqrt(a_j+d_jτ+e_jτ²)) angle types, with complete coefficients in actual pinned ANGLE_FORMULA.json; summing over 848 regions and dividing by 4pi gives P(N=9)=.240831877715316..., P10=.448600849546146..., P11=.0916775535797135..., P12=.2188897191588237.... The pinned check.py exact rational interval sign arithmetic and table assertions were read in full (original script not reexecuted); I independently reconstructed snub vertices/facets/60 edges/31 normal planes via convex geometry, Monte-Carlo checked 300,000 projections with ONLY counts 9..12, and separately evaluated all 18 exact table-angle terms numerically, reproducing the four masses with <1e-12 deviation and sum=1. Exact finite chamber enumeration, when independently replayed, would certify all configurations; numerical checks alone do not replace that certificate; source uses exact arithmetic for arrangements.

## originality

PASS

Best-of-knowledge novelty is the specific fully quantified invariant, not the underlying classical method or any known special-case total count. The dual-section and appearance/orthographic silhouette aliases do not remove the need to integrate the 31-normal-circle arrangement; no searched matching full probability table was identified. The geometry and mean are prerequisites but do not determine probability of each 9/10/11/12 shadow count; broad methods are not dominating precomputed values.

## value

PASS

The snub cube is a canonical highly symmetric yet chiral Archimedean polyhedron, and the full Haar-view silhouette distribution is a natural stereological invariant not supplied by its face and edge counts. The unequal areas of 848 normal chambers make an exact 18-angle aggregation nontrivial and reusable for computational geometry/ray projection benchmarks; unlike counting the chamber census alone, its formula measures probabilities exactly. It is motivated finite classification, not an arbitrary tiny sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
