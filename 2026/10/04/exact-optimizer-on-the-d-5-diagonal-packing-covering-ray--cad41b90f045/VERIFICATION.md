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

Run `python verify.py` in the same directory as this file. A successful replay prints `VERIFY_OK`, followed by `vertices 41` and `max_squared_radius 27/50`.

The checker uses Python's exact `Fraction` arithmetic. It verifies the packing minimum at \(\tau=4/15\), rechecks the explicit hole distance, enumerates all candidate vertices formed by five active inequalities among the twelve chamber halfspaces, retains exactly the feasible vertices, and confirms that their maximum squared norm is \(27/50\). It also checks the endpoint identities and strict margins used by the piecewise lower-bound proof.

The global statement for every \(\tau>0\) is not inferred from sampled parameters. It follows from the explicit piecewise formulas in `RESULT.md`; the finite enumeration is needed only to prove the covering upper bound at the equality parameter.
