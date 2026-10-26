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

# Reproduction
Execute `python verify_windmill.py` with Python 3.9 or later; it uses only the standard library. The program enumerates occupied-vertex states by exact rational first-step recursions and compares them against the closed formulas. There are 36 full-dynamics comparisons, 15 one-pair checks and 15 odd-blade checks (66 assertions of formulas in total); the largest full-dynamics calculation evaluates 3,072 distinct masks. The analytic proof, not the finite tests, establishes all size and rate quantifiers and limiting statements. Published-source searches cannot prove historical uniqueness, and no independent audit has been performed.
