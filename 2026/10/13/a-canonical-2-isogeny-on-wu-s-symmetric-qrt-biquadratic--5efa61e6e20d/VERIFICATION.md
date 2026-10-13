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

The initiating source was checked at the exact symmetric QRT equation, its projective completion, Proposition 10.1, the discriminant, and the stated genus-one conclusion. In particular,
\[
\Delta_Q
=
\alpha\gamma
\bigl((2\alpha+\beta)^2-4\gamma\bigr)
\bigl((2\alpha-\beta)^2-4\gamma\bigr)
\neq0
\]
implies \(\alpha\gamma\neq0\).

In bihomogeneous coordinates the curve is
\[
X_1^2Y_1^2
+\alpha(X_1^2Y_0^2+X_0^2Y_1^2)
+\beta X_0X_1Y_0Y_1
+\gamma X_0^2Y_0^2=0.
\]
The involution changing the signs of both \(X_1\) and \(Y_1\) is visibly an automorphism. Its only possible ambient fixed points are \((0,0)\), \((0,\infty)\), \((\infty,0)\), and \((\infty,\infty)\). Their substitutions require, respectively, \(\gamma=0\), \(\alpha=0\), \(\alpha=0\), or an impossible vanishing of the leading coefficient. Hence the action is free.

The invariant-field calculation is exact:
\[
u=x^2,
\qquad
v=xy,
\]
and
\[
[k(C):k(u,v)]=2.
\]
Substituting \(y=v/x\) and multiplying the original equation by \(u=x^2\) gives
\[
\alpha u^2+(v^2+\beta v+\gamma)u+\alpha v^2=0.
\]
Thus this field is exactly the fixed field. Since the quotient is etale of degree \(2\), Riemann--Hurwitz gives quotient genus \(1\).

When \(O\in C(k)\) is chosen as origin, the quotient map sends \(O\) to the chosen quotient origin and is therefore an elliptic-curve homomorphism. Its kernel is the two-point orbit \(\{O,\tau(O)\}\), proving that \(\tau(O)\) is nonzero rational two-torsion and that the deck involution is translation by that point.

No finite experiment, numerical approximation, or unproved classification enters the verification. The only access limitation in the literature comparison is that a related 2026 paper on a different elliptic model was inspected at abstract level only.
