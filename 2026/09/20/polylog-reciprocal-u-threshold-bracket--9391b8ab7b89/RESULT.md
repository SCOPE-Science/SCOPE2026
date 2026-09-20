# A quantitative bracket for the polylogarithmic reciprocal-smoothing threshold

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Let \(\mathcal S\) be the normalized univalent class in the unit disk and
\(\mathcal U\) the Aksentiev class
\[
\mathcal U=\left\{F:\left|F'(z)\left(\frac z{F(z)}\right)^2-1\right|<1
\ \ (z\in\mathbb D)\right\}.
\]
For \(f\in\mathcal S\), write
\[
\frac z{f(z)}=1+\sum_{n\ge1}b_nz^n
\]
and, for real \(\sigma\), define the polylogarithmic reciprocal smoothing
\(F_\sigma\) by
\[
\frac z{F_\sigma(z)}=
\frac z{f(z)} * \frac{\operatorname{Li}_\sigma(z)}z
=
1+\sum_{n\ge1}\frac{b_n}{(n+1)^\sigma}z^n ,
\]
whenever the reciprocal on the right is zero-free in \(\mathbb D\).

Define the universal \(\mathcal U\)-tail exponent
\[
\tau_{\mathcal U}:=
\inf\left\{s:\ 
F_\sigma\in\mathcal U\text{ for every }f\in\mathcal S
\text{ and every }\sigma\ge s\right\}.
\]

Set
\[
T(s):=\sum_{n=2}^\infty
\frac1{(n-1)(n+1)^{2s}},
\qquad
R(s):=2^{1-s}+\sqrt{T(s)}.
\]
There is a unique \(s_*\in(1,3/2)\) satisfying \(R(s_*)=1\), and
\[
1.4135195<s_*<1.41352.
\]
Then
\[
\boxed{1\le \tau_{\mathcal U}\le s_*
      =1.41351950\ldots}.
\]

Thus the explicit universal upper bound \(3/2\) in Ali--Obradović--Ponnusamy
can be lowered to the root \(s_*\), while no universal \(\mathcal U\)-tail
threshold below \(1\) is possible.

## Context

Ali, Obradović and Ponnusamy introduced the transform above and proved
\(F_\sigma\in\mathcal U\) for every \(f\in\mathcal S\) when
\(\sigma\ge3/2\). They ended the paper with a terse problem asking for the
smallest parameter for which the transform belongs to \(\mathcal U\) or
\(\mathcal S\).

Because \(F_0=f\), that final sentence cannot literally mean the smallest
isolated parameter for membership in \(\mathcal S\). The present record
therefore addresses the natural monotone \(\mathcal U\)-tail question
suggested by their Corollary 1.7: from which exponent onward is
\(F_\sigma\in\mathcal U\) forced for every \(f\in\mathcal S\)?

The upper bound here keeps their area-theorem mechanism but avoids an
additional coarse tail majorization: the exact square-summable tail
\(T(s)\) is retained. The lower bound comes from an explicit family of
starlike root transforms and is independent of the upper-bound argument.

The statement concerns only this universal \(\mathcal U\)-tail exponent.
It does not claim to resolve every literal interpretation of the source's
final problem or determine a universal \(\mathcal S\)-tail threshold.

## Proof

### 1. The upper bound

For \(f\in\mathcal S\), the area theorem gives
\[
\sum_{n=2}^\infty(n-1)|b_n|^2\le1,
\]
and Bieberbach's second-coefficient estimate gives \(|b_1|\le2\).

Put
\[
p_\sigma(z):=\frac z{F_\sigma(z)}
=1+\sum_{n\ge1}\frac{b_n}{(n+1)^\sigma}z^n.
\]
For \(r=|z|<1\), Cauchy--Schwarz yields
\[
\begin{aligned}
|p_\sigma(z)-1|
&\le \frac{2r}{2^\sigma}
+\left(\sum_{n=2}^\infty(n-1)|b_n|^2\right)^{1/2}
 \left(\sum_{n=2}^\infty
 \frac{r^{2n}}{(n-1)(n+1)^{2\sigma}}\right)^{1/2}\\
&\le 2^{1-\sigma}r+
 \left(\sum_{n=2}^\infty
 \frac{r^{2n}}{(n-1)(n+1)^{2\sigma}}\right)^{1/2}.
\end{aligned}
\]
Both summands decrease with \(\sigma\). At \(\sigma=s_*\), the same
expression with \(r=1\) equals \(R(s_*)=1\); because \(r<1\), the displayed
bound is strictly smaller than \(1\). Hence \(p_\sigma\) is zero-free in
\(\mathbb D\) for every \(\sigma\ge s_*\).

Moreover,
\[
U_{F_\sigma}(z)
:=F_\sigma'(z)\left(\frac z{F_\sigma(z)}\right)^2-1
=p_\sigma(z)-zp_\sigma'(z)-1
=-\sum_{n=2}^\infty
\frac{(n-1)b_n}{(n+1)^\sigma}z^n .
\]
Therefore
\[
|U_{F_\sigma}(z)|
\le
\left(\sum_{n=2}^\infty(n-1)|b_n|^2\right)^{1/2}
\left(\sum_{n=2}^\infty
\frac{(n-1)r^{2n}}{(n+1)^{2\sigma}}\right)^{1/2}.
\]
For \(\sigma\ge s_*>1.4\), the second square is \(<1\). For example, at
\(s=1.4\),
\[
\sum_{n=2}^\infty\frac{n-1}{(n+1)^{2.8}}
<
\sum_{n=2}^{10}\frac{n-1}{(n+1)^{2.8}}
+\int_{10}^\infty x^{-1.8}\,dx
<0.423.
\]
Hence \(|U_{F_\sigma}(z)|<1\) throughout \(\mathbb D\), proving
\(F_\sigma\in\mathcal U\).

The function \(R\) is continuous and strictly decreasing on \(s>0\).
Also \(R(1)>1\), while \(R(3/2)<1\), so \(s_*\) exists and is unique.

### 2. No universal \(\mathcal U\) bound below \(1\)

Fix \(\sigma<1\). Choose an integer
\[
m>\max\left\{2,\frac2{1-\sigma}\right\},
\qquad \alpha:=\frac2m\in(0,1),
\]
and consider
\[
f_m(z):=\frac z{(1-z^m)^{2/m}}.
\]
Since
\[
\frac{zf_m'(z)}{f_m(z)}=
\frac{1+z^m}{1-z^m},
\]
its real part is positive in \(\mathbb D\), so \(f_m\) is starlike and
therefore belongs to \(\mathcal S\).

Write
\[
(1-z^m)^\alpha=1+\sum_{k\ge1}c_kz^{mk}.
\]
For \(0<\alpha<1\),
\[
-c_k=
\frac{\alpha\,\Gamma(k-\alpha)}
{\Gamma(1-\alpha)\Gamma(k+1)}>0,
\qquad
-c_k\sim
\frac{\alpha}{\Gamma(1-\alpha)}k^{-1-\alpha}.
\]
For the transformed reciprocal,
\[
p_{\sigma,m}(z)
=1+\sum_{k\ge1}
\frac{c_k}{(mk+1)^\sigma}z^{mk},
\]
and formally
\[
p_{\sigma,m}(z)-zp_{\sigma,m}'(z)-1
=
\sum_{k\ge1}
\frac{(mk-1)(-c_k)}{(mk+1)^\sigma}z^{mk}.
\]
All coefficients on the right are positive. Since
\[
\frac{(mk-1)(-c_k)}{(mk+1)^\sigma}
\asymp k^{-\sigma-\alpha}
\]
and \(\sigma+\alpha<1\), its radial sum diverges as \(z=r\uparrow1\).
If \(p_{\sigma,m}\) has a zero in \(\mathbb D\), then \(F_\sigma\) is not
even analytic there. Otherwise, the displayed \(\mathcal U\)-expression
exceeds \(1\) for \(r\) sufficiently close to \(1\). In either case,
\(F_\sigma\notin\mathcal U\).

Thus every \(\sigma<1\) fails as a universal \(\mathcal U\) exponent, so
\(\tau_{\mathcal U}\ge1\).

### 3. Numerical localization of \(s_*\)

For a finite partial sum through \(N\), the omitted tail satisfies
\[
0<
\sum_{n>N}\frac1{(n-1)(n+1)^{2s}}
\le
\sum_{m=N}^\infty m^{-(2s+1)}
\le
\frac{(N-1)^{-2s}}{2s}.
\]
Using \(N=5000\) gives
\[
R(1.4135195)>1,\qquad R(1.41352)<1,
\]
which certifies the quoted bracket. The accompanying verification script
computes these two-sided bounds directly.

## Originality and literature check

The primary 2013 paper states the transform, proves the universal
\(\sigma\ge3/2\) result, and explicitly leaves a terse smallest-parameter
question. Because \(F_0=f\), the novelty claim here is deliberately restricted
to the monotone universal \(\mathcal U\)-tail formulation above. Searches
through the paper's title/DOI, the exact
polylogarithmic reciprocal transform, \(\mathcal U\)-class terminology,
Hadamard-convolution terminology, and later polylogarithm-based geometric
function papers did not locate a published improvement of the \(3/2\)
threshold or the explicit starlike obstruction below \(1\).

A 2015 paper on \(\mathcal U\)-radii cites the 2013 work and develops
different radius problems; its accessible text does not supply this
polylogarithmic threshold. Later papers using polylogarithm convolution
operators study other subclasses and operators.

The originality claim is therefore limited to the quantitative bracket
for this specific universal \(\mathcal U\)-tail problem, to the best of
our knowledge. A differently indexed result phrased as a multiplier or
fractional-integration theorem remains a residual risk.

## Limitations

- The gap \(1\le\tau_{\mathcal U}\le1.41351950\ldots\) remains substantial;
  the exact universal \(\mathcal U\)-tail exponent is not determined.
- The source's final problem is tersely phrased and, since \(F_0=f\), admits
  a trivial literal reading on the \(\mathcal S\) side. This record addresses
  the monotone universal \(\mathcal U\)-tail interpretation only and does not
  determine a universal \(\mathcal S\)-tail threshold.
- The upper bound uses only the area theorem and \(|b_1|\le2\), so sharper
  coefficient correlations may lower it.
- A prior equivalent theorem in multiplier/fractional-integral language
  could have escaped the searches.

## Reproducibility

Run `artifacts/verify_threshold.py` with Python 3.11 or later. It uses
only the standard library and evaluates a finite partial sum plus a
proved integral tail bound.

## References

1. R. M. Ali, M. Obradović, and S. Ponnusamy,
   *Necessary and sufficient conditions for univalent functions*,
   Complex Variables and Elliptic Equations 58 (2013), 611--620.
   DOI: 10.1080/17476933.2011.599116.
2. R. M. Ali and N. M. Alarifi,
   *The \(\mathcal U\)-Radius for Classes of Analytic Functions*,
   Bulletin of the Malaysian Mathematical Sciences Society 38 (2015),
   1705--1721. DOI: 10.1007/s40840-015-0115-3.
