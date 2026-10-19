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

# Reproducibility and boundaries

Execute `python verify.py` with Python 3.10 or later (standard library only). The checker recomputes exact occurrence-weighted plane-tree leaf distributions, the Narayana marginal formula, the covariance regression and likelihood-ratio interval property by enumerating sizes through ten; it separately tests the critical monotonicity ratios with exact `fractions.Fraction` arithmetic over 232,286 parameter triples. All tests passed in the prepared scientific package. These finite checks are cross-checks; proof of arbitrary sizes is in RESULT.md via the contraction bijection and symbolic monotonicity.

The source paper used as the dated starting point is arXiv:1312.1211v1 (public 2013-12-04, primary MSC 60C05). Its general asymptotic covariance is acknowledged as prior work and not independently novel here. An inaccessible plausible 2009 primary paper remains an originality risk. No independent audit or external scientific validation has been performed.
