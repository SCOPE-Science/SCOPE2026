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

# Reproducibility and limits

Run `python check_seedbank.py` from this directory with Python 3 and SymPy installed. The code checks 256 strictly interior rational parameter tuples, the symbolic Jacobian determinant and inverse, stationary pair-state balances and triple conditional laws, a singular boundary, and a named exact rational example. A successful run finishes with `PASS`.

The mathematical proof is in `RESULT.md`. The finite computations do not prove the full parameter result by enumeration; every quantified theorem step is proved algebraically there. No finite-sample confidence statement follows from structural identification. Full historical-priority certification and independent audit have not been performed. No external validation evidence is represented.
