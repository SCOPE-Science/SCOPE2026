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

The new theorem is proved analytically in `RESULT.md`: (i) the maximal-slope pair forces a unique center value, (ii) piecewise-affine selectors give the universal upper bound, and (iii) explicit pairs attain each candidate ratio, including those defining the maximum. Positive arm lengths, constant data, the two-arm boundary, ties of selector pairs, and arbitrary finite leaf counts are covered by the argument.

The standalone `check_amle_star.py` was executed with Python and SciPy. Its output was:

```
PASS {'independent_LP_masks': 3220, 'attaining_pairs': 50, 'random_pairs': 3000, 'equilateral_cases': 13} total 6283
```

The separate numerical benchmark solves a linear program for each potential center-pair selector and each output coordinate, with the boundary Lipschitz unit polytope encoded directly as pairwise inequalities. The attaining examples and random data inequalities are evaluated with rational inputs. No run timeout, incomplete enumeration, or extrapolation is claimed to be a proof for arbitrary leaf counts; the general proof is symbolic. Independent audit has not been performed.
