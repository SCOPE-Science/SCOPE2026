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

The exact checker `artifacts/verify.py` performs the following finite symbolic checks over \(\mathbb Q(\omega)\) with \(\omega^2=-19\):

- reconstructs the conic equation after the source's plane parametrization and verifies that its quadratic matrix has determinant \(-5913/4\);
- verifies that the Khatri--Rao matrix has rank \(5\), center \([0:-2:0:3:2:2]\), and target hyperplane \(w_0+3w_1+w_2=0\);
- computes the row-line restriction \(44t^2+16t+17\) and discriminant \(-2736\), certifying two distinct row directions;
- checks explicit normalization preimages and their common target \([0:17:-51:-66:-77:-44]\);
- verifies immersivity at both preimages and a nonzero tangent-transversality minor \(2357771608607690880\omega\);
- computes the Jacobian/Fitting ideal of \(V(us,ut,vs,vt)\) and verifies that it is the square of the maximal ideal, with quotient basis \(1,u,v,s,t\) and length \(5\).

The global uniqueness of the singular point follows from the projection geometry in RESULT.md: any double fiber corresponds to a secant through the center, and any differential failure corresponds to a tangent incidence. The row-line calculation gives exactly one secant and no tangent incidence. The checker is finite and exact; it does not attempt a classification of other projection centers.
