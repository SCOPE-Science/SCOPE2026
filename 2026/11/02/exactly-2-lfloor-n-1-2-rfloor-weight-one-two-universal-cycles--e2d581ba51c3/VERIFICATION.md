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

The theorem is proved for all integers \(n\ge2\) by a finite-state structural argument and BEST Euler tour counting. Independent finite checks are included only as reproducibility evidence:

- `python3 verify_euler.py` performs edge-distinguishing depth-first exhaustive enumeration of rooted Euler tours at each \(2\le n\le11\) and compares with the formula. The unique root outgoing edge fixes rotation.
- `python3 verify_trees.py` independently forms the directed Laplacian on all vertex words of weight at most two and computes the exact root cofactor using Bareiss fraction-free determinant elimination for \(2\le n\le11\).

Their full standard output is included in `verify_euler_output.txt` and `verify_trees_output.txt`. The computations neither certify the all-length theorem on their own nor establish publication priority. No independent audit has been performed.
