---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification notes

Exact identities: independent Poisson thinning gives rates lambda, alpha, alpha, c and total delta; the stationary one-point exponential-age Gaussian mixture is Laplace; conditioning on the last pair-affecting event gives the stated one-dimensional integral exactly. Critical asymptotic steps: Gaussian Mills estimates, the unique time saddle, the K_2 Bessel integral, and the finite Laplace moment at tilt k_2/2.

A numerical quadrature script `verify.py` compares exact finite-threshold integrals against asymptotic predictions at explicitly specified parameters and confirms a trend toward unit ratio. Such comparisons cannot establish an infinite-threshold limit.

Limits: parameters N,m,r,D fixed, 2 <= m < N; not uniform at vanishing common-reset intensity, not a full growing-particle extreme law. The motivating literature already provides the full exact pair density, so novelty of the sharp asymptotic needs independent assessment.
