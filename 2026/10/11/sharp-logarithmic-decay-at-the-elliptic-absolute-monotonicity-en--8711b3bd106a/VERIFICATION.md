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

The source coefficient representation is
\[
a_n
=
\frac{(-1)^nC}{15^{n+1}}
-
\int_1^{\infty}\rho(t)t^{-n-1}\,dt.
\]
The pole term is exponentially small, so the proof reduces to the endpoint behavior of \(\rho\).

For
\[
t=1+u,
\qquad
r=t^{-1/2},
\qquad
r'=\sqrt{1-r^2},
\]
the source branch-cut formula uses
\[
c=\log(4r/r')
=
\frac12\log(16/u).
\]
The standard elliptic expansions verified against NIST DLMF 19.12.1 and 19.5.1 give
\[
\frac\pi2\mathcal K(r)-c\mathcal K(r')
=
\frac{\pi}{8}u+O\!\left(u^2\log(1/u)\right).
\]
Hence
\[
\rho(1+u)
\sim
\frac{u}{\pi\log^2(16/u)}.
\]

To verify the moment conversion directly, define
\[
I_n
=
\int_0^{\delta}
\frac{u(1+u)^{-n-1}}{\log^2(16/u)}\,du
\]
and set
\[
L_n=\log(16n),
\qquad
u=v/n.
\]
Then
\[
n^2L_n^2I_n
=
\int_0^{n\delta}
 v\left(1+\frac vn\right)^{-n-1}
 \left(\frac{L_n}{L_n-\log v}\right)^2dv.
\]
On every fixed compact interval the integrand converges to
\[
ve^{-v}.
\]
For
\[
v\le\sqrt n,
\]
the logarithmic ratio is uniformly bounded and the kernel has an exponential majorant; for
\[
v>\sqrt n,
\]
the kernel is exponentially small in \(\sqrt n\). Therefore
\[
n^2L_n^2I_n\to1.
\]
This proves
\[
-a_n
\sim
\frac{1}{\pi n^2\log^2(16n)}.
\]

Finally,
\[
-f'''(x)
=
\frac\pi2
\sum_{n\ge3}
(-a_n)n(n-1)(n-2)x^{n-3},
\]
whose coefficients are asymptotic to
\[
\frac{n}{2\log^2(16n)}.
\]
The standard Abelian theorem for positive regularly varying power-series coefficients of index one gives
\[
-f'''(x)
\sim
\frac{1}{2(1-x)^2\log^2(16/(1-x))}.
\]

All infinite statements are established analytically. Formal coefficient division and finite numerical values, when used for sanity checking, are not treated as proof.
