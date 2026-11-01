---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS: For the rectangular Voronoi cell D²=sum(a_i² U_i²), U_i independent uniform [-1/2,1/2]. Independently integrated the first three cumulants 1/12, 1/180 and 1/3780 and recovered S=sum x_i, Q=sum x_i², R=sum x_i³. Newton identities give cubic coefficients and volume product. Cauchy and an explicit (one large, two equal) positive triple give the exact two-moment feasible interval. The sorted trigonometric arc x_j=S/3+A cos(theta+2pi j/3) yields V²=B+E cos 3theta and the half-open zero-boundary at Q=S²/2. For stability, the polynomial coefficients are Lipschitz in moment data on positive compact families; the three-root Rouché matching gives a 1/3 exponent, and symmetric opposite delta-perturbations with equal first two moments and cubic third-moment difference rule out larger exponents. Independently checked collision/cumulant algebra. The checker is finite diagnostic; the proof is analytic.

## originality

PASS

PASS with explicit archival risk: A prior distance-distribution empirical-process paper on tori and papers on random triangles/energy do not supply, in the material read, a three-dimensional exact finite-moment inverse and sharp positive-volume fiber. The most similar published Resultary finite-moment reconstruction concerns projection volumes of Euclidean orthotopes, not quotient geodesic distances. Silverman 1978 full text remained inaccessible, so priority assessment is best-of-knowledge only.

## value

PASS

PASS: Intrinsic distance distribution on a rectangular flat torus is an isometry-invariant measurement; exact three-moment reconstruction, two-moment volume collapse threshold and sharp local instability are natural, mathematically useful inverse-geometric facts. The fiber is not merely Newton substitution: positivity boundaries and the full sharp volume interval need an exact geometric analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
