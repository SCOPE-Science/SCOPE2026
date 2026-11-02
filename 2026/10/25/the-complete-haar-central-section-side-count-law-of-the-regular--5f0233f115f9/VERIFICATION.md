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

Reconstructed 24 signed-permutation vertices (±1,±1,±(sqrt2-1)), 36 edges and 14 facets. The ordered-absolute-normal chamber 0<y<x<1 yields exact facet-crossing expression N=4+2[1<x+a y]+2[a<x+y AND y<1-a x]+2[y<x-a], a=sqrt2-1. Four threshold lines partition the chamber into six listed triangles/quadrilateral tiles, whose unit-normal spherical Jacobian is (1+x²+y²)^(-3/2), with 48 full-sphere chambers. Independent spherical solid-angle implementation gave four masses (0.151052693273...,0.500227288252...,0.281397356296...,0.067322662178...) summing 1 and expected count 6.52997997475809. For all 210,000 independent Gaussian directions, geometric original-edge counting matched the analytic piecewise formula exactly (zero other counts), and histograms matched within 0.00076. All-direction proof rests on exact inequalities and six-tile geometry, not finite random samples.

## originality

PASS

A previously published cube–octahedron intersection family result supplies the quadrilateral marginal of this regular truncated cube; that part is not claimed original. Lonke gives central *cube* means, related Resultary records give rectangular-box hexagon probabilities, random central 4-cube face vectors, width or tetrahedron quantities, not the full four-atom distribution for this truncated cube. Knowing p4, normalization and expected sides leaves additional degrees of freedom, so p8 and p10 require new chamber partitions. Older Voss 1982 might have a covering table; abstract-only and disconnected institutional access prevent confident whole-paper exclusion, captured as priority risk.

## value

PASS

The regular truncated cube is a canonical Archimedean solid. The exact four-atom Haar central-section law, including separate octagon and positive decagon masses, solves the full natural face-count distribution rather than a mean or single tail. It is needed to distinguish polygon-type frequencies in integral geometry, while the previously known quadrilateral component alone plus the mean does not determine other masses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
