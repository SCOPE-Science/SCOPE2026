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

# Verification notes

The accompanying `verify.py` was executed with Python and SymPy. It checked exactly, for each \(M\in\{3,4,5,6\}\), the defining equations, the rank-two Jacobian on explicit generic linear and isotropic rank-one singular points, and the rank \(2M-2\) Hessian on the full Jacobian tangent space. All eight instances passed, and the program printed `VERIFY_OK`. It also checked the hollow-matrix determinant, the rank-one relation determinant, and the degree formula algebraically.

The general proof is independent of those finite experiments: it uses the rank bound for nonzero hollow symmetric \(3\)-by-\(3\) matrices, an exact rank-one determinant, irreducibility and degree of a Segre-embedded smooth quadric, and two formal normal-form constructions. Its conclusions concern the reduced singular locus and dense open subsets, not the full singular scheme or intersections of strata. Independent mathematical audit has not been performed.
