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

The analytical proof in `RESULT.md` uses two explicit lower-bound coalition families and exhibits equal-attainment allocations, including all boundary and homogeneous cases. The standalone checker `VERIFY.py` uses Python's exact `fractions.Fraction` arithmetic to check efficiency, exact lower-bound equality, and all type-count proper coalitions for every \(0\le a,b\le32\) except \((0,0)\): 1088 parameter profiles and 312544 inequalities.

With SciPy available, the same checker separately solves 54 full, unsymmetrized signed-allocation least-core linear programs, for all populations of size at most 9. Their optimum deficits agree numerically with the exact formula (tolerance \(10^{-8}\)). An all-size theorem follows from the printed proof, not from finite experiments. There is no external/independent validation or exhaustive literature completeness certificate.
