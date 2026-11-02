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

The standalone `check.py` uses the stated exact formulas without external datasets. Invoke `python check.py` with Python 3, SciPy. Its recorded output is embedded as `check_output.json`. It checks independent normalization integrals, the zero-flux second boundary identity, pressure density agreement, increasing pressure, agreement of state-potential and direct force integrals, the local quadratic shape law, large-aspect slope, and the positive integral of the derivative controlling monotonicity.

All 356 assertions passed. Uniform positivity, every-dimensional majorization and the all-stiffness existence statement are proved analytically in RESULT.md, not by numerical tests. None of these tests constitutes independent validation or establishes originality.
