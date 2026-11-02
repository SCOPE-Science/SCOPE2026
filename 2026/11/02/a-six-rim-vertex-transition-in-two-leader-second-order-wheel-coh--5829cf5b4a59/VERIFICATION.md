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

# Reproducible finite and analytic checks

Run `python verify.py` with Python 3.8 or later; no third-party modules are needed. The program forms the unit-weight wheel Laplacian independently at every order from three to ten rim vertices and evaluates the first and second inverse traces of **all 216** labelled two-leader principal grounded submatrices, with exact rational Gaussian elimination. It verifies the exact winner sets and tie counts for every order. It separately evaluates every rim-pair orbit by Schur-complement inversion of the two path blocks and checks exact equality of the objectives; the orbit values are also stored in `finite_cases.csv`.

The two performance comparisons on the six-rim wheel are exactly \(25/12>2\) for the inverse trace and \(157/144<9/8\) for the inverse-square trace. The script also checks the rational assertions \(400<405\) and \(27/100<10/36\) used to separate the all-size analytic bounds.

The infinite part is not computer-exhausted: for every rim-pair grounding at \(n\ge11\), the constant follower test vector gives \(J_2\ge(n-1)^2/36\). For every hub–rim grounding, nonnegative resolvent walk counts are dominated by the infinite path, giving \(J_2\le 3(n-1)/(5\sqrt5)<27(n-1)/100\). Since \(n-1\ge10\), the latter is strictly smaller than the former. This proves the asserted infinite tail; the finite computation covers the remaining cases.

No exact optimizer ranking among two-rim placements for all \(n>10\) is claimed, and no independent mathematical audit has been performed.
