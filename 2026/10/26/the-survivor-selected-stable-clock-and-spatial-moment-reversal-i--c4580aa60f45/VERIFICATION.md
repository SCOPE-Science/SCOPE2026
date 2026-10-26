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

# Reproducibility and limits

The file `VERIFY.py` can be run from the same directory using `python VERIFY.py`; it uses NumPy and SciPy, with mpmath import available. In the tested numerical environment it reported `PASS 110 deterministic checks` with warnings configured as errors. It checks the killed Bessel kernel at multiple positive clock times, survival normalization for a unit-height start, exact stopped first moments, the integrated survival identity for second moments, Mellin integrals for Gamma-scaled stable clocks, large-refresh spectral survival constants, and algebraic Rayleigh-stable mixture moment identities.

The source model uses an independent positive rate environment. The key exact distribution identity for the total refreshed operational time is verified analytically through a Laplace transform, not estimated by Monte Carlo. Existence of the conditional limiting law and the critical all-time moment threshold are analytic claims based on the reflected-kernel local limit, clock moment bounds and regular variation. The tests do not prove an infinite-time assertion, a global uniqueness claim, or an independent originality assessment.

Mathematical boundary conditions: the walk begins at a fixed positive integer and is killed on the first visit to zero; the rate law is parameterized by \(0<\alpha<1\); the scaling limit is along integer multiples of the fixed rate-refresh duration. The moment finiteness statement holds at every positive physical time. No claim is made for the exponential-rate endpoint \(\alpha=1\), where moments of all orders exist.
