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

The source coefficient-series root is
\[
\frac{\pi}{4M}
=
2\sum_{m=1}^{\infty}
\frac{\rho_\alpha^m}{1+\alpha m}.
\]
Every term is increasing in
\[
\rho_\alpha
\]
and decreasing in
\[
\alpha,
\]
which gives uniqueness and strict parameter monotonicity.

For
\[
T_\alpha(r)
=
2\sum_{m=1}^{\infty}
\frac{r^{m+1}}{(m+1)(1+\alpha m)},
\]
termwise differentiation on compact subdisks gives
\[
T_\alpha'(r)=S_\alpha(r).
\]
Thus
\[
R_\alpha
=
\int_0^{\rho_\alpha}
(a-S_\alpha(t))\,dt
\]
and
\[
R_\alpha'
=
2\sum_{m=1}^{\infty}
\frac{
m\rho_\alpha^{m+1}
}{
(m+1)(1+\alpha m)^2
}
>0.
\]

For
\[
\beta=1/\alpha,
\]
the exact decomposition
\[
\sum_{m=1}^{\infty}
\frac{r^m}{m+\beta}
=
-\log(1-r)
+
\sum_{m=1}^{\infty}
r^m
\left(
\frac1{m+\beta}-\frac1m
\right)
\]
has a uniformly summable correction because
\[
\left|
\frac1{m+\beta}-\frac1m
\right|
\le
\frac{\beta}{m^2}.
\]
At
\[
r=1,
\]
the correction is
\[
-\psi(1+\beta)-\gamma.
\]
This proves
\[
\log\frac1{1-\rho_\alpha}
=
\frac{\pi\alpha}{8M}
+
\psi\!\left(1+\frac1\alpha\right)
+
\gamma
+
o(1).
\]

The covering expansion follows from
\[
T_\alpha(1)
=
\frac2\alpha
-
\frac{2}{\alpha^2}
\sum_{m=1}^{\infty}
\frac1{m^2(m+1)}
+
O(\alpha^{-3})
\]
and
\[
\sum_{m=1}^{\infty}
\frac1{m^2(m+1)}
=
\frac{\pi^2}{6}-1.
\]
Because
\[
1-\rho_\alpha
\]
is exponentially small, replacing
\[
T_\alpha(\rho_\alpha)
\]
by
\[
T_\alpha(1)
\]
changes the expansion by less than any fixed inverse power of
\[
\alpha.
\]

All arguments are infinite-series identities or dominated-convergence estimates. No finite truncation or numerical extrapolation is used as proof.
