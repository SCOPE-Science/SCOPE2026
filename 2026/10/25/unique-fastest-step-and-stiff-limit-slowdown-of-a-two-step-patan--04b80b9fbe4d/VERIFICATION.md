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

# Verification of the exact local Patankar relaxation law

The supplied `verify.py` uses SymPy to check the closed nonlinear recurrence against the MPE-embedded two-step algebra, Jacobian derivatives at equilibrium, characteristic boundary signs, MPE comparison polynomial, critical-point quartic identity, small- and large-step leading limits, and uniqueness of the positive critical root by its sign pattern. Separate exact-rational arithmetic then checks 392 two-component updates over a grid of eight positive steps and seven values for each of the two preceding imbalances. All tested states lie strictly inside the mass-one positive simplex.

Command: `python verify.py` (requires Python 3 and SymPy). The expected terminal message includes `392 exact-rational updates`; computed numerical values are \(h_*=0.536566092485493\ldots\) and \(\rho(h_*)=0.767326987978960\ldots\).

The mathematically universal claims follow from the exact derivation and inequalities in `RESULT.md`. Checks do not certify global convergence, full parameter-family uniqueness outside the given order conditions, or publication priority. No independent scientific audit has been performed.
