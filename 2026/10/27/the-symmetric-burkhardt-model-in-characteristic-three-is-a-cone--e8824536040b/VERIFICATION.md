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

# Verification scope

Run `python3 verify.py` with a standard Python 3 interpreter. The checker directly enumerates all projective points over \(\mathbf F_3\) in the 5- and 6-coordinate presentations and evaluates elementary symmetric polynomials, the constrained Jacobian equations, and two tangent-cone Hessian determinants.

Expected output:

```text
S(F3)=25; singular S(F3)=15; nodal-chart Hessian dets=1,1
B(F3)=76; singular B(F3)=46; 15 predicted singular lines
VERIFY_OK
```

This calculation verifies all \(\mathbf F_3\)-point counts and the stated local Hessian examples; it is not exhaustive over algebraic closures. The proof's cubic-root argument and standard K3 resolution theorems supply the infinite-field conclusions. No independent audit has been performed.
