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

# Verification of the Gaussian stochastic extragradient phase diagram

Run `python3 verify.py` in the same directory as this file; the script requires only the Python standard library. The implemented stochastic oracle updates are reconstructed directly from the predictor and corrector equations. Gaussian polynomial moments are computed by the independent integration-by-parts recurrence; derived rational identities, the sharp strict stability condition, minibatch covariance, and the interior correlation minimizer are checked. A fixed-seed independent bivariate Gaussian experiment compares simulated one-step squared-norm amplification with the analytic factor.

The packaged script completed 539 exact-rational assertions and one seeded numerical comparison, giving empirical amplification approximately \(0.972236\) against analytic \(0.972350\). The numerical tolerance applies to that finite random comparison only. No finite enumeration or simulation proves mean-square behavior at arbitrary dimensions or infinitely many iterates; universality follows from the direct analytic conditional expectation identity and induction, which are given in `RESULT.md`. The Gaussian recurrence and factorization were checked in exact arithmetic. Independent mathematical review has not been performed.
