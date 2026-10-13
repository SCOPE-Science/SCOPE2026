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

For the map
\[
X=xD(y)e^{r(1-x)},
\qquad
Y=\beta b x(1-S(y)),
\]
with
\[
S(y)=e^{-y(1+c y)},
\qquad
D(y)=(1-b)+bS(y),
\]
the checker solves the source's positive-equilibrium equation
\[
H(y)=f(y)-g(y)=0.
\]

At each reconstructed equilibrium it builds the Jacobian
\[
J=
\begin{pmatrix}
1-rx & -b x e^{r(1-x)}S(y)(1+2cy)\\
y/x & \beta b xS(y)(1+2cy)
\end{pmatrix}
\]
and checks
\[
\det(I-J)=-r y H'(y).
\]

For
\[
(\beta,b,c,r)=(2,0.49,3,1),
\]
the lower root is approximately
\[
(x,y)=(0.9947339,0.0104492)
\]
with multipliers approximately
\[
0.0106013,\qquad 1.0195174.
\]

For
\[
(\beta,b,c,r)=(2,0.49,3,3),
\]
the lower root is approximately
\[
(x,y)=(0.9985180,0.0088588),
\]
and the checker verifies a real multiplier greater than \(1\).

The replay confirms the source examples and algebraic identity. The general theorem itself is proved symbolically in `RESULT.md`.
