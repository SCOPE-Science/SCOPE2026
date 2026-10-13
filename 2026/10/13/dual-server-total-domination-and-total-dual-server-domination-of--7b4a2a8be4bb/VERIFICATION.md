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

The theorem has an analytic proof for arbitrary positive part sizes. The accompanying `verify.py` performs a separate finite stress test directly from the definitions.

It enumerates every nondecreasing complete-multipartite part profile of total order from \(2\) through \(8\), then enumerates every red-blue-white labeling. For DST it requires every white vertex to see both colors and every selected vertex to have a selected neighbor. For TDS it requires every white vertex to see both colors and every red or blue vertex to have a same-color neighbor.

The recorded output is:

`ALL CHECKS PASSED`

`profiles=58`

`dst_assignments_enumerated=177534`

`tds_assignments_enumerated=177534`

`orders=2..8`

This computation checks finite boundary behavior only. It is not an exhaustive proof for unbounded part sizes; the infinite statement rests on the structural proof in `RESULT.md`.
