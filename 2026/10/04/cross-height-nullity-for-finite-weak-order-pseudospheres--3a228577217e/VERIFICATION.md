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
The symbolic fence construction in `RESULT.md` is the proof. The executable check is a finite stress test of every branch of that construction.

Run:

`python3 artifacts/verify.py`

The program builds weak orders from level-size tuples, enumerates every order-preserving map for seven unequal-height source-target pairs, constructs the proof-prescribed fence to a constant, checks that every intermediate is order preserving, and checks that each consecutive pair is pointwise comparable. The case with source level sizes \((4,2)\) and target level sizes \((2,2,2)\) exercises the nonbinary spanning-level branch that is absent from the earlier two-point-level special case.

The replay checks \(11{,}435\) maps in total and must end with `VERIFY_OK`. These computations do not prove the infinite family; the all-heights proof is the symbolic argument in `RESULT.md`.
