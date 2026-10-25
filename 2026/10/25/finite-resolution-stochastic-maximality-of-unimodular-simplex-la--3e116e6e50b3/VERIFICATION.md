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
# Verification notes

The exact checker `miniature_law_checker.py` uses integer combinatorial coefficients and rational arithmetic only; it tests 3,366 cases across dimensions \(1\) through \(6\), positive resolution up to \(12\), plus Pick-theorem reconstruction for six concrete lattice polygons. It tests the complete vector of probabilities, the positive \(h^*\)-mixture, monotone likelihood ratios, tails and their strictness, the equality condition, and the mean formula. The command is `python miniature_law_checker.py` and the expected success line is `MINIATURE_LAW_EXACT_OK cases= 3366`.

The mathematical proof is independent of finite enumeration. It uses two standard facts, exact Ehrhart series expansion and Stanley nonnegativity, plus elementary combinatorial and beta-integral identities. The first public source date is taken from the research lead arXiv:2605.20905, submitted on 20 May 2026. An independent external proof review has not been performed.
