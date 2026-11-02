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

Run `python3 verify.py` using Python 3 standard library only. The expected final line is:

```
PASS exhaustive_sequences=54240 exact_CDF_inequalities=551570 greedy_coupling_edges=19273 boundary_cases_included=true
```

The program convolves the exact integer weights of all 15 nonnegative three-outcome probability triples with denominator 4, for every ordered sequence of 1 through 4 summands. This gives 54,240 cases, including zero weights. For each with positive probability of both parity classes it verifies every neighboring-lattice CDF inequality by exact integer cross-multiplication.

A separate deterministic pseudorandom sample of rational triples with denominator 7 at sizes 1 through 12 checks the same inequalities and constructs the increasing-quantile coupling with exact `fractions.Fraction` masses. It verifies that each paired support index differs by zero or one and that the total transported mass is one. A one-summand sharpness example is also checked.

These finite verifications are independent computational tests of the formula; they are not a proof for unbounded sample sizes or real-valued parameters. The general theorem follows from the analytic phase-interlacing argument, Bernoulli stochastic orderings, and boundary limits in `RESULT.md`. The mathematical status is self-reviewed only; no independent audit is represented.
