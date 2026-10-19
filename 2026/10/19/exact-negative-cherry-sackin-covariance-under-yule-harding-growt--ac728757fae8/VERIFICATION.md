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

# Verification and reproducibility

Run `python3 verify_yule.py` in the same directory as this document using a standard Python 3 installation. No third-party dependencies are required. The code independently computes exact integer counts of leaf-splitting histories for each unordered canonical tree shape and then evaluates the expected cherry count, Sackin sum, cherry-member depth sum and mixed covariance. It compares four statistics exactly at each \(n=3,\ldots,12\), plus the same four moments at each \(n=3,\ldots,300\) using independently constructed rational moment recurrences; 1232 exact assertions pass.

This finite verification does not prove the formulas for arbitrary size. The general proof comes from the tree-by-tree conditional moment identities and induction in `RESULT.md`. It depends on uniform selection among **current leaves**, topology-only depth in edges, and explicit starting state at three leaves. The normalization differs from external-branch lengths in a continuous-time coalescent. No independent audit, computer-formal proof or exhaustive search of all published literature is claimed.
