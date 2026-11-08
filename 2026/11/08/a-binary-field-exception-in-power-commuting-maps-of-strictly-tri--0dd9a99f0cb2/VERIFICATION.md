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

The included exact-arithmetic verification has two independent implementations. `verify.py` builds the formal cubic coefficient matrix (93 by 100) and its Boolean reduction (83 by 100) directly from matrix-unit multiplication. It checks an integral 59 by 59 minor with determinant -1, a nonsingular binary 55 by 55 minor, and all proposed solution vectors. `verify_direct.py` independently enumerates the 1,024 binary input matrices, tests all 45 explicit solution maps in the original commutator identity, and computes rank 55 for the pointwise linear constraint system.

Replay commands: `python3 verify.py` and `python3 verify_direct.py` alongside `rank_certificate.json`. Both were executed successfully, yielding `VERIFY_OK` and `VERIFY_OK_DIRECT` respectively. Exact ranks certify the finite linear-algebra step; the proof separately invokes finite-field interpolation for all field orders greater than two. No claim of independent verification or independent publication-priority assessment is made. No classification in matrix sizes larger than five is asserted.
