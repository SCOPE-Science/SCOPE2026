---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Finite m6 gives a mean-square second derivative with Gaussian increment variance bounded by m6 times the squared separation. Kolmogorov continuity and integration give a C² version. Bulinskaya's lemma applies to X' (its one-point Gaussian density is uniformly bounded), so critical points on compact intervals are simple. Rice gives J using independence of X' and X'' by evenness of the covariance. The disjoint open two-mesh intervals around strict lattice peaks each contain an interior continuous maximum; the two end effects disappear in the expected intensity. For V=1-r(h)>0 the comparison differences have correlation (1-2r(h)+r(2h))/(2V), giving the stated arccos formula including perfect correlations by continuity. For u=(4V-V(2h))/(2V), u=(m4/(2m2))h²[1+(m4/(12m2)-m6/(6m4))h²+o(h²)]; the square-root and arccos corrections combine to the stated coefficient. Its numerator is m2² times the variance of ω² under the derivative-energy law. In the bandlimit range the arccos input is the mean of cos(hω) under the (1-cos(hω))-weighted spectral law. This law is a decreasing positive tilt, in ω², of the derivative-energy law, so its mean ω² does not increase. Strict convexity of cos(h sqrt(x)) on [0,Ω²] (sin z-z cos z>0 for 0<z≤π) gives strict Jensen unless ω² is constant there. The tilt preserves nonzero spectral support. For one absolute frequency the formula gives p_h=hω*/(2π) through hω*=π, including the perfect-correlation endpoint. A zero-frequency atom has no effect.

## originality

PASS

The already-known exact discrete probability and leading infill limit are not new; the second-order coefficient is a direct refinement of those formulas. The inspected results do not give the combined all-mesh non-overcount and sub-Nyquist rigidity characterizing equality, which is the supported distinct contribution.

## value

PASS

The strict equality classification answers when sampling preserves an exact continuous extrema intensity at a finite spacing. It separates a single-frequency process from genuinely mixed derivative spectra even below Nyquist; this is more informative than the sign of the infinitesimal bias. The explicit coefficient further quantifies discrepancies among processes that share the same continuous peak intensity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
