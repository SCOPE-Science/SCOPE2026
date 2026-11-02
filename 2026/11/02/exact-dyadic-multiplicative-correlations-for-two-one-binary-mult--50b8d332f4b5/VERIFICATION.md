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

# Verification
The standalone `verify.py` is executable with ordinary Python 3 and has no third-party dependencies. It checks eight values \(2\le k\le9\), 14 direct dyadic prefix sums per parameter, explicit signed carry transition rows, the exact vector relation, and additional recurrence terms. The symbolic row identity in `RESULT.md`, not these finite checks, proves the infinitely quantified formula. Independent audit has not been performed.
