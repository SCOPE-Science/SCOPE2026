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

Run `python verify.py` in the same directory. Python's standard-library `fractions.Fraction` checks every displayed rational inequality and the thirteen-pair sieve, multiplicative orders, and the five exact divisor-sum identities. An independent direct computation checks 85,248 cases with \(a=1,2\), distinct odd \(p<q<167\), and \(1\le b,c\le8\) using integer multiplicative formulas rather than ratio comparisons.

The finite scan does **not** prove the universal negative assertions. The proof in `RESULT.md` uses exact monotonicity and the two unbounded-exponent multiplicative-order contradictions. Publication priority is subject to independent literature verification.
