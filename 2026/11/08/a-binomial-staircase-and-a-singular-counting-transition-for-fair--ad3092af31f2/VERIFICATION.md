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
# Reproducibility checks and limits

The standalone Python 3 program `verify_chores.py` enumerates every labeled two-agent assignment of \(2t\) chores for \(1\le t\le7\). It evaluates EFX item-by-item, checks positive-weighted fPO certificates against the explicit crossed-chore obstruction, and tests the closed count at exactly represented rational values including equality and both sides of the predicted jump thresholds.

Actual replay from the packaged program: PASS, 85 distinct exact-parameter instances, 356,980 complete labeled allocation evaluations. The check uses no random inputs, floating-point approximations, network sources, or nonstandard libraries.

The exhaustive checks are *finite*. They do not prove the formula for all positive integers or real ratios, do not certify published novelty, and do not establish the entropy limit. The universal mathematical justifications are the fractional exchange and weighted-sum certificates, the EFX inequalities and inclusion-exclusion count, and the binomial tail estimates using Stirling's formula in `RESULT.md`.
