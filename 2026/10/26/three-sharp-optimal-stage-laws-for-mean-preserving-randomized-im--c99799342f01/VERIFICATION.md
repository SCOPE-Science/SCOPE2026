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
# Reproducible checks and limits

The self-contained analytical proof is in RESULT.md. The standalone `CHECK.py` uses exact SymPy simplification to check the three global supporting-line identities, the contact locations and masses, the three minimum formulas, and equality of their adjacent endpoint limits. It then tests 1,278 exact-rational inequalities on selected finite stage grids as illustrative cross-checks. Execute `python CHECK.py` with Python 3 and SymPy installed.

The structural factorization identities are exact. The sign analysis in RESULT.md is the universal proof: endpoint-chord positivity for the first regime, the squared tangency formula for the middle regime, and positivity of the midpoint-tangent bracket for the third regime. The finite-grid tests do not certify universal optimality and should not be used independently as evidence for it.

No independent audit has been conducted. The result is only for real scalar decay with iid mean-half stage laws and exact arithmetic in the stage solves; no claims are made for general nonlinear, nonautonomous, or multi-eigenvalue systems.
