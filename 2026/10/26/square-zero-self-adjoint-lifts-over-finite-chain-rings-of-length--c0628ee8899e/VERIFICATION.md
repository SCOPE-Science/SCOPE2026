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

The self-contained Python checker `symmetric_checker.py` enumerates all self-adjoint square-zero matrices for five finite cases. The ring operations distinguish characteristic-\(p\) dual numbers from characteristic-\(p^2\) residue extensions; their predicted counts agree. The printed final marker is `SYMMETRIC_CHAIN_TWO_LIFTS_OK`.

Direct exhaustive coverage is restricted to \(n=2,3\), \(q=3,5\), and the specified rings. The theorem for arbitrary size and all odd prime-power residue fields is proved by the exact lifting construction and symmetric-Jordan tensor calculation in `RESULT.md`. No independent external audit or formal proof certificate is claimed.
