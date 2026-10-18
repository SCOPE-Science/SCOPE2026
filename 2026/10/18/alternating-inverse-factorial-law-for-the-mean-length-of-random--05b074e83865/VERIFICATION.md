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

The exact expectation follows analytically from Cauchy's perimeter formula, a triangular-cap survival probability, Tonelli's theorem, beta integrals, and a signed Taylor remainder for \((1+x)^{-3/2}\). The latter controls every finite-series truncation and its limit, not just selected numerical parameters.

Reproduction: install Python 3.10 or later with SciPy and run `python CHECK.py`. It checks direct independent support quadrature at eight sample counts, the signed inequalities, two exact base cases (including a separate one-point edge-length integral), deterministic convex-hull Monte Carlo benchmarks with fixed seeds, and large-sample asymptotic consistency. Random sampling and numerical quadrature support but cannot replace the infinite analytic proof.

The earliest motivating manuscript was publicly submitted in October 2025. An independent audit of the present result has not been performed. Unindexed prior calculations, especially alternative formulations of mean lower-chain length, remain an originality risk.
