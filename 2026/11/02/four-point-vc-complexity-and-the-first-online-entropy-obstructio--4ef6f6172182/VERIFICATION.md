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

The exact finite tests were executed using `VERIFY.py` and `ALT_CHECK.py`. The former enumerates every path in the indicated finite range, checks peak conditions and counts, exhausts all coordinate partitions in the online recursion, and replays four complete decision-tree witnesses from `certificates.json`. Its independent literal-set recursion checks the smaller cases. The latter uses a separate literal-set representation to reject depth eight at semilength nine and depth nine at semilengths ten and eleven. The all-size VC bound is proved combinatorially; its six-size witness is reproduced by computation and padded in the proof. All-size exact Littlestone growth is unproved beyond the displayed logarithmic lower bound.

Exact expected terminal messages: `TWO_DEFECT_DYCK_ALL_CHECKS_PASS` and three `ALTERNATIVE_UPPER_PASS` lines. No external reviewer or independent audit has assessed this result.
