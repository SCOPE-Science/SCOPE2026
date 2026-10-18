---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The final theorem quantifies genuine continuous copulas Cφ(u,v)=uv[u+(1−u)φ(v)] with φ differentiable in (0,1), φ≤1, vφ(v)→0 at zero, φ+vφ′≥0, vφ′≤1, and mandatory continuity at v=1 with φ→1. Since vφ is nondecreasing from 0, φ≥0; integrating φ′≤1/v to the upper endpoint gives φ(v)≥max(0,1+ln v). With D(v)=v(1−φ(v)), the Spearman rho is −2∫D(v)dv and its infimum is −(1−e^{−2})/2≈−0.432332358381694. Equality would force φ=max(0,1+ln v) identically, whose kink at e^{-1} violates interior differentiability, so lower endpoint unattained. Density c(u,v)=1−(1−2u)D′(v) is nonnegative under the two derivative bounds; integration by parts with D(0)=D(1)=0 gives Kendall tau=−4/3∫D=(2/3)rho. The explicit soft-maximum φ_ε(v)=ε ln[1+(e^{1/ε}−1)v^{1/ε}] is smooth and admissible for ε>0, approaches the kink as ε↓0, and approaches φ≡1 as ε→∞; continuity in ε fills the entire open-lower/closed-upper segment. Independent symbolic checks and high-precision integration corroborate constants and limiting family, but unrestricted conclusion follows analytically.

## originality

PASS

Bentoumi–El Ktaibi–Chesneau (2025) Proposition 3.1 defines this exact asymmetric scheme, gives twelve examples and association tables for four with rho down to −1/3; their inspected tables/analysis do not optimize over every admissible tuning function. Rodríguez-Lallena–Úbeda-Flores (2010) Corollary 3 already proves the rho–tau proportion for the broader quadratic-section copula family: that ratio is explicitly PRIOR, not novelty. Their general quadratic-section theorems do not impose φ′≤1/v and do not give this class-specific logarithmic envelope, unattainability or smooth saturating family. This assessment covers only that restricted envelope and its exact attainable range; older FGM/constrained variation optimization may contain an equivalent bound.

## value

PASS

The exact attainable concordance range determines the model capacity and inferential limits of a recently introduced copula construction. The source tabulated only four subclasses with rho≥−1/3, whereas the full admissible class reaches arbitrarily close to −0.43233; the strict unattained endpoint and explicit smooth family are substantive functional-constraint results. The universal rank-correlation ratio is prior and is used only to express the two-coordinate range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
