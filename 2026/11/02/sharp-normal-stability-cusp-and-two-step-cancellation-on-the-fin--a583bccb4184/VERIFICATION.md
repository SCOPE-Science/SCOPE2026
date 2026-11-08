---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

PASS for even N>=4 identical-frequency globally coupled discrete-time Kuramoto–Sakaguchi and regular Z1=0, rho=|Z2|<1. Differentiation at Z1=0 yields J=I+(K/N)Q R_alpha Q^T, with Gram G=N^-1 Q^T Q positive, tr G=1, det G=(1-rho^2)/4. Thus N−2 unit tangent multipliers and normal lambda±=1+(K/2)(cos alpha ± sqrt(rho^2−sin^2 alpha)). The three exact Jury inequalities give strict normal contraction iff cos alpha<0, K>0 and K<K_c; K_c=-4cos alpha/(1−rho^2) below rho=|sin alpha| and 4/(−cos alpha+sqrt(rho^2−sin^2 alpha)) above it. These branches rise/fall, with max 4/(−cos alpha), including the sin alpha=0 endpoint nuance. Every rho<1 is realized by antipodal pairs. At alpha=2pi/3, phases (0,pi/6,pi,7pi/6) and K=4 the normal matrix is exactly [[0,0],[-2sqrt(3),0]], nonzero with square zero; this is derivative-only cancellation, NOT nonlinear finite-time extinction. Independently recomputed exact Gram and Jordan nilpotence. 

## originality

PASS

PASS with material full-text priority caveat. Continuous-time Ashwin–Bick–Burylko 2016 studies first-harmonic-incoherent families, and published discrete quadrature two-cluster and repulsive network results concern different reductions. The 2026 Gade–Gupta paper studies discrete phase-lag model; accessible abstract emphasizes continuum Lorentzian-frequency stability and numerics, while its full text was not obtainable via OA/arXiv or authorized institutional connection. Therefore no categorical claim it excludes this exact normal classification; residual priority risk retained.

## value

PASS

PASS. The second harmonic distinguishes phase geometries with identical vanishing first harmonic, and exact normal stability optimizes allowable discrete gain. The interior cusp and nontrivial square-zero derivative are meaningful structural phenomena specific to the finite discrete-time phase map and do not follow from continuous-time stability slogans.

The dated certificate retains the supplied scientific assessment, sources and limitations.
