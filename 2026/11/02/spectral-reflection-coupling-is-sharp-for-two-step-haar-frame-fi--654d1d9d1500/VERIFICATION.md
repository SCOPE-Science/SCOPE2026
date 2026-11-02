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
# Verification and reproducibility

Install `numpy` according to `requirements.txt`, then run `python verify.py` from this package. Successful execution checks the 15 sixth-moment pair partitions, contraction identities for multiple exact rational positive spectra, exact and mixed-sign coupling comparisons, the finite-difference expansion, equivariance under spectral reflection, and numerical Haar-frame covariance consistency including a non-diagonal Hessian. The actual completed run emitted:

`VERIFY_OK sixth-moment contractions=4, exact mode-coupling/risk checks=8, finite-difference spectral-reflection checks=3, Haar covariance simulations=15000`

`VERIFY_OK non-diagonal covariance=20000, exact d1 extremal couplings=3`

The checker is a reproducibility aid, not an exhaustive or infinite verification. The universal theorem follows from the full finite-difference identity, the sixth-moment formula, scalar Cauchy--Schwarz, and the simultaneous equality construction in `RESULT.md`. The finite-horizon and stationary conclusions additionally require independently repeated two-step blocks and a spectral radius strictly below one. No independent scientific audit, provenance certification, or publication-priority determination has been performed. The coupling may require inaccessible Hessian spectral information in a black-box setting.
