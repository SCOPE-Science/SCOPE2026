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

The primary estimate is
\[
\left|
\frac{F(w_r+A\eta)}{F(w_r)}
e^{-\eta L_r}
-
1
\right|
\le
\frac{
|\eta|\varkappa(r)L_r
}{
\delta(r)
},
\qquad
|\eta|
\le
\frac{\delta(r)}{L_r},
\]
with
\[
\delta(r)\to\infty
\]
and bounded \(\varkappa(r)\).

Setting
\[
\eta=\frac{\zeta}{L_r}
\]
gives
\[
\left|
G_r(\zeta)e^{-\zeta}-1
\right|
\le
\frac{
|\zeta|\varkappa(r)
}{
\delta(r)
}.
\]
Hence
\[
G_r\to e^\zeta
\]
locally uniformly. Cauchy estimates give local uniform convergence of derivatives.

For every
\[
R<\pi,
\]
the exponential is injective on a slightly larger centered disk. If two points for \(G_r\) collided infinitely often, compactness would give either two distinct limit points with the same exponential value or a coalescing pair whose difference quotient tends to
\[
e^\zeta\ne0.
\]
Both alternatives are impossible.

For the sharpness witness
\[
F(z)=\exp(e^z),
\]
one has
\[
L_r=e^r.
\]
With
\[
a_r
=
\arcsin\!\left(\frac{\pi}{L_r}\right),
\]
the exact identity
\[
L_r
\left(
e^{ia_r}-e^{-ia_r}
\right)
=
2\pi i
\]
gives
\[
F(r+ia_r)=F(r-ia_r).
\]
The rescaled collision radius is
\[
R_r
=
L_ra_r
=
L_r\arcsin\!\left(\frac{\pi}{L_r}\right)
\longrightarrow\pi.
\]

Class membership of the witness is checked directly with
\[
\delta(r)=\frac12e^{r/2}.
\]
No numerical experiment or finite enumeration is used in the proof.
