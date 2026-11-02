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

The exact symbolic checker is `verification.py`. Requires Python 3 and SymPy. Execute `python verification.py` in the directory containing the checker. It verifies the two-pulse mean and pre-pulse deficit identities, the constrained three-pulse gradient formulas, and a rational three-pulse witness, followed by 36 deterministic numerical cases. It does not search prior literature or certify physical applicability.

The mathematical proof does not rely on the numerical checks. Boundary cases of zero pulse effectiveness and colliding pulses are excluded by the strict assumptions. Independent external audit has not been conducted.
