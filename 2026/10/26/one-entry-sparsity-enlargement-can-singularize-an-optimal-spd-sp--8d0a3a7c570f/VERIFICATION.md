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
# Verification notes

The companion `verify_spai.py` uses only standard-library exact rational arithmetic (`fractions.Fraction`). To reproduce, execute `python verify_spai.py` from the extracted package directory. It evaluates the columnwise normal equations, SPD leading minors, the exact rank-collapse and objective gap, explicit rational perturbations, and small two-dimensional SPD examples. Its finite checks do not prove the dimension-free or limiting assertions; the accompanying exact proof establishes those claims. No external independent audit has been performed.
