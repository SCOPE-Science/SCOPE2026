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

The executable `check_approximation.py` uses Python 3's standard `fractions` and `math` libraries. From the directory containing it, run `python3 check_approximation.py`.

The program independently computes the exact Gram-matrix squared least-squares error in the monomial basis for \(p\), and the exact unit-conductance network effective resistance, for every \(n=0,1,\ldots,7\). It constructs an explicit residual \(R\) with all polynomial row and column constraints, divides \(1-R\) by \((1-z)(1-w)\) by prefix sums, checks its degree bound, and verifies the exact upper and lower inequalities. All calculations use rational arithmetic. The execution yielded:

```
n=0 exact_minimum=3/4
n=1 exact_minimum=7/12
n=2 exact_minimum=17/36
n=3 exact_minimum=71/180
n=4 exact_minimum=27/80
n=5 exact_minimum=1483/5040
n=6 exact_minimum=3281/12600
n=7 exact_minimum=2939/12600
PASS: 8 independent Gram/network equalities, 8 polynomial divisibility, 16 exact interval inequalities.
```

The infinitely many-degree theorem is proved symbolically using polynomial factorization, elementary inequalities, and a combinatorial block construction. The finite tests only confirm specific computations and conventions; they are neither an exhaustive search nor an independent audit. No claim about unrelated weights or every polynomial is implied.
