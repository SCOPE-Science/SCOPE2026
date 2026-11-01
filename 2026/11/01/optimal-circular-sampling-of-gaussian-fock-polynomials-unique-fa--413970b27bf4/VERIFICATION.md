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

# Reproduction and scientific limits

The all-degree proof derives the Gram diagonal and uses a Rayleigh-quotient lower bound, strict one-variable minimax, equality in Rayleigh bounds, and square Fourier-moment unitarity. Stirling and the Poisson mode estimate give the sharp prefactor. The attached `check_sampling.py` was executed with Python and NumPy and passed 694 finite assertions for exact regular-polygon Gram spectra, random positive-weight/angular configurations, off-optimum radii and numerical asymptotics. The random experiments are not exhaustive and are not used as infinite proofs.

The optimization includes all strictly positive scalar sample weights (normalized to a fixed sum), all distinct angular placements, and all positive *common* radii, for exactly one more sample than polynomial degree. It excludes varying radii across points and additional samples. The first public source is the preprint posted 24 September 2021. No independent audit or third-party validation has been performed.
