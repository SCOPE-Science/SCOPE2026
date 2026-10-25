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

# Reproducible verification

Run `python3 verify.py` from the directory containing the accompanying source file. It uses only Python's standard library, `fractions.Fraction`, `itertools` and `math`.

The program enumerates each recursive-tree parent assignment and each Bernoulli-retention pattern for \(1\le n\le7\), for three rational values of \(p\). It independently computes the retained-forest component and singleton counts, then matches the exact rational covariance and the stated mean formulas. It additionally checks the mixed-covariance recurrence against the closed formula for \(8\le n\le100\). All comparisons use exact rational arithmetic, not floating-point approximations.

These finite tests do not establish the identity for arbitrary \(n\) or \(p\). The proof in RESULT.md supplies the complete general argument through conditional transitions, Bernoulli score differentiation, and recurrence solving; the asymptotic statement additionally uses standard gamma and harmonic estimates. No separate independent audit is represented.
