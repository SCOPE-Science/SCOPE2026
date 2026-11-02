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

The analytic proof is in `RESULT.md`. Execute `python3 verify.py`; Python 3.10+ with only the standard library is required. The script rechecks the algebra's sign predictions for sampled parameters, tests the permutation statement for four seasons, checks the \(p=1\) commuting boundary numerically, and uses exact rational arithmetic to certify a three-season violation of ascending sorting for \(p=2\). It passed with 11,444 sampled comparisons and the exact fraction witness. This is not an independent audit or a computational proof of universal quantification.

The strict comparison for all inputs, the invariant interval, and the sharpness argument are established by the symbolic identities and monotonicity calculations in the paper, not by enumeration. The result does not establish long-run effects or optimal scheduling beyond the stated domain.
