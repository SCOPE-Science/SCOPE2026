# Exact nonlinear conditional transport profiles for shear diffusion with resetting

## Finding
For the stationary Brownian tracer with global Poisson resets to the origin, subjected between resets to planar linear shear,
\[
 dX_t=gY_t\,dt+\sqrt{2D}\,dW_t^{(1)},\qquad dY_t=\sqrt{2D}\,dW_t^{(2)},
\]
with independent standard Wiener processes, diffusivity \(D>0\), reset rate \(r>0\) and shear \(g\in\mathbb R\), write \(z=|y|\sqrt{r/D}\). Then for **every real \(y\)** the canonical continuous versions of the stationary conditional mean and variance are
\[
 \boxed{\mathbb E[X\mid Y=y]=\frac{g}{4r}y(1+z)},
\]
\[
 \boxed{\operatorname{Var}(X\mid Y=y)=\frac Dr(1+z)+\frac{Dg^2}{48r^3}(4z^3+12z^2+15z+15)}.
\]
Thus the shear-induced conditional mean grows quadratically in transverse displacement, not linearly, and for nonzero shear the conditional variance grows cubically as \(|y|\to\infty\). In particular, its positive derivative as a function of \(|y|\) is exact over the entire range. These identities hold at arbitrary shear, not only in perturbation theory. The stationary conditional law is exactly a generalized-inverse-Gaussian mixture of Gaussians, so every conditional moment is determined by a finite polynomial evaluation.

## Assumptions and scope
Independent planar Brownian noise has the covariance convention \(\mathbb E[(\sqrt{2D}W_t^{(i)})^2]=2Dt\). Each rate-\(r\) reset simultaneously sends both coordinates to \((0,0)\) and starts independent Brownian increments. The stationary law exists for all \(D>0\), \(r>0\), \(g\in\mathbb R\). Conditional expectations are interpreted as continuous versions at all \(y\), since conditioning at an individual point has probability zero. The claim does not apply to partial-coordinate resetting or nonzero resetting coordinates. The nontrivial conditional mean assertion requires \(g\ne0\), while the formulas also hold for \(g=0\).

## Proof
At a stationary observation time, the age \(A\) since the last reset is exponentially distributed with rate \(r\). Conditional on \(A=a\), the independent increment representation is
\[
 Y=\sqrt{2D}W_2(a),\qquad X=\sqrt{2D}W_1(a)+g\sqrt{2D}\int_0^a W_2(s)\,ds.
\]
Consequently \(Y\mid A=a\) is centered Gaussian with variance \(2Da\). The Brownian bridge decomposition gives
\[
 X\mid(Y=y,A=a)\sim\mathcal N\left(\frac{gay}{2},\;2Da+\frac{Dg^2a^3}{6}\right).
\]
Indeed \(\mathbb E[\int_0^aW_2(s)ds\mid W_2(a)]=aW_2(a)/2\) and the conditional integral variance is \(a^3/12\). Bayes' formula makes the conditional age density proportional to
\[
 a^{-1/2}\exp\left(-ra-\frac{y^2}{4Da}\right),\qquad a>0.
\]
Its normalization implies the exact stationary transverse Laplace density
\[
 f_Y(y)=\frac12\sqrt{r/D}\exp(-z),\qquad z=|y|\sqrt{r/D}.
\]
For every nonnegative integer \(n\), using the standard modified-Bessel integral and the explicit half-integer expansion,
\[
 \mathbb E[A^n\mid Y=y]=\frac{P_n(z)}{(2r)^n},\quad
 P_n(z)=\sum_{k=0}^n\frac{(n+k)!}{k!(n-k)!2^k}z^{n-k}.
\]
The identity extends continuously through \(y=0\), where the posterior age is Gamma with shape \(1/2\) and rate \(r\). In particular
\[
 P_1=z+1,\quad P_2=z^2+3z+3,\quad P_3=z^3+6z^2+15z+15,
\]
so \(\operatorname{Var}(A\mid Y=y)=(z+2)/(4r^2)\). Total conditional expectation now yields the first boxed identity. Total conditional variance gives
\[
 \begin{aligned}
 \operatorname{Var}(X\mid Y=y)&=2D\,\mathbb E[A\mid Y=y]+\frac{Dg^2}{6}\mathbb E[A^3\mid Y=y]\\
 &\quad+\frac{g^2y^2}{4}\operatorname{Var}(A\mid Y=y).
 \end{aligned}
\]
Using \(y^2=z^2D/r\) and the three polynomials yields the second boxed identity. Since the coefficients of each positive power of \(z\) in this variance are positive (and the linear diffusion term is always positive), it increases strictly with \(|y|\). The highest terms are
\[
 \mathbb E[X\mid Y=y]\sim \frac{g}{4\sqrt{Dr}}y|y|,
 \qquad \operatorname{Var}(X\mid Y=y)\sim\frac{g^2}{12\sqrt D\,r^{3/2}}|y|^3
\]
for fixed \(g\ne0\), \(D\) and \(r\), as \(|y|\to\infty\). Because the age posterior and the conditional normal law are explicit, all conditional moments follow by Gaussian-moment expansion and the displayed \(P_n\) formula.

## Verification
Execute `python verify.py` with Python 3, SymPy and SciPy. It verifies symbolic polynomial identities, recovers the published global stationary covariance \(\operatorname{Cov}(X,Y)=2Dg/r^2\) and global horizontal variance \(\operatorname{Var}(X)=2D/r+4Dg^2/r^3\), then independently integrates 45 conditional age moments and compares 15 conditional mean-variance pairs across three parameter sets. The numerical integrals are checks of a proved analytic formula, not its proof. For the global comparisons, use that \(z=|Y|\sqrt{r/D}\) is Exp(1), hence \(\mathbb E[z^n]=n!\).

## Relationship to prior work
Abdoli, Olsen and Löwen (arXiv:2410.10333v1) established the shear-reset model, exact reset-free Gaussian propagation, the stationary renewal integral, unconditional covariances, skewness and kurtosis, and a perturbative stationary joint density. Their exact joint renewal representation is the starting point, not a novelty claim. The result here performs the distinct conditional Gaussian-bridge/Bessel calculation to determine the previously implicit fiberwise regression, variance, and full conditional age-moment hierarchy. Those closed conditional polynomial laws and their sharp quadratic/cubic far-field profiles were not located in the inspected primary text. The elementary Brownian-bridge and Bessel identities are standard, not claimed as new.

## Limitations
This is an exact population-distribution result; no finite-observation inferential bounds are proved. The formulas rely on simultaneous resetting of both coordinates, isotropic independent Brownian noises and linear shear. The general joint renewal integral in the source mathematically contains the conditional laws implicitly, and an unlocated broader conditional-mixture result might imply the stated specialization; priority beyond the checked sources is not certified. For \(g=0\) the cubic term disappears, though the conditional variance still grows linearly with \(|y|\).

## References
1. I. Abdoli, K. S. Olsen, H. Löwen, *Shear-Driven Diffusion with Stochastic Resetting*, arXiv:2410.10333v1 (first public 2024-10-14), https://arxiv.org/html/2410.10333v1; especially sections II–III, Appendix A–B.
2. K. S. Olsen, H. Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039v1 (2024-06-14), https://arxiv.org/html/2406.10039v1; a different protocol without the same shear-conditioned law.
3. M. R. Evans, S. N. Majumdar, *Diffusion with stochastic resetting*, Phys. Rev. Lett. 106, 160601 (2011); background stationary renewal principle as referenced in [1].
