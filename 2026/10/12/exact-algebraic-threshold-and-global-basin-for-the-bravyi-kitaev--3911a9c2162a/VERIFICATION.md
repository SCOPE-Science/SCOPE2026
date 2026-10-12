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

The proof is analytic. Exact algebra factors the published fixed-point defect and reduces its only nontrivial physical zero to
\[
z^3+z^2-2z-16=0.
\]
The derivative \(3z^2+2z-2\) is positive for \(z\ge2\), and the cubic changes sign between \(2\) and \(3\). The reciprocal substitution \(z=y+y^{-1}\) is one-to-one from \((0,1]\) onto \([2,\infty)\), completing uniqueness. The sign of the same factor gives the two monotone basins.

`artifacts/verify.py` was executed from its packaged path. It symbolically checks the factorization and reciprocal reduction, computes the root to high precision, and performs supplementary sign checks. The stored output begins with `VERIFY_OK` and includes

`epsilon_star=0.14148029265616723834457933046600748495661194250918`

Finite numerical checks are not used to prove the infinite iteration statement. No claim is made about global optimality among all magic-state distillation protocols.
