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

The exact first-step coefficients of the displayed source recurrence were reconstructed from its equations (3.3) and (3.6), including the zero-Neumann right boundary. Universal positivity is an infinite-step statement proved by a forward-sweep induction, not by finite testing. The coefficient-sign converse uses one-step nonnegative witnesses.

Run `python3 verify.py` with the Python standard library. The program prints `VERIFY_OK` if its exact rational identities, finite example tests, first-step negative witness, and positive-cone propagation checks all succeed. It uses floating-point only to evaluate the positive boundary value \(25+e^{0.01}\); the strict negativity follows separately from the elementary exact bound \(e^{0.01}<2\).

The verification does not test the entire family of grid choices computationally, and no independent scientific audit has been performed.
