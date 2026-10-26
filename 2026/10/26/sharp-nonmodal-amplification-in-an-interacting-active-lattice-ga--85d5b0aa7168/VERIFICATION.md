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

# Reproducibility and mathematical boundaries

The standalone `verify.py` requires Python 3, NumPy, SciPy and SymPy. From the directory containing the supplied files, execute `python verify.py`. The script checks the matrix-square identity for each Fourier generator symbolically, the Hermitian-part off-diagonal and determinant, the unique special density, the factorized separation of modal and nonmodal boundaries, and the exact optimizer of the half-filling triangular off-diagonal envelope. It then samples two-by-two matrix exponentials in the spectrally stable/amplifying and stable/contractive regimes, and checks the nonasymptotic half-filling operator-gain bracket for representative activity values.

The symbolic calculations verify the pivotal algebraic identities; the numerical mode checks are finite and illustrative only. The infinite-dimensional necessary-and-sufficient amplification criterion is established separately by Fourier Parseval and a modewise energy estimate covering **every** nonzero integer Fourier wave number. The asymptotic gain bound follows from an all-mode operator-triangle estimate and a maximizer of a decaying positive discrete sequence, not from numerical extrapolation. The specified norm is that of physical plus/minus species-density deviations; changing norm is outside the claim.

This package does not test finite-particle stochastic realizations, nonlinear perturbation persistence, or robustness under weighted norms. No independent scientific audit has been performed.
