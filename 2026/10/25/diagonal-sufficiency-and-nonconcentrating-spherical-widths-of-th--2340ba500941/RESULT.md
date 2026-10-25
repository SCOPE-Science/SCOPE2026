# Diagonal sufficiency and nonconcentrating spherical widths of the White Whale zonotope

## Finding
For each integer \(d\ge 2\), let the *White Whale* be the full-dimensional Euclidean zonotope
\[
\mathcal W_d=\sum_{b\in\{0,1\}^{d}\setminus\{0\}}[0,b]\subset\mathbb R^d.
\]
Its full Euclidean width in a unit direction \(u\in S^{d-1}\) is denoted by \(w_d(u)\). Define the normalized width, diagonal projection, and profile
\[
X_d(u)=2^{-d}w_d(u),\qquad T_d(u)=\sum_{i=1}^d u_i,
\]
\[
F(t)=\frac12\mathbb E|t+Z|=\frac{e^{-t^2/2}}{\sqrt{2\pi}}+t\left(\Phi(t)-\frac12\right),\qquad Z\sim N(0,1).
\]
The following statements form one asymptotic Euclidean-width theorem.

**Deterministic diagonal reduction.** There is an absolute constant \(C<\infty\) such that, for all \(d\ge2\) and unit vectors \(u\),
\[
\left|X_d(u)-F(T_d(u))\right|\le C\left(\sum_{i=1}^d|u_i|^3\right)^{1/3}.
\]
In particular, for any sequence of unit directions with \(\max_i|u_i|\to0\), the width error tends to zero, even if the diagonal projection has no limit.

**Spherical distribution and moments.** If \(U_d\) is Haar-uniform on \(S^{d-1}\), then, for every fixed \(p>0\),
\[
\mathbb E\left|X_d(U_d)-F(T_d(U_d))\right|^p\longrightarrow0,
\qquad X_d(U_d)\ \Longrightarrow\ F(Z).
\]
All positive moments of \(X_d(U_d)\) converge to those of \(F(Z)\). The limit is nonconstant, non-Gaussian, and supported on \([1/\sqrt{2\pi},\infty)\), with
\[
\boxed{\mathbb EF(Z)=\frac1{\sqrt\pi},\qquad
\operatorname{Var}(F(Z))=\frac1{12}+\frac{\sqrt3-2}{2\pi}>0.}
\]
Indeed \(F\) is even and strictly increasing in \(|t|>0\), so for \(x\ge1/\sqrt{2\pi}\) its exact distribution function is \(2\Phi(F^{-1}_{+}(x))-1\), where \(F^{-1}_{+}\) denotes the inverse of \(F\) restricted to \([0,\infty)\).

**Sharp mean correction.** The spherical mean obeys
\[
\boxed{\mathbb E X_d(U_d)=\frac1{\sqrt\pi}\left(1+\frac1{8d}+O(d^{-2})\right).}
\]
Thus the number of segment generators is exponential in the ambient dimension, yet the normalized directional width retains a strictly positive limiting variance; moreover, its entire leading fluctuation is asymptotically determined by the single diagonal projection \(T_d\).

## Assumptions and scope
The Euclidean structure is the original ambient Euclidean metric on \(\mathbb R^d\); no affine renormalization, intrinsic quotient, or stochastic change of generator lengths is made. Each nonzero Boolean vector occurs once as a segment generator. Width is the distance between opposite supporting hyperplanes; it is unaffected by translating the zonotope from the original convention \([0,b]\) to its centrally symmetric translate. The statements concern deterministic unit directions or Haar-uniform random unit directions and the limit \(d\to\infty\). All limits of moments refer to ordinary nonnegative real powers; no assertion concerns the distribution of individual normal-cone angles or finite-dimensional vertex counts.

## Proof
**1. Exact support identity.** Since the support function is additive under Minkowski summation,
\[
h_{\mathcal W_d}(u)=\sum_{b\ne0}\max(0,u\cdot b),\qquad
w_d(u)=\sum_{b\in\{0,1\}^d}|u\cdot b|.
\]
Let \(\varepsilon_1,\ldots,\varepsilon_d\) be independent symmetric signs. The substitution \(b_i=(1+\varepsilon_i)/2\) gives the exact identity
\[
X_d(u)=\frac12\,\mathbb E_{\varepsilon}\left|T_d(u)+\sum_{i=1}^d\varepsilon_i u_i\right|.
\]
The zero Boolean vector contributes zero, so its inclusion in the average causes no change.

**2. Uniform conditional Gaussian replacement.** Fix any unit vector \(u\), and write \(S_u=\sum_i\varepsilon_i u_i\). Independent standard Gaussian variables \(G_i\) give \(\sum_iG_i u_i\sim N(0,1)\). For fixed \(t\), set \(g_t(y)=|t+y|/2\) and let \(g_{t,\delta}\) denote its convolution with a centered Gaussian density of standard deviation \(\delta>0\). The Lipschitz constant of \(g_t\) is \(1/2\), so
\[
\|g_t-g_{t,\delta}\|_\infty\le\frac\delta2\mathbb E|G_1|.
\]
The weak derivative \(g_t'\) is bounded by \(1/2\). Moving two derivatives onto the smoothing density yields \(\|g_{t,\delta}'''\|_\infty\le C_0\delta^{-2}\), uniformly in \(t\). Replace the sign summands \(\varepsilon_i u_i\) by Gaussian summands \(G_i u_i\) one at a time. The means and variances match, and third-order Taylor remainder bounds each replacement by
\[
C_1\delta^{-2}|u_i|^3\bigl(\mathbb E|\varepsilon_i|^3+\mathbb E|G_i|^3\bigr).
\]
Consequently, uniformly in \(t\) and \(u\),
\[
\left|\mathbb E g_t(S_u)-\mathbb E g_t(G_1)\right|
\le C_2\left(\delta+\delta^{-2}\sum_i|u_i|^3\right).
\]
Taking \(\delta=(\sum_i|u_i|^3)^{1/3}\) proves the deterministic bound, including its universal constant. The choice is valid because a unit vector has a positive sum of absolute cubes. Since \(\sum_i|u_i|^3\le\max_i|u_i|\), the claimed deterministic consequence follows.

**3. Random-direction limit and integrability.** Realize \(U_d=(G_1,\ldots,G_d)/(\sum_iG_i^2)^{1/2}\) with independent standard Gaussians. Gaussian tails and the law of large numbers imply \(\max_i|U_{d,i}|\to0\) in probability. Hence the bound from Step 2 gives \(X_d(U_d)-F(T_d(U_d))\to0\) in probability. Moreover,
\[
|X_d(u)-F(T_d(u))|\le\tfrac12(\mathbb E|S_u|+\mathbb E|G_1|)
\le\tfrac12(1+\sqrt{2/\pi}),
\]
so this convergence holds in \(L^p\) for every fixed \(p>0\).

Writing \(T_d(U_d)=(d^{-1/2}\sum_iG_i)/(d^{-1}\sum_iG_i^2)^{1/2}\), the numerator is exactly standard normal and the denominator tends in probability to one. Slutsky's theorem yields \(T_d(U_d)\Rightarrow Z\), and continuity of \(F\) proves \(X_d(U_d)\Rightarrow F(Z)\).

For every positive integer \(k\), spherical rotational symmetry gives
\[
\mathbb E|T_d(U_d)|^{2k}
=\frac{d^k(2k-1)!!}{d(d+2)\cdots(d+2k-2)}\le(2k-1)!!.
\]
Also \(X_d(u)\le (|T_d(u)|+1)/2\), by the sign representation and Cauchy--Schwarz. Thus the required arbitrarily high moments are uniformly bounded, proving convergence of every positive moment.

**4. Exact first limiting moments.** With independent standard normals \(Z,H,H_1,H_2\),
\[
\mathbb EF(Z)=\tfrac12\mathbb E|Z+H|=\pi^{-1/2}.
\]
For \(A=(Z+H_1)/\sqrt2\) and \(B=(Z+H_2)/\sqrt2\), their variances are one and their correlation is \(1/2\). The elementary bivariate normal identity
\[
\mathbb E|A||B|=\frac2\pi\left(\sqrt{1-\rho^2}+\rho\arcsin\rho\right)
\]
can be obtained by differentiating in \(\rho\), using Gaussian integration by parts and the sign-correlation formula \(\mathbb E[\operatorname{sgn}A\operatorname{sgn}B]=2\arcsin\rho/\pi\), then integrating from \(\rho=0\), where the absolute-product expectation is \(2/\pi\). Therefore
\[
\mathbb EF(Z)^2=\tfrac14\mathbb E|Z+H_1||Z+H_2|
=\frac{\sqrt3}{2\pi}+\frac1{12},
\]
which gives the stated variance after subtracting \(1/\pi\). Differentiation of the closed form shows \(F'(t)=\Phi(t)-1/2\), so \(F\) has a unique minimum \(F(0)=1/\sqrt{2\pi}\) and diverges with \(|t|\). This proves the support and distribution-function assertions.

**5. Mean-width correction.** Rotational invariance gives, for a fixed Boolean vector with \(k\) ones,
\[
\mathbb E|U_d\cdot b|=\sqrt{k}\,\mu_d,\qquad
\mu_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)}.
\]
Summing the \(\binom dk\) Boolean vectors with \(k\) ones gives the exact finite identity
\[
\mathbb E X_d(U_d)=\frac{\mu_d}{2^d}\sum_{k=1}^d\binom dk\sqrt k
=\mu_d\,\mathbb E\sqrt K,\qquad K\sim\operatorname{Bin}(d,1/2).
\]
The Gamma-ratio expansion and a Taylor expansion about \(\mathbb EK=d/2\) yield, respectively,
\[
\mu_d=\sqrt{\frac2{\pi d}}\left(1+\frac1{4d}+O(d^{-2})\right),\qquad
\mathbb E\sqrt K=\sqrt{\frac d2}\left(1-\frac1{8d}+O(d^{-2})\right).
\]
For the latter, the centered binomial third moment vanishes, the fourth moment is \(O(d^2)\), and the lower-tail event \(K<d/4\) has exponentially small probability; a fourth-order Taylor expansion on its complement gives the stated remainder. Multiplication completes the expansion.

## Verification
An accompanying standard-library Python checker enumerates all Boolean generators directly and, in dimensions \(2\), \(3\), and \(4\), independently enumerates **every vertex of the generator coefficient cube** to compare full zonotope widths in 42 sampled directions. All 42 comparisons passed. Additional exact finite-dimensional first and second spherical moment computations use the binomial and four-cell multinomial formulas, not simulation. Their variances at dimensions \(8\), \(16\), \(32\), and \(64\) are approximately \(0.0310139\), \(0.0357622\), \(0.0382111\), and \(0.0394468\), tending toward the proved limit \(0.04068789486\). Further finite simulations inspect the deterministic profile approximation, and balanced-sign unit directions show convergence toward \(F(0)\). Reproduce with `python3 white_whale_checker.py`; the saved output is `white_whale_checker.log`. Numerical checks are finite corroboration only. The proofs of the all-dimensional statements are the analytic arguments above.

## Relationship to prior work
Deza, Hao and Pournin's 2022 first-public preprint defines this full Boolean-subset zonotope and studies its exponential-size vertex set, orbitwise enumeration, resonance hyperplane arrangement, edge counts, and special vertex degrees. These combinatorial results establish the object but do not furnish its random Euclidean directional-width law. Stinson, Gleich and Constantine study Gaussian sampling of exposed zonotope vertices and their normal cones for general generator matrices; their results do not imply the one-dimensional limit profile or its variance for this particular Boolean-subset generator matrix. General zonotope support additivity and Gaussian central limit arguments are standard proof ingredients and are not claimed as new.

A related complete-bipartite *graphical* zonotope with one small color class has a limiting profile proportional to \(\mathbb E|t-Z|\). The profile coincidence is acknowledged; the White Whale has \(2^d-1\) Boolean-subset generators in dimension \(d\), rather than edge-difference generators of a graph. Neither the geometry nor its Haar normalization is identified by the graphical result, and the explicit diagonal approximation for the White Whale requires the separate proof above. This work does not claim the folded-Gaussian profile as an entirely new probability distribution; it claims its proved realization and moment behavior for the specified zonotope family.

## Limitations
The limit is for full directional width and its moments, not Hausdorff convergence of normalized convex bodies, not angular normal-cone measures for individual vertices, and not a solution of the resonance-arrangement chamber-count problem. The deterministic error rate is deliberately nonoptimal. No independent mathematical audit has been performed. A semantically equivalent geometric width theorem could exist in unindexed literature despite the targeted searches recorded separately in the review materials.

## References
1. A. Deza, M. Hao, L. Pournin, *Sizing the White Whale*, first public preprint 2022-05-26, arXiv:2205.13309v1, https://arxiv.org/abs/2205.13309. Consulted full primary preprint, especially Sections 1--5 and their propositions and tables.
2. K. Stinson, D. F. Gleich, P. G. Constantine, *A randomized algorithm for enumerating zonotope vertices*, first preprint 2016-02-22, arXiv:1602.06620v1, https://arxiv.org/abs/1602.06620. Consulted Sections 1--3 and the statements about Gaussian normal-cone probabilities.
3. A. Deza, L. Pournin, N. Sukegawa, *The diameter of lattice zonotopes*, arXiv:1905.04750, https://arxiv.org/abs/1905.04750. Its accessible abstract concerns lattice-zonotope diameters, not spherical-width distributions; the full text was not used for a noncoverage claim.
