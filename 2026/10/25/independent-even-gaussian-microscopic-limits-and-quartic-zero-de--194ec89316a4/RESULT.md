# Independent even-Gaussian microscopic limits and quartic zero depletion for palindromic Kac polynomials

## Finding
Let \(\xi_0,\xi_1,\ldots\) be independent standard circular complex Gaussian variables, normalized by \(\mathbb E\xi_j=\mathbb E\xi_j^2=0\) and \(\mathbb E|\xi_j|^2=1\). For every integer \(n\ge1\), form the monic-up-to-random-leading-coefficient reciprocal polynomial
\[
P_{2n}(z)=\sum_{j=0}^{n-1}\xi_j(z^j+z^{2n-j})+\xi_n z^n.
\]
At the two fixed points of reciprocal inversion on the unit circle define entire functions
\[
F_n^\pm(w)=n^{-1/2}e^{-w}P_{2n}(\pm e^{w/n}).
\]
Then \((F_n^+,F_n^-)\) converges jointly in distribution in the compact-open topology of \(\mathcal H(\mathbb C)^2\) to two **independent** copies of the even Gaussian entire function
\[
F(w)=2\int_0^1\cosh(tw)\,dW(t),
\qquad
\mathbb E[F(w)\overline{F(v)}]=4\int_0^1\cosh(tw)\overline{\cosh(tv)}\,dt,
\]
where \(W\) is circular complex Gaussian white noise on \([0,1]\). Therefore the locally rescaled zero point processes around \(z=1\) and \(z=-1\), with zeros counted with multiplicity, converge jointly to independent copies of the zero process of \(F\). Each limiting zero multiset is invariant under \(w\mapsto-w\).

For \(w=x+iy\), the limiting zero-intensity density with respect to planar area is
\[
\rho(w)=\frac{1}{4\pi}(\partial_x^2+\partial_y^2)
\log\!\left(\frac{\sinh(2x)}{x}+\frac{\sin(2y)}{y}\right),
\]
with the continuous values \(2\) used for each quotient at zero. In particular, its **exact leading local depletion** is
\[
\rho(w)=\frac{4}{45\pi}|w|^2+O(|w|^4),\qquad
\mathbb E\,\#\{w:F(w)=0,\ |w|<r\}=\frac{2}{45}r^4+O(r^6)
\quad(r\downarrow0).
\]
For every finite \(n\ge1\), the reciprocal polynomial has almost surely no zero on \(|z|=1\), and exactly \(n\) zeros inside and \(n\) outside the unit circle.

## Assumptions and scope
The coefficient law is exactly independent **circular complex Gaussian**, and the reciprocal symmetry is \(z^{2n}P_{2n}(1/z)=P_{2n}(z)\), **without** complex conjugation. The distinct normalization \(n^{-1/2}\) and the logarithmic local coordinate \(z=\pm e^{w/n}\) are essential; the claim is for fixed compact sets in the complex \(w\)-plane as \(n\to\infty\). The stochastic integral is the holomorphic Gaussian modification of an isonormal complex Gaussian process in \(L^2[0,1]\). The zero-point-process assertions count multiplicity and refer to vague convergence of locally finite counting measures.

## Proof
**1. Reciprocal and even structure.** Direct expansion yields
\[
F_n^+(w)=\frac1{\sqrt n}\left(2\sum_{j=0}^{n-1}\xi_j\cosh((1-j/n)w)+\xi_n\right),
\]
\[
F_n^-(w)=\frac1{\sqrt n}\left(2\sum_{j=0}^{n-1}(-1)^j\xi_j\cosh((1-j/n)w)+(-1)^n\xi_n\right).
\]
Both functions are even in \(w\), and \(P_{2n}\) satisfies \(z^{2n}P_{2n}(1/z)=P_{2n}(z)\).

**2. Joint analytic Gaussian limit.** Circularity gives all pseudo-covariances \(\mathbb E[F_n^\varepsilon(w)F_n^\delta(v)]=0\). The two diagonal covariance kernels coincide:
\[
K_n(w,v)=\frac4n\sum_{j=0}^{n-1}\cosh((1-j/n)w)\overline{\cosh((1-j/n)v)}+\frac1n.
\]
Uniformly on compact \((w,v)\)-sets, Riemann sums give
\[
K_n(w,v)\longrightarrow K(w,v)
=4\int_0^1\cosh(tw)\overline{\cosh(tv)}\,dt.
\]
The cross covariance is
\[
\mathbb E[F_n^+(w)\overline{F_n^-(v)}]
=\frac4n\sum_{j=0}^{n-1}(-1)^j\cosh((1-j/n)w)\overline{\cosh((1-j/n)v)}+\frac{(-1)^n}{n}.
\]
Pairing consecutive terms and bounding the derivative of the smooth summand on the unit interval gives a uniform \(O_{C}(n^{-1})\) bound on any compact \(C\subset\mathbb C^2\). Thus the limiting Gaussian pair has block-diagonal covariance and, by circularity, independent components. For each \(R>0\), the second moments on \(|w|=R+1\) are bounded uniformly in \(n\). Subharmonicity and Cauchy's formula give a constant \(c_R\) such that
\[
\mathbb E\sup_{|w|\le R}|F_n^\pm(w)|^2
\le c_R\sup_{|w|=R+1}\mathbb E|F_n^\pm(w)|^2<\infty.
\]
Markov's inequality, Montel compactness and a diagonal argument prove tightness in \(\mathcal H(\mathbb C)^2\); Gaussian finite-dimensional convergence identifies the stated weak limit. The stochastic-integral representation has precisely the kernel \(K\) and an entire analytic modification.

**3. Zero-process limit.** Because \(F(0)\) is nondegenerate circular complex Gaussian with variance \(4\), the limit is almost surely not the zero function. For a deterministic bounded domain whose boundary has zero area, the Edelman–Kostlan formula below gives zero expected number of limiting zeros on its boundary, so almost surely none there. The argument principle and Hurwitz's theorem make the zero counting map continuous at such holomorphic functions (multiplicities included). The continuous-mapping theorem proves joint vague convergence of zero measures. Evenness yields opposite pairs in the logarithmic coordinate. Independence of limiting fields gives independence of their zero processes.

**4. Exact intensity and fourth-order zero count.** Since
\[
|\cosh(t(x+iy))|^2=\frac{\cosh(2tx)+\cos(2ty)}{2},
\]
the diagonal covariance is
\[
K(w,w)=\frac{\sinh(2x)}{x}+\frac{\sin(2y)}{y}>0.
\]
Edelman–Kostlan gives \(\rho=(4\pi)^{-1}\Delta\log K(w,w)\). Taylor expansion near the origin yields
\[
K(w,w)=4+\frac43(x^2-y^2)+\frac4{15}(x^4+y^4)+O(|w|^6),
\]
\[
\log K(w,w)=\log4+\frac13(x^2-y^2)
+\frac1{90}(x^4+y^4)+\frac19x^2y^2+O(|w|^6).
\]
The harmonic quadratic term contributes no Laplacian, while the quartic terms give
\[
\Delta\log K(w,w)=\frac{16}{45}(x^2+y^2)+O(|w|^4).
\]
Integrating against planar area on a disk of radius \(r\) proves the two displayed depletion asymptotics, including the coefficient \(2/45\). The integrable expected zero measure has no atom at the origin since \(F(0)\ne0\) almost surely.

**5. Finite-degree exact half split.** On \(z=e^{i\theta}\) one has
\[
e^{-in\theta}P_{2n}(e^{i\theta})=\xi_n+2\sum_{j=0}^{n-1}\xi_j\cos((n-j)\theta).
\]
Condition on \(\xi_0,\ldots,\xi_{n-1}\). The second term traces a differentiable curve in the complex plane and therefore has planar Lebesgue measure zero. Since the independent \(\xi_n\) has a smooth planar density, the probability that this expression vanishes at **any** \(\theta\) is zero. The leading coefficient \(\xi_0\ne0\) almost surely, giving degree exactly \(2n\). Reciprocal symmetry pairs each zero \(z\) with \(1/z\); without unit-circle zeros, exactly \(n\) lie on each side. The assertion holds simultaneously for all \(n\) by countable intersection.

## Verification
The accompanying standalone script `verify.py` checks the quartic bivariate covariance expansion, its Laplacian, exact finite-degree Gaussian Taylor moments at the reciprocal fixed point, and a direct cross-covariance bound for both windows. Execution from a clean Python environment with SymPy gives:

`CHECK_OK: quartic covariance, Laplacian, finite-n zero-mass coefficients, fixed-point decorrelation`

For the finite-window Taylor coefficient \(F_n^+(w)=A_n+C_nw^2+O(w^4)\), the script checks the exact expression for the \(r^4\)-coefficient of expected local zero mass,
\[
2\left(\frac{\mathbb E|C_n|^2}{\mathbb E|A_n|^2}
-\frac{|\mathbb E(C_n\overline{A_n})|^2}{(\mathbb E|A_n|^2)^2}\right),
\]
where
\[
\mathbb E|A_n|^2=4+n^{-1},\quad
\mathbb E(C_n\overline{A_n})=\frac2n\sum_{k=1}^n(k/n)^2,\quad
\mathbb E|C_n|^2=\frac1n\sum_{k=1}^n(k/n)^4.
\]
The coefficient tends to \(2/45\). Numerical finite checks are not substitutes for the analytic convergence and zero-process arguments above.

## Relationship to prior work
Kawada (arXiv:2610.11324v1; publicly posted October 8, 2026) determines radial laws and fluctuations for usual independent-coefficient Kac/Littlewood ensembles, with a separate dependence criterion for counting the fraction of disk roots. Its full-text theorems do not identify a two-fixed-point limit of non-conjugated palindromic Gaussian polynomials or the quartic microscopic zero hole. Kabluchko, Khoruzhenko and Marynych (arXiv:2511.12302v1, Sections 1.6 and 4) study **self-inversive** ensembles with conjugated reversed coefficients; their associated trigonometric fields are real on the unit circle and can have many unit-circle zeros. The present **self-reciprocal without conjugation** model instead has almost surely none. General Gaussian-analytic-zero tools, including Edelman–Kostlan, provide the expected-intensity identity, not the particular limiting covariance or two-window independence; the tools themselves are not claimed as novel.

## Limitations
The argument is restricted to circular complex Gaussian independent half-coefficients and the two reciprocal fixed points \(1\) and \(-1\). It gives leading microscopic expected-zero depletion, not higher correlation functions, a non-Gaussian universality theorem, a global radial limit, or rates of convergence of point processes. The displayed fourth-order coefficient is exact but is not a universal constant across unrelated random-polynomial ensembles. Historical priority has not been independently established; classical general Gaussian analytic function results could implicitly cover some consequences. No independent mathematical audit has been performed.

## References
1. S. Kawada, *Universal Radial Laws for Random Polynomials: Erdős Problem #522 and Non-Universal Fluctuations*, arXiv:2610.11324v1, first posted 2026-10-08, https://arxiv.org/html/2610.11324v1.
2. Z. Kabluchko, B. Khoruzhenko and A. Marynych, *On the distribution patterns of zeros for random polynomials with regularly varying coefficients*, arXiv:2511.12302v1, first posted 2025-11-15, https://arxiv.org/html/2511.12302v1.
3. T. Tao and V. Vu, *Local universality of zeroes of random polynomials*, International Mathematics Research Notices 2015, https://doi.org/10.1093/imrn/rnu084.
4. K. Noda, *Expected number of zeros of random power series with finitely dependent complex Gaussian coefficients*, arXiv:2106.02860 (related dependent Gaussian setting).
5. J. Hough, M. Krishnapur, Y. Peres and B. Virág, *Zeros of Gaussian Analytic Functions and Determinantal Point Processes*, AMS, 2009 (general zero-intensity framework).
