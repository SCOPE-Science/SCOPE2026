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

# Verification notes

Run `python verify.py` with Python 3 and SymPy. The check program reconstructs stationary generator balances and derives the mean and component second moments symbolically, verifies the centered-variance rational factorization, and independently checks the Brownian-age integral for the difference of raw moments. Exact arithmetic verifies the strict-negative midpoint witness and the four phase-boundary scaling limits. Across 270 parameter quadruples, 1,080 exact generator and moment identities are checked; with 18 symbolic and 4 exact witness checks, all 1,102 assertions passed in the recorded execution.

The sign theorem for **all** positive confinement and reset rates rests on the explicit quartic coefficients and Descartes' rule, together with exact intermediate-value witnesses; finite testing is only supplementary. Simple-root continuity, not finite root enumeration, proves asymptotic branch selection. The results do not cover zero propulsion, zero confinement, or resetting just one state component. Both the original and revised versions of the closest model manuscript were compared for the qualitative covariance-ellipse classification. Independent scientific audit has not been performed.
