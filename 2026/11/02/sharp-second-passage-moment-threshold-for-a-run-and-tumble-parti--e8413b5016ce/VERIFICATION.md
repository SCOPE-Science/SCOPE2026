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

# Reproducible verification

Run `python verify.py` with Python 3 and SymPy. The script symbolically checks the large-position logarithmic-flux exponent, the orientation-corrected first-moment generator limit, the quartic generator drift, the second-moment leading coefficient, the deterministic zero-speed moment recursion check, and positive rational examples. The file was executed on the packaged source prior to serialization.

These calculations corroborate the exact algebra used in the proof. They do not independently verify infinite-domain passage-time integrability, accessibility of the outer state region, or publication priority: those claims rely on the analytic comparison, stopped-generator and source-inspection arguments in RESULT.md. The only status established here is self-review; independent auditing has not been performed.
