---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Normalize the leading sign first; the all-positive sign sector and its simultaneous negative copy have total sign probability 1/16. In magnitudes the last nontrivial Hurwitz minor gives B₂>u B₄+u⁻¹ B₀ with u=B₁/B₃, and implies the preceding minor. The folded-Cauchy u is independent of the three remaining magnitudes. The Gaussian cone (G₄>0,G₀>0,G₂−uG₄−u⁻¹G₀>0) already forces G₂>0, so its probability must be multiplied by eight. The trivariate sign expansion yields the two negative arcsines with correlations −u/s, −1/(us), s²=1+u²+u⁻². Inversion of u exchanges them and preserves the Cauchy measure; u=tan θ gives the stated compact integral and its exact coefficient. Leading coefficient, zero roots, and nonzero imaginary roots occur on null sets: for the latter, assuming A₃≠0 requires t²=A₁/A₃ and the quartic Hurwitz determinant to vanish. Independently, odd index occurs iff the product of roots A₀/A₄ is negative; complex pairs have positive product, so each odd index has mass 1/4 by the P(−z) symmetry. The cited Corollary 5.2/Lemma 3.1(c) also establishes that relation. A fresh 65-digit mpmath integration on [0,1,∞] of atan(u²/√(1+u²))/(1+u²) gave h=0.00928384472429811895714992419655543453132463760732168417153218…; this is not an interval certificate. The inspected frozen checker uses Simpson on the displayed θ parametrization and was not executed.

## originality

PASS

The same iid quartic ensemble, determinant, bound and exact linear index relations are already known. The surviving exact fact is the reduction of the endpoint probability to the stated single elementary quadrature, not the index relations or general Gaussian orthant identity. The most relevant primary source estimates the one unknown scalar rather than supplying this evaluation.

## value

PASS

This is the precise remaining unknown in an already studied Gaussian quartic index law. Reducing the five-coefficient probability to one smooth-ended elementary quadrature replaces Monte Carlo/least-squares estimates with an exact practical benchmark and determines the entire distribution when combined with known constraints. It does not claim a higher-degree result or an elementary closed form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
