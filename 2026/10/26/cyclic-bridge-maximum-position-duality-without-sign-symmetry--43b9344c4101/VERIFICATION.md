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

The analytic proof is the deterministic orbit sum in equation (4), averaged under cyclic invariance, plus a law-preserving reroot-and-negated-reversal map for the stronger joint symmetry. These steps work in the presence of tied maxima and dependent increments.

The accompanying `verify.py` was executed with Python 3 and returned PASS for 10,376 zero-sum integer strings, 59,387 orbit-lag pairs, and 1,274 symmetric simple random-walk bridges. It compared complete reflected joint histograms, tested odd powers 1, 3, and 5, and confirmed a skew example where the unconditional reflection does not hold.

Finite enumeration is diagnostic only; it cannot establish an all-length theorem. The Brownian formulas follow separately from circular-shift invariance and the standard Brownian bridge covariance kernel.
