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

Let
\[
p=\frac{q}{q-1},
\qquad
\rho=\omega^{1/(2-q)}.
\]
For an ordered dual vector with
\[
M=\max\{|u_1|,|u_2|\},
\qquad
m=\min\{|u_1|,|u_2|\},
\]
the exact norm is
\[
\|u\|_{X^*}
=
\begin{cases}
\bigl(M^p+\omega^{1-p}m^p\bigr)^{1/p},&m\le\omega M,\\
(M+m)/(1+\omega)^{1/q},&m\ge\omega M.
\end{cases}
\]

For \(r=m/M\), the normalized Euclidean profile on the first branch has logarithmic derivative
\[
\frac{r\bigl(\omega^{1-p}r^{p-2}-1\bigr)}
{\bigl(1+\omega^{1-p}r^p\bigr)(1+r^2)},
\]
so its unique minimum is \(r=\rho\). The second branch is strictly increasing. Consequently,
\[
a=(1+\rho^2)^{-(2-q)/(2q)}
\]
and
\[
b=\max\left\{1,\frac{\sqrt2}{(1+\omega)^{1/q}}\right\}
\]
are the exact Euclidean comparison constants.

Euclidean Ptolemy gives
\[
C_{\mathrm{Pt}}(X^*)\le(b/a)^2.
\]
For
\[
0<\omega\le2^{q/2}-1,
\]
the triple
\[
x=(\rho,1),\qquad
y=\frac{1-\rho}{1+\rho}(-1,\rho),\qquad
z=(1-\rho)(-1,1)
\]
attains
\[
\frac{2}{(1+\omega)^{2/q}}(1+\rho^2)^{(2-q)/q}.
\]
For
\[
2^{q/2}-1\le\omega<1,
\]
the triple
\[
x=(1,-\rho),\qquad
y=(-1,-\rho),\qquad
z=(0,-\rho-\rho^{-1})
\]
attains
\[
(1+\rho^2)^{(2-q)/q}.
\]
Thus the exact formula holds on both regimes and agrees at the phase boundary.

The proof is fully symbolic. No finite enumeration, timeout, or numerical search is used to establish the quantified result. The unproved scope is dimension above two and Lorentz families with more than two weights.
