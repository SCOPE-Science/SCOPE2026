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

# Verification and reproducibility

The primary theorem is derived analytically in `RESULT.md`. Reproduce the supporting exact-rational checks with:

```
python3 verify.py
```

The Python script uses only the standard library. It checks the following exact algebraic equalities with rational inputs: the general adjoint-pair two-product identity on 400 deterministic matrix samples of dimensions 1 through 5; the two-component strongly convex–concave block-curvature identity on 405 examples; the complete scalar starting-state comparison on 200 configurations; and six explicitly evaluated witness/positive-definiteness assertions. The expected output is:

```
PASS: 1011 exact-rational matrix and vector assertions
```

These are independent computational consistency tests on finite samples, **not** an exhaustive verification of infinitely many dimensions, coefficients or step lengths. The proof of the universally quantified claims is the explicit trace identity and exact block multiplication in `RESULT.md`; the witness uses rational exact calculations and a principal-minor positive-definiteness certificate. Both sampling protocols are compared after exactly two component updates and at the identical step. No floating-point tolerance, Monte Carlo simulation, unreported training or external data are used. There has been no independent external audit.
