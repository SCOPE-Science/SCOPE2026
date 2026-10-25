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

# Verification record

The source spectrum was derived from the sum of the four-cycle damped oscillatory covariance and the independent binary-switch covariance. Exact rational simplification yields the quadratic positivity identity in `RESULT.md`. Its denominator is strictly positive for all stated parameters and nonnegative squared frequencies.

Run `python VERIFY.py` with Python 3, NumPy and SciPy. In the recorded verification, the script passed 321 assertions covering: exact spectral-difference identities at several biases and rates; independent matrix-resolvent spectra from the original eight-state Markov generator; the critical bias root; continuous and discontinuous switching-rate thresholds; finite-frequency double-root tangencies; and direct numerical global-frequency maximization.

The theoretical verification includes the uniqueness of the switching threshold, the strict monotonicity of the critical-bias function, and the normal-form scaling of the global spectral peak in all three regimes. These steps are proved in `RESULT.md`; finite numerical tests by themselves cannot establish them.

Unproved outside the stated domain: nonuniform four-state rings, non-independent switches, other observables, other Markov-network topologies, and independent originality certification.
