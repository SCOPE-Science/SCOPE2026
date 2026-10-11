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

For
\[
\omega_{n,\beta}
=
\int_0^1
t^n
\log^\beta\!\left(
\frac{e}{1-t}
\right)dt,
\]
the primary source proves
\[
\omega_{n,\beta}
\sim
\frac{\log^\beta(n+3)}{n+3}.
\]

Hence the inclusion
\[
A_{\log^\alpha}^2
\hookrightarrow
A_{\log^2}^2
\]
has monomial singular values
\[
\left(
\frac{\omega_{n,2}}
{\omega_{n,\alpha}}
\right)^{1/2}
\sim
\log^{1-\alpha/2}(n+3),
\]
which tend to zero exactly when
\[
\alpha>2.
\]
The source endpoint boundedness therefore makes the Hilbert map compact in that range.

For endpoint noncompactness, define
\[
f_N(z)
=
(\log N)^{-3/2}
\sum_{n=N}^{\lfloor N^2\rfloor}z^n.
\]
The domain norms are uniformly bounded above and below because
\[
(\log N)^{-3}
\sum_{n=N}^{N^2}
\frac{\log^2n}{n}
\asymp1.
\]
The coefficient supports escape, so \(f_N\) converges weakly to zero.

For
\[
N\le m\le N^{3/2}
\]
and
\[
N^{3/2}\le n\le N^2,
\]
one has
\[
m+n+1\le3n.
\]
Therefore
\[
\widehat{Hf_N}(m)
\ge
\frac{(\log N)^{-3/2}}{3}
\sum_{N^{3/2}\le n\le N^2}\frac1n
\ge
c(\log N)^{-1/2}.
\]
Consequently,
\[
\|Hf_N\|_{A^2}^2
\ge
\frac{c^2}{\log N}
\sum_{N\le m\le N^{3/2}}\frac1{m+1}
\ge
c_0>0.
\]
Thus a bounded weakly null sequence has images bounded away from zero, which is impossible for a compact operator.

Below the threshold, the primary source's explicit coefficient sequence proves failure of the mapping property.

No finite experiment or numerical approximation is used.
