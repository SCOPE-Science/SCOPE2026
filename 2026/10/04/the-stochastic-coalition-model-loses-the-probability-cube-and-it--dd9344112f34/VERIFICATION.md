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
The general checks are analytic.

For the printed stochastic equations with \(\sigma>0\), a constant solution requires the diffusion vector
\[
\sigma(x,y,z)^{\mathsf T}
\]
to vanish. Hence only \((0,0,0)\) can be a point equilibrium.

On \(Y=Z=0\), the enterprise-\(A\) equation reduces to
\[
dX_t=-k_A X_t\,dt+\sigma X_t\,dW_t,
\qquad
k_A=\frac12ua^2,
\]
with exact solution
\[
X_t=x_0\exp\!\left[\left(-k_A-\frac{\sigma^2}{2}\right)t+\sigma W_t\right].
\]
Its normal upper tail gives a strictly positive probability that \(X_t>1\) for every \(x_0\in(0,1)\), \(\sigma>0\), and \(t>0\).

The bundled checker independently verifies the source-parameter arithmetic
\[
k_A=1.2,\qquad
\pi r_A-k_A=3.8,
\]
and evaluates the illustrative escape probability
\[
\Pr(X_{0.05}>1)\approx0.1957956707
\]
for \(x_0=0.8\) and \(\sigma=2\).

Finite computation is not used to prove noninvariance or the equilibrium obstruction.
