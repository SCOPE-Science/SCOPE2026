---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS. For the specified real 2×2 SPD Schur family, Δ=E^{−1}−I has signed eigenvalues a=r/(1−r)>0 and −c=−r/(1+r), 0<r<1, γ>1. On the almost-sure nonzero scalar core d=a u²−c v², Q has eigenvalues γ and γ+(a²u²+c²v²)/d. With t=|u/v| half-Cauchy, nonpositivity occurs precisely for c(γ−c)/(a(γ+a))<t²<c/a; integrating 2/[π(1+t²)] yields exactly the submitted arctangent formula and a strictly positive value. Maximizing as γ↓1 reduces to 2/π(atan x−atan x²); derivative quartic gives unique maximizer x≈0.4354205447 and unattained supremum ≈0.142154976126. The simple pole of the signed ratio at sqrt(c/a) gives lim z P(||Q||>z)=2r/[π sqrt(1−r²)] and divergent first moment. For any FIXED ridge ε>0, the core zero curve has a transverse point with positive Gaussian density and nonzero numerator; the negative side implies nonSPD and the 1/|d+ε| integral diverges. Independently checked the scalar probability and supremum numerically at multiple r,γ, and the exact r=1/2 γ=2 witness has eigenvalues 2 and −7/3 although the exact Schur matrix is SPD. These checks supplement the unrestricted analytic proof, not Monte Carlo inference.

## originality

PASS

PASS, best of knowledge for the exact Gaussian nonSPD probability, optimal envelope, z^{-1} norm-tail constant and fixed-ridge failure in THIS signed Schur construction. Nakatsukasa–Park 2023 had already shown plain indefinite Nyström can be deterministically arbitrarily inaccurate; that generic phenomenon is not presented as new. Liang–Huang 2026 defines the precise signed Schur update and positive core ridge, and the accessible abstract/source construction do not establish this unconditional quantitative Gaussian law; the same full paper could not be newly read because lawful arXiv/OA delivery failed and Oxford access reported VPN disconnected. Chen et al 2026 concerns another indefinite Nyström construction, abstract only. Genuine residual same-model priority risk remains, not an automatic scientific failure.

## value

PASS

PASS. Loss of positive definiteness in an explicitly SPD two-by-two Schur problem invalidates conventional SPD preconditioner assumptions; an exact Gaussian failure probability and universal global envelope quantify that risk. The Cauchy pole proves an unconditional infinite expected norm, and persistence under every fixed ridge shows that a routine safeguard does not remove the pathology. This is a meaningful small-dimensional structural counterexample with quantitative sharpness, not merely the known fact that indefinite matrices exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
