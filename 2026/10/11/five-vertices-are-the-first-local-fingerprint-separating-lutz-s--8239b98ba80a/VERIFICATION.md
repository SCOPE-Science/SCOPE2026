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

Run `python3 verify.py` with a standard Python 3 interpreter. The script contains the published facet table, constructs the two child balls, recomputes all nonempty faces, and checks the full \(f\)-vector \((12,58,84,37)\) and mod-two Betti vector \((1,0,0,0)\) of each.

It then checks the explicit boundary permutation \((2\,3)(5\,6)(7\,10)(8\,12)(9\,11)\), exhaustively enumerates all vertex subsets of sizes \(1\) through \(5\), computes each induced-subcomplex profile, and verifies equality through size \(4\) and the exact six multiplicity shifts at size \(5\).

All matrix ranks are computed exactly over \(\mathbb F_2\). There is no randomization, numerical tolerance, or unexamined subset in the stated range. The script does not test other coefficient fields or claim anything about unrelated simplicial balls.
