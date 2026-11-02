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

# Reproducibility and limits

Run `python3 checker.py` with Python 3 standard library. The checker uses exact fractions to compare independently convolved geometric stage distributions against finite-horizon dynamic programming that optimizes each controlled decision. It covers \(1\le a,b\le5\), \(\varepsilon\in\{0,1/3,1/2,2/3,1\}\), and all horizons through 22, with 6250 exact rational assertions.

The all-size stochastic ordering and square-root-window limit are proved in `RESULT.md` using a monotone visited-count coupling, independent geometric stages, Riemann sums, Lyapunov normal convergence, uniform integrability and Chebyshev's inequality. Enumeration cannot verify these infinite-domain statements. The test files are standalone, but no independent audit has been performed.
