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

# Reproducible checks and boundaries

The scientific statement concerns exact arithmetic and all real \(\kappa\ge1\). The mathematical proof uses a coordinate-invariant Hessian whitening, a Gaussian angular-density integral, maximal coupling, a polar radial lift, and a polynomial zero-set argument for jointly Gaussian pairs. The probability of successful two-step termination is independent of the particular deterministic \(x_0\ne0\). These analytic facts, not randomized testing, prove optimality and the almost-sure geometric stopping law.

To exercise the implementation, run `python verify.py` from the directory containing the embedded files. Python's standard library suffices. With the fixed seed the program generated \(16{,}000\) coupled sketch pairs for each of \(\kappa\in\{1,4,9,25\}\), checked empirical individual marginal means and second moments against \(N(0,I_2)\), compared the empirical orthogonal-pair frequency with \(q_*(\kappa)\), and checked exact-update residuals on the matching branch. It also checked numerical midpoint integration of the overlap. The run reported `PASSED finite probabilistic diagnostics: 64000 coupled Gaussian sketch pairs`.

Limitations of verification: observed Gaussian moments or small residuals are finite-precision diagnostics, not certificates of exact distribution, optimality, or infinite-horizon termination. The external independent audit is not performed. No tolerance-based or high-dimensional guarantees are claimed.
