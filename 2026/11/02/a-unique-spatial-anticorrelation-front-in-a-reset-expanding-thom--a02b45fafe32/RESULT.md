# A unique spatial anticorrelation front in a reset-expanding Thomas–Fermi condensate

## Finding

In the one-dimensional, large-particle-number Thomas–Fermi hydrodynamic expansion subject to independent Poisson returns to the initial condensate, the *reset-age-induced covariance of the macroscopic density at the cloud center and at a point* changes sign at exactly one positive distance. This is a statement about run-to-run fluctuations of the deterministic mean-field density evaluated at a random stationary reset age, not about microscopic quantum density fluctuations.

Specifically, let \(x_0>0\) be the initial Thomas–Fermi edge, \(\omega>0\) the initial longitudinal trap frequency and \(r>0\) the resetting rate. There exists a unique \(z_*(r,\omega)>0\) such that, for a stationary reset-age realization of the density field \(\mathcal R(x)\),

\[
\operatorname{Cov}(\mathcal R(0),\mathcal R(x))
\begin{cases}
>0,&0\le |x|<x_0z_*,\\
=0,&|x|=x_0z_*,\\
<0,&|x|>x_0z_*.
\end{cases}
\]

The front location has two sharply different resetting limits. With the dimensionless resetting rate \(\alpha=r/(\sqrt2\,\omega)\),

\[
 z_*(r,\omega)=\frac1{\sqrt3}+O(\alpha^{-2})
 \quad(\alpha\to\infty),
\]

while, writing \(L=\log(1/\alpha)\),

\[
\boxed{\quad z_*(r,\omega)\sim\frac{2}{3\alpha L\log L}
\quad(\alpha\downarrow0).\quad}
\]

Thus fast resetting places the unique covariance sign reversal *inside* the initial Thomas–Fermi edge, near \(x_0/\sqrt3\); slow resetting displaces it parametrically *outside* that edge, with a sharp double-logarithmic correction.

## Assumptions and scope

Take the normalized initial Thomas–Fermi profile

\[
\rho_0(x)=\frac{3}{4x_0}\bigl(1-(x/x_0)^2\bigr)_+,
\quad u_+=\max\{u,0\}.
\]

In the hydrodynamic approximation, free expansion from this profile is self-similar:

\[
\rho(x,t)=\frac{3}{4x_0\lambda(t)}
\left(1-\frac{x^2}{x_0^2\lambda(t)^2}\right)_+,
\]

where \(\lambda\) is the unique solution of

\[
\lambda''(t)=\frac{\omega^2}{\lambda(t)^2},\qquad
\lambda(0)=1,\qquad\lambda'(0)=0.
\]

The condensate is returned to this complete initial profile at independent Poisson times of rate \(r\). At a stationary observation time the elapsed time \(T\) since the last return is exponentially distributed with rate \(r\). Define the random *macroscopic profile* \(\mathcal R(x)=\rho(x,T)\). All covariances below are with respect to \(T\) alone, at fixed \(x\), after taking the Thomas–Fermi hydrodynamic approximation; no finite-particle or quantum connected-correlation assertion is made.

Introduce the bounded random variable \(U=1/\lambda(T)\in(0,1)\), and for \(z\ge0\) set \(B_z(u)=u(1-z^2u^2)_+\). Then

\[
\mathcal R(0)=\frac{3U}{4x_0},\qquad
\mathcal R(x_0z)=\frac{3B_z(U)}{4x_0}.
\]

Write \(m=\mathbb E[U]\). The unique front is characterized by

\[
\frac{\mathbb E[U B_{z_*}(U)]}{\mathbb E[B_{z_*}(U)]}=m.
\tag{1}
\]

Both expectations in the left-hand ratio are finite, with strictly positive denominator for every finite \(z\). Their integral representations below give a reproducible one-variable determination of the front without simulated particles.

## Proof

**1. Reset-age law and integral representation.** Multiplying the expansion equation by \(\lambda'\) and using the initial data gives

\[
\lambda'(t)=\sqrt2\,\omega\sqrt{1-1/\lambda(t)}.
\]

Thus \(\lambda(t)\) is strictly increasing for \(t>0\), tends to infinity and is inverted by

\[
\sqrt2\,\omega\,t=F(\lambda):=\sqrt{\lambda(\lambda-1)}+
\operatorname{arsinh}\sqrt{\lambda-1},\qquad \lambda\ge1.
\]

As \(F'(\lambda)=\sqrt{\lambda/(\lambda-1)}\), the random expansion factor has density

\[
 h_\alpha(\lambda)=\alpha e^{-\alpha F(\lambda)}F'(\lambda),
 \qquad \lambda>1,\qquad \alpha=\frac{r}{\sqrt2\,\omega}.
\tag{2}
\]

This is normalized since \(F\) maps \([1,\infty)\) onto \([0,\infty)\). In particular, the law of \(U\) has a strictly positive density throughout \((0,1)\). For any bounded measurable \(g\), \(\mathbb E[g(U)]=\int_1^\infty h_\alpha(\lambda)g(1/\lambda)\,d\lambda\). Set

\[
I_1(z)=\mathbb E[B_z(U)]
=\alpha\int_{\max(1,z)}^\infty e^{-\alpha F(\lambda)}F'(\lambda)
\left(\frac1\lambda-\frac{z^2}{\lambda^3}\right)d\lambda,
\]

\[
I_2(z)=\mathbb E[U B_z(U)]
=\alpha\int_{\max(1,z)}^\infty e^{-\alpha F(\lambda)}F'(\lambda)
\left(\frac1{\lambda^2}-\frac{z^2}{\lambda^4}\right)d\lambda.
\tag{3}
\]

**2. Strictly ordered weighted means.** Put \(q(z)=I_2(z)/I_1(z)\). This is the mean of \(U\) under the probability law obtained by weighting its density with \(B_z(U)\). For \(0\le z_1<z_2\), the ratio of the two unnormalized weights, wherever the later weight is positive, is

\[
\frac{B_{z_2}(u)}{B_{z_1}(u)}
=\frac{1-z_2^2u^2}{1-z_1^2u^2}.
\]

It is strictly decreasing in \(u>0\) when \(z_2>z_1\); if the support shrinks, all deleted mass is at the larger values of \(u\). Hence the family of weighted laws is strictly ordered in the monotone-likelihood-ratio order. One direct verification uses two independent copies \(U_1,U_2\) under the \(z_1\)-weighted law: the covariance of the increasing function \(u\) and the decreasing likelihood ratio is strictly negative because its symmetric double-integral integrand is \(\frac12(u-v)(R(u)-R(v))<0\) on a set of positive product measure. This proves

\[
q(z_2)<q(z_1).
\tag{4}
\]

Dominated convergence makes \(q\) continuous, because \(0\le B_z(U)\le U\le1\) and \(I_1(z)>0\) for every finite \(z\). At zero,

\[
q(0)=\frac{\mathbb E[U^2]}{\mathbb E[U]}
=m+\frac{\operatorname{Var}(U)}m>m,
\]

as the reset age is nondegenerate. At large \(z\), \(B_z(U)>0\) forces \(U<1/z\), so \(0<q(z)\le1/z\to0<m\). By continuity and (4), there is exactly one positive solution of (1). Finally,

\[
\operatorname{Cov}(\mathcal R(0),\mathcal R(x_0z))
=\left(\frac3{4x_0}\right)^2 I_1(z)\bigl(q(z)-m\bigr).
\tag{5}
\]

Equation (5) proves all three covariance signs and their strictness.

**3. Fast resetting.** If \(z\le1\), no positive-part cutoff is active, so (5) gives the *exact* polynomial relation

\[
\operatorname{Cov}(U,B_z(U))
=\operatorname{Var}(U)-z^2\operatorname{Cov}(U,U^3).
\tag{6}
\]

Here \(\operatorname{Cov}(U,U^3)>0\) by strict monotonicity of the two functions and nondegeneracy. With \(T\sim\operatorname{Exp}(r)\), the short-age expansion is

\[
U=1-\tfrac12\omega^2T^2+O(\omega^4T^4).
\]

Exponential tails permit this expansion inside moments as \(r/\omega\to\infty\). Using \(\mathbb E[T^2]=2/r^2\), \(\mathbb E[T^4]=24/r^4\) and \(\operatorname{Var}(T^2)=20/r^4\),

\[
\operatorname{Var}(U)=\frac{5\omega^4}{r^4}+O\left(\frac{\omega^6}{r^6}\right),
\qquad
\operatorname{Cov}(U,U^3)=\frac{15\omega^4}{r^4}+O\left(\frac{\omega^6}{r^6}\right).
\]

Their ratio tends to \(1/3\), so the unique root eventually lies in \((0,1)\) and (6) yields

\[
z_*^2=\frac{\operatorname{Var}(U)}{\operatorname{Cov}(U,U^3)}
=\frac13+O(\alpha^{-2}),
\quad z_*=\frac1{\sqrt3}+O(\alpha^{-2}).
\tag{7}
\]

**4. Slow resetting and the doubly logarithmic front.** Let \(\alpha\downarrow0\), \(L=\log(1/\alpha)\). The exact expansion-clock function satisfies

\[
F(\lambda)=\lambda+\tfrac12\log\lambda+O(1),
\qquad F'(\lambda)=1+O(\lambda^{-1})
\quad(\lambda\to\infty).
\tag{8}
\]

Splitting the integral at \(\lambda=1/\alpha\), with the exponential damping above that scale, establishes

\[
m=\alpha\int_1^\infty e^{-\alpha F(\lambda)}\frac{F'(\lambda)}\lambda d\lambda
=\alpha\bigl(L+O(1)\bigr).
\tag{9}
\]

For arbitrary fixed \(k>0\), take the test distance

\[
z_k=\frac{k}{\alpha L\log L}.
\]

Then \(z_k\to\infty\), \(\alpha z_k\to0\), and \(\log(1/(\alpha z_k))=\log L+\log\log L-\log k\sim\log L\). Using (8) in (3), the logarithmic range \(z_k\ll\lambda\ll1/\alpha\) gives

\[
I_1(z_k)=\alpha\left(\log\frac1{\alpha z_k}+O(1)\right)
\sim\alpha\log L.
\tag{10}
\]

For the numerator, changing to \(\lambda=z_ku\) and applying dominated convergence to the integrable function \(u^{-2}-u^{-4}\) gives

\[
I_2(z_k)\sim\frac\alpha{z_k}
\int_1^\infty(u^{-2}-u^{-4})du
=\frac{2\alpha}{3z_k}.
\tag{11}
\]

Combining (9)–(11),

\[
\frac{q(z_k)}m\longrightarrow\frac2{3k}.
\tag{12}
\]

For any fixed \(k_-<2/3<k_+\), (12) shows \(q(z_{k_-})>m>q(z_{k_+})\) for all sufficiently small \(\alpha\). By the already-proved strict decrease of \(q\), \(z_{k_-}<z_*<z_{k_+}\). Letting the bracket constants tend to \(2/3\) proves

\[
\boxed{z_*\sim\frac2{3\alpha\log(1/\alpha)\log\log(1/\alpha)}}.
\]

This also proves that the front escapes every fixed multiple of the original edge as resetting becomes slow.

## Verification

The accompanying `verify.py` performs independent quadrature in expansion-scale and exponential-reset-age variables, verifies normalization and moment identities, locates the unique zero numerically, checks strictly decreasing weighted means on finite grids, and compares the two limiting regimes. It was executed against the actual packaged script and returned 454 passed deterministic checks. These finite computations are **not** substitutes for the strict monotone-likelihood-ratio argument or the asymptotic analysis.

To reproduce in an environment with Python 3 and the dependency in `requirements.txt`, run `python verify.py` from the directory containing this document. The integrands are written explicitly in equations (2)–(3), and no external datasets, unpublished computations or missing files are required.

## Relationship to prior work

Mesquita, Kulkarni, Majumdar and Sabhapandit establish the hydrodynamic Thomas–Fermi expansion, its exact reset-age scale law and the resulting averaged density, edge distribution and counting statistics [1]. Their equations (28), (35), (37), (41), (48), (51), and (63)–(69) supply the underlying random-profile construction. Those ingredients are *not* claimed as new. The assessed result is the all-distance unique **sign threshold** of the local macroscopic density covariance and its sharply distinct fast- and slow-reset asymptotics, especially the double logarithm; these statements require comparison of tilted densities and a singular two-scale analysis and were not identified in the inspected original main text or appendices.

De Mauro, Biroli, Majumdar and Schehr analyze non-Poissonian common resetting in an independent Brownian gas [2]. Biroli, Larralde, Majumdar and Schehr analyze mean densities and spatial order statistics of an independently diffusing resetting gas [3]. Their conditional-mixture methodology is relevant, but their Brownian single-particle profiles and observables do not assert the present Thomas–Fermi density-covariance front. General monotone-likelihood-ratio comparisons explain the uniqueness mechanism once the particular weighted family is identified; the scale \(1/(\alpha\log(1/\alpha)\log\log(1/\alpha))\) also uses the specific ballistic expansion-clock tail.

## Limitations

This is a theorem within the self-similar, large-particle-number Thomas–Fermi hydrodynamic description and Poisson resetting. It concerns covariance of the **macroscopic mean-field density across independent reset ages**, not finite-particle quantum connected density correlation or shot-noise fluctuations. The limit \(\alpha\downarrow0\) is taken *after* adopting that hydrodynamic model; a finite-particle condensate may leave its domain of validity at very late ages. No claim is made for finite resetting return durations, non-Poisson clocks, non-self-similar initial profiles, nonzero post-reset velocity, or a full joint distribution of microscopic density observations. Numerical quadrature alone cannot prove uniqueness, monotonicity in reset rate, or the sharp asymptotics; only the statements proved above are claimed. In particular, no global monotonicity of \(z_*\) as a function of \(r\) is asserted.

## References

[1] N. Mesquita, M. Kulkarni, S. N. Majumdar and S. Sabhapandit, *Weakly interacting Bose-Einstein condensate with stochastic resetting*, arXiv:2609.37110v1, first publicly submitted 2026-09-29. Full text: https://pdfs.assets.alphaxiv.org/2609.37110v1.pdf ; record: https://arxiv.org/abs/2609.37110 .

[2] G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658v2, first public 2025-09-08, https://arxiv.org/abs/2509.06658 .

[3] M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme Statistics and Spacing Distribution in a Brownian Gas Correlated by Resetting*, Physical Review Letters 130, 207101 (2023), DOI 10.1103/PhysRevLett.130.207101, https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.130.207101 .
