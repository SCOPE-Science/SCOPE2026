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

# Verification of the moment-identity theorem

Run `python verify.py` with Python 3. The code uses only the standard library's exact `fractions.Fraction` rational arithmetic. It verifies the first-step recursion and nonsingularity of the all-target identification matrix for finite irreducible random-parameter transition matrices with 2–7 states, and detects deliberate destination-moment mismatch. It also verifies the exact first/second moment algebra underlying the two-destination lognormal witness. It passed 6,502 exact rational checks.

These checks are diagnostic, not a substitute for the general algebraic proof. The rigorous necessity argument uses the fundamental matrix of any finite irreducible embedded chain and the absence of self-loops. Independent audit has not been performed.
