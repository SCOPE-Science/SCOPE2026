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
# Computational verification and limits

Run the standalone file with Python 3:

```bash
python3 wheel_smooth_fixed_point_check.py
```

The script independently constructs every orientation of the wheel for \(3\le m\le9\), discards cyclic orientations by topological sorting, computes reachability and nontransitive arcs, and checks the closed and spoke-stratified counts. It asserts total orientations \(3^m-3\) and ends with `VERIFY_OK`.

Observed smooth counts for \(m=3,4,5,6,7,8,9\): \(24,58,140,344,868,2234,5808\). Finite enumeration cannot prove the all-\(m\) result. The algebraic proof is the five-part argument in `RESULT.md`. No independent audit or external proof certification was performed.
