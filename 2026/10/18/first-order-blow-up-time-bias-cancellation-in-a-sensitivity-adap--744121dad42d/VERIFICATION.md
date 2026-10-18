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

Run `python verify.py` with a current standard Python interpreter. The checker uses `fractions.Fraction` to establish exact equality of the finite one-step reciprocal identity at its selected rational inputs, then evaluates the precise sensitivity-adaptive Euler recurrence at three shrinking tolerances and five pairs of initial value and parameter. It compares the resulting step count and signed time error with the independently derived asymptotic formulas, including two tuned cases. Its successful execution yields `PASS: 92 rational-algebraic and deterministic numerical assertions`.

All asymptotic and all-parameter conclusions come from the analytic proof in RESULT.md. Finite numerical tests are not exhaustive, are not a substitute for that proof, and do not show an exact nonzero three-halves-order term. Scientific bibliographic comparisons have residual uncertainty; no independent audit has been performed.
