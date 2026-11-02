---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For q>=2 and 0<r<1, the subcritical resolvent kernel equals (1-r²)/(1-rA+qr²) on the full adjacency spectrum [-2sqrt(q),2sqrt(q)]. Differentiating r yields g_r(t) strictly increasing, so its endpoint constraints give exactly the two sharp b bounds. At r=q^{-1/2}, the Vergara radial positivity matrix becomes r^{i+j}(min(i,j)+1)(alpha+beta max(i,j)), with PSD precisely between b=0 and b=(q-1)/(q+1): negativity of diagonals for b<0, of 2x2 minors for larger b; endpoint Gram matrices and convexity show sufficiency. For r above critical, normalized adjacent-index minors tend to -[beta/(1-(qr²)^-1)]², excluding b!=0, and pure r^distance is PSD via negative-type tree metric. This proves all finite subsets and included boundaries analytically; the independent SymPy and Fraction checks only corroborate formulas and one minor.

## originality

PASS

PASS on inspected primary literature: Vergara (2019) supplies the essential general positive-trace-class criterion, not an evaluated first-order exponential sharp cone; Haagerup/Steenstrup/Szwarc and Haagerup/Knudby provide general multiplier/spherical-measure theories rather than an identical family-specific three-regime evaluation. Semantic indexed Resultary search found no dominating record. The first-order cone is a nontrivial explicit application, though a differently worded prior evaluation remains a real priority risk.

## value

PASS

The distance-perturbed exponential is a natural first-order deformation of a tree covariance. Exact admissible coefficients, their one-sided threshold and complete rigidity above critical decay are usable and structurally motivated infinite-tree facts; the sharp border follows distinct spectrum and radial-matrix obstructions rather than routine a posteriori samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
