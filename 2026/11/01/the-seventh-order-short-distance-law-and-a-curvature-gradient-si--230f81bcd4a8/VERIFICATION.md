---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS. For C^6 strictly convex planar body K with positive curvature, the displacement density of two independent uniform points is g_K(z)/A² where g is covariogram. For fixed direction its exact chord representation is ∫(ell(v)-t)_+dv. At each tangency, Frenet local boundary has coefficients b2=κ/2,b3=κ_s/6,b4=(κ_ss+3κ³)/24; independent root-series reversion checked inward chord depth δ(q)=κ q²/8+[9κ^4+3κ κ_ss-5κ_s²]q^4/(1152κ)+o(q^4). Integrating δ from 0 to t and over all directions yields t³ term ∫κ²/12 and t^5 term ∫(9κ^4-8κ_s²)/2880 after Gauss map and by-parts. Radial t dt, density normalization, and equal-area radius r=ρ sqrt(A/π) give the stated ρ²,ρ³,ρ⁵,ρ⁷ coefficients, especially A^(3/2)/(20160 π^(7/2)) times the invariant. Independently evaluated ∫[9/(1+a cos kθ)^3-8k²a²sin²(kθ)/(1+a cos kθ)^5]dθ for k=2,3,4 and amplitudes 0,.2,.5,.9 and verified exact π[18-(9+8k²)a²-(9+2k²)a⁴]/(1-a²)^(7/2). Its numerator is strictly decreasing in a² and changes sign once for every k>=2; k=3,a=1/2 gives -56π/(3√3), disk ρ⁷ coefficient 1/(1120π). Numeric finite checks corroborate, while local uniform-in-direction Taylor remainder and analytic proof handle continuum of K.

## originality

PASS

PASS, best-of-knowledge. Wang’s primary 2026 convex-body pair-distance paper defines the same equal-area normalized D_K and its perimeter first correction, not the seventh-order curvature-gradient invariant in inspected theorem sections. A prior polygon result has a fourth-order exact term in a disjoint nonsmooth class. Older isotropic autocorrelation/curvature literature (Brazke thesis and related studies) can cover lower-order curvature terms and potentially stronger expansions; its full thesis was inaccessible and is a named historical-priority risk, not proof of novelty. The exact seventh-order derivative-energy term and sign-changing support-function family are not implied by the inspected first- and third-order results.

## value

PASS

PASS. This derives a universal new-order geometric coefficient of the natural distribution of random pairwise distances for any sufficiently smooth strictly convex planar body. The curvature-gradient energy 9κ^4-8κ_s² changes sign within explicit smooth harmonic-support families, a structural boundary absent from perimeter and positive curvature-square coefficients. The all-body formula plus sharp one-crossing sign phenomenon is mathematically informative, not arbitrary numeric slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
