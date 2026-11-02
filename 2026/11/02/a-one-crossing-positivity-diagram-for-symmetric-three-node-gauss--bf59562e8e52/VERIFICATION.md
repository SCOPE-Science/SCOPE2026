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

The provided `verify.py` was executed with Python 3 and mpmath and reported 389 successful finite checks. It independently solves the 3-by-3 Gaussian kernel system and compares it to the explicit formulas, numerically integrates the central cardinal function, checks representative positivity and negativity regimes and flat-kernel limits, and isolates the prescribed one-half-node threshold. The universal statement is proved by the separate pairwise monotone-ratio lemma in RESULT.md; no finite check is presented as a proof for all parameters. The root is defined by the exact weight equation, not by its printed decimal approximation. All calculations are exact analytic expressions except the explicitly numerical examples.
