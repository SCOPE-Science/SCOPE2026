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

The file `verify.py` uses only the Python standard library. It enumerates every one of the \(n!\) equally likely insertion orders for \(2\le n\le8\), constructs each actual binary search tree, and computes the path-to-maximum length and zero-child node count directly. It checks the exact mixed moment and the exact covariance using rational arithmetic. It independently checks the split identity for each \(2\le n\le500\), including the boundary corrections, and computes the closed formula with `Fraction`.

Reproduce by executing `python verify.py`. The tests are finite; the proof in `RESULT.md` establishes the general infinite sequence. No independent review has been performed. For \(n\le3\), variance formulas for large \(n\) should not be substituted for the exact small-sample distributions. The asymptotic correlation uses the published variance of occupied leaves in the cited binary-search-tree model.
