---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

At fixed common time t>0, H_l(t)~Poisson(ct log(l+1)); nondegenerate Gaussian harmonic blocks vanish exactly when H_l=0, producing independent Bernoulli I_l with p_l=(l+1)^(-ct). Summation gives conditional M_L~L^(1-theta)/(1-theta), D_L~2L^(2-theta)/(2-theta) for theta<1, with Chernoff and Bernstein deviations exponentially summable. At theta=1 a sparse geometric subsequence gives M_L/log L->1; the product Laplace transform of D_L/L tends to integral_0^1(e^(-2sx)-1)dx/x, the pre-existing twice-Dickman law. At theta>1 first Borel-Cantelli gives finite holes yet E D_infinity=infinity for theta<=2. Conditioning and integrating yields random exponent (1-cT_beta)_+ and its mixture atom/density; E_beta(-s)~1/(Gamma(1-beta)s) establishes annealed L/(c Gamma(1-beta) log L), L²/(c Gamma(1-beta) log L). Covariance trace sum (2l+1)(l+1)^(-4)log(l+1) converges. Independently recomputed conditional means at theta=.4,1,1.4,2.5 for L=40000; infinite claims rest on proof, not that finite check.

## originality

PASS

Basic Bernoulli occupancy, conditional almost-sure limits, weighted-Dickman and Mittag-Leffler Laplace asymptotics are all known. Novelty assessed only for the combined natural grey-field spectral-hole model with shared random time, observable exponent distribution, the integrability boundary, and annealed/quenched gap. Search produced no covering published statement; this is best-of-knowledge, not certified priority.

## value

PASS

Completely absent entire multipoles are a geometrically meaningful sparse observable in a non-Gaussian isotropic field. The classification separates almost-sure finite-hole, conditional mean-divergence, critical compound-Poisson/Dickman and genuinely logarithmic annealed regimes. This contrast is not contained in second moments or pointwise spectral covariance and informs interpretation of random spectral support; components are textbook occupancy facts, so value is in their precise model-specific joint phase boundary, not in re-proving the Dickman theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
