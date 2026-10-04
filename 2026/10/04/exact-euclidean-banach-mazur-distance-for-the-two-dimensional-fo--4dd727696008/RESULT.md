# Exact Euclidean Banach--Mazur distance for the two-dimensional fourth-power Cesàro norm
## Finding
Let \(X=\mathrm{ces}_4^{(2)}\) be \(\mathbb R^2\) with
\[
N(x,y)=\left(|x|^4+\left(\frac{|x|+|y|}{2}\right)^4\right)^{1/4}.
\]
Let \(s_*\) be the unique positive solution of
\[
(1+s)^3(\sqrt{17}-s)=16s.
\]
Then
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2
=
D_*
:=
\frac{\sqrt{16+(1+s_*)^4}}{\sqrt{17}+s_*^2}
\approx 1.26068368922021387435,
\]
so \(d_{\mathrm{BM}}(X,\ell_2^2)\approx1.12280171411528129816\). An optimal Euclidean pullback norm, unique only up to the symmetries not analyzed here and an overall positive scalar, is represented by
\[
|(x,y)|_* = \sqrt{x^2+\frac{y^2}{\sqrt{17}}}.
\]

## Assumptions and scope
The space is the real two-dimensional Cesàro space with exponent \(4\). The Banach--Mazur distance is the multiplicative linear distance to the Euclidean plane. No assertion is made for other exponents or higher-dimensional Cesàro spaces. The exact value above is an implicit algebraic value: \(s_*\) is characterized by a quartic equation together with the uniqueness statement proved below.

The finite-dimensional Cesàro family \(\mathrm{ces}_p^{(n)}\) is the classical family defined by Maligranda, Petrot and Suantai. Their Section 4 explicitly gives
\[
\|x\|_{p,n}=\left(\sum_{k=1}^n\left(\frac1k\sum_{i=1}^k|x_i|\right)^p\right)^{1/p}.
\]
For \(p=4\) and \(n=2\), this is exactly the displayed norm \(N\).

## Proof
For a positive-definite quadratic form \(Q\), write \(q(z)=z^TQz\) and
\[
\Delta(Q)=
\frac{\sup_{z\ne0} N(z)^2/q(z)}{\inf_{z\ne0} N(z)^2/q(z)}.
\]
If \(Q=T^TT\), then \(\Delta(Q)=(\|T\|\,\|T^{-1}\|)^2\). Consequently,
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2=\inf_{Q>0}\Delta(Q). \tag{1}
\]

The norm \(N\) is invariant under independent sign changes of the two coordinates. Given any \(Q\), rescale it so that
\[
q(z)\le N(z)^2\le \Delta(Q)q(z)
\]
for every \(z\). Conjugating \(Q\) by each of the four coordinate sign-change matrices preserves both inequalities. Averaging the four quadratic forms therefore preserves both inequalities and kills the off-diagonal term. Hence the infimum in (1) may be taken over diagonal forms without loss. After an overall scalar normalization, write
\[
q_t(x,y)=x^2+t y^2,\qquad t>0. \tag{2}
\]
This is a reduction over all linear isomorphisms, not an axial ansatz.

In the first quadrant put \(s=y/x\) for \(x\ne0\). Then
\[
F_t(s)=\frac{N(1,s)^2}{1+t s^2}
=\frac{\sqrt{16+(1+s)^4}}{4(1+t s^2)},\qquad s\ge0,
\]
and \(F_t(\infty)=1/(4t)\). Thus
\[
\Delta(t)=\frac{\max_{0\le s\le\infty}F_t(s)}{\min_{0\le s\le\infty}F_t(s)}. \tag{3}
\]

Set \(r=\sqrt{17}\), \(t_0=1/r\), and \(A=r/4\). The endpoint values coincide:
\[
F_{t_0}(0)=F_{t_0}(\infty)=A.
\]
Moreover, for \(s>0\), squaring the desired inequality \(F_{t_0}(s)>A\) reduces exactly to
\[
16+(1+s)^4-17\left(1+\frac{s^2}{\sqrt{17}}\right)^2
=s\left(4+(6-2\sqrt{17})s+4s^2\right)>0.
\]
The quadratic factor is positive because its leading coefficient is positive and its discriminant is
\[
(6-2\sqrt{17})^2-64=40-24\sqrt{17}<0.
\]
Therefore the two endpoints are the only minima of \(F_{t_0}\).

Differentiation gives
\[
\operatorname{sgn}F_{t_0}'(s)=\operatorname{sgn}h(s),\qquad
h(s)=(1+s)^3(\sqrt{17}-s)-16s.
\]
For \(0<s<r\), write \(h(s)=s(\phi(s)-16)\), where
\[
\phi(s)=\frac{(1+s)^3(r-s)}s.
\]
Its logarithmic derivative has the sign of
\[
-3s^2+2rs-r.
\]
This concave quadratic has two positive roots \(\alpha<\beta\), with \(\alpha<1<\beta<r\). On \(0<s\le1\),
\[
\frac{(1+s)^3}s\ge\frac{27}4,\qquad r-s>3,
\]
so \(\phi(s)>81/4>16\). Hence the local minimum \(\phi(\alpha)\) already exceeds \(16\); the subsequent local maximum does as well. On \((\beta,r)\), \(\phi\) decreases strictly from a value above \(16\) to \(0\). Thus there is exactly one positive root \(s_*\) of \(h\), and \(F_{t_0}\) rises to a single global maximum there. Equation (3) therefore gives
\[
\Delta(t_0)
=
\frac{F_{t_0}(s_*)}A
=
\frac{\sqrt{16+(1+s_*)^4}}{\sqrt{17}+s_*^2}
=D_*. \tag{4}
\]

It remains to prove that no other diagonal form improves (4). If \(t<t_0\), then \(F_t(0)=A\) while \(F_t(s_*)>F_{t_0}(s_*)\), so
\[
\Delta(t)\ge\frac{F_t(s_*)}{F_t(0)}>D_*.
\]
If \(t>t_0\), use the other endpoint. The ratio
\[
\frac{F_t(s_*)}{F_t(\infty)}
=
\frac{t\sqrt{16+(1+s_*)^4}}{1+t s_*^2}
\]
is strictly increasing in \(t\), because its derivative is \(\sqrt{16+(1+s_*)^4}/(1+t s_*^2)^2>0\). Hence it is larger than its value \(D_*\) at \(t=t_0\), and again \(\Delta(t)>D_*\). Together with the sign-symmetry reduction, this proves (4) is the global Banach--Mazur optimum over every invertible linear map.

## Verification
The accompanying `verify.py` uses only the Python standard library. It brackets the unique positive root by \(3.511<s_*<3.512\), bisects the defining equation at high precision, verifies the root residual, checks the negative discriminant used in the endpoint-minimum proof, and recomputes
\[
s_*\approx3.51117271438721386120,\quad
D_*\approx1.26068368922021387435,\quad
\sqrt{D_*}\approx1.12280171411528129816.
\]
The checker is supplementary: global optimality is supplied by the analytic symmetry reduction and monotonicity proof, not by finite sampling.

## Relationship to prior work
Maligranda, Petrot and Suantai define the finite-dimensional Cesàro spaces and compute the James constant only for \(\mathrm{ces}_2^{(2)}\); their Problem 4 asks for James constants at \(p\ne2\). Their full text contains no Banach--Mazur statement. Zuo's 2012 paper computes the Ptolemy constant of the two-dimensional Cesàro space only at exponent \(2\). Zuo, Huang, Huang and Wang later treat the same \(\mathrm{ces}_q^{(2)}\) family in their Example 5, but for a Gao-type constant rather than Banach--Mazur distance; that paper lists primary MSC \(46\mathrm{B}20\). Targeted searches using Cesàro, Banach--Mazur, John ellipsoid, optimal ellipse, and the exact \(\sqrt{17}\) parameter did not locate a prior formula implying (4).

The present statement is not implied by the known \(p=2\) formulas. The fourth-power norm has a different radial profile, and the optimizer is determined by the nontrivial balance \(t_0=1/\sqrt{17}\) together with the interior contact slope \(s_*\).

## Limitations
The claim is restricted to the real two-dimensional exponent-
\(4\) Cesàro norm. It does not give a formula for general \(p\), higher dimensions, or uniqueness of the optimizer modulo all possible symmetries. The literature comparison cannot prove absolute bibliographic uniqueness; an unindexed equivalent result remains a residual possibility. A later same-family paper was only partially text-searchable during the comparison, although its inspected Cesàro section concerns a different invariant and targeted searches found no Banach--Mazur formula.

## References
1. L. Maligranda, N. Petrot, S. Suantai, “On the James constant and B-convexity of Cesàro and Cesàro--Orlicz sequence spaces,” *Journal of Mathematical Analysis and Applications* 326 (2007), 312--331. DOI 10.1016/j.jmaa.2006.02.085. Available online 17 April 2006.
2. Z. Zuo, “The Ptolemy constant of absolute normalized norms on the real plane,” *Journal of Inequalities and Applications* 2012, 107. DOI 10.1186/1029-242X-2012-107.
3. Z. Zuo, Y. Huang, X. Huang, Y. Wang, “The Gao-Type Constant of Absolute Normalized Norms on \(\mathbb R^2\),” *Mathematics* 10 (2022), 4591. DOI 10.3390/math10234591.
