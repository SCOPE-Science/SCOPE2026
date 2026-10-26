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

The standalone source `verify_fractional_ctrw.py` is included in the accompanying package. With Python 3, NumPy and SciPy installed, run `python verify_fractional_ctrw.py` in the directory containing that file. The source was executed from its actual package-source path and reported `PASS: 2804 deterministic comparisons`.

Tests independently compare hyperbolic absorbing resolvents with finite tridiagonal matrix inverses for interior sites; enumerate allowed first-detour paths and target-boundary exclusions by brute force; reconstruct the exponential tilt of the Mittag-Leffler law by a signed series of Gamma distributions; compare numerical integrations of total-variation coefficients with their exact Gamma/Beta formulas; verify normalization and strict nonconstancy of the Dirichlet first-order correction; and test the memoryless detour asymptotic over multiple finite interval sizes.

The verifier is a finite numerical and symbolic-normalization supplement. It is not a proof of the infinite-rate limit or of originality. The analytic proof uses the exact renewal/path conditionalization, absolutely convergent signed Gamma expansion in total variation, fixed-length tensor-product expansion, and a parity/path-count bound. Its remainders are for fixed lattice size and exponent; there are no assertions of uniformity as \(N\to\infty\) or \(\beta\to1\). Independent audit has not been performed.
