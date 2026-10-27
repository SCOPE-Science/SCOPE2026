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
# Reproducibility
Run `python checker.py` with SymPy installed. The checker computes exact coordinate moments from the beta distribution, checks the moment normalization in dimensions 2 through 25, and proves the displayed quotient derivative identity symbolically. Its observed output was:

`PASS: 144 normalized-moment, derivative, and special-value symbolic assertions`

These finite symbolic cases cannot establish the all-dimensional theorem; the proof in RESULT.md establishes that statement. The key analytic lemmas to check are the trace-free eigenvalue third- and fourth-power sum inequalities, their equality conditions, and the reduction from complex to real extremizers. Independent review remains unperformed.
