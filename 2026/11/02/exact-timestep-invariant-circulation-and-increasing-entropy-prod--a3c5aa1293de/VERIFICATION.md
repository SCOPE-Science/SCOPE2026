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

# Verification
The package includes `verify_rounding_circulation.py`, a standalone Python-standard-library checker using exact rational arithmetic for its transition identities. It was run on 532 parameter pairs with output `VERIFY_OK 532 exact rational four-state transition systems, plus entropy calculations`. It checked positivity and exact row and column sums, the paired adjacent-edge rates, stationary currents, conditional moments and finite-step entropy calculations. It did not check mathematical publication novelty or constitute independent certification.

The proof is algebraic, for all \(0<c<1\) and \(0<h<1/(1+c)\). Rational test cases do not replace that proof. The strictly positive entropy derivative and the finite-matrix zero-step convergence follow from explicit formulas and standard matrix-product convergence, not an empirical asymptotic extrapolation.
