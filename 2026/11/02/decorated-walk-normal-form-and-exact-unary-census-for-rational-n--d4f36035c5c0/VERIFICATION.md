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
# Reproducibility and verification

Run `python3 checker.py` with Python 3.9 or newer and no external dependencies. The script computes three independent semantics in integer arithmetic: full-grammar closure on every half-grid, enumeration of all allowable decorated half-grid vectors, and a tridiagonal transfer-matrix power. It compares the three complete finite sets for \(d=1,2,3\) and derives transfer-matrix counts for \(d=1,\ldots,8\). Successful execution ends with `ALL_CHECKS_OK`.

The checker tests exhaustive finite samples of the *syntax closure*, not an unbounded sequence of denominators. The proof for all \(d\ge1\) relies on the affine-component induction, the max-min piecewise-linear representation theorem, and the weighted-walk estimate in `RESULT.md`. The cited representation theorem is externally published mathematical work, not an independent audit of this result. No independent audit has been performed.
