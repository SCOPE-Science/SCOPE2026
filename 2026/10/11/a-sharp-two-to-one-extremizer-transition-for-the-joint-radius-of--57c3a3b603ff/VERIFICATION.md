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

# Mathematical verification
The analytic reduction to \(F_c(y)\) is direct expansion of two fourth powers. Exact optimization is complete for all \(0\le c\le1\) and all Hilbert-space dimensions at least two. The endpoint derivative sign and the factored excess are independently checked in `verify.py` for a rational parameter sample; sampled trigonometric optimization illustrates consistency but is not the argument for continuum correctness. The expansions \(1-y_*=6\delta+O(\delta^2)\) and \(F_c(y_*)-F_c(1)=(9/2)\delta^2+O(\delta^3)\) are exact consequences of the rational formulas. Repeat by running `python3 verify.py`. Bibliographic originality is not independently audited and the complete 2026 motivating manuscript was inaccessible.
