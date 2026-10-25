---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducible scientific checks

Run `python verify_polygon.py` from the directory containing this file and the packaged standalone script. The program uses Python standard-library rational arithmetic and trigonometric functions only; no internet access, external datasets, or third-party papers are required.

Exact rational checks of the cap shoelace formula give \(19/8\) on an equilateral triangle, \(233/108\) on a square and \(361/180\) on a regular hexagon. For the triangle and hexagon, dividing the vertical coordinate by \(\sqrt3\) makes all vertices rational; the area and first-moment ratio is unchanged. Four additional tests compare clipping against an independent two-parameter triangle quadrature on polygons with \(5,7,9,12\) vertices. Five more samples compare \(n^2(\Lambda_n-\Lambda_\circ)\) to \(5\pi\sqrt{15}/12\) at \(n=80,120,200,320,500\). The script passed all 15 groups on the packaged source.

These finite checks do not establish the general norm identity or the limit. The complete proof is in RESULT.md, using the reproducing kernel, convexity, polygon moment identities and controlled radial asymptotics. Floating-point comparisons use explicit tolerances, while the three rational values are exact equalities. The published priority check remains provisional. No independent audit or external verification has been performed.
