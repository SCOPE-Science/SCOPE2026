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

# Verification record

The companion `verify.py` requires only Python 3's standard library. It computes exact beta-binomial probabilities, checks finite-population subset enumerations, and matches exact moments against independent symbolic formulas across finite parameter grids. It also reports Gaussian-CDF and Poisson total-variation errors on representative large parameter configurations. These are finite consistency checks, not infinite proofs.

The analytic proof checks the exact conditional variance decomposition, the Beta-to-normal gamma representation with endpoint fractions allowed, the conditional binomial central limit theorem and its joint independence, and the total-variation Poisson coupling. The necessity argument uses explicit non-Gaussian subsequential limit laws and covers the degenerate Poisson parameter zero. Reproduction command: `python verify.py` in a directory containing the extracted files.

**Limits.** Independent audit is not performed. Older negative-hypergeometric papers may contain equivalent asymptotic results, and some were unavailable in full. No independent certification or historical-priority guarantee is asserted.
