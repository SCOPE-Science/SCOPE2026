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

Run `python3 check_two_apex.py` in this package directory with Python 3, NumPy and SciPy installed. The script enumerates vertices of the anchored Lipschitz ball using half-space intersections, then solves an unrestricted real-linear extension linear program. A successful run prints `TWO_APEX_UNRESTRICTED_LP_OK` after 12 fully feasible parameter cases, including the sharp contractive boundary. The exact theorem is proved in `RESULT.md`; floating-point numerical checks do not establish a statement quantified over all parameters. No independent scientific audit has been performed.
