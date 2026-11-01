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

# Reproduction and limitations

Install `sympy` using `requirements.txt` and run `python3 verify.py`. This performs symbolic checks for the algebraic phase threshold, orientation-endpoint contact centers and strict concavity coefficient, as well as 3,077 independent five-vertex minimum-enclosing-circle enumerations over 17 axis ratios and 181 orientations. On completion the script prints `ALL_CHECKS_PASSED`. The finite samples do not prove an all-orientation geometric minimum; the proof in `RESULT.md` does so through exact inequalities, an obtuse-triangle boundary argument, and active-contact certificates. No independent audit is asserted.
