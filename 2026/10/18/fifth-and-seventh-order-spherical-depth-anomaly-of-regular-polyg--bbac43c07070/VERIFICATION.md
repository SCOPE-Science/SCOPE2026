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

The derivation uses normalized angular area density, independent-angle autocorrelation, the square-wave Fourier identity, uniform integration-by-parts remainder estimates, and explicit Dirichlet beta values. Its analytic proof, not numerical experiments, establishes the claim for infinitely many odd integers. Running `python check_depth_asymptotic.py` with mpmath and numpy yielded `VERIFY_OK independent_FFT_checks=10 coefficients=9 triangle_baseline=1`. The checker tests finite Fourier truncations against independent FFT convolution and validates the triangle formula; it is not an independent scientific audit. The asymptotic is not asserted to hold with its displayed error bound at each small odd integer.
