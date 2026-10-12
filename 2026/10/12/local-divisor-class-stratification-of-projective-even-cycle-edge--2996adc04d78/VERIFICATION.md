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

The algebraic computations implemented in `artifacts/verify.py` use exact integers. For each \(1\le a,b\le11\), an independent Smith-normal-form calculation checks that the row/column relation matrix has rank \(a+b-1\), every nonzero Smith invariant factor equals \(1\), and the cokernel has free rank \((a-1)(b-1)\). For \(2\le m\le10\), the checker independently enumerates all coordinate zero-pattern strata and verifies the component count, torus fixed-point count and maximal local class-group rank. For \(2\le m\le8\), it exhaustively checks squarefree monomial membership in the Jacobian ideal against membership in the proposed intersection of coordinate primes. Output: `VERIFY_OK 87506 Smith normal forms, zero patterns, radical-Jacobian ideals`.

The finite test ranges do not establish the infinite theorem. The proof uses the rank-one incidence kernel of the even cycle, the squarefree monomial ideal identity, Serre normality and an exact divisor-class localization presentation. The Smith tests serve only as independent regression checks of the presentation.
