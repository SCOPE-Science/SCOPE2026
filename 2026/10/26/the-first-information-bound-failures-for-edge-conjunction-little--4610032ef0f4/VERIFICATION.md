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

The finite recurrence is proved in `RESULT.md`. Compile and run `verify_all.cpp` using a C++17 compiler to compute all 2,097,151 nonempty graph masks on seven vertices; then run `check_types.py` to independently check the two constructive graph families and compare their exact labeled masks with those reported by the C++ computation. The source and captured output are included. The independent checker is not an external scientific audit. The classification does not extend beyond seven vertices.
