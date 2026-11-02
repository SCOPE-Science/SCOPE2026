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

The proof establishes an all-integer inequality by a three-invariant induction, with explicit base and digit cases and an asymptotically sharp sequence. `verify.py` implements an independent exact-arithmetic test of all three inequalities and the constructed witness counts. Finite execution cannot establish an infinite theorem; correctness rests on the mathematical induction in `RESULT.md`.
