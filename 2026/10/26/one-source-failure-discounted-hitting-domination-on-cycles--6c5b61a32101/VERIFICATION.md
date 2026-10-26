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

# Verification record

The mathematical proof uses the exact recurrence for random-walk hitting support on source-to-source paths, a deletion-to-adjacent-gap equivalence, a sharp cyclic gap construction, and a rooted cyclic transfer count. The source's original two-boundary recurrence is acknowledged; no independence is claimed.

Run `python verify_resilience_exact.py` to reconstruct support after removal of each pin from rational linear systems. The test examines cycles with 3 through 8 vertices, fidelities 2/5 and 3/5, and every rational critical gap cutoff B from 1 through n. The completed output was `VERIFY_OK exact rational direct deletion checks: 6688`.

Run `python verify_cycle_transfer.py` to enumerate the claimed optimum configurations independently by vertex subsets and by closed transfer walks. It checks all 77 instances with 3 through 13 vertices and B from 2 through n, including B=3 explicit counts. The completed output was `VERIFY_OK independent trace and subset census: 77`.

Both programs use only the Python standard library. Finite exact checks substantiate implementation and small parameter boundaries but cannot substitute for the all-integer proof. Cases with more than one simultaneous pin failure, graph-vertex deletion, other graph families, and external mathematical validation remain unexamined.
