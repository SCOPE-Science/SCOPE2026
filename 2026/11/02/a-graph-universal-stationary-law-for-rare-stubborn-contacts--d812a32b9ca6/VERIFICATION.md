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

The analytic proof establishes the fixed-network infinite-time stationary law and its rare-contact limit. The standalone Python 3 script `verify_gossip.py` was run from the packaged source and passed 290 exact-rational generator, topology, and rare-anchor checks, including all stationary first/second moment residuals. The numerical values displayed by the script are illustrative; no finite enumeration proves the general result.

The proof uses a positive-probability contraction word for invariant-law uniqueness, a Laplacian energy identity for disagreement, and a Wasserstein-contractive effective empirical-mean recursion. Their assumptions and the normalization of each update are written in `RESULT.md`. No independently conducted audit or independent validation is claimed.
