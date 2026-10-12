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

The analytic proof is the certificate for the infinite theorem. It separates every candidate by whether the weight already reaches \(N\) or \(2k\), then proves that any lighter function has a fully nonempty part and satisfies the exact singleton-support lower bound.

`verify.py` independently reconstructs the definition on all complete-multipartite profiles of orders two through five for \(k=2,3,4\). For every vertex assignment by subsets of \([k]\), it tests the empty-vertex rainbow condition and the singleton-support condition directly, computes the true optimum, and compares it with the theorem. It also compares the theorem with the published complete-bipartite piecewise formula on a larger finite parameter range.

The finite exhaustive range is not a proof of the arbitrary-order theorem. It is a regression and boundary check for the analytic derivation. The external literature comparison remains subject to ordinary indexing risk, and independent audit has not been performed.
