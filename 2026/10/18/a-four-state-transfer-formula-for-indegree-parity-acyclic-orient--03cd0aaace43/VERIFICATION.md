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

# Reproduction and limits

Run `python3 verify_wheel.py` from the same directory. No third-party packages are required. The script evaluates every edge orientation of each wheel with rim sizes three through eight, computes indegree parity from directed incidence, checks acyclicity by Kahn's topological-sort algorithm, and compares all resulting counts with the stated four-state matrix product.

The tested wheels have 64, 256, 1,024, 4,096, 16,384 and 65,536 orientations respectively: 87,360 distinct edge orientations in all. All 504 feasible parity signatures are covered. The expected acyclic totals are 24, 78, 240, 726, 2,184 and 6,558 respectively. The full proof for every rim size is in `RESULT.md`; these finite tests are not claimed as universal or externally certified evidence.

The matrix formula returns nonnegative integers for every binary input. Its arithmetic-operation count is linear in rim length; exact-integer bit operations are not constant-time in that length.
