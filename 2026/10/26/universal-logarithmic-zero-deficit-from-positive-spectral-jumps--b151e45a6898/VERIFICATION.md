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

The zero-intensity normalization is derived directly from the covariance \(K(z,z)=u(z)/(1-|z|^2)\) and the Edelman–Kostlan formula. The logarithmic coefficient follows from an explicit decomposition of a piecewise smooth spectral function into periodic sawtooths and a Lipschitz remainder; local Poisson estimates control the integrated error by \(O(\log^2(1/(1-r)))\). The normalized limiting profile is obtained from the same local estimate.

The script `check_jump_zeros.py` is a finite numerical check, runnable with Python 3 and SciPy. It passed 120 assertions for four explicit two-arc models. Numerical success does not prove the uniform Poisson estimates or any statement about general spectra.

The paper comparisons cover the full accessible open text of Noda–Shirai (2021 preprint/2023 journal article) and the relevant main theorem, spectral representation, asymptotic expansion and example sections of Shirai (2025). The 2025 article's fixed-direction smoothness hypothesis does not resolve behavior exactly at a spectral jump or the disk-integrated asymptotic. An unindexed stronger general result remains possible.

Independent mathematical audit and independent validation have not been performed.
