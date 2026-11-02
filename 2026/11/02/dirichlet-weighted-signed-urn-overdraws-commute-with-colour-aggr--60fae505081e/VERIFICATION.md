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

Use `python checker.py` from the directory containing this report. Python 3's standard-library `fractions.Fraction` and `math.factorial` compute all checks exactly. The checker reconstructs Bernstein Gram matrices from independent Dirichlet monomial formulas, performs exact Gaussian elimination and compares colour-aggregated and direct coarse signed laws for finite instances. It checks both hypergeometric conservativity and the \(64/315\) signed total-variation discrepancy, as well as the fourth-degree orthogonal-polynomial shortcut.

Observed: `PASS: 2101 exact-rational assertions; weighted aggregation, hypergeometric conservativity, normalization, and sharp obstruction`.

The checker deliberately samples finite parameter configurations, so it does not prove universally quantified aggregation. That proof uses the Dirichlet conditional-moment identity and uniqueness of Bernstein duals; its key steps are written in RESULT.md. The two comparison signed measures are normalized but not nonnegative; total variation here refers to half their \(\ell^1\) difference. No independent mathematical audit is recorded.
