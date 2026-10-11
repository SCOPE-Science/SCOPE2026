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

The proof is symbolic and valid for every integer \(k\ge3\). The accompanying `artifacts/verify.py` is an independent finite replay: for each \(3\le k\le14\), it constructs \(C_{k+6}^2\), checks graph connectivity for every six-subset complement, constructs the full downward closure, and verifies the claimed face vector and reduced Euler characteristic. The stored output ends with `VERIFY_OK`.

Finite enumeration is not an exhaustive proof over all \(k\). It checks representative values and the implementation of the definitions; the all-parameter conclusion rests on the cyclic-run proof in `RESULT.md`.
