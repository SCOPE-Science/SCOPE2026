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
c=1-2\log2,
\]
\[
A_1(r)=r-(1-r)\log(1-r),
\]
and
\[
A_2(r)=r+(1-2r)\log(1-r).
\]
The source sharp radii solve
\[
r+2MA_j(r)=1+2Mc.
\]

Subtracting the two equations at common \(r\) gives
\[
2M\bigl(A_2(r)-A_1(r)\bigr)
=
2M(2-3r)\log(1-r).
\]
Inside \(0<r<1\), this vanishes only at
\[
r=\frac23.
\]
Substitution gives
\[
M_*=\frac{1}{2(\log192-1)}.
\]

At a root,
\[
\partial_M H_j
=
\frac{1-r}{M}
>
0.
\]
For the second radius,
\[
\partial_r H_2
=
1+2M
\left(
\frac{r}{1-r}
-
2\log(1-r)
\right)
>
0.
\]

For the first radius, with
\[
\varepsilon=1-r,
\]
the root equation gives
\[
2M
=
\frac{\varepsilon}
{2\log2-\varepsilon(1+\log\varepsilon)}.
\]
Hence
\[
\partial_r H_1
=
\frac{2\log2+\varepsilon}
{2\log2-\varepsilon(1+\log\varepsilon)}
>
0.
\]
Thus both roots are differentiable and strictly decreasing with \(M\).

The source equations become, near \(M=0\),
\[
\varepsilon_1
=
2M
\left(
2\log2-\varepsilon_1(1+\log\varepsilon_1)
\right),
\]
and
\[
\varepsilon_2
=
2M
\left(
2\log2-\log\varepsilon_2-\varepsilon_2+2\varepsilon_2\log\varepsilon_2
\right).
\]
These imply
\[
\varepsilon_1\sim4(\log2)M,
\]
and
\[
\varepsilon_2\sim2M\log(1/M).
\]

At the upper parameter endpoint,
\[
1+2Mc
=
1-\frac{M}{M_c}
=
\eta.
\]
The expansions
\[
A_1(r)=2r-\frac{r^2}{2}+O(r^3),
\]
and
\[
A_2(r)=\frac32r^2+O(r^3)
\]
give
\[
r_1\sim\frac{\eta}{1+4M_c},
\qquad
r_2\sim\eta.
\]

The numerical value
\[
M_*=0.117439939755438\ldots
\]
and the common radius \(2/3\) were recomputed as a consistency check only. The proof of uniqueness, ordering, and asymptotics is symbolic.
