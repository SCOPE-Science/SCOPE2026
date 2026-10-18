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

# Verification and limitations

The deterministic `verify.py` program, runnable with `python3 verify.py`, compares four independently specified finite representations: binomial reflection enumeration for the absorbed discrete walk; its finite Poisson mixture; the integer-order Bessel kernel; and the continuous Fourier integral. It additionally checks time-resampling mixtures and finite geometric spectral sums for iid rates supported on \(\{1,3\}\). Every check is a finite mathematical consistency test, not a substitute for the infinite-series proof. No external formal or independent verification is asserted.

The proof in `RESULT.md` supplies the infinite assertions: the nonnegative reflection/Bessel survival identity, monotone resampling-time sandwich, spectral resolvent by Tonelli, near-zero integrability substitution, and Karamata's Laplace theorem with Potter bounds. The irregular-rate assumption is restricted to finite nonnegative iid rates, with positive probability of being nonzero. The stationary or full first-passage distribution is not classified. Literature priority and correlated-rate extensions remain unproved.
