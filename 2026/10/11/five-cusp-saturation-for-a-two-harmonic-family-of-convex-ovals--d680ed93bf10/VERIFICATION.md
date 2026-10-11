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

The symbolic checker reconstructs the proof from the support function.

It verifies
\[
p+p''
=
R-3a\cos(2t)-24b\sin(5t)
\]
and the Wigner signed support
\[
\frac{p(t)-p(t+\pi)}2=b\sin(5t).
\]
Thus the five Wigner cusp parameters are the five simple zeros of \(\sin(5t)\) modulo \(\pi\).

For the centre symmetry set, the checker differentiates
\[
\frac{\rho(t)}{\rho(t+\pi)}
\]
and verifies that its numerator is
\[
-24b\left(
10R\cos(5t)
-a\bigl(9\cos(7t)+21\cos(3t)\bigr)
\right).
\]
After setting
\[
\lambda=-3a/R,\qquad x=\cos t,
\]
the cusp equation is checked to factor as
\[
2xQ_\lambda(x^2)=0.
\]

The checker computes
\[
\operatorname{disc}_yQ_\lambda
=
-6400
(\lambda^2+2\lambda-4)
(147\lambda^2+630\lambda+500),
\]
as well as
\[
Q_\lambda(0)=25-21\lambda,
\qquad
Q_\lambda(1)=5(1+\lambda).
\]
It verifies the sign witnesses at \(\lambda=\pm1/2\) and the two explicit roots at \(\lambda=0\). These exact identities certify two simple roots in \((0,1)\) throughout \(|\lambda|<1\).

The finite numerical examples printed by the checker are supplementary regression checks only. The theorem for every admissible parameter follows from the symbolic argument.
