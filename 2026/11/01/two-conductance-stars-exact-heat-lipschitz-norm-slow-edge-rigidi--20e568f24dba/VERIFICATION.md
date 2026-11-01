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

Run `python verify.py` in the same directory. It requires only Python 3 standard-library modules. Exact rational arithmetic checks the full leaf-gradient intertwining on seven representative integer-rate configurations. An independent full-state heat uniformization evaluates 28 parameter-time cases and tests the analytic norm and edge ranking; seven high-contrast cases corroborate the limiting envelope. It prints a CHECK_OK result upon success. A separate additional numerical test of 90 parameter-time cases also passed.

# Analytic coverage and limitations

The uniformization and numerical tests alone cannot certify any continuum of parameters or infinitely many numbers of leaves. Those quantifiers are handled by the explicit two-by-two gradient reduction, the three-exponential strict comparison, and the exact algebraic bound in `RESULT.md`. No independent audit has been performed.
