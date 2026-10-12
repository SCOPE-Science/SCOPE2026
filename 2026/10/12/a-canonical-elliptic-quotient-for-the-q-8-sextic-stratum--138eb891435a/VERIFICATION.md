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

The exact checker verifies the projective matrix relations \(A^2=B^2\), \(A^4=B^4=1\), and \(BAB^{-1}=A^{-1}\), as well as invariance of the sextic polynomial under both generators. It checks the central fixed-line factorization \(YZ(Y^4+Z^4)\), the equations defining the three fixed pairs in the coordinate \(t=Y/Z\), and the Riemann--Hurwitz arithmetic giving quotient genus \(1\).

The proof of exhaustiveness is group-theoretic: every nontrivial subgroup of \(Q_8\) contains its central involution, so there cannot be ramification away from the six central fixed points. The characteristic restriction makes the action tame and the six fixed points distinct.

The verification does not compute a Weierstrass model or \(j\)-invariant of the quotient, and it does not decide which special parameter values have automorphisms strictly larger than the displayed \(Q_8\).
