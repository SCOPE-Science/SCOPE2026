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

# Reproduction and limits

The exact analytic chain is the Wronskian-based index phase, the two-term convergent Macdonald expansion, the Riccati stationary equation, and a nondegenerate phase implicit-function calculation. The script `check.py` recomputes numerical stationary points directly from special functions and compares them with both asymptotic coefficients. It uses `mpmath` and reports the tested orders and indices; successful finite checks alone do not prove the infinite result. No independent audit was performed. The remainder estimates hold for each fixed positive \(\nu\) only.
