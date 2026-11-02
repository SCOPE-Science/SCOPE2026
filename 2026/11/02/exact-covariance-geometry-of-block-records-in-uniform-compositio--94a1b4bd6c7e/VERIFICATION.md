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

Run `python3 checker.py` from the directory containing this file and the program. The program uses Python standard-library integer and rational arithmetic, enumerates uniform positive compositions for all \(2\le n\le14\), and separately enumerates every continuous-label ordering for selected smaller cases. In the reviewed run it reported 432 exact identities/sign assertions and 305826 microstates.

The code checks both entries of the proposed full covariance matrix and a mean identity. It does **not** establish the all-order coefficient identity, strict sign beyond the tested range, or any infinite-regime limit. Those claims are proven analytically in `RESULT.md`. No independent audit has been performed.
