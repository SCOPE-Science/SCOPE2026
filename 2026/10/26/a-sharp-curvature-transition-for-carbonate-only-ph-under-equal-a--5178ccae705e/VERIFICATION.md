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

PASS: Idealized three-species carbon equilibrium has x=[H+]/K1>0, r=K2/K1>0, C/A=(x²+x+r)/(x+2r) with positive derivative onto C/A>1/2. Exact second pH derivative is a positive factor times P_r=x³+6rx²+(16r²-r)x+2r². Symbolic differentiation and exact discriminant -4r³(4r-1)²(112r-1) were recomputed independently; at r=1/112, P=(8x+1)(28x-1)²/6272, root x=1/28 maps to C/A=6/7. Cubic sign and Descartes analysis yield strict convexity for r>=1/112 (isolated zero curvature at equality), exactly two inflections and +,-,+ for r<1/112. Taylor expansion yields concentration gap 8A/3 sqrt(1/112-r)+O(A(1/112-r)). Jensen and local reverse Jensen give claimed pooling-bias signs; no universality asserted when mixing across regions.

## originality

PASS

Deffeyes carbonate mass action, Schulz et al fixed-alkalinity changes, Egleston et al buffer factors are old. The new claimed output is exact global Hessian sign phase at 1/112 and onset for the carbonate-only, fixed-A idealization. Wigley–Plummer 1976 specifically treats carbonate-water mixing but only abstract was accessible, a material historical-priority risk, not an automatic rejection.

## value

PASS

Exact global curvature and sharp bifurcation distinguish physically motivated equal-alkalinity averaging regimes and both signs of bias. The complete one-variable two-inflection classification and square-root onset have use even within simplified carbonate-water models; not full seawater or environmental field inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
