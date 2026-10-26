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

The analytic proof uses exact hypergeometric mean payoffs, birth–death stationary balance and differentiation of the mean drift. `check.py` independently differentiates detailed-balance products with exact rational arithmetic rather than reproducing the drift derivation alone. It tested 302 exact-rational parameter instances and two finite-selection numerical cases using the original nonlinear transition probabilities; command `python check.py` returned `PASS: 302 exact-rational comparisons; two direct nonlinear-transition tests`.

The tests do not prove arbitrary population-size boundary statements by enumeration. The analytic reflection argument establishes those results. No independent audit has been performed.
