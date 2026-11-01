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

# Reproducibility and scope

The companion `checker.py` checks exact finite Cesàro-square entries and the dyadic formulas and rank separation in finite sections; it reported 174,080 finite assertions passed with NumPy. Run with `python3 checker.py`. The proof of the Schatten threshold is analytic, using a dyadic singular-value count and Schatten quasi-triangle inequalities; finite checks cannot verify the infinite assertion. Independent mathematical auditing has not been performed.
