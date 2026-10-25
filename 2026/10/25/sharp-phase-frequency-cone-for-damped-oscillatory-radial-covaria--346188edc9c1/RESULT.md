# Sharp phase–frequency cone for damped oscillatory radial covariances

## Finding

Let \(d\) be a positive integer, \(\alpha>0\), \(\omega>0\), and \(\beta\in\mathbb R\). On \(\mathbb R^d\) define the normalized, stationary, isotropic kernel
\[
K_{\alpha,\omega,\beta}^{(d)}(x,y)=e^{-\alpha r}\bigl[\cos(\omega r)+\beta\sin(\omega r)\bigr],\quad r=\|x-y\|_2.
\]
Write \(\phi=\arctan(\omega/\alpha)\in(0,\pi/2)\). Then this kernel is positive semidefinite for every finite collection of sites and coefficients **if and only if**
\[
\boxed{\phi\le\frac{\pi}{d+1}\quad\text{and}\quad-\cot(d\phi)\le\beta\le\cot\phi=\frac{\alpha}{\omega}.}
\]
Whenever these inequalities hold, the kernel is in fact strictly positive definite on pairwise distinct sites; both coefficient endpoints are included. For each \(d\ge2\), the maximal admissible oscillation-to-decay ratio is \(\tan(\pi/(d+1))\); at this largest frequency the coefficient is uniquely \(\beta=\cot(\pi/(d+1))\). Setting \(\beta=0\) recovers the classical damped-cosine condition \(\omega/\alpha\le\tan(\pi/(2d))\). The upper coefficient face is also exactly the cancellation \(K'(0^+)=-\alpha+\beta\omega=0\), while the lower face forces the zero-frequency spectral density \(F_d(0)=0\); both remain strictly positive definite on distinct sites.

In particular, \(e^{-r}(\cos r+\sin r)\) is strictly positive definite on \(\mathbb R^3\), but not positive definite on \(\mathbb R^4\). Its dimension-three Fourier spectrum is the explicit nonnegative function \(64\pi\|\xi\|_2^2/(\|\xi\|_2^4+4)^2\).

## Assumptions and scope

The Fourier convention is \(\widehat f(\xi)=\int_{\mathbb R^d}e^{-i\xi\cdot x}f(x)\,dx\), with no normalization factor in the forward transform. The kernel is the real-valued, even function of \(x-y\) displayed above; \(d\ge1\) is an integer and all parameters are real with \(\alpha,\omega>0\). Positive definiteness means the usual nonnegative quadratic-form condition for every number of sample sites; strict positive definiteness means positivity whenever sites are pairwise distinct and coefficients not all zero. When \(\omega=0\), the kernel is \(e^{-\alpha r}\), independent of \(\beta\), and is strictly positive definite in every dimension. The \(\omega>0\) theorem is not asserted for negative decay or non-Euclidean distances.

## Proof

**1. Fourier transform.** For real \(a>0\), direct radial integration (or the Gaussian-subordination identity below) gives
\[
\widehat{e^{-a\|\cdot\|}}(\xi)
=c_d\frac{a}{(a^2+\rho^2)^{(d+1)/2}},\quad
c_d=2^d\pi^{(d-1)/2}\Gamma((d+1)/2),\quad \rho=\|\xi\|_2.
\]
One derivation uses \(e^{-ar}=\frac{a}{2\sqrt\pi}\int_0^\infty t^{-3/2}\exp(-a^2/(4t)-tr^2)\,dt\). Fubini and the Fourier transform of \(e^{-t\|x\|^2}\) then give
\(\widehat{e^{-ar}}=a\pi^{(d-1)/2}\int_0^\infty t^{-(d+3)/2}e^{-(a^2+\rho^2)/(4t)}\,dt/2\), which evaluates to the displayed constant. The **Fourier-transform identity** extends holomorphically to \(\operatorname{Re}a>0\) by dominated convergence of the original Fourier integral on compact subsets of that half-plane, followed by the identity theorem. The auxiliary Gaussian-subordination integral is only used for real \(a>0\).

Put \(z=\alpha-i\omega\). Since
\[
e^{-\alpha r}[\cos(\omega r)+\beta\sin(\omega r)]=\operatorname{Re}((1-i\beta)e^{-zr}),
\]
its exact spectral density is
\[
F_d(\rho)=c_d\operatorname{Re}\!\left[\frac{(1-i\beta)z}{(z^2+\rho^2)^{(d+1)/2}}\right].
\]
Here the power uses the principal logarithm. The quantity \(z^2+\rho^2\) lies strictly below the real axis for every finite \(\rho\), because its imaginary part is \(-2\alpha\omega<0\); it never crosses the branch cut. The overall real-valued spectral density is continuous, and the radial kernel is integrable.

**2. Continuous spectral phase.** Set \(b=\arctan\beta\in(-\pi/2,\pi/2)\), \(\phi=\arctan(\omega/\alpha)\), and \(\theta(\rho)=\operatorname{Arg}(z^2+\rho^2)\). The argument is continuous and strictly increases from \(\theta(0)=-2\phi\) to \(\lim_{\rho\to\infty}\theta(\rho)=0\). Indeed, the denominator's imaginary part is fixed strictly negative while its real part increases with \(\rho^2\). Therefore the sign of \(F_d(\rho)\) is the sign of \(\cos q(\rho)\), where
\[
q(\rho)=-b-\phi-\frac{d+1}{2}\theta(\rho).
\]
This strictly decreasing phase fills the open interval between
\[
q(0)=d\phi-b,\qquad q(\infty)=-\phi-b.
\]
Its total phase sweep is exactly \((d+1)\phi\), regardless of \(\beta\).

**3. Exact positivity interval.** Because \(\phi\in(0,\pi/2)\) and \(b\in(-\pi/2,\pi/2)\), the lower endpoint satisfies \(-\pi<q(\infty)<\pi/2\). If the spectral cosine is nonnegative everywhere, that lower endpoint must lie in \([-\pi/2,\pi/2]\), so the entire connected phase interval must lie in that same nonnegative cosine band. Conversely, inclusion of the whole phase interval in this band is sufficient. The two necessary and sufficient inequalities are therefore
\[
d\phi-b\le\frac\pi2,\qquad-\phi-b\ge-\frac\pi2,
\]
which are equivalent to \(d\phi-\pi/2\le b\le\pi/2-\phi\). The interval is nonempty exactly when \(\phi\le\pi/(d+1)\). In this range \(d\phi\in(0,\pi)\), so monotonicity of tangent on \((-\pi/2,\pi/2)\) yields \(\beta\ge\tan(d\phi-\pi/2)=-\cot(d\phi)\) and \(\beta\le\tan(\pi/2-\phi)=\cot\phi\). This proves the complete parameter classification.

Bochner's theorem applies because the radial function is continuous and integrable: positive definiteness is equivalent to \(F_d\ge0\) pointwise. At either boundary the cosine phase is zero at at most one endpoint \(\rho=0\) or \(\rho=\infty\), not on a nontrivial interval, so \(F_d(\rho)>0\) for all finite \(0<\rho<\infty\). For distinct sites, the Fourier quadratic form is the integral of \(F_d(\|\xi\|)|\sum_j c_j e^{i\xi\cdot x_j}|^2\); the nontrivial exponential polynomial cannot vanish on an open set. Thus all admissible kernels are strictly positive definite. At the frequency endpoint \(\phi=\pi/(d+1)\), the admissible interval for \(\beta\) contracts to a single point \(\cot\phi\).

**4. The dimension-three witness.** For \(d=3\), \(\alpha=\omega=\beta=1\), \(z=1-i\) and \(c_3=8\pi\). The spectral formula reduces exactly to
\[
F_3(\rho)=8\pi\operatorname{Re}\!\frac{-2i}{(\rho^2-2i)^2}=\frac{64\pi\rho^2}{(\rho^4+4)^2}.
\]
The dimension-four criterion requires \(\phi\le\pi/5\), whereas \(\phi=\pi/4\), proving failure in dimension four; it is not a merely numerical inference.

## Verification

The Fourier normalization and analytic continuation can be checked independently by integrating the radial Fourier–Bessel formula. The companion `CHECKER.py` numerically tests agreement with this independent integral in dimensions one, two, three, and five, and checks sign transitions immediately outside both coefficient endpoints. The checker is illustrative; it is not used to infer the infinite-range theorem. Every branch, coefficient boundary, and positive-definiteness quantifier is handled analytically above.

## Relationship to prior work

Schoenberg's radial positive-definiteness theory and its dimension nesting are summarized in Gneiting's 2011 preprint, especially Section 2, and give the general structural backdrop, not these sharp four-parameter inequalities. The established `RMdampedcos` model is exactly the \(\beta=0\) cross-section of this result, with condition \(\alpha/\omega\ge\cot(\pi/(2d))\). Schubert–Korte–Brockmann–Schuh study damped oscillatory time-series covariances via second-order Gauss–Markov processes, but their one-dimensional stationary autocorrelations do not determine positivity of radial extensions to dimensions two and above. The novelty claimed here is the **full frequency–phase admissibility cone in arbitrary Euclidean dimension**, not the Fourier transform of \(e^{-ar}\), general Bochner theory, or the previously known cosine-only slice.

## Limitations

The result is confined to integer-dimensional Euclidean distances, positive damping, positive frequency and one damped harmonic. It does not assert positivity on spheres with geodesic distance, on arbitrary metric spaces, or for mixtures of unrelated damped components. An identical full parameter cone in unindexed or inaccessible literature cannot be ruled out by bounded search. All review described here is self-review; there has been no independent audit or validation.

## References

1. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077v1, first posted 2011-11-30, especially Section 2; https://arxiv.org/abs/1111.7077.
2. `RandomFields` documentation, *RMdampedcos: Exponentially Damped Cosine*, https://rdrr.io/cran/RandomFields/man/RMdampedcos.html; classical cosine-only admissibility condition.
3. T. Schubert, J. Korte, J. M. Brockmann, W.-D. Schuh, *A Generic Approach to Covariance Function Estimation Using ARMA-Models*, Mathematics 8 (2020), 591, DOI 10.3390/math8040591, especially Sections 3 and 8; https://doi.org/10.3390/math8040591.
