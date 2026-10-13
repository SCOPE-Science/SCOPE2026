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

# Verification record

The independently executable `verify.py` recomputes the two companion matrices directly, forms the monodromy in chronological order, and compares its trace against the cyclic run-length formula for every binary word with a fresh update of length one through eight (502 words). It checks every determinant is zero, path-polynomial recurrences and small-run eigenvalue roots numerically to 30-digit precision, and the exact square-zero claim at the large golden-ratio parameter. It prints `VERIFY_OK` only when all tests pass.

These are finite symbolic and numeric consistency tests, not a proof of the unbounded statement. The general argument is the exact rank-one Floquet decomposition and the path-adjacency characteristic polynomial. The step-to-step delayed recurrence, initial-pair convention, equality cases, and fixed-schedule limitation are explicitly stated in the proof. This review is same-model only; independent validation was not performed.
