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

# Verification

Run `python verification/check_weighted_maximal.py` using Python 3 standard libraries; the script is self-contained. It completed 17,682 exact-rational assertions over finite paths and multiple rational endpoint masses, checking explicit interval maxima, ramp witnesses, the perturbation bound, and the equal-weight contraction.

Independent mathematical audit is not performed. Enumeration does not prove the all-dimensional claims; the interval-extension argument, the boundary estimates, and the weighted-average perturbation inequality in `RESULT.md` provide the proof for every specified positive parameter.

The literature comparisons concern the specific weighted finite-path Lipschitz-seminorm result and do not establish publication priority against unindexed work.
