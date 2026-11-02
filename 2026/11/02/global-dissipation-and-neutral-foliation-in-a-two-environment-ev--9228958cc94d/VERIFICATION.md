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

# Mathematical verification record

The proof uses exact differentiation, the strictly positive payoff-gap assumptions, properness of the separable energy, LaSalle's invariance principle, and the structure of regular compact level sets of a planar flow. These checks are not external validation.

The supplied `verify.py` program was executed with SymPy and SciPy. It reports `PASS` for symbolic identities (payoff-quotient numerator, exact energy derivative, equilibrium), then checks the environmental logit-odds invariant in three independently chosen admissible examples. It verifies decreasing energy with negative determinant, conservation at zero determinant for a non-mirror payoff pair, and increasing energy with positive determinant. Numerical integrations are not relied on for infinite-time conclusions.

The theorem does not determine the precise boundary omega-limit set in the positive-determinant regime. It does not apply to unequal environmental feedback parameters, unsymmetrized community fractions, or boundary initial conditions.
