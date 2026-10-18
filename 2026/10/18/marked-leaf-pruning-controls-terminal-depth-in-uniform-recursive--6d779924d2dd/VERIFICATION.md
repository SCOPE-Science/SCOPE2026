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

# Reproducibility

Execute `python3 verify_rrt_pruning.py` from this directory; it needs only Python's standard library. It enumerates every independent-parent recursive tree with three through eight vertices, compares the full bivariate depth/leaf histogram to the Eulerian-derivative polynomial, verifies the closed covariance formula, and checks all possible prescribed subsets of intermediate leaf labels against the pruned depth distribution. It reports 695 exact assertions. The finite enumeration does not certify the unrestricted theorem; the accompanying written proof does.

The proof of the conditional law relies on independence and support of parent choices; no external symbolic theorem prover or third-party data is required. The outdegree and depth marginal recursions are derived in the proof. Independent external scientific validation has not been performed.
