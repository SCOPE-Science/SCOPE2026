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

# Computational verification

Run `python3 verify.py` with a Python 3 standard library. The program reproduces the exact example numerically, checks the sign of the extinction sensitivity using a small one-sided increment, tests strict decline of the Perron eigenvalue on grids for seven parameter choices, and confirms that the sample high-dispersal regime is subcritical.

Successful execution prints a PASS line and the example's model parameters, critical rate, and founder-establishment probabilities. Near-critical fixed-point iteration can converge slowly, so verification deliberately avoids numerical evaluation at the exact spectral threshold. The symbolic proof in `RESULT.md` establishes all infinite and boundary assertions. Numeric checks alone neither prove monotonicity for all real parameters nor establish literature novelty.
