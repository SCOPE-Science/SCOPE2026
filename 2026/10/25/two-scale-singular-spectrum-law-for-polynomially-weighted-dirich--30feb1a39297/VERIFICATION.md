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

# Reproduction and scope

Run `python verify.py` from the same directory with Python 3, NumPy and SciPy. The script checks exact rational normalized-basis coefficient identities for differentiation orders one through three and two exact coefficient-norm indices. It compares the first two analytic Hilbert--Schmidt coefficients against rapidly converging positive series for four independent parameter choices and compares the banded singular-value calculations for a coupled polynomial on Hardy space with the predicted operator-norm and Schatten limits. The finite-parameter singular-value errors decrease as the dilation approaches the identity in the tested range. No data download is required.

The infinite-dimensional theorem is proved by the five steps in RESULT.md: exact matrix representation; trace moments with controlled tails; convergence of level counting and all Schatten powers; norm-edge trial vectors; and the explicit Hilbert--Schmidt expansion. The checks cannot establish quantifiers over all polynomial coefficients, all positive Schatten exponents or the limiting parameter. No independent audit has been performed.
