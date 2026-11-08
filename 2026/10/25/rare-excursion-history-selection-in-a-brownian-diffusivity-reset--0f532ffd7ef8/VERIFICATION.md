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

PASS: Stationary regeneration gives Exp(r) backward age independent of an excursion. Brownian scaling exactly gives (X_0,H(u))=(2Λ A J,√2Λ√A B_u) with J=∫_0^1 B_t dW_t. For Volterra T, e_n=√2 cos((n−1/2)πt), f_n=√2 sin((n−1/2)πt), σ_n=1/((n−1/2)π). The unique top σ1=2/π exceeds σ2=2/(3π). Orthogonal normal-product chaos yields E exp(θJ)=(cos θ)^−1/2, and offmode R has exp moments strictly beyond 1/σ1. K0 asymptotics give P(σ1 ξ1η1>z)~√(σ1/(2πz))exp(−z/σ1); independent R exponential tilt contributes 2/√π and tight offmode continuous path. Conditional leading Gaussian factors balance with two equal signs, producing B/√z→±(2/√π)sin(πu/2) in C[0,1]. Age posterior has exponent Φ_x(s)=rs+πx/(4Λs), unique saddle s_x=√(πx/(4Λr)), second derivative 2r/s_x and width h_x=√(s_x/(2r)); Laplace localization with near-leading tail gives standardized N(0,1). The scaling identity multiplies the path by √Λ and squaring continuously gives deterministic 4Λ/π sin²(πu/2) uniformly. Independently reconstructed all seven Git blob IDs and exact tree SHA; 48 high-precision singular vector checks, exact symbolic saddle identities, direct gamma-density tail ratios (z=8,16,32) and independent offmode-product convergence corroborate constants. The infinite-dimensional tilt/localization rests on analytic dominated convergence and Gaussian tightness, not on the finite checks; the theorem is valid for fixed positive r,Λ and x→∞ only.

## originality

PASS

PASS, qualified best of knowledge: The identical reset bath was studied by Santra–Basu–Sabhapandit (2022), who already established its stationary spatial tail and integral saddle. Masó-Puigdellosas et al. gave general position-conditioned reset-age renewal PDFs. De Marco–Friz gave rare-strike terminal conditional volatility for a different nonreset fixed-horizon model. After checking these actual statements and a Resultary semantic search under several aliases, none inspected directly states or logically implies the simultaneous whole-past Brownian amplitude sine profile and normalized reset-age CLT in this particular regenerative system without additional path-level singular-mode and second-order saddle analysis. Generic conditional Gaussian-chaos theorems and historical priority remain explicitly possible, so this is not an exhaustive novelty certificate.

## value

PASS

PASS: The canonical model has anomalously heavy stationary position tails; an extreme displacement could arise from unusual age, amplitude, or future driver noise. A complete conditioned continuous-history law and explicit Gaussian reset-age fluctuations reveal which mechanism dominates, including a universal rate-independent physical diffusivity shape. This is a natural exact rare-event path invariant and material information beyond marginal tail rates or a generic renewal Bayes formula; it does not overclaim finite-threshold inference, pathwise convergence, or a general stochastic-volatility theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
