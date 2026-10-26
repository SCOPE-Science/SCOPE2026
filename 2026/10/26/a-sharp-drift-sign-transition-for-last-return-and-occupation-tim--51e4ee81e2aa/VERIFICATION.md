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

The analytic proof verifies the strict successive ballot coefficient ratio and its MLR consequence for every horizon and every real \(p\in(0,1)\). The standalone `verify_lastzero.py` enumerates all sign paths for \(n=1,\ldots,7\) and five rational choices of \(p\) each, checks the full exact bivariate joint law cellwise, and tests the sharp covariance signs. It reports 35 successful exact rational parameter sets. These finite calculations corroborate, but cannot substitute for, the general MLR argument. No independent external audit has been performed.
