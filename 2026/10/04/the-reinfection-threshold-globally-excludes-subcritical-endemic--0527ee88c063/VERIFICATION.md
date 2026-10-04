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

The mathematical verification uses the scalar endemic-equilibrium equation from the source and checks the following exact implications.

1. Positive endemic equilibria are equivalent to positive roots of
\[
F(I;\beta,B)=
\frac{\Lambda\beta(M+\beta\sigma I)}{(A+\beta I)(\mu+\beta\sigma I)}
+\frac{\delta BI}{\mu+BI}-K.
\]
2. For every \(I>0\), both \(\partial F/\partial\beta\) and \(\partial F/\partial B\) are strictly positive.
3. At \(\beta=\beta_1^\ast\) and \(B=\beta_2^\ast\), clearing the positive denominator gives
\[
-\frac{I^2K(\beta_1^\ast)^2}{AM^2\delta}(C_0+C_1I),
\]
with
\[
C_0=(K-\delta)P^2+A\delta\mu\sigma(M-\mu)(M-A\sigma)>0,
\qquad
C_1=M\beta_1^\ast\sigma(K-\delta)P>0.
\]
Therefore the corner value is strictly negative for every \(I>0\), and parameter monotonicity propagates that sign to the full claimed rectangle.

The bundled `verify.py` uses only the Python standard library. It evaluates the threshold formulas and the corner factorization with exact rational arithmetic on multiple nondegenerate rational parameter sets and checks representative monotonicity comparisons. Running it from the extracted packaged artifact prints `VERIFY_OK`.

The checker is not an exhaustive proof over real parameters; the universal proof is the symbolic sign argument above. No independent audit has been performed.
