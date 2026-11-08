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

# Verification record

`transfer_verify.py` calculates the sixteen time-pair rung letters, 256 transfer pair-states and the open-neighbor majority truth tables. It checks all 256 entries of the exact order-five recurrence certificate and the eight displayed signature multiplicities, and compares full transfer counts with the Fibonacci–Lucas expressions for \(2\le n\le80\). This is the certificate needed for the all-length count, rather than a sample-only argument.

`bruteforce_verify.py` independently constructs ladder edges and evaluates the local synchronous majority rule twice for every one of the \(4^n\) binary configurations at each \(2\le n\le10\). It checks fixed points, all two-step periodic points, and those changing at every vertex. The standalone programs require only Python's standard library. Both scripts were executed successfully; the actual outputs are saved as `transfer_output.txt` and `bruteforce_output.txt`.

The programs give internally reproducible verification, not independent human certification. No exhaustive count of transient basins or first-entry times is claimed. This document does not establish priority against unpublished or unindexed work.
