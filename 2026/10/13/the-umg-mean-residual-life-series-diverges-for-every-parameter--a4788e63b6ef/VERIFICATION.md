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
Let
\[
\xi=\frac{y}{1-y}
\]
and
\[
S_X(u)
=
\left(
1+\theta u+
\frac{\theta^2u^2}{2(1+\theta)}
\right)e^{-\theta u}.
\]
The defining UMg MRL numerator is
\[
I(y)
=
\int_\xi^\infty
\frac{S_X(u)}{(1+u)^2}\,du.
\]

The source series has signed term
\[
a_k
=
\frac{(k+1)(-1)^k}{\theta^{k+1}}
\left[
\Gamma(k+1,\theta\xi)
+
\Gamma(k+2,\theta\xi)
+
\frac{\Gamma(k+3,\theta\xi)}{2(1+\theta)}
\right].
\]
For all sufficiently large \(k\),
\[
|a_k|
\ge
\frac{k+1}{2(1+\theta)\theta^{k+1}}
(k+2)^{k+2}e^{-(k+3)},
\]
so the terms do not approach zero.

The exact numerator used by the checker is
\[
I(y)
=
\frac{e^{-\theta\xi}}{2(1+\theta)}
\left[
\theta+(2-\theta^2)(1-y)
\right]
+
\frac{\theta^3e^\theta}{2(1+\theta)}
E_1\!\left(\frac{\theta}{1-y}\right).
\]

The bundled checker compares this expression against direct quadrature at multiple \((\theta,y)\) pairs and evaluates source-series terms. At \((\theta,y)=(1,0.4)\), the valid MRL is
\[
0.2833221886367211246550\ldots,
\]
while the source-series terms grow rapidly in magnitude.
