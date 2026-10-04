# A quantitative energy-score bottleneck for Lipschitz distributional reduction
## Finding
Let \(p\ge 2\), \(R>0\), and \(1\le q<p\). Let \(X\) be uniform on the Euclidean sphere \(S_R^{p-1}\). Let \(Z\sim\mu\) be independent of \(X\), assume \(\mathbb E\|Z\|<\infty\), and define the conditional response law
\[
P_x=\operatorname{Law}(x+Z).
\]
For probability laws with finite first moment, write the Euclidean energy distance as
\[
\mathcal D^2(P,Q)=2\mathbb E\|U-V\|-\mathbb E\|U-U'\|-\mathbb E\|V-V'\|,
\]
with \(U,U'\) independent from \(P\) and \(V,V'\) independent from \(Q\). Define
\[
\Delta_\mu(R)=\inf_{\|u\|=1}\mathcal D^2(P_{Ru},P_{-Ru}).
\]
Then \(0<\Delta_\mu(R)\le 4R\).

Let \(e:S_R^{p-1}\to\mathbb R^q\) be \(L_e\)-Lipschitz. Let the predictive generator have fixed independent noise \(\eta\) and output \(d(e(x),\eta)\), where for every noise value the map in the encoded coordinate obeys
\[
\|d(z,\eta)-d(z',\eta)\|\le L_d\|z-z'\|.
\]
Let \(Q_x\) be the generated law. For the population energy score, define the regret
\[
\mathfrak r(Q;P)=\mathbb E_{Y\sim P}\!\left[\operatorname{ES}(Q,Y)\right]-\mathbb E_{Y\sim P}\!\left[\operatorname{ES}(P,Y)\right]=\frac12\mathcal D^2(P,Q).
\]
If
\[
C_p(t)=\frac12 I_{t^2-t^4/4}\!\left(\frac{p-1}{2},\frac12\right),
\]
denotes the normalized mass of a spherical cap of chord radius \(tR\), then
\[
\boxed{\quad
\mathbb E\,\mathfrak r(Q_X;P_X)
\ge
\frac{\Delta_\mu(R)}{16}\,
C_p\!\left(\frac{\Delta_\mu(R)}{16R(1+2L_eL_d)}\right).
\quad}
\]
The lower bound is strictly positive for every finite \(L_eL_d\).

For the noiseless special case \(\mu=\delta_0\), one has \(\Delta_\mu(R)=4R\), hence
\[
\mathbb E\,\mathfrak r(Q_X;P_X)
\ge
\frac R4 C_p\!\left(\frac{1}{4(1+2L_eL_d)}\right).
\]
Since
\[
C_p(t)\sim
\frac{\Gamma(p/2)}{(p-1)\sqrt\pi\,\Gamma((p-1)/2)}\,t^{p-1}
\qquad (t\downarrow0),
\]
any sequence of such subambient bottlenecks whose population energy-score regret tends to zero on a fixed translation model must have \(L_eL_d\to\infty\); the displayed bound decays with exact order \((1+2L_eL_d)^{-(p-1)}\).

## Assumptions and scope
The result concerns a full-dimensional translation regression family indexed by a sphere. The response noise may be arbitrary with finite first moment; bounded noise, as used in common consistency assumptions for generative distributional regression, is included. The encoder is required to be Lipschitz, and the generator must be uniformly Lipschitz only in the encoded argument. No density, differentiability, injectivity, or parametric assumption is imposed on \(\mu\).

The statement is a population lower bound for the energy-score objective. It does not assert that every regression problem needs \(p\) latent coordinates. It applies when distinct covariates index distinct translated conditional laws over the whole sphere. Problems whose conditional law genuinely factors through a lower-dimensional feature are outside the obstruction.

## Proof
For a probability law \(P\), the population energy-score regret equals one half of squared energy distance:
\[
\mathfrak r(Q;P)=\frac12\mathcal D^2(P,Q).
\]
The quantity \(\mathcal D\) is a metric on probability laws with finite first moment.

First, \(\Delta_\mu(R)>0\). For every unit vector \(u\), the two laws \(P_{Ru}\) and \(P_{-Ru}\) differ, because a finite probability measure on \(\mathbb R^p\) cannot be invariant under a nonzero translation. Energy distance vanishes only for equal laws. Moreover, the map \(u\mapsto\mathcal D^2(P_{Ru},P_{-Ru})\) is continuous: using independent \(Z,Z'\sim\mu\),
\[
\mathcal D^2(P_{Ru},P_{-Ru})
=2\mathbb E\!\left[\|Z-Z'+2Ru\|-\|Z-Z'\|\right],
\]
and the integrand is Lipschitz in \(u\). Compactness of the unit sphere gives a positive minimum. The same identity and the triangle inequality give \(\Delta_\mu(R)\le4R\).

Because \(q<p\), the Borsuk--Ulam theorem applied to the restriction of \(e\) to \(S_R^{p-1}\) gives an antipodal pair \(x,-x\) with
\[
e(x)=e(-x).
\]
The two predictive laws at this pair therefore coincide; call the common law \(Q\). By the triangle inequality for \(\mathcal D\),
\[
\mathcal D(P_x,P_{-x})
\le
\mathcal D(P_x,Q)+\mathcal D(Q,P_{-x}).
\]
Hence one endpoint, denoted \(x_*\), satisfies
\[
\mathfrak r(Q;P_{x_*})\ge\frac{\Delta_\mu(R)}8.
\]
This is the topological collision. The next step turns the single collision into positive population risk.

Couple the generated laws at \(z,x_*\) using the same generator noise. Then
\[
W_1(Q_z,Q_{x_*})\le L_eL_d\|z-x_*\|.
\]
The within-target term in the energy score is translation invariant. Coupling the cross term and the two generated copies gives
\[
\left|\mathfrak r(Q_z;P_z)-\mathfrak r(Q_{x_*};P_{x_*})\right|
\le
(1+2L_eL_d)\|z-x_*\|.
\]
Put \(M=1+2L_eL_d\) and
\[
\rho=\frac{\Delta_\mu(R)}{16M}.
\]
Since \(\Delta_\mu(R)\le4R\), one has \(\rho/R\le1/4\). Every point in the spherical cap \(\|z-x_*\|\le\rho\) therefore has
\[
\mathfrak r(Q_z;P_z)\ge\frac{\Delta_\mu(R)}{16}.
\]
The normalized surface measure of that cap is
\[
C_p(\rho/R)
=
\frac12 I_{(\rho/R)^2-(\rho/R)^4/4}\!\left(\frac{p-1}{2},\frac12\right).
\]
Integrating the pointwise lower bound over the cap proves the displayed inequality.

The noiseless specialization follows because the energy distance between \(\delta_x\) and \(\delta_{-x}\) has squared value \(4R\). The small-cap expansion follows from the standard beta-function expansion at zero and yields the stated necessary growth of \(L_eL_d\).

## Verification
The proof was replayed from the definitions with four independent checks. First, the translation identity for \(\mathcal D^2\) was expanded directly and its upper bound \(4R\) verified from the Euclidean triangle inequality. Second, the antipodal collision was checked against the exact dimension condition \(q\le p-1\) required by Borsuk--Ulam. Third, the energy-score regret Lipschitz estimate was reconstructed term by term: one copy of \(W_1\) comes from the target-versus-predictive cross term and one from the predictive self-distance term, giving \(1+2L_eL_d\). Fourth, the spherical-cap formula was checked from the first-coordinate density of the uniform sphere and gives the small-cap exponent \(p-1\).

No finite simulation or numerical enumeration is used as evidence for the theorem. The argument is analytic; the beta-function expression only evaluates the exact measure of the cap generated by the proof.

## Relationship to prior work
Henzi, Liu, and Shen prove in Lemma 3 of *Sufficiently Reduced Distributional Regression* that arbitrary measurable reductions can be compressed even to one real coordinate through Borel isomorphisms. The same paper immediately notes that smoothness restrictions rule out arbitrary reduced dimensions, imposes Lipschitz assumptions on the reduction and generator for its consistency theory, and leaves selection of the reduced dimension outside that theory. The present result supplies a quantitative population-risk obstruction in a canonical translation family: below ambient dimension, vanishing energy-score regret is impossible at bounded encoder--generator Lipschitz product.

The concurrent Belted Engression work assumes a low-dimensional sufficient predictor together with regularity conditions and derives estimation guarantees conditional on that structure. It does not provide a feasibility lower bound for a chosen reduced dimension.

Classical nonlinear-width theory and modern manifold-width results use Borsuk--Ulam-type arguments to lower-bound worst-case deterministic reconstruction error under continuous low-dimensional encoders. Those results are important prior structure and cover the qualitative topological collision. The claim here is not that collision. The additional statement is a distributional-regression bound for the proper energy-score objective with a stochastic decoder law: uniform Lipschitz control propagates the collision to a cap of positive covariate probability, producing an explicit population regret floor and the necessary \((1+2L_eL_d)^{-(p-1)}\) scaling.

Batson, Haaf, Kahn, and Roberts study topological obstructions in deterministic autoencoders and show that nontrivial topology can force poor reconstruction regions even when latent and intrinsic dimensions agree. Their setting and loss are different from conditional-law prediction with energy score; their paper does not state the cap-integrated energy-score bound above.

## Limitations
The lower bound is not claimed to be the minimax-optimal constant. It is a certified floor obtained from one antipodal collision and its Lipschitz neighborhood. A stronger waist theorem could potentially enlarge the bad set and improve the constant.

The covariate distribution is uniform on a sphere. The proof extends immediately to distributions that put a known positive mass in every sufficiently small neighborhood of the Borsuk--Ulam collision, but no such extension is claimed here. The result also does not cover discontinuous encoders; indeed, measurable one-dimensional sufficient encodings are known to exist abstractly. Finally, the theorem controls population energy-score regret, not optimization error, finite-sample estimation error, or the behavior of a particular training algorithm.

## References
1. Alexander Henzi, Tiange Liu, and Xinwei Shen, *Sufficiently Reduced Distributional Regression*, arXiv:2609.29291v1, 2026.
2. Wenxi Tan, Bing Li, and Lingzhou Xue, *Belted Engression: Sufficient Dimension Reduction for Generative Distributional Regression*, arXiv:2609.23789v1, 2026.
3. Joshua Batson, C. Grace Haaf, Yonatan Kahn, and Daniel A. Roberts, *Topological Obstructions to Autoencoding*, Journal of High Energy Physics 2021, article 280; arXiv:2102.08380.
4. Ronald A. DeVore, Ralph Howard, and Charles A. Micchelli, *Optimal nonlinear approximation*, Manuscripta Mathematica 63 (1989), 469--478.
5. Jonathan W. Siegel, *Sharp lower bounds on the manifold widths of Sobolev and Besov spaces*, Journal of Complexity 85 (2024), 101884; arXiv:2402.04407.
6. Jiří Matoušek, *Using the Borsuk--Ulam Theorem*, Springer, 2003.
7. Gábor J. Székely and Maria L. Rizzo, *Energy statistics: A class of statistics based on distances*, Journal of Statistical Planning and Inference 143 (2013), 1249--1272.
