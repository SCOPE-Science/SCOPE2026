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

# Reproducibility and scope of checks

The standalone script `verify.py` uses exact `fractions.Fraction` arithmetic to compare analytic risks to a direct enumeration of retained-edge subsets and their connected components on each graph. Run `python3 verify.py` and compare its JSON output byte-for-byte after ordinary newline normalization with `certificate.json`.

Checks cover all thresholds on three- through nine-vertex examples at probabilities \(1/4\), \(1/2\), and \(3/4\); symbolic/combinatorial Bernstein-coefficient identities and sign blocks across sizes four through sixty; strict log-concavity of coefficient ratios for the same finite ranges; and finite strict mean comparisons. The eight-vertex risk reversal is checked at two exact rational probabilities on opposite sides of the algebraic threshold.

These checks are not an exhaustive experiment over all sizes or real transmissibility values. The infinite assertions, the absence of additional crossover parameters, and the mean comparison are established in `RESULT.md` by exact formulas and analytical inequalities. No independent scientific audit has been performed.
