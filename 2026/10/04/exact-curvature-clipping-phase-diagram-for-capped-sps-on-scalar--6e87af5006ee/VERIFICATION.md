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
The proof reduces capped SPS on each scalar quadratic to an exact affine map with coefficient \(r_i=\min(1/(2c),a_i\gamma_b)\).

`verify.py` checks the affine reduction, invariant first- and second-moment identities, all-capped and all-uncapped formulas, the two-component cap thresholds, and finite-depth moment recursion using exact rational arithmetic.

Finite enumeration is not used to prove stationarity. Existence and uniqueness follow from uniform contraction, and the stationary moments follow from exact fixed-point equations in `RESULT.md`.
