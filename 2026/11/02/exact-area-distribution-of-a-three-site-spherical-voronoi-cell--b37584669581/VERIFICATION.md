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

A site-labelled Voronoi cell is the intersection of two origin-centered bisector hemispheres and hence a spherical lune of perimeter 2π and area 2(π-Θ). For fixed tagged north-pole site the independent bisector normals have density (e·n)_+/π; integrating their angle by the Gaussian ReLU positive-wedge formula gives an exact density and CDF [a(2+cos a)-3 sin a]/(6π), 0<a<2π. Independent SymPy integration confirms CDF derivative, E A=4π/3, second moment 20π²/9−10/3, P(A<=π)=1/6, variance 4π²/9−10/3; exchangeability and A1+A2+A3=4π give covariance 5/3−2π²/9. Proof is exact; simulations are not used as an unrestricted certificate.

## originality

PASS

Kabluchko–Thäle give spherical binomial-Voronoi typical-cell face statistics in the same random-site model, and Cho–Saul already give the Gaussian angular kernel. Those inputs do not, in the inspected primary sections, give the complete area CDF/variance for a site-labelled 3-site cell; Li et al. concern random query-to-fixed-site nearest distances. A prior unindexed spherical-lune-area law remains possible.

## value

PASS

Three sites give the first nontrivial site-labelled spherical Voronoi area law beyond two, while the cell perimeter stays deterministic and combinatorial face counts alone cannot supply area fluctuations. The closed distribution, moments and covariance are natural exact benchmarks for random spherical tessellation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
