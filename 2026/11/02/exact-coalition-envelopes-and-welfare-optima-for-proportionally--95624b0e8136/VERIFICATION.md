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

# Reproducible exact checks

Execute `python3 verify_pf.py` with a standard Python 3 installation. The program uses only the standard library and performs exact rational arithmetic. In the reviewed execution its output was:

```
PASS: exact finite envelopes, witnesses and welfare optima: 2548 instances
PASS: 12 sharp-component examples; strict UFS/PF welfare example
```

For each finite profile it enumerates all nonempty coalitions that contain each designated agent; compares their maximum demands with the proposed prefix/suffix envelope and its coalition witness; verifies endpoint order; independently checks representative points in all gap cells; and compares the optimizer with a separate exhaustive critical-point calculation. The two final groups test exact sharpness and the strict welfare distinction.

The finite tests do not establish the theorem for arbitrary numbers of agents, arbitrary positions, or irrational parameters. The universal proof is given in `RESULT.md`, including all normalization, endpoint, tie and empty-feasible-set cases. Publication priority has not been externally certified.
