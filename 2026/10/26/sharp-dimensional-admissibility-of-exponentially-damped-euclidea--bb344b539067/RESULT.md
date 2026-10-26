# Sharp dimensional admissibility of exponentially damped Euclidean wave kernels

## Finding
For positive real parameters \(a,\omega\), define the continuous radial function
\[
 k_{a,\omega}(r)=
 \begin{cases}
 e^{-ar}\dfrac{\sin(\omega r)}{\omega r},&r>0,\\
 1,&r=0.
 \end{cases}
\]
For every odd integer \(d=2p+1\ge3\), the stationary kernel \(K(x,y)=k_{a,\omega}(\|x-y\|_2)\) on \(\mathbb R^d\) is positive semidefinite for **all finite point sets** if and only if
\[
 \boxed{2p\arctan(\omega/a)\le\pi.}
\]
Whenever this condition holds, the Gram matrix is **positive definite** for every configuration of pairwise distinct points. The threshold includes equality. Equivalently, for odd \(d\ge5\), the sharp condition is \(\omega/a\le\tan(\pi/(d-1))\); in dimension three all positive ratios are admissible. In particular, dimensions five, seven and nine require, respectively, \(a\ge\omega\), \(a\ge\sqrt3\,\omega\) and \(a\ge(1+\sqrt2)\omega\).

More precisely, the radial Fourier transform has a *complete sign-phase description*. Write \(p=(d-1)/2\), and define for \(s\ge0\)
\[
 \beta(s)=\operatorname{Arg}\bigl(s^2+a^2-\omega^2+2ia\omega\bigr)
 \in(0,2\arctan(\omega/a)].
\]
Then the Fourier transform of \(k_{a,\omega}\), with the nonunitary convention described below, is a strictly positive factor times \(\sin(p\beta(s))\). Consequently the spectral sign changes occur exactly when \(\beta(s)=j\pi/p\) for integers \(j\) strictly between \(0\) and \(2p\arctan(\omega/a)/\pi\). The zero associated with such an integer occurs at
\[
 s_j=\sqrt{2a\omega\cot(j\pi/p)-a^2+\omega^2}.
\]
An endpoint equality gives \(s=0\); in the admissible equality case the density is positive for all \(s>0\). In every inadmissible regime there is a nonempty open interval of strictly negative spectral density.

## Assumptions and scope
Here \(a>0\), \(\omega>0\), \(d\in\{3,5,7,\ldots\}\), and \(x,y\) range over the entire Euclidean space \(\mathbb R^d\). Positive semidefiniteness means \(\sum_{j,k=1}^N c_j\overline{c_k}K(x_j,x_k)\ge0\) for every integer \(N\ge1\), every configuration of sites and every complex coefficient vector. The radial Fourier transform is
\[
 \widehat k_d(\xi)=\int_{\mathbb R^d} k_{a,\omega}(\|x\|_2)e^{-ix\cdot\xi}\,dx,
 \qquad s=\|\xi\|_2.
\]
The exponential damping ensures absolute integrability in every fixed dimension. Values at \(s=0\), and the value of the kernel at \(r=0\), are taken by continuous extension. This result does not claim a classification in arbitrary even dimensions or at \(a=0\).

## Proof
**1. Base transform.** The three-dimensional radial Fourier formula and the elementary integral of a product of damped sines give, first for \(s>0\),
\[
\begin{aligned}
\widehat k_3(s)
 &=\frac{4\pi}{\omega s}\int_0^\infty e^{-ar}\sin(\omega r)\sin(sr)\,dr\\
 &=\frac{8\pi a}
 {[a^2+(\omega-s)^2][a^2+(\omega+s)^2]}.
\end{aligned}
\]
The expression extends continuously to zero. Put \(u=s^2\) and
\[
 z(u)=u+(a-i\omega)^2,
 \qquad Q(u)=z(u)\overline{z(u)}.
\]
As \(\operatorname{Im}(z(u)^{-1})=2a\omega/Q(u)\),
\[
 \widehat k_3(\sqrt u)=\frac{4\pi}{\omega}\operatorname{Im}z(u)^{-1}.
\]

**2. Dimension walk and its normalization.** For any radial exponentially integrable function and any \(d\ge1\), the standard Bessel integral for its Fourier transform is
\[
 \widehat f_d(s)=(2\pi)^{d/2}s^{1-d/2}
 \int_0^\infty f(r)r^{d/2}J_{d/2-1}(sr)\,dr.
\]
Differentiating the Bessel factor using \(\frac{d}{ds}[s^{-\nu}J_\nu(sr)]=-r s^{-\nu}J_{\nu+1}(sr)\) proves, for \(s>0\),
\[
 \widehat f_{d+2}(s)=-\frac{2\pi}{s}\frac{d}{ds}\widehat f_d(s)
 =-4\pi\frac{d}{du}\widehat f_d(\sqrt u).
\]
For this kernel, exponential decay justifies differentiation under the integral and extension to \(s=0\). Apply the recurrence \(p-1\) times to the three-dimensional identity, using \(\frac{d^m}{du^m}z(u)^{-1}=(-1)^m m!z(u)^{-m-1}\). The complete odd-dimensional transform is
\[
 \boxed{
 \widehat k_{2p+1}(s)=
 \frac{(4\pi)^p(p-1)!}{\omega}\,
 \operatorname{Im}\bigl[s^2+(a-i\omega)^2\bigr]^{-p}.
 }
\]
All prefactors are strictly positive.

**3. Exact sign test.** The complex number \(z(u)\) has a strictly negative imaginary part. Thus write \(z(u)=|z(u)|e^{-i\beta(\sqrt u)}\). Its argument angle satisfies
\[
 \beta(0)=2\arctan(\omega/a),\quad
 \lim_{s\to\infty}\beta(s)=0,\quad
 \frac{d\beta(\sqrt u)}{du}=-\frac{2a\omega}{|z(u)|^2}<0.
\]
It follows immediately that
\[
 \widehat k_{2p+1}(s)=
 \frac{(4\pi)^p(p-1)!}{\omega|z(s^2)|^p}
 \sin(p\beta(s)).
\]
Since \(\beta\) runs continuously and strictly over \((0,2\arctan(\omega/a)]\), its sine is nonnegative throughout precisely when \(2p\arctan(\omega/a)\le\pi\). For the converse, if the upper endpoint is strictly greater than \(\pi/p\), the angle interval contains some \(\beta\) in \((\pi/p,\min\{2\pi/p,2\arctan(\omega/a)\})\), yielding a negative open frequency band. The displayed formula for the roots follows by solving \(\cot\beta=(s^2+a^2-\omega^2)/(2a\omega)\). All asserted boundary cases follow from this same sign calculation.

**4. Positive definiteness and strictness.** A continuous integrable stationary function is positive semidefinite on all finite configurations if and only if its Fourier transform is nonnegative, by Bochner's theorem and uniqueness of the Fourier transform of a finite positive measure. When the threshold holds, the spectral density is strictly positive on every frequency with \(s>0\), even at the endpoint. Thus for distinct points the Bochner quadratic form is an integral of \(|\sum_j c_j e^{i\xi\cdot x_j}|^2\) against a density positive on an open set. A finite sum of distinct exponentials cannot vanish identically on an open set unless all its coefficients vanish, proving strict positive definiteness. When the threshold fails, negative density on an open frequency band rules out positive semidefiniteness.

## Verification
A standalone `verify.py` reproduces the exact symbolic dimension-walk identities in dimensions three, five and seven; it also cross-checks their numerical complex-power form through dimension eleven and samples both sides of the threshold. Run `python verify.py` with Python 3 and SymPy installed. Finite samples do not establish the for-all-frequency claim; that is furnished by Step 3. All formulas and constants use the Fourier convention in the scope paragraph.

## Relationship to prior work
The classical Euclidean wave kernel \(\sin(\omega r)/(\omega r)\) is standard in dimension three; multiplying it by the dimension-free positive definite exponential retains positive definiteness there by the Schur product principle (Genton 2001, Table 1). That argument does **not** imply positive definiteness in higher dimensions. The exact rescue criterion above determines when exponential damping permits dimension five and successively higher odd dimensions. Gneiting (arXiv:1111.7077) discusses positive-definite radial families and dimension walks in a spherical setting. Schubert et al. (2021) analyze damped sine/cosine ARMA-derived covariance models, but their denominator-free oscillatory model does not imply the present sinc-factor classification. The finding is a concrete dimension-dependent sign theorem, not a new general dimension-walk or Bochner criterion.

## Limitations
The theorem is for strictly positive damping and frequency and odd Euclidean dimensions at least three; its scope does not include a complete even-dimensional phase diagram. The algebraic checker is supplementary and is not independent verification or a substitute for the analytic proof. Literature indexing may miss equivalent claims, including ones formulated as spectral density or dimension-walk criteria. A 2001 source predates the day-resolved source date used in metadata, but its publication information is only month-resolved in the material inspected.

## References
- Marc G. Genton, *Classes of Kernels for Machine Learning: A Statistics Perspective*, Journal of Machine Learning Research 2 (2001), 299–312, especially Table 1. https://www.jmlr.org/papers/volume2/genton01a/genton01a.pdf (publication documented as December 2001).
- Tilmann Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077, originally posted 2011-11-30. https://arxiv.org/abs/1111.7077
- Till Schubert, Jan Martin Brockmann, Johannes Korte and Wolf-Dieter Schuh, *On the Family of Covariance Functions Based on ARMA Models*, Engineering Proceedings 5 (2021), article 37, doi:10.3390/engproc2021005037. https://doi.org/10.3390/engproc2021005037
