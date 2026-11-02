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

The finite-patch generator and stationary equations were checked with exact `fractions.Fraction` arithmetic using the attached standalone `CHECKER.py`.

Run `python3 CHECKER.py` using Python 3.8 or newer. Expected final line begins `PASS 10975 exact checks`. The checker tests all \(2^N\) configurations for \(N=3,4\), 216 positive rational parameter sets (including full catastrophes), stationarity, all joint moments through order \(N\), inverse recovery, the Jacobian identity, and two distinct models with identical two-site observations.

The generator-to-moment recursion and the global inverse are proved in `RESULT.md`; finite checks corroborate them and are not used to infer a universal statement by enumeration. No stochastic estimation from finite data, imperfect detection, heterogeneous sites, or inference of absolute time scale is established.
