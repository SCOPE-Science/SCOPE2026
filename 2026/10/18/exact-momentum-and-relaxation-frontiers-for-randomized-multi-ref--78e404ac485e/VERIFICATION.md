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

# Verification summary

The derivation is self-contained in `RESULT.md`. Independently run `python verify.py` with the packages in `requirements.txt`; its captured output is in `verification_output.txt`. The exact symbolic assertions verify the squared-coefficient variance, the covariance characteristic value at one, the stable deterministic impulse-energy Gramian, the equivalent small-gain inequality, and the first and second spectral-radius derivatives. Enumeration checks the reflection parity probability without a binomial shortcut for a range of integer dimensions and reflection counts. Direct multi-step scenario sums reproduce the covariance recurrence. Numerical spectra test interior and exterior points of the critical frontier.

One run returned 1,007 successful deterministic assertions. These finite checks cannot certify all real parameters or any infinite-time convergence statement; the infinite claim uses the Lyapunov identity and the arithmetic renewal theorem. The special unrelaxed Kaczmarz case has earlier mathematical coverage. Other potentially equivalent covariance or momentum analyses cannot be ruled out by search absence alone.
