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

From a directory containing `verify.py`, execute `python3 verify.py` with any standard Python 3 implementation. It requires no external packages. The program calculates all permutation arrays independently of the symbolic argument for \(1\le n\le8\); evaluates every mixed indicator covariance using exact integer counts and `fractions.Fraction`; tests the exact signed covariance formulas through \(n=1000\); and checks the positive covariance limit's finite approximation is between zero and \(1/2\) on a supplied size sequence.

Observed output on the included script:

```
PASS: 500825 exact checks; exhaustive permutations n<=8 and formula checks n<=1000
```

The proof for every \(n\) is the subset-conditioning calculation and integer inequality in `RESULT.md`. No finite verification implies an infinite claim on its own. The independent audit status above is descriptive only and has not been assessed here.
