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

The standalone file `verify_universal_jet.py` works over the characteristic-zero polynomial ring with algebraically independent parameters for all coefficients permitted by the normalized geometry. Execute `python3 verify_universal_jet.py` with SymPy installed. The actual output was:

```
UNIVERSAL_TRIPLE_LINE_QUADRATIC_JET_OK
fano_jacobian_det: 1
second_type_local_equation_quadratic_jet: -6*e*f*k
quadratic_hessian_det: -36*k**2
```

The code verifies the four Grassmannian Fano equations have transverse Jacobian the identity, the zero obstruction through degree two in the free parameters, and the exact universal quadratic determinant jet for the full cubic with symbolic coefficients. The crucial geometric reductions and limits are documented in `RESULT.md` and are not inferred solely from software. The general polynomial identity holds in characteristic zero, subject to the explicit nonzero coefficient \(k\); the local nodality statement uses smoothness, the formal implicit-function theorem and the cited singular-support theorem.

Independent audit: not performed.
