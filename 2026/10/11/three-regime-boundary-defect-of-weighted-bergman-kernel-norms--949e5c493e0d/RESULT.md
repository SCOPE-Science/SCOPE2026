# Three-regime boundary defect of weighted Bergman kernel norms

## Finding

Fix
\[
\alpha>-1
\]
and
\[
1<p<\infty.
\]
Write
\[
\beta=\alpha+2,
\qquad
c=(p-1)\beta,
\qquad
a=\frac{\beta+c}{2}=\frac{p\beta}{2},
\qquad
d=\frac{\beta-c}{2}=\frac{(2-p)\beta}{2}.
\]

For the weighted Bergman reproducing kernel
\[
K_z(w)=\frac{1}{(1-\overline zw)^\beta},
\]
with
\[
dA_\alpha(w)
=
(\alpha+1)(1-|w|^2)^\alpha\,dA(w),
\]
put
\[
s=1-|z|^2
\]
and define the singularity-normalized kernel norm
\[
M_{p,\alpha}(s)
=
s^{c/p}\|K_z\|_{p,\alpha}.
\]

The sharp Forelli--Rudin upper constant is the exact boundary value
\[
L_{p,\alpha}
=
\left[
\frac{\Gamma(\beta)\Gamma(c)}
{\Gamma(a)^2}
\right]^{1/p},
\]
but the rate at which
\[
M_{p,\alpha}(s)
\]
approaches this value changes sharply at
\[
c=1.
\]

For
\[
0<c<1,
\]
\[
\frac{M_{p,\alpha}(s)}{L_{p,\alpha}}
=
1+
\frac{\lambda_{p,\alpha}}{p}s^c
+
o(s^c),
\]
where
\[
\lambda_{p,\alpha}
=
\frac{\Gamma(-c)\Gamma(a)^2}
{\Gamma(c)\Gamma(d)^2}
<0.
\]

At the critical line
\[
c=1,
\]
\[
\frac{M_{p,\alpha}(s)}{L_{p,\alpha}}
=
1
-
\frac{d^2}{p}
s\log\frac1s
+
O(s).
\]

For
\[
c>1
\]
and
\[
p\ne2,
\]
\[
\frac{M_{p,\alpha}(s)}{L_{p,\alpha}}
=
1
-
\frac{d^2}{p(c-1)}s
+
o(s).
\]

At the Hilbert exponent
\[
p=2,
\]
the defect vanishes identically:
\[
M_{2,\alpha}(s)\equiv1.
\]

Since
\[
c=(p-1)(\alpha+2),
\]
the transition occurs at
\[
p
=
1+\frac1{\alpha+2}.
\]
Thus the normalized kernel profile is only fractional-power regular at the boundary below this exponent, has a logarithmic derivative singularity at the exponent itself, and has an ordinary linear boundary defect above it, apart from the exact Hilbert cancellation.

## Assumptions and scope

The weighted area measure and kernel normalization are exactly those used in the cited recent Bergman-operator paper:
\[
dA_\alpha(z)
=
(\alpha+1)(1-|z|^2)^\alpha\,dA(z),
\]
where
\[
dA
\]
is normalized planar area, and
\[
K_z(w)
=
(1-\overline zw)^{-(2+\alpha)}.
\]

The recent source proves two-sided bounds for
\[
\|K_z\|_{p,\alpha}
\]
and uses these normalized kernels in its compactness and Berezin-transform arguments. The older sharp Forelli--Rudin theorem supplies the exact leading boundary constant. The result here concerns the next boundary term after that leading singularity has been removed.

The parameters
\[
\alpha
\]
and
\[
p
\]
are fixed while
\[
|z|\to1^-.
\]
No simultaneous parameter limit is claimed.

## Proof

By rotational invariance, the norm depends only on
\[
r=|z|.
\]
Set
\[
s=1-r^2.
\]

The angular expansion of
\[
|1-r\rho e^{i\theta}|^{-p\beta}
=
|1-r\rho e^{i\theta}|^{-2a}
\]
and the beta integral for the radial variable give
\[
\|K_z\|_{p,\alpha}^p
=
{}_2F_1(a,a;\beta;r^2).
\]
Indeed, the weighted radial moment of
\[
|w|^{2n}
\]
is
\[
(\beta-1)
\int_{\mathbb D}
|w|^{2n}(1-|w|^2)^{\beta-2}\,dA(w)
=
\frac{n!}{(\beta)_n},
\]
which produces precisely the Gauss hypergeometric series.

Euler's transformation yields
\[
{}_2F_1(a,a;\beta;r^2)
=
s^{-c}
{}_2F_1(d,d;\beta;r^2).
\]
Therefore the exact normalized identity is
\[
M_{p,\alpha}(s)^p
=
{}_2F_1(d,d;\beta;1-s).
\]

Since
\[
\beta-2d=c>0,
\]
Gauss' value at one gives
\[
{}_2F_1(d,d;\beta;1)
=
\frac{\Gamma(\beta)\Gamma(c)}
{\Gamma(\beta-d)^2}
=
\frac{\Gamma(\beta)\Gamma(c)}
{\Gamma(a)^2}.
\]
This proves the exact boundary limit
\[
M_{p,\alpha}(s)\to L_{p,\alpha}.
\]

Now suppose
\[
0<c<1.
\]
The connection formula at
\[
1-s
\]
gives
\[
{}_2F_1(d,d;\beta;1-s)
=
C\,{}_2F_1(d,d;1-c;s)
+
D\,s^c{}_2F_1(a,a;1+c;s),
\]
where
\[
C=
\frac{\Gamma(\beta)\Gamma(c)}
{\Gamma(a)^2}
\]
and
\[
D=
\frac{\Gamma(\beta)\Gamma(-c)}
{\Gamma(d)^2}.
\]
Because
\[
s=o(s^c)
\]
for
\[
0<c<1,
\]
the two hypergeometric factors equal
\[
1+O(s),
\]
so
\[
M_{p,\alpha}(s)^p
=
C
\left[
1+
\frac{D}{C}s^c
+
o(s^c)
\right].
\]
Taking the positive
\[
p
\]
th root proves the subcritical formula with
\[
\lambda_{p,\alpha}=D/C.
\]
Here
\[
d>0
\]
and
\[
\Gamma(-c)<0,
\]
so
\[
\lambda_{p,\alpha}<0.
\]

Next assume
\[
c>1.
\]
Differentiation gives
\[
\frac{d}{dx}
{}_2F_1(d,d;\beta;x)
=
\frac{d^2}{\beta}
{}_2F_1(d+1,d+1;\beta+1;x).
\]
The derivative has a finite boundary value because
\[
(\beta+1)-2(d+1)=c-1>0.
\]
Gauss' formula gives
\[
\left.
\frac{d}{dx}
{}_2F_1(d,d;\beta;x)
\right|_{x=1}
=
C\frac{d^2}{c-1}.
\]
Hence
\[
{}_2F_1(d,d;\beta;1-s)
=
C
\left[
1-\frac{d^2}{c-1}s+o(s)
\right].
\]
Taking the
\[
p
\]
th root gives the supercritical expansion.

If
\[
p=2,
\]
then
\[
d=0,
\]
so the exact normalized hypergeometric factor is
\[
{}_2F_1(0,0;\beta;1-s)=1.
\]
This is the exact Hilbert cancellation.

Finally suppose
\[
c=1.
\]
Then
\[
d=\frac{\beta-1}{2}
\]
and the derivative hypergeometric function is zero-balanced:
\[
\beta+1=2(d+1).
\]
Its standard boundary law is
\[
{}_2F_1(d+1,d+1;\beta+1;1-s)
=
\frac{\Gamma(\beta+1)}
{\Gamma(d+1)^2}
\log\frac1s
+
O(1).
\]
Consequently,
\[
\frac{d}{dx}
{}_2F_1(d,d;\beta;x)
=
C d^2\log\frac1{1-x}
+
O(1)
\]
as
\[
x\to1^-.
\]
Integrating over
\[
[1-s,1]
\]
gives
\[
{}_2F_1(d,d;\beta;1-s)
=
C
\left[
1
-
d^2s\log\frac1s
+
O(s)
\right].
\]
Taking the
\[
p
\]
th root completes the critical case.

## Verification

The exact identity
\[
M_{p,\alpha}(s)^p
=
{}_2F_1(d,d;\beta;1-s)
\]
was independently replayed from the weighted radial moments and Euler's transformation.

For
\[
0<c<1,
\]
the coefficient from the connection formula was checked against direct high-precision evaluations of the hypergeometric function for representative values of
\[
\alpha
\]
and
\[
p.
\]

At
\[
c=1,
\]
the ratio
\[
\frac{
M_{p,\alpha}(s)^p/C-1
}{
s\log(1/s)
}
\]
converges numerically to
\[
-d^2,
\]
as predicted by the zero-balanced derivative calculation.

For
\[
c>1,
\]
the ratio
\[
\frac{
M_{p,\alpha}(s)^p/C-1
}{s}
\]
converges to
\[
-\frac{d^2}{c-1}.
\]
At
\[
p=2,
\]
the normalized profile is exactly constant, providing a separate exact check.

The numerical evaluations are consistency checks only; every asymptotic statement follows from exact hypergeometric identities and Gauss boundary formulas.

## Relationship to prior work

Lou, Rasila, and Zhu use weighted normalized reproducing kernels as a basic tool in their boundedness and compactness theory. Their Lemma 8 gives
\[
s^{-c/p}
\le
\|K_z\|_{p,\alpha}
\le
L_{p,\alpha}s^{-c/p},
\]
and their compactness argument uses the weak convergence of the corresponding normalized kernels. The inspected article does not give the first boundary defect of the normalized norm.

Liu's sharp Forelli--Rudin theorem proves that the upper constant in the source bound is sharp and, through the Euler transformation, supplies the exact leading boundary limit. The inspected full text gives no next-order expansion of this weighted-disk kernel norm.

The special-function connection and derivative formulas used here are classical. The new mathematical content is their application to the precise weighted Bergman normalization used by the recent operator theorem, producing a parameter-dependent regularity phase at
\[
(p-1)(\alpha+2)=1.
\]

Searches for second-order Forelli--Rudin asymptotics, weighted Bergman kernel norm defects, zero-balanced critical corrections, and the exact threshold above did not locate a published statement implying this three-regime result.

## Limitations

The result concerns the standard power weights on the unit disk. General radial weights do not have the same explicit hypergeometric kernel formula.

Only the first nonzero boundary defect is given. Higher corrections can be obtained from longer connection-formula expansions.

The result sharpens the kernel normalization used in the cited compactness theorem but does not by itself give a quantitative essential-norm theorem for arbitrary operators.

The limit keeps
\[
\alpha
\]
and
\[
p
\]
fixed. No uniformity is claimed as either parameter approaches the critical curve simultaneously with
\[
|z|\to1^-.
\]

## References

1. Z. Lou, A. Rasila, and S. Zhu, *A class of linear operators on Bergman spaces*, arXiv:2507.09154v1, first posted 12 July 2025; Complex Analysis and Operator Theory 20 (2026), Article 95, DOI: 10.1007/s11785-026-01947-z.
2. C. Liu, *Sharp Forelli--Rudin estimates and the norm of the Bergman projection*, Journal of Functional Analysis 268 (2015), 255--277, DOI: 10.1016/j.jfa.2014.09.027.
3. NIST Digital Library of Mathematical Functions, Chapter 15, *Hypergeometric Function*, especially the Euler transformation, connection formulas, differentiation formula, and zero-balanced boundary asymptotics.
