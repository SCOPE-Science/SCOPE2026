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

# Reproducible checks and limitations

Run `python check.py` with Python 3, NumPy, and SciPy from the extracted package directory. The 2578 diagnostic assertions cover independent flux transfer-matrix eigenvalues, 35 sampled competitors in both material layers for each of 64 parameter families, weak-strength asymptotics, and physical scaling. The analytic proof, not the finite enumeration, supports universal existence, uniqueness, and the sharp constant. The code does not inspect publication priority; external review has not been performed.
