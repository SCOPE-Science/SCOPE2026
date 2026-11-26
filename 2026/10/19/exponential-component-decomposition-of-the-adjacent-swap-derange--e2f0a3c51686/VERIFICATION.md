---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python3 verify.py` in this directory. The script uses the Python standard library to enumerate all derangements for orders two through five, construct their complete adjacent-position-swap graphs, and compare the intrinsic and unrestricted distances of every distinct reachable pair. It also checks the displayed path and independently computes the two distances at order six. The extension to arbitrary orders is proved by the fixed-tail argument in `RESULT.md`, not by running the program at progressively larger orders.
