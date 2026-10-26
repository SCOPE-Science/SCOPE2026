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

# Reproducible verification

Run `python3 verify_coupon_cov.py` with a standard Python 3 interpreter; no third-party packages are required. The script compares two independently formulated exact-rational covariance calculations for every integer \(2\le m\le60\). One calculation uses the positive-prefix-tail sum; the other uses mixed-moment Markov recurrences for the evolving count of distinct labels. It separately checks conditional means and strict negativity. The printed floating-point scaled covariance values for larger sizes illustrate, but do not prove, convergence to \(-\sqrt{\pi/8}\).

Proof obligations discharged analytically in `RESULT.md` are the tail-sum identity, geometric-stage conditional laws, their strict stochastic comparison, a uniform Gaussian majorant for the main asymptotic sum, exponentially negligible late-prefix contributions, and the marginal variance normalizations. The finite verifier neither surveys historical mathematical priority nor proves an infinite statement.
