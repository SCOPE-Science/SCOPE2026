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

The accepted claim was checked directly from the equilibrium equations of arXiv:2609.27270v2.

1. Under exchange symmetry, the cleared equations reduce to two quadratics with common coefficients \(A=d/K\), \(B=d/L\), and \(C=d-a_1/K\).
2. Their difference factors as \( (x_1-x_2)(A(x_1+x_2)+C) \). This exhausts diagonal versus off-diagonal equilibria.
3. The diagonal equation has exactly one positive root because its leading coefficient is positive and its constant term is \(-a_0<0\).
4. On the off-diagonal branch, the sum is \(S=a_1/d-K\) and direct substitution forces \( (B-A)x_1x_2=a_0\). Conversely, any positive distinct roots of the resulting quadratic satisfy both cleared equations.
5. The source's two symmetric examples were replayed numerically from the formulas. The first gives approximately \(0.00277864\) and \(8.99722136\); the second gives approximately \(0.01020409\) and \(98.98979591\), matching the source's rounded coordinates.
6. The edge cases \(L=K\), \(a_1\le dK\), and zero discriminant were checked separately. Zero discriminant merges the reflected pair with the unique diagonal equilibrium.

The global stability conclusion is not independently reproved here; it is a direct application of Theorem 1 of arXiv:2609.27270v2 after the new algebraic criterion has established exactly three distinct positive equilibria. No stochastic conclusion and no local normal-form classification at the equality surface is claimed.
