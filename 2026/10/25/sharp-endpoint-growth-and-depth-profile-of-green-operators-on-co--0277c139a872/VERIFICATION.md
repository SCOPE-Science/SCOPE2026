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

A standalone exact-Fraction test (`check.py`) constructs the complete rooted graph in eleven branching/height configurations. For every matrix row and column it tests the unnormalized Poisson equation and symmetry; it also checks zero row sums, row-depth estimates, the error parameter, leaf-sign classification and closed leaf row formula. Exact-rational assertions passed: 9,424. The code uses no external modules and can be run with Python 3 using `python check.py`. Finite testing is a consistency check only; the analytical statements for unbounded height and branching are proved in RESULT.md. The independent audit status remains not performed.
