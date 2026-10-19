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

The supplied `verify.py` directly enumerates rank-one symmetric square-zero matrices over prime fields and an extension field, evaluates literal matrix commutators, and checks the arithmetic formula against exhaustive counts of all ordered tuples in eleven configurations. Run with `python verify.py`; the successful output ends `VERIFY_OK_SYMMETRIC_RANKONE 11 cases`.

The finite tests include the parameters \((n,q,t)=(2,2,3),(2,3,3),(2,5,2),(3,2,3),(3,3,3),(4,2,3),(4,3,2),(4,4,2),(4,5,2),(5,2,3),(6,2,2)\). Their observed counts are respectively \(8,1,49,22,105,176,513,1216,6625,736,544\). Tests are exhaustive in these finite cases and are not a proof for arbitrary parameters. The separate geometric component theorem is checked mathematically via the isotropic-Grassmannian incidence argument, not by this program. No independent audit has been performed.
