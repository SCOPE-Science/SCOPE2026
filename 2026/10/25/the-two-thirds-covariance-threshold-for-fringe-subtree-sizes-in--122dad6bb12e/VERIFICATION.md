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

The included `verify.py` runs directly with the Python 3 standard library. It enumerates all insertion permutations for tree sizes \(2\le n\le8\), constructs their ordered binary search trees and fringe-subtree profiles, and checks the stated conditional means and covariance spectrum using exact fractions. It separately checks the finite-sum formula, every sign, and both conservation identities for \(2\le n\le200\).

The executed checker finished with `VERIFY_OK`. Its last substantive results were `PERMUTATION_EXHAUSTION_PASS 8 40320 permutations 7 size strata` and `FINITE_SUM_AND_PROFILE_PASS n=2..200`.

The unrestricted mathematical proof is the root-splitting recurrence, the three defect moments, and the total-covariance identity in `RESULT.md`. Exhaustive checks for bounded sizes are not infinite proof. A verification of historical priority is not a consequence of code execution.
