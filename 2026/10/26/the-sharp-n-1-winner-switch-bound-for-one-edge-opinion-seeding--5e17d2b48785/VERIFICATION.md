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

Run `python verify.py` using Python 3. The checker has no third-party dependencies and uses exact rational arithmetic throughout. It constructs the family for \(m=2,\ldots,17\), checks every crossing order and winner interval, and independently solves the equilibrium linear system at selected exact parameter values. Its successful final line is `ALL_EXACT_RATIONAL_CHECKS_PASSED`.

The infinite-family theorem follows from the analytical inequalities and upper-envelope argument in `RESULT.md`; finite checking alone would not prove that theorem. The checker does not certify uniqueness relative to all historical literature, global optimum for different objectives, or consequences for multi-seed optimization.
