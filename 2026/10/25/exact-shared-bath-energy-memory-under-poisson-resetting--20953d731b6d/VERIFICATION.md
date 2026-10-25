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

# Reproducibility and verification

From the same directory, run `python checker.py`. It requires Python, SymPy and SciPy and has no external data dependency. The expected result is saved in `checker_output.txt`.

The checker recomputes stationary polynomial-generator moment identities; it is not just matching archived outputs. It symbolically tests the two-time covariance kernel, the sum over dimensions, the exact integrated covariance and normalization, and an independently derived Brownian-age mixture for fourth moments. It also evaluates 15 independent quadratures of the lag kernel for several positive rates, amplitudes and integer dimensions, comparing the result with the closed expression.

Limits: the analytic proof, rather than finitely many checks or quadratures, establishes the result for all finite dimensions, all positive parameters and all nonnegative lags. The checks do not establish scientific priority or cover changed resetting protocols. No separate independent review has been performed.
