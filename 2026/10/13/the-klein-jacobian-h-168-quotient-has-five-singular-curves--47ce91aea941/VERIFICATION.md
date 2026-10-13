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
The accompanying `verification/verify.py` replays the finite arithmetic and local cyclic-quotient checks used after the literature classification has reduced the problem to explicit stabilizer types.

It verifies:

- \(21\) involutions contribute three translated generic-\(C_2\) elliptic curves each, hence \(63\) such curves after separating the axis fixed by the unique containing \(C_4\).
- The source counts \(28\) generic-\(C_3\) and \(21\) generic-\(C_4\) elliptic curves.
- Setwise stabilizer orders \(8,6,8\) give orbit lengths \(21,28,21\), hence \(3+1+1\) curve-orbits.
- The displayed order-two and order-four tangent matrices have determinant one and fixed-space dimension one; the order-four transverse eigenvalues are \(i,-i\).
- For \(n=2,3,4\), the invariant monomials \(a=u^n\), \(b=v^n\), \(c=uv\) satisfy \(ab=c^n\), giving transverse \(A_{n-1}\).
- The final component profile is five curve components plus the two isolated \(\frac1{7}(1,2,4)\) points supplied by the source.

The verifier is not an exhaustiveness certificate for the group action. Exhaustiveness rests on the full-text stabilizer and fixed-locus classification in arXiv:2107.03745. No finite sampling is used to infer an infinite geometric statement. Special dissident/intersection germs are intentionally outside the claim.
