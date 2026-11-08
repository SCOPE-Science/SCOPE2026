---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For λ>1, x=ηc>0, d=λ−1, u=xβ and v=x²(β²+d²), the actual discrete feedback update for scalar sign ξ becomes the conformal real matrix M_ξ=(1+ξu)I+ξxdJ (J skew-orthogonal), so ||z_n||²/||z_0||² is exactly the product of m_ξ=1+v+2ξu>0. The stationary symmetric sign chain (p in (0,1], including deterministic alternation) visits both equally, hence almost-sure norm log-rate (1/4)logΔ; Δ<1 is equivalent to β²>d² and 0<x<sqrt[2(β²−d²)]/(β²+d²). In this domain a<1<b with ab<1. For every real q>0, exact path summation gives E||z_n||^q/||z0||^q=πD_q(P_p D_q)^(n−1)1, Perron spectral radius classification with simple positive eigenvectors for 0<p<1. Symmetric similarity has derivative a negative rank-one form in p; its PF leading vector never lies in the zero direction because A≠B, proving unique strictly decreasing crossing p_q=(1−A)(B−1)/(A+B−2AB) in (0,1). Hyperbolic sine ratio proves p_q strictly increases from 0 to 1 with q. p=1 uses deterministic alternating two-step product. At p=1/2 moment q=2 growth factor 1+v>1; rational witness λ=2, β=−2, x=1/5 gives a=2/5,b=2, p2=3/4,p4=7/8, enabling p=4/5 stable second, unstable fourth. Independently recomputed transfer Perron values for multiple (a,b), q and p below/at/above each threshold; symbolic supplied checker was read but is not substitute for all-real-q proof.

## originality

PASS

Best-of-knowledge PASS restricted to the explicit fixed-feedback discrete controlled bilinear game phase diagram for all real positive moments, p_q monotonic ordering and concrete 2nd/4th coexistence witness; the underlying Markov spectral stability theory is acknowledged established.

## value

PASS

A complete all-positive-moment phase diagram for an explicit minimax feedback discretization with correlated signs is a natural control and stochastic stability question. The strict threshold hierarchy, p2>1/2 anti-persistence boundary and concrete almost-sure stable/second stable/fourth unstable witness quantify a substantive risk/stability separation. General Perron method is routine prior mathematics, but its exact parameter optimization and all-order threshold here is a useful nontrivial closed classification, within explicitly limited model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
