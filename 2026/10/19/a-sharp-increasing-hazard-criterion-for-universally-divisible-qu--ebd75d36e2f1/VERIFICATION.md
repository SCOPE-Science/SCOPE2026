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

The stationary-in-age renewal formula, time-local channel decomposition, and cyclic-unitary failure witness are verified analytically in `RESULT.md`. `check.py` uses finite-step NumPy computations and exact Fraction arithmetic to check channel composition, positivity in tested nondecreasing examples, and explicit negative witnesses for age-drop positions 1 through 14. Run with `python check.py` after installing `numpy>=1.24`.

The exact initial two-step certificate has reset probabilities 2/5 and 1/5; it yields \(Y_1=\operatorname{diag}(7/25,-2/25,0)\), \(q_1=4/5\), and a negative eigenvalue \(-2/25\) in the uniquely forced intermediate map. No finite computation substitutes for the all-dimension, all-time analytical proof. Independent scientific validation has not been performed.
