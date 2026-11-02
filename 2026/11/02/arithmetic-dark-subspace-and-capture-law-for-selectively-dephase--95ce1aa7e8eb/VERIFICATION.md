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

# Reproduction and limits

Run `python checker.py` in a Python 3 environment with NumPy and SciPy, and run `python verify_arithmetic.py` with the Python standard library. It directly forms the trace-decreasing Lindblad matrix in the site outer-product basis, evaluates the regularized zero-frequency resolvent for each localized source, and compares the resulting retained mass with the exact gcd prediction. The script was executed with 151 cases passing a tolerance of \(1.5\times10^{-4}\) at regularizer \(10^{-8}\). The regularizer produces finite numerical bias, so the comparison is not an exact-infinite-time numerical certificate.

An additional independent finite check iterated path sizes \(2\le N\le79\), all possible single sink positions, selected one-site noise masks (including the empty set), and sample source vertices, verifying 37,908 exact integer-index relationships and floating-point trigonometric sums. The all-length theorem is proved separately in RESULT.md.

The key mathematical steps to review are spectral nondegeneracy, the implication from a nonzero limiting trace to a positive stationary Cesàro limit, the Hilbert–Schmidt dephasing identity, the argument forcing each noisy-site stationary population to zero through the first path mode, and the root-of-unity sum. No independent audit has yet been performed.
