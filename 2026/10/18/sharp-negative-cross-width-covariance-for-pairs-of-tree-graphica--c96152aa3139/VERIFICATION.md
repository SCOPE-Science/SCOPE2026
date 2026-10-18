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

# Reproducibility of the cross-width covariance theorem

Run `python3 verify.py` with Python 3 and its standard library. The checker regenerates all labelled spanning trees from Prüfer codes at orders four, five, and six. It measures the exact degree cross-product and common-edge count for **all 1,695,497 ordered pairs**, and checks both the asserted minimum and its necessary-and-sufficient equality conditions. The exact minima are attained by 12, 480, and 28,080 ordered labelled pairs, respectively.

For every one of 160 prescribed random unit directions in orders four through seven, the checker independently enumerates the endpoints of the generating Minkowski sum and verifies that maximum minus minimum vertex support equals the root-segment width expression. It also compares fixed-seed covariance estimates from 150,000 Gaussian-derived spherical directions at orders four and twelve against the exact gamma-function covariance expression. The run ends with `VERIFY_OK`.

These checks cannot establish an infinite-order theorem or mathematical uniqueness; the proof is given in `RESULT.md`. The source record concerning individual-tree width variance contains the already-known absolute-Gaussian pair kernel; this is credited rather than claimed as new. Independent audit status is not performed.
