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

Execute `python3 verify_c4.py` with the Python standard library. This uses exact fractions for all ball averages and determinants and pairs of rationals for the Q(sqrt(10)) eigenvector calculation. Its successful result is:

```text
EXACT_CHECK_OK; checked=81; rational-PSD=79; exceptional=2;
exceptions=(0,1,0,1),(1,0,1,0); coefficient and eigenvector checks passed
rational-PSD-by-number-of-global-balls={0: 14, 1: 32, 2: 24, 3: 8, 4: 1}
```

For each of the 79 nonexceptional matrices, the program proves strict positive definiteness of (29/20)I minus its exact Gram matrix by checking every leading principal minor. It then independently checks the four nontrivial coefficients of the exceptional Gram characteristic polynomial, the exact algebraic eigenvector identity, the threshold inequality, and strict radius-choice consistency. The proof in RESULT.md explains why these finite certificates cover every real input to the four-vertex graph. Numerical sampling, independent peer review, and the corresponding result for arbitrary cycles are not part of these checks.
