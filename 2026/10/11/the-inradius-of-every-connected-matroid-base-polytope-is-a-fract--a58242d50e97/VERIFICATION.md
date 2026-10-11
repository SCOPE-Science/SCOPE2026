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
The theorem is proved analytically in `RESULT.md`; no finite computation is used as a substitute for the arbitrary-matroid argument.

Checks performed:
- The base polytope is kept in its intrinsic affine hull \(x(E)=k\).
- The projected normal of \(x(S)\le\operatorname{rk}_M(S)\) is
  \[
  \mathbf 1_S-\frac{|S|}{n}\mathbf 1_E,
  \]
  with squared norm
  \[
  \frac{|S|(n-|S|)}{n}.
  \]
- A ball of radius \(t\) centered at \(x\) satisfies the subset inequality exactly when
  \[
  x(S)+t\,c(S)\le\operatorname{rk}_M(S).
  \]
- Dualizing the resulting linear program gives nonnegative subset weights with equal total weight through every ground-set element. Their common value is positive, so normalization gives a fractional partition.
- For every basis \(B\), fractional partitioning gives
  \[
  \sum_S\lambda_S\operatorname{rk}_M(S)\ge
  \sum_S\lambda_S|B\cap S|=k,
  \]
  confirming the sign of the dual numerator.
- Connectedness gives full intrinsic dimension and hence positive inradius, so the optimal dual scale saturates the geometric denominator constraint.
- The uniform-matroid specialization was independently checked from the direct distances from the hypersimplex barycenter to \(x_e=0\) and \(x_e=1\).

Limits:
- Disconnected matroids require projection to a smaller component-defined affine hull and are outside the claim.
- No assertion is made that an optimal fractional partition has a uniquely determined support.
