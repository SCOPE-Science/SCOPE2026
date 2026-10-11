# Exact conditional variance profile of the Kaplan–Yorke stationary measure
## Finding
Consider the classical Kaplan–Yorke map
\[
T_\alpha(x,y)=\left(2x\!\pmod 1,\;\alpha y+\cos(4\pi x)\right),
\qquad |\alpha|<1.
\]
Let \(\mu\) be an invariant Borel probability measure supported on the bounded attracting strip and suppose its first-coordinate marginal is Lebesgue measure on \([0,1)\). Write \(X(x,y)=x\) and \(Y(x,y)=y\). Then, for Lebesgue-almost every \(x\),
\[
\boxed{\mathbb E_\mu[Y\mid X=x]=\cos(2\pi x)}
\]
and
\[
\boxed{\operatorname{{Var}}_\mu(Y\mid X=x)=
\frac{{\alpha^2}}2\left(\frac1{{1-\alpha^2}}+\cos(2\pi x)\right)}.
\]
The corresponding conditional second moment is
\[
\mathbb E_\mu[Y^2\mid X=x]
=
\frac1{{2(1-\alpha^2)}}
+\frac{{\alpha^2}}2\cos(2\pi x)
+\frac12\cos(4\pi x).
\]
Consequently,
\[
\mathbb E_\mu[Y]=0,
\qquad
\operatorname{{Var}}_\mu(Y)=\frac1{{2(1-\alpha^2)}}.
\]
Thus the stationary vertical spread is not merely known globally: its heteroscedastic profile over the expanding coordinate is fixed exactly. For \(\alpha\ne0\), the conditional variance is strictly positive and ranges between
\[
\frac{{\alpha^4}}{{2(1-\alpha^2)}}
\quad\text{{and}}\quad
\frac{{\alpha^2(2-\alpha^2)}}{{2(1-\alpha^2)}}.
\]

## Assumptions and scope
The first coordinate is taken modulo one and the second coordinate is not reduced modulo one. The parameter satisfies \(|\alpha|<1\). The support assumption may be replaced by finite second moment; bounded support is natural on the attracting strip because the vertical dynamics is a contraction with bounded forcing.

The theorem applies to any invariant probability measure with Lebesgue first marginal, in particular to the natural stationary measure generated from Lebesgue-distributed expanding-coordinate histories. It does not claim that all invariant measures of the map have Lebesgue first marginal; the doubling map has many other invariant marginals.

The result is classified under MSC 2020 \(37A05\), because its object is an invariant probability measure and its proof uses the transfer operator of a discrete dynamical system.

## Proof
Let \(P\) denote the Perron operator of the doubling map with respect to Lebesgue measure:
\[
(Pf)(x)=\frac12\left(f\left(\frac x2\right)+f\left(\frac{{x+1}}2\right)\right).
\]
Disintegrate \(\mu\) over its Lebesgue first marginal and define
\[
m(x)=\mathbb E_\mu[Y\mid X=x],
\qquad
s(x)=\mathbb E_\mu[Y^2\mid X=x].
\]
Conditioning the invariance equation on the next first coordinate gives
\[
m(x)=\cos(2\pi x)+\alpha(Pm)(x).
\]
Indeed, the two inverse branches of the doubling map have equal Lebesgue weights, and on either branch \(u\) satisfying \(2u=x\pmod1\) one has
\[
\cos(4\pi u)=\cos(2\pi x).
\]
Now
\[
P[\cos(2\pi \cdot)]=0.
\]
Hence \(m(x)=\cos(2\pi x)\) solves the equation. It is the unique square-integrable solution because \(P\) is a contraction on \(L^2\) and \(|\alpha|<1\), so \(I-\alpha P\) is invertible by a Neumann series.

For the second moment, invariance gives
\[
s(x)=\cos^2(2\pi x)
+2\alpha\cos(2\pi x)(Pm)(x)
+\alpha^2(Ps)(x).
\]
Since \(Pm=0\), this reduces to
\[
s=(I-\alpha^2P)^{{-1}}h,
\qquad
h(x)=\cos^2(2\pi x)=\frac12+\frac12\cos(4\pi x).
\]
The doubling Perron operator acts on these Fourier modes by
\[
Ph=\frac12+\frac12\cos(2\pi x),
\qquad
P^2h=\frac12,
\qquad
P^kh=\frac12\quad(k\ge2).
\]
Summing the Neumann series yields
\[
s(x)=
\frac1{{2(1-\alpha^2)}}
+\frac{{\alpha^2}}2\cos(2\pi x)
+\frac12\cos(4\pi x).
\]
Finally,
\[
m(x)^2=\frac12+\frac12\cos(4\pi x),
\]
so subtraction gives the conditional-variance formula. Integrating over \([0,1)\) gives the global mean and variance. The extrema follow from \(-1\le\cos(2\pi x)\le1\).

## Verification
The accompanying checker verifies the Fourier-coefficient recurrence for the conditional second moment, the subtraction producing the conditional variance, and its exact lower endpoint. It returns `VERIFY_OK`.

The proof itself is analytic. No finite orbit sample, histogram, or numerical regression is used to infer the identities.

## Relationship to prior work
Kaplan and Yorke introduced the multidimensional difference-equation setting in the 1979 Lecture Notes in Mathematics volume that contains the chapter “Chaotic behavior of multidimensional difference equations.” The volume was published on 1 August 1979. The chapter's opening pages were inspected directly and establish its multidimensional-chaos and attractor-dimension program; later standard references record the canonical two-dimensional skew-product normalization used here.

Liang's 2016 open article uses the Kaplan–Yorke map as a benchmark and writes its Frobenius–Perron operator explicitly. That article studies information flow and causality. Targeted full-text searches of the accessible article text found no occurrences of “variance,” “moment,” or “conditional” matching the theorem above. The published Frobenius–Perron equation is compatible with, but does not state, the closed conditional first- and second-moment solution proved here.

Standard summaries and dimension literature emphasize the map's Lyapunov/correlation/capacity dimensions. Those geometric quantities do not determine the displayed fiberwise mean and variance functions.

## Limitations
The theorem fixes only the first two conditional moments. It does not give a closed formula for the full conditional distribution, its dimension, entropy, or higher conditional cumulants.

The Lebesgue-marginal hypothesis is essential to the equal inverse-branch weights used by \(P\). Other invariant first-coordinate marginals need not obey these formulas.

The original 1979 chapter was only partially text-extractable in the inspected copy, so a differently phrased moment identity in later pages remains a residual bibliographic risk. A complete same-object 2016 research article was therefore used for the strongest direct comparison available in this run.

## References
1. J. L. Kaplan and J. A. Yorke, “Chaotic behavior of multidimensional difference equations,” in *Functional Differential Equations and Approximation of Fixed Points*, Lecture Notes in Mathematics 730, 204–227 (1979), DOI 10.1007/BFb0064319.
2. H.-O. Peitgen and H.-O. Walther (eds.), *Functional Differential Equations and Approximation of Fixed Points*, Lecture Notes in Mathematics 730, Springer (1979), DOI 10.1007/BFb0064306.
3. X. S. Liang, “Information flow and causality as rigorous notions ab initio,” *Physical Review E* 94, 052201 (2016), DOI 10.1103/PhysRevE.94.052201.
