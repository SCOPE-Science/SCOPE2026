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

For the stationary Markov process with generator D fʺ+r(f(cx)-f(x)), |c|=exp(-ε/2)∈(0,1), D,r>0, synchronous coupling gives uniqueness and a two-sided stochastic integral exists in L². Stationary Fourier product equals independent Laplace sum with geometric scales. With Y_ε=ε sqrt(r/D)X, ε log E exp(θY_ε/ε)=εΣ_{j≥0}-log(1-θ²e^{-jε}) for |θ|<1, bounded between Li₂(θ²) and Li₂(θ²)+ε log(1/(1-θ²)) by monotone Riemann sums. Limiting pressure derivative -2log(1-θ²)/θ is strictly increasing onto all R, so interior tilts give concentrated lower bounds; finite-cover Chernoff + exponential tightness establish full LDP speed 1/ε with even strict-convex Legendre rate. Series invert to I(y)=y²/4-y⁴/64+O(y⁶) near zero, I(y)=|y|-π²/6+exp(-|y|/2)+O(|y|exp(-|y|)) for large y, and I(y)<y²/4 for y≠0. Bounded pressure/rate comparisons passed 19 independent numerical checks. No finite-ε uniform tail prefactors are claimed.

## originality

PASS

Exact stationary Laplace factors and weak-contraction Gaussian limit were proved by Pierce and Tal-Friedman–Roichman–Reuveni; Biroli et al established stationary density and fixed-c exponential tails for either sign. The assessed statement is a two-scale fixed-stationary law LDP at displacements O(1/ε), explicit Li₂ pressure with finite-ε enclosure and sharp crossover. Fixed-c tails or Gaussian weak limit do not directly imply this joint asymptotic. General near-unit q-products, weighted-Laplace perpetuities and Gartner–Ellis results are possible prior stronger tools and an explicit originality risk.

## value

PASS

A natural experimentally motivated resetting model has Gaussian central scale O(ε^-1/2) but different rare-position scale O(ε^-1). The exact dilogarithmic cost, quantitative sub-Gaussian comparison and finite-parameter mgf control resolve a useful physical/mathematical crossover; not merely a renamed known stationary transform.

The dated certificate retains the supplied scientific assessment, sources and limitations.
