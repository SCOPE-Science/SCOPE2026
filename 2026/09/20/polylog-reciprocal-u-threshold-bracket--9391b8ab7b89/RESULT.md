# A starlike obstruction below one for the reciprocal polylogarithmic \(\mathcal U\)-tail

## Statement

Let \(\mathcal S\) be the normalized univalent class in the unit disk and let
\[
\mathcal U=
\left\{
F:
\left|
F'(z)\left(\frac{z}{F(z)}\right)^2-1
\right|<1
\quad (z\in\mathbb D)
\right\}.
\]
For \(f\in\mathcal S\), write
\[
\frac{z}{f(z)}=1+\sum_{n\ge1}b_nz^n
\]
and define the reciprocal polylogarithmic smoothing by
\[
\frac{z}{F_\sigma(z)}
=
1+\sum_{n\ge1}\frac{b_n}{(n+1)^\sigma}z^n
\]
whenever this reciprocal is zero-free in \(\mathbb D\).

Define
\[
\tau_{\mathcal U}
=
\inf\left\{
s:
F_\sigma\in\mathcal U
\text{ for every }f\in\mathcal S
\text{ and every }\sigma\ge s
\right\}.
\]
Then
\[
\boxed{\tau_{\mathcal U}\ge1.}
\]

More precisely, every real \(\sigma<1\) admits an explicit starlike
\(f\in\mathcal S\) for which \(F_\sigma\) is either not analytic in
\(\mathbb D\) or does not belong to \(\mathcal U\).

An earlier result published on 20 September 2026 already gives
\[
\tau_{\mathcal U}\le1.41351950\ldots.
\]
That upper bound is prior work and is not a contribution of this repaired result.

## Proof

Fix \(\sigma<1\). Choose an integer
\[
m>\max\left\{2,\frac{2}{1-\sigma}\right\},
\qquad
\alpha=\frac{2}{m}\in(0,1),
\]
and set
\[
f_m(z)=\frac{z}{(1-z^m)^{2/m}}.
\]
Since
\[
\frac{zf_m'(z)}{f_m(z)}
=
\frac{1+z^m}{1-z^m},
\]
the real part is positive in \(\mathbb D\), so \(f_m\) is starlike.

Write
\[
(1-z^m)^\alpha=1+\sum_{k\ge1}c_kz^{mk}.
\]
For \(0<\alpha<1\),
\[
-c_k
=
\frac{\alpha\,\Gamma(k-\alpha)}
{\Gamma(1-\alpha)\Gamma(k+1)}
>0,
\qquad
-c_k\sim
\frac{\alpha}{\Gamma(1-\alpha)}k^{-1-\alpha}.
\]
Thus
\[
p_{\sigma,m}(z)
:=
\frac{z}{F_\sigma(z)}
=
1+\sum_{k\ge1}\frac{c_k}{(mk+1)^\sigma}z^{mk}.
\]

If \(p_{\sigma,m}\) has a zero in \(\mathbb D\), then \(F_\sigma\) is not
analytic there. Otherwise,
\[
p_{\sigma,m}(z)-zp_{\sigma,m}'(z)-1
=
\sum_{k\ge1}
\frac{(mk-1)(-c_k)}{(mk+1)^\sigma}z^{mk}.
\]
All coefficients are positive and satisfy
\[
\frac{(mk-1)(-c_k)}{(mk+1)^\sigma}
\asymp k^{-\sigma-\alpha}.
\]
The choice of \(m\) gives \(\sigma+\alpha<1\), so the radial sum diverges as
\(z=r\uparrow1\). Hence for \(r\) close enough to \(1\),
\[
\left|
F_\sigma'(r)
\left(\frac{r}{F_\sigma(r)}\right)^2-1
\right|>1.
\]
Therefore \(F_\sigma\notin\mathcal U\).

Since this works for every \(\sigma<1\), the universal tail exponent satisfies
\[
\tau_{\mathcal U}\ge1.
\]

## Prior boundary

Ali, Obradović and Ponnusamy proved the universal sufficient condition
\(\sigma\ge3/2\) and posed a smallest-parameter problem. A separate result
published earlier on 20 September 2026 lowered the universal sufficient upper
threshold to \(1.41351950\ldots\). The contribution here is only the explicit
lower obstruction \(\tau_{\mathcal U}\ge1\).

## Limitations

The exact threshold remains unknown. This result does not determine a universal
\(\mathcal S\)-tail threshold and does not resolve every literal reading of the
2013 terminal problem.

## References

1. R. M. Ali, M. Obradović, and S. Ponnusamy,
   *Necessary and sufficient conditions for univalent functions*,
   Complex Variables and Elliptic Equations 58 (2013), 611--620,
   DOI 10.1080/17476933.2011.599116.
2. *An exact area-theorem Hilbert envelope lowers a polylogarithmic reciprocal
   univalence threshold*, published 20 September 2026.
