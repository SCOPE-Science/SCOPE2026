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
Exact-rational check: run `python3 check.py` next to this file. It reconstructs the actual \(D^*D\) Gram matrices and tests the inverse first columns, diagonal finite sums, and central maxima for every order \(1\le r\le5\) and length \(1\le d\le11\). Expected result: `EXACT_CHECK_OK 715`.

The all-orders proof is analytical; the finite enumeration does not certify statements for untested orders or lengths. An independent scientific audit has not been performed.
