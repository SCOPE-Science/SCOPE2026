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

The analytic proof establishes the complete claim for all real \(c>1\), every integer \(d\ge2\), and each fixed integer marginal order \(k\). Numerical checks are supporting diagnostics only. Execute `python verify.py` with Python and `mpmath` installed to reproduce checks of three beta integrals, four bivariate Gamma-reflection identities, and the high-dimensional information and binomial-event limits at three finite dimensions.

The likelihood normalization follows from the exact Dirichlet change of variables and uniform marginals given by the published spherical-copula density. The finite tests neither prove arbitrary-dimensional limits nor exclude undiscovered prior literature. The total-variation expression is a lower bound, not an exact sharp evaluation. Independent assessment is not performed.
