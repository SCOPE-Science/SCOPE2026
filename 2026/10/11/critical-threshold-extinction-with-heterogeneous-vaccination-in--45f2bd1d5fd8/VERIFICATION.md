---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Reconstructed the full n-group invariant simplex, disease-free S_i=s_i=(μ_i+γ)/(μ_i+ν_i+γ)>0 and true next-generation infected matrix K=(Ds BA+α Ds BI DI^{-1}) DA^{-1}. For ρ(K)=1, Perron p>0 and q^T=p^T Ds BI DI^{-1}>0 give exact cancellation Wdot=Σ_i p_i (S_i-s_i) f_i for W=p·A+q·I. The susceptible excess e_i obeys e_i_dot=-(μ_i+ν_i+γ)e_i-S_i f_i-γ(A_i+I_i). Adding H=Σ p_i(e_i)_+ yields the exact nonpositive Dini derivative: Σ_{e_i<0}p_i e_i f_i−Σ_{e_i>0}p_i(s_i f_i+κ_i e_i+γ(A_i+I_i)). At e_i=0 its upper Dini derivative is zero since e_i_dot≤0; nonsmoothness is handled. Any infected state on a positive-time invariant zero-derivative ω-limit orbit forces f_j>0 for some j by strictly positive transmission diagonal; constancy forbids e_j≠0, yet at e_j=0 the derivative is −s_j f_j−γ(A_j+I_j)<0, causing an immediate strict derivative contradiction. All infected classes therefore decay; stable linear susceptible errors and conservation give global attraction, and W≤V plus variation-of-constants gives Lyapunov stability, including γ=0 and n=1. Independently generated an exact heterogeneous two-group rational critical example with μ=(1,2), ν=(2,1), α=γ=δA=δI=1, BA=BI=((8/3,3/2),(8/9,3)), K=((2/3,1/4),(1/3,3/4)); verified p=q=(1,1), cancellation, both surplus/deficit branches and zero-boundary crossing for three rational admissible states: Vdot=−193/120, 0, −151/160. These finite calculations corroborate algebra, not the all-n proof. The strict-subcritical and supercritical sides follow independently for this exact K from eventual S_i≤s_i+ε plus Metzler comparison and infected linearized instability; they are background, not assigned novelty.

## originality

PASS

A qualified best-of-knowledge PASS for the vaccinated R0=1 endpoint, not for the Perron method or strict-subcritical theorem. The identical model of Ottaviano–Sensi–Sottile (arXiv:2202.02993, 2022; 2023 journal) explicitly proves vaccinated GAS only when R0<1 (Theorem 5) and handles equality only without vaccination (Section 3.1, Theorem 6). The complete Shuai–van den Driessche (2013) general Perron method uses a globally nonnegative Lyapunov remainder, unavailable when vaccinated susceptible levels exceed their disease-free levels. Guo–Li–Shuai (2012) has one susceptible variable with a global incidence dominance assumption; this is not available for independent S_i>s_i. The exact new correction uses positive susceptible excess for each group and fills the published nonhyperbolic threshold gap. A potentially related 2018 vaccinated SEIRS primary full text remained inaccessible after OA/preprint search and authorized institutional retrieval, so direct coverage cannot be decisively excluded; this is recorded as a genuine residual risk.

## value

PASS

The exact R0=1 vaccinated endpoint is a motivated nonhyperbolic gap in a specific published multigroup SAIRS theorem, not a routine numerical parameter substitution. Group-specific vaccination places the DFE susceptible levels below admissible initial S_i, invalidating the naive infection-only Lyapunov sign. The new Perron-weighted positive-part susceptible-excess term restores a global monotone functional for any n and independent nonzero ν_i with arbitrary irreducible BA,BI. It completes the closed R0≤1 disease-free phase boundary, an exact structural stability fact relevant to multiple-group infectious-disease dynamics. The statement is deterministic autonomous with fixed group totals and linear force of infection; no critical decay rate, stochastic/delayed extension or endemic classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
