---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For mu,v0,D,gamma>0, k=gamma/(2mu), theta=2muD/v0², stationary density is Gaussian convolution of athermal beta density (1-u²)^{k-1}. Let t=1/theta, I_n=∫_0^1 y^{n-1/2}(1-y)^{k-1}e^{-ty}dy; integration by parts yields exact 2t(I_{n+1}-I_{n+2})=(2n+1)I_n-(2n+2k+1)I_{n+1}. F_k(t)=2t I1/I0-1 equals center-curvature sign, and for k in (0,1) every zero satisfies F'=(1-k)/t>0 and endpoints change sign, hence exactly one transition. ∂_kF<0 implies theta_c decreases k. Set b_n=2tI_{n+1}/I_n-(2n+1): recurrence b_n=(I_{n+1}/I_n)(b_{n+1}+2(1-k)) and eventual negativity show the power series for f'(z)/z has at most one positive-to-negative coefficient sign change; so global derivative has one zero on z>0 below threshold and none above; k>=1 is unimodal. At criticality fourth-derivative ratio f4(0)/f(0)=-8(1-k)t_c²<0, giving z_*=sqrt(3/2) sqrt(theta_c-theta)+O_k((theta_c-theta)^(3/2)) and x_*=sqrt(3/mu)sqrt(D_c-D)+O((D_c-D)^(3/2)). Independent 280-node Jacobi quadrature checked F' and quartic identities for k=.15,.5,.85. Finite diagnostics corroborate only.

## originality

PASS

Best-of-knowledge independent comparison of the precise surviving theorem to same-object primary mathematics, Resultary semantic matches, general covering results and exact numeric searches; known foundations explicitly excluded from claimed novelty. Relevant inaccessible source risks are material and unresolved historical-priority caveats, not automatic scientific failure. The novelty rests on global modal rigidity and parameter-independent onset coefficient, NOT the known beta convolution or center-curvature transition.

## value

PASS

The exact global mode count, strict persistence dependence of the threshold, and universal observable peak-onset constant sqrt(3/mu) provide a complete one-dimensional stationary modality classification beyond a known implicit curvature equation. The nontrivial global sign-series argument excludes hidden additional peaks and the amplitude coefficient is physically calibrated; meaningful even absent a broader theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
