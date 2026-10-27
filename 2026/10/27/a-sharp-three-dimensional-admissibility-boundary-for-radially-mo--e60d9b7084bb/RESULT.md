# A sharp three-dimensional admissibility boundary for radially modulated Matérn kernels

## Finding

For all real parameters \(a>0\) and \(\omega\geq0\), put \(r=\|x-y\|_2\) and consider the stationary isotropic kernel on \(\mathbb R^3\)
\[
K_{a,\omega}(x,y)=(1+ar)e^{-ar}\cos(\omega r).
\]
The kernel is positive semidefinite for every finite configuration if and only if
\[
\boxed{a^2\geq5\omega^2.}
\]
Every admissible kernel is strictly positive definite on pairwise distinct sites, including the equality boundary. If \(a^2<5\omega^2\), its radial Fourier spectral density has exactly one sign change: it is strictly negative below a unique frequency \(s_*\in(0,\omega)\) and strictly positive above that frequency. At \(a^2=5\omega^2\) with \(\omega>0\), the spectral density vanishes only at frequency zero, to quadratic order.

For comparison, the same radial formula in one Euclidean dimension is strictly positive definite for every \(a>0\) and \(\omega\geq0\), without a frequency restriction. Thus cosine modulation of the Matérn smoothness-\(3/2\) envelope has a sharp dimension-sensitive covariance admissibility boundary.

## Assumptions and scope

All parameters are real; \(a>0\) and \(\omega\geq0\). The norm is Euclidean. Positivity means that for every integer \(N\geq1\), every \(x_1,\ldots,x_N\in\mathbb R^3\), and every \(c_1,\ldots,c_N\in\mathbb C\),
\[
\sum_{j,k=1}^{N}\overline{c_j}c_kK_{a,\omega}(x_j,x_k)\geq0.
\]
Strictness refers to pairwise distinct sites and nonzero coefficient vectors. The Fourier transform is normalized by
\[
\widehat f(\xi)=\int_{\mathbb R^3}f(x)e^{-i\langle x,\xi\rangle}\,dx,
\qquad f(x)=(2\pi)^{-3}\int_{\mathbb R^3}\widehat f(\xi)e^{i\langle x,\xi\rangle}\,d\xi.
\]
The theorem does not assert a characterization in every Euclidean dimension or on curved spaces. Its comparison with dimension one is exact.

## Proof

**Step 1: Exact transform.** Write \(s=\|\xi\|_2\). The kernel's radial profile is continuous and integrable on \(\mathbb R^3\), and the three-dimensional radial Fourier formula gives, for \(s>0\),
\[
\widehat K_{a,\omega}(s)=\frac{4\pi}{s}\int_0^\infty r(1+ar)e^{-ar}\cos(\omega r)\sin(sr)\,dr.
\]
Differentiation of \(\int_0^\infty e^{-ar}\sin(kr)\,dr=k/(a^2+k^2)\) yields
\[
\int_0^\infty r(1+ar)e^{-ar}\sin(kr)\,dr
=\frac{8a^3k}{(a^2+k^2)^3}
\]
for every real \(k\). Combining the two sine frequencies gives
\[
\widehat K_{a,\omega}(s)=\frac{16\pi a^3}{s}
\left[\frac{s+\omega}{(a^2+(s+\omega)^2)^3}
+\frac{s-\omega}{(a^2+(s-\omega)^2)^3}\right].
\]
The expression extends continuously to \(s=0\).

**Step 2: Exact sign polynomial.** Let
\[
D_\pm(s)=a^2+(s\pm\omega)^2
\]
and define
\[
\begin{aligned}
P_{a,\omega}(X)={}&X^3+(3a^2+9\omega^2)X^2\\
&+(3a^4+6a^2\omega^2-5\omega^4)X\\
&+(a^2+\omega^2)^2(a^2-5\omega^2).
\end{aligned}
\]
An exact polynomial expansion gives
\[
(s+\omega)D_-(s)^3+(s-\omega)D_+(s)^3=2sP_{a,\omega}(s^2).
\]
Consequently, including \(s=0\) by continuity,
\[
\boxed{\widehat K_{a,\omega}(s)=\frac{32\pi a^3P_{a,\omega}(s^2)}{D_+(s)^3D_-(s)^3}.}
\]
The denominator is everywhere positive. In particular,
\[
P_{a,\omega}(0)=(a^2+\omega^2)^2(a^2-5\omega^2),
\qquad P_{a,\omega}(\omega^2)=a^6.
\]

**Step 3: Positive regime and strictness.** If \(a^2\geq5\omega^2\), the coefficients of \(X^3\), \(X^2\), and \(X\) in \(P\) are strictly positive and the constant coefficient is nonnegative. Thus \(\widehat K(s)>0\) for all \(s>0\); at equality it is zero at \(s=0\) and positive elsewhere. The continuous Fourier transform is integrable (its tail is of order \(s^{-6}\)), so Fourier inversion and Bochner's theorem establish positive semidefiniteness. The Fourier density is positive on an open set of positive measure; for pairwise distinct sites and a nontrivial coefficient vector, the finite exponential sum \(\sum_jc_je^{i\langle\xi,x_j\rangle}\) cannot vanish almost everywhere. Integrating its squared modulus against \(\widehat K(\xi)\) proves strict positive definiteness.

**Step 4: Sharp failure and spectral obstruction.** If \(a^2<5\omega^2\), then \(P(0)<0\), while \(P(\omega^2)=a^6>0\). Written in descending powers of \(X\), the coefficient sequence has signs \(+,+,\pm,-\); omitting any zero coefficient leaves exactly one sign change. Descartes' rule of signs and the intermediate value theorem give exactly one positive root \(X_*\in(0,\omega^2)\), simple. Hence \(s_*=\sqrt{X_*}\) is the unique positive frequency at which \(\widehat K\) changes sign, negative on \(0\leq s<s_*\) and positive on \(s>s_*\). A continuous Fourier density that is negative on an open set cannot represent a positive-definite integrable stationary kernel, by the converse direction of Bochner's theorem. Necessity follows.

**Step 5: One-dimensional contrast.** In \(\mathbb R\), the Matérn envelope \((1+a|t|)e^{-a|t|}\) has Fourier transform \(4a^3/(a^2+s^2)^2\). Multiplication by \(\cos(\omega t)\) shifts this positive spectrum symmetrically, giving
\[
\widehat K^{(1)}_{a,\omega}(s)=2a^3\left[
\frac1{(a^2+(s-\omega)^2)^2}+
\frac1{(a^2+(s+\omega)^2)^2}\right]>0.
\]
This proves the stated unrestricted one-dimensional strict positive definiteness.

## Verification

The standalone file `check_spectrum.py` uses Python 3 standard-library arithmetic. It performs exact sparse-integer-polynomial verification of the numerator identity for symbolic \(a,\omega,s\), followed by independent Simpson quadrature checks of the three-dimensional radial Fourier integral in both admissible and inadmissible regimes, including a boundary sample. Execute it using `python3 check_spectrum.py`. It is supplementary reproducibility evidence, not an infinite-domain proof. The analytical coefficient argument and Descartes' rule supply the infinite-parameter claims.

## Relationship to prior work

The normalized envelope is the standard Matérn covariance with smoothness \(3/2\), explicitly recorded in Rasmussen and Williams (2006, §4.2). The isotropic positive-definiteness framework is reviewed by Gneiting (2011 preprint, §2). Wilson and Adams (2013, §3) construct spectral-mixture oscillatory covariances with cosine factors of **linear coordinate differences**; their formulae do not give this radial-distance cosine times the Matérn envelope in \(\mathbb R^3\). Hu, Lindgren, Simpson and Rue (2013, §3.1) construct isotropic oscillating random fields with a **nonnegative rational quartic spectral density**, a different family. Hristopulos (2014, §§III–V) derives Spartan and Bessel–Lommel oscillatory covariance classes, not the present sharp sign classification. General kernel validity, spectral-mixture approximation, or an alternative oscillatory covariance construction does not itself imply the threshold \(a^2\ge5\omega^2\).

## Limitations

The result is a classification for this specific one-parameter Matérn smoothness level and real radial cosine modulation in dimension three, with a one-dimensional comparison. It does not classify dimensions two or greater than three, other Matérn smoothness parameters, anisotropic modulations, or arbitrary mixtures. The uniqueness claim concerns the Fourier **radial sign-change frequency**, not zeros of the spatial covariance, which oscillates. The literature comparison is bounded to the inspected sources and accessible research records; it does not prove that no equivalent theorem appears elsewhere. No independent scientific audit has been completed.

## References

1. C. E. Rasmussen and C. K. I. Williams, *Gaussian Processes for Machine Learning*, 2006, Chapter 4, §4.2, equations (4.14)–(4.17). https://gaussianprocess.org/gpml/chapters/RW4.pdf
2. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077v1, submitted 2011-11-30, §2. https://arxiv.org/abs/1111.7077
3. A. G. Wilson and R. P. Adams, *Gaussian Process Kernels for Pattern Discovery and Extrapolation*, arXiv:1302.4245v1, submitted 2013-02-18; ICML 2013, §3. https://proceedings.mlr.press/v28/wilson13.pdf
4. X. Hu, F. Lindgren, D. Simpson, and H. Rue, *Multivariate Gaussian Random Fields with Oscillating Covariance Functions using Systems of Stochastic Partial Differential Equations*, arXiv:1307.1384v1, submitted 2013-07-04, §3.1. https://arxiv.org/abs/1307.1384
5. D. T. Hristopulos, *Radial Covariance Functions Motivated by Spatial Random Field Models with Local Interactions*, arXiv:1401.2823v1, submitted 2014-01-13, §§III–V. https://arxiv.org/abs/1401.2823
