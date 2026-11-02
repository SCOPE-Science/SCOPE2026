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

The accompanying `checker.py` is a standalone Python 3 script using only the standard library. Its `check` entry point enumerates all labelled finite posets through five vertices and every loop set, computes the original two-step transit relation and the Hasse digraph independently, and compares the exact simple and rooted loop counts on every tree Hasse diagram with the theorem. The source code and its expected final sentinel `ALL_CHECKS_OK` are included. Finite enumeration is not a proof of arbitrary finite size; see the written graph/path proof in `RESULT.md`. Independent audit has not been performed.
