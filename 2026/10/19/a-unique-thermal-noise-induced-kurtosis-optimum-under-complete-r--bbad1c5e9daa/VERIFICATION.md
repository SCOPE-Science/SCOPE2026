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

# Verification scope

The accompanying standalone `verify.py` reconstructs the stationary Gaussian age-mixture moments from elementary Laplace transforms, independently verifies the exact rational excess-kurtosis formula, differentiates it, and compares the derivative to the explicit polynomial whose coefficient-sign pattern proves uniqueness of the optimum. It checks the noise-free \(57\) limiting excess kurtosis, the two positive-thermal-noise endpoints and strict thermal-noise dependence. It also performs 20 numerical quadratures of the original age distribution, six numerical derivative-root checks and three reproducible Gaussian age-mixture simulations with 1,500,000 draws each.

# Actual result

The reproducibility script completed with `PASS`. For \(h=1\), its unique numerical optimum was \(k=1.1739006879\ldots\) and the maximum excess kurtosis was \(5.5229089372\ldots\). All 20 quadrature comparisons met an absolute tolerance of \(2\times10^{-7}\). Monte Carlo comparisons were subjected to a conservative absolute tolerance of \(0.18\) because fourth-moment estimators have appreciable variance.

# What has not been established

Finite numerical checks are not proofs of all-parameter uniqueness; that conclusion follows from the exact derivative identity and Descartes' rule in `RESULT.md`. No external or independent audit has been performed. No statement about operational optimality of a search or any other observable is verified. The full correctness proof assumes instantaneous complete resets and a Gaussian active force initialized at zero each cycle.

# Reproducibility

Run `python verify.py` with Python 3 and recent SymPy, NumPy and SciPy. No data files, network requests, proprietary code or external dependencies other than those packages are required.
