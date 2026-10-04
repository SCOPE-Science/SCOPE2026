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

For an arbitrary positive-definite quadratic pullback \(q\), let
\[
m=\inf_{z\ne0}\frac{N_\lambda(z)^2}{q(z)},\qquad M=\sup_{z\ne0}\frac{N_\lambda(z)^2}{q(z)}.
\]
The squared Euclidean distortion is \(M/m\). Averaging \(q\) over independent sign changes of the two coordinates preserves the bounds \(m q\le N_\lambda^2\le M q\) after averaging and kills the cross term. Thus it suffices to use \(q_t=x_1^2+t x_2^2\), \(t>0\).

With \(u=x_2^2/x_1^2\),
\[
\frac{N_\lambda^2}{q_t}=\frac{\max\{\lambda^2,1+u\}}{1+t u}.
\]
The branch point is \(u=\lambda^2-1\). Monotonicity on each branch gives
\[
D(t)=
\begin{cases}
\dfrac{1+t(\lambda^2-1)}{\lambda^2 t},&0<t\le\lambda^{-2},\\
1+t(\lambda^2-1),&\lambda^{-2}\le t\le1,\\
\lambda^2t,&t\ge1.
\end{cases}
\]
The first expression decreases and the latter two increase on their respective ranges, so the minimum is exactly \(2-\lambda^{-2}\) at \(t=\lambda^{-2}\).

For the von Neumann--Jordan lower bound, the two unit vectors
\[
\left(\lambda^{-1},\sqrt{1-\lambda^{-2}}\right),\qquad
\left(\lambda^{-1},-\sqrt{1-\lambda^{-2}}\right)
\]
give ratio \(2-\lambda^{-2}\). Any Euclidean pullback of squared distortion \(D\) gives \(C_{\mathrm{NJ}}\le D\) by the parallelogram identity, hence the exact distance proves equality.

Limits: the proof is specific to the real two-dimensional Banaś--Frączek norm and does not classify all optimal isomorphisms. No numerical sampling or finite enumeration is used as a substitute for the global argument.
