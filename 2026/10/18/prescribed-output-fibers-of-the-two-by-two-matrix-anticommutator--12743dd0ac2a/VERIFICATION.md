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
# Verification details

Run `python3 verify.py` using Python 3 and no external packages. The source directly enumerates all \(q^8\) ordered matrix pairs, forms their anticommutators by field operations, and reconstructs the expected count for each of the \(q^4\) targets independently using kernel and eigenline calculations.

All prescribed targets matched for \(q=2,3,4,5\), including the nonprime extension field \(\mathbb F_4\); observed total pair counts were 256, 6561, 65536 and 390625. The output ends in `VERIFY_OK`. The verification does not certify the infinite family beyond these finite checks; that conclusion follows from the linear-algebra proof. Earlier studies cover the zero-fiber count and are explicitly excluded from the nonzero-output novelty assertion.
