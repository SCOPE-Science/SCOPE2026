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

# Reproduction and limitations

Run `python3 verify_double_star.py` with Python 3 and no third-party libraries. It checks the exact arithmetic identity certifying the \(p=q=1,\beta=2\) optimum, rational interior stationary-point identities, 1,100 numerical instances of the analytic attaining construction (each with a singular-value check and objective equality), and nine independent bounded-domain grid comparisons. The expected final status begins `VERIFY_OK`; the generated count reflects the actual tests and is printed by the program.

The general formula is established by the proof in RESULT.md, not by numerical experiments. Floating-point checks and finite grids cannot rule out counterexamples at arbitrary parameter values and are not infinite certificates. All checks pertain to the stated freely variable complex edge coefficients and nonnegative bridge-functional multiplier. No independent audit has been performed.
