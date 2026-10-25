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

# Verification of cyclic length-three sphere formulas

The standalone `verify_cyclic3.py` enumerates each input over the specified small alphabets and forms a set of resulting output words using both nonidentity cyclic three-rotations at every allowable position, plus the unchanged word. In a separate calculation it evaluates the factor statistics \(H\) and \(K\), then tests \(|\mathcal B_3(x)|=2n-3-2H-K\). A separately constructed three-state weighted recurrence calculates the entire output-ball-size polynomial coefficient by coefficient. It also checks total populations, exact rational means and maximum-count recurrence (for alphabets having at least three symbols).

The finite exhaustive domains are \(q=2, 3\le n\le11\); \(q=3,3\le n\le9\); \(q=4,3\le n\le8\); and \(q=5,3\le n\le7\). There are 27 parameter combinations and 218584 inspected input words. The script is Python standard-library only. `verify_cyclic3.log` is its execution output and ends with `VERIFY_OK`.

Finite testing is an error-catching check, not an infinite proof. The derivation and all-parameter quantifiers follow from the window-collision classification and inductive transfer matrix in `RESULT.md`. There is no independent external audit.
