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

# Verification of the dispersion crossover

The proof follows from the exact Stratonovich-to-Itô decomposition, the four angular Fourier moments \(\mathbb E e^{im\phi_t}=e^{-m^2\delta t}\), and the centered renewal-reward covariance formula. The critical algebra is independently checked in `verify.py` using symbolic identities: \(z_L^2=2/[(k+1)^3(k+2)]\) and \(a_2-a_4-z_L^2=2(k^3+k^2+k-2)/[(k+1)^3(k+4)]\).

The script then simulates 400,000 independent Poisson-duration cycles for each rate \(k\in\{0.3,0.6,0.81,1.1,2,5\}\), taking the exact Gaussian angular endpoint and independent residual translational normal increment in an isotropic-Schur specialization. With the stated fixed random seed, all six transverse-minus-longitudinal covariance differences agree with the formula to within five Monte Carlo standard errors. This is an exact-cycle sampler, not an Euler discretization of the orientation process.

The positive cubic derivative proves a single positive crossover and the sign for all physical rates. Finite Monte Carlo cannot establish an infinite-time theorem. No finite-duration reset actuation, externally forced drift, interactions, or independent external scientific validation is included.
