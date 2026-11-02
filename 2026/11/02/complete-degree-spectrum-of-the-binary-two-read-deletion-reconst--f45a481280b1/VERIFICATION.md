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

# Verification and scope

The checker `verification/check.py` uses only Python 3's standard library. It constructs all distinct one-deletion descendants of every binary word through length nine and compares the resulting graph degrees to an independent run-of-differences implementation. Across these lengths it checks 174,251 unordered pairs of distinct words.

For lengths one through fourteen, it enumerates degree histograms and checks a formally independent coefficient recurrence for the stated bivariate generating function, then calculates the first two moments using exact rational arithmetic and compares them to the claimed formulas. Extremal degree multiplicities are also checked. The recorded output is `verification/output.txt`.

These are finite consistency checks. The exact all-length claims depend on the Type-A structural theorem and the formal word-decomposition/moment proof. Publication priority has not been independently certified, and no independent mathematical audit has been performed.
