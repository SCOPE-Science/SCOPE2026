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

For the source's Parameter Set 1,
\[
Q=10,\qquad \beta=0.2,\qquad \Delta P=0.1,\qquad C_l=2,\qquad C_g=5,
\]
so the \(x\)-axis drift coefficient is
\[
a_x=\beta Q\Delta P+C_l-C_g=-2.8.
\]

On the invariant \(x\)-axis, conditions (16)-(18) reduce to
\[
-2.8x\le-x,\qquad0\le0,\qquad0\le0,
\]
so the source's displayed drift test is met for every \(x>0\).

For
\[
dx=a_xx\,dt+\sigma x\,dW,
\]
the exact solution is
\[
x(t)=x_0\exp\!\left[
\left(a_x-\frac{\sigma^2}{2}\right)t+\sigma W_t
\right].
\]
At \(\sigma=3\),
\[
2a_x+\sigma^2=3.4>0,
\]
hence
\[
\mathbb E[x(t)^2]=x_0^2e^{3.4t}.
\]
The pathwise exponent is instead
\[
a_x-\sigma^2/2=-7.3<0.
\]

The bundled `verification/verify.py` recomputes these identities and also checks the general \(p\)-moment exponent
\[
pa_x+\frac{p(p-1)}2\sigma^2.
\]
It uses only the Python standard library and prints `VERIFY_OK` on success.

Unproved limits: no full nonlinear necessary-and-sufficient stochastic stability classification is asserted, and no claim is made about the source's particular simulation noise values.
