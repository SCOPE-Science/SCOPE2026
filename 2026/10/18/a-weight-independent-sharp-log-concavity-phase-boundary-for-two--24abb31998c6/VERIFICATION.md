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

# Verification and limits

The analytic proof requires only factoring the two Gamma densities, differentiating a positive log-density, and maximizing a one-variable rational function or, equivalently, using an exact completed square. No numerical optimization, inaccessible external theorem, or code output is used to establish the universal result.

The accompanying standalone `check_gamma_mixture.py` script uses Python's standard library `fractions` and evaluates the original second derivative, rational-expression form, and completed-square expression independently at many exact integer-shape and rational points. It verifies the exact maximizer for integer gaps and checks three critical cases. Execution returned:

`PASS: 1013 exact-rational checks and three sharp analytic examples`

The finite checks cannot establish the inequalities for every real shape or every weight; those quantifiers are addressed in `RESULT.md`. Independent validation, reproduction by another party, and external audit have not been performed.
