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

# Reproducibility

`verify_telegraph_voter.py` requires only Python 3's standard library. Run `python verify_telegraph_voter.py` in the directory containing the extracted file. The script constructs the complete Markov generator including environmental flips, and independently solves the stationary first- and second-moment recurrences. The recorded check returned: `PASS: 175 independent full-generator pair comparisons and 6 exact-formula checks`.

The tests cover 2 through 6 interior sites and rates 0.01, 0.2, 0.4070307623281496, 1 and 10; the rational formula is additionally tested at 0.001, 0.1, 0.4, 1, 10 and 100. Numerical linear-system tolerances are explicit. These tests do not certify an infinite parameter domain. The all-size mathematical justification is the closed Dirichlet recurrence and backward dual construction given in `RESULT.md`.
