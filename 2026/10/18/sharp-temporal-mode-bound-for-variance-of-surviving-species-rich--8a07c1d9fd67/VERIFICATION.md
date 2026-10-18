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

# Checks and limits

`verify.py` was executed with Python 3 standard library. It checked the analytical derivative at the declared chronological witnesses for community sizes 1 through 10, all 110 expected signs, and the rational inequalities used to control slower and faster hazard classes. The run terminated successfully.

Reproduction: `python verify.py`. The core proof is symbolically displayed in `RESULT.md`; its zero-count induction and uniform geometric-series witness bounds are valid for every finite positive integer community size and do not rely on the finite checker. Neither the verifier nor the argument establishes empirical applicability to correlated or nonexponential extinctions. Bibliographic originality has not been independently certified.
