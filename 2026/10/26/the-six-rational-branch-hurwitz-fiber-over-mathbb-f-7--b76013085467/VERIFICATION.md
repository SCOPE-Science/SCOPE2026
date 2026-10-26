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

# Exact verification

The polynomial normal form is a monic cubic in the fiber coordinate. Over \(\mathbb F_7\), its discriminant is \(3Q^3+R^2\). The fixed branch divisor is \(X^6-Y^6\), and the scalar \(\kappa\) is nonzero. The search domain is precisely three coefficients of a binary quadratic and four of a binary cubic, each in seven elements, hence \(7^7=823543\) choices.

Run `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify`. Its tested output is `VERIFY_OK 823543 coefficients, 12 models, 2 fixed-base classes, 1 unmarked class; points=13`. The C++ checker enumerates all coefficient vectors, expands the discriminant, checks every coefficient, compares the complete solutions with the two explicit families, checks the fiber-scaling orbit and target swap, and enumerates all rational points of the source cubic.

Run `python check_evaluation.py` with NumPy available. The independently implemented checker evaluates the discriminant at all six nonzero rational slopes rather than expanding and matching coefficients. It checks the nonzero leading value, recovers the same twelve solutions and both fiber-scaling orbits, and independently counts thirteen source points. It reports `INDEPENDENT_VERIFY_OK 12`. Both commands were executed successfully.

A separable binary sextic of degree six that vanishes at the six distinct slopes and has nonzero leading coefficient must be proportional to \(X^6-Y^6\). This justifies the independent checker. Neither checker asserts anything about degree-three covers with a different geometric branch divisor, higher-characteristic fields, or geometric solutions over the algebraic closure. The general geometric and cover-descent steps are proved in the main result, not inferred from the finite loops. No external independent audit has been performed.
