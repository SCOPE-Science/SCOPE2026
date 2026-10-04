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

`verify_qs_divisibility.py` performs three exact checks.

1. It implements the Johnson--Kollár/Fletcher injection criterion directly for the only nonautomatic coordinate subsets and compares it with the claimed divisibility test for all \(2\le r\le30\) and \(1\le a\le b\le3r\).
2. It independently computes local Reid--Tai ages in the two heavy quotient charts and checks the canonical-strip formula for all \(2\le r\le60\) and \(1\le a\le b\le4r\).
3. It enumerates the canonical strip and checks the exact counting upper bound for every \(2\le r\le200\).

A successful replay prints `VERIFY_OK`. The finite ranges are consistency checks only; the infinite claims are proved symbolically in RESULT.md.
