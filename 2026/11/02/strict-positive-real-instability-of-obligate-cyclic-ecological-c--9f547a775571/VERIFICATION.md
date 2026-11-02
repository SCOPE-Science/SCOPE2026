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

The mathematical certificate is the argument that at every strictly positive equilibrium, the absolute value of the successor-column entry in each row of the column-scaled interaction matrix strictly exceeds all other row entries together by the strictly positive intrinsic death rate. Linear interpolation from the signed cycle-permutation matrix to the full scaled interaction matrix preserves strict row dominance after a column permutation. Its determinant therefore has the exact negative sign of the pure cycle matrix. The Jacobian characteristic polynomial changes sign between zero and sufficiently large positive arguments, giving a genuine positive real eigenvalue.

Run `python3 verify.py` using Python 3 with no third-party packages. The deterministic test checks 84 rationally constructed positive equilibria of dimensions 3 through 9, with five exact homotopy determinant samples each, followed by 13 uniform witnesses through order 15. Expected standard output:

```
PASS: 84 nonuniform rational equilibria n=3..9, 5 exact homotopy points each; 13 explicit witnesses n=3..15.
```

The test was executed successfully on the embedded program. Its numerical range is finite and supplements rather than proves the all-order conclusion. The proof does not certify dynamic behavior other than instability of strict positive equilibrium points. Independent validation has not been performed.
