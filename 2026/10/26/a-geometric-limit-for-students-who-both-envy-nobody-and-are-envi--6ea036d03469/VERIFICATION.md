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

The source code `CHECK.py` is packaged alongside the result. It ran successfully using Python standard-library arbitrary-precision rational arithmetic. The independent profile enumeration covered every strict-ranking profile for one through four students; the analytic joint-factor recurrence and finite-law inversion were checked for one through twelve students. The checked three-student distribution is \(\Pr(C_3=0)=4/9\), \(\Pr(C_3=1)=1/3\), and \(\Pr(C_3=3)=2/9\). These finite computations do not certify the infinite statement; its proof is given in `RESULT.md`. The geometric weak limit is established by pgf convergence for \(0<z<1\), not numerical extrapolation. No independent scientific audit has been conducted.
