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

The general theorem is verified by the proof in `RESULT.md`.

A separate finite checker, `verify.py`, represents a finite equivalence relation by the integer partition of its class sizes. For every pair of partitions of nonempty sets of size at most \(8\), and for each \(1\le q\le4\), it recursively solves the exact \(q\)-round Ehrenfeucht--Fraisse game and compares the answer with the two truncated-profile conditions. The expected terminal output is `VERIFY_OK`.

This computation checks small cases and boundary behavior only. It is not an exhaustive proof for unbounded \(q\) or structure size, and no independence claim is made.
