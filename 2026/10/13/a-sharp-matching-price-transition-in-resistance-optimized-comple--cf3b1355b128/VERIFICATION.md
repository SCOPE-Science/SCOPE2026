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

# Verification of priced perfect-matching network allocation

The standalone file `verify_matching.py` requires only Python 3 standard-library modules. From the same directory as `RESULT.md`, execute:

```bash
python3 verify_matching.py
```

Its expected success line is:

```text
VERIFY_OK 66 exact cases, 660 budget-constrained comparisons; spectrum, matrix inverse, and threshold
```

It evaluates even orders \(N=4,6,8,10,12\), with rational parameters \(r\) chosen so that \(t=2/(1+r^2)\) and the theorem's unique symmetric optimum are rational. It independently constructs the full Laplacian, inverts \(L+J/N\) over exact fractions, checks the spectral resistance formula, checks the budget, tests alternative nonnegative feasible symmetric weights, and checks the difference to deleting the matching. It also tests exact threshold equalities through \(N=14\).

The code checks finitely many cases, not all real prices or all graph sizes. Its rational alternative allocations are not a global optimizer proof. Global correctness, uniqueness, and limits require the analytic argument in `RESULT.md`. The critical nonstandard ingredients are the decomposition into matched-pair antisymmetric and pair-symmetric Laplacian eigenspaces and the strict matrix inverse-trace convexity argument.

No independent scientific audit has been performed.
