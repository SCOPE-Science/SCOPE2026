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

# Reproducibility and claim boundary

Run `python brownian_gyrator_optimal_checker.py` with Python, NumPy, and SciPy. The checker returned `PASS: 716 deterministic checks` on the packaged code before delivery.

The reproducibility program independently evaluates the stationary Lyapunov equation, the exact matrix exponential, fourth-order Gaussian pairings, and four-dimensional Gaussian quadrature, then checks the optimizing root and its monotonicity over a finite grid. These computations support the displayed finite-lag formula; they do not constitute an exhaustive verification over the continuum of parameters.

The infinite-domain claim follows analytically from the stationary Gaussian covariance, Wick expansion, strict convexity bound \(\sinh(2vt)\le v\sinh(2t)<v(e^{2t}-1)\), and the exact near-critical equation for \(q=e^{-2t_*}\). The equality/degenerate cases \(u=0\), \(T_x=T_y\), and \(|u|=1\) are excluded as defined in RESULT.md.

The optimality criterion is solely the magnitude of the expectation divided by the standard deviation of a *single* stationary signed two-observation chord. No statistical confidence, sample-size accuracy or experimental optimum for correlated time series is asserted.

An independent calculus comparison of the signal maximum \(\operatorname{artanh}(v)/v\) and SNR maximum establishes the strict ordering for all admissible couplings; its asymptotic gap follows from the displayed limits.
