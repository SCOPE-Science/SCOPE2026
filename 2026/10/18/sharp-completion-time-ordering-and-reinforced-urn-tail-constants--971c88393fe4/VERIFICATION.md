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

The included `verify.py` requires Python 3 and only its standard library. Running `python3 verify.py` from the directory containing the file independently evaluates the three stopping-time CDFs using exact multivariate sampling formulas and dynamic count-vector recurrences. It also verifies the single- and pair-deficiency probabilities and the leading-tail constant numerically over specified finite test grids.

Successful execution reports 79 finite-horizon triples, 237 independent exact formula/recurrence comparisons, and 45 tail-consistency checks. The analytic arguments in `RESULT.md`, rather than those computations, establish all quantified infinite claims. The checker does not certify source novelty or independence of verification.
