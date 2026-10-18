# A sharp two-observation support transition for reweighted Gaussian-mixture likelihoods

## Finding

**Theorem (complete two-observation support classification and random-weight law).** Fix \(a>0\) and \(0<q<1\). Observe the two points \(-a\) and \(a\) under the one-dimensional Gaussian location-mixture kernel with *known unit variance*. Optimize the normalized positive-weight log-likelihood

\[
\ell_{a,q}(G)=q\log\!\int_{\mathbb R}e^{-(\theta+a)^2/2}\,dG(\theta)
 +(1-q)\log\!\int_{\mathbb R}e^{-(\theta-a)^2/2}\,dG(\theta)
\]

over all Borel probability measures \(G\) on \(\mathbb R\). The omitted Gaussian normalizing constant is immaterial. Define

\[
a_{\mathrm c}(q)=\begin{cases}
\left[\dfrac{\log((1-q)/q)}{2(1-2q)}\right]^{1/2},&q\ne\tfrac12,\\
1,&q=\tfrac12,
\end{cases}\qquad z=a(1-2q).
\]

There is **exactly one maximizing mixing measure** \(\widehat G\). It has **one atom** if and only if \(a\le a_{\mathrm c}(q)\), in which case \(\widehat G=\delta_z\). For \(a>a_{\mathrm c}(q)\), it has **exactly two distinct atoms**, both of positive mass. Thus the exact critical distance between the observations is \(2a_{\mathrm c}(q)\) Gaussian standard deviations.

For \(q\ne1/2\), the transition is *nonlocal in support*: as \(a\downarrow a_{\mathrm c}(q)\) from above, one atom tends to \(z_{\mathrm c}=a_{\mathrm c}(q)(1-2q)\) and its mass tends to one; the other atom tends to \(-z_{\mathrm c}\) and its mass tends to zero. Yet the global singleton sensitivity certificate already fails for \(a>a_{\mathrm c}(q)\) while its curvature at \(z\) stays negative throughout the nonempty interval

\[
a_{\mathrm c}(q)<a<a_{\mathrm{loc}}(q):=\frac{1}{2\sqrt{q(1-q)}}.
\]

For equal weights \(q=1/2\), the two support atoms instead coalesce continuously at the origin as \(a\downarrow1\).

**Exact random-reweighting law.** Suppose the two positive likelihood weights are independent \(\operatorname{Gamma}(\alpha,\alpha)\) variables (shape and rate \(\alpha>0\)), normalized to sum to one. Their first normalized weight is \(Q\sim\operatorname{Beta}(\alpha,\alpha)\). For \(a\le1\), the NPMLE has one atom almost surely. For every \(a>1\), let \(x_a\in(0,1)\) be the unique nonzero solution of

\[
\operatorname{arctanh}(x_a)=a^2x_a.
\]

Then the exact probability of a **two-atom** NPMLE is

\[
\boxed{\quad
\Pr\{\#\operatorname{supp}(\widehat G)=2\}
=1-2I_{(1-x_a)/2}(\alpha,\alpha),\quad a>1,
\quad}
\]

where \(I_u(\alpha,\alpha)\) is the regularized incomplete beta integral. In particular, for uniform normalized weights (\(\alpha=1\)) this probability equals \(x_a\), and for \(\alpha=2\) it equals \((3x_a-x_a^3)/2\). As \(a\downarrow1\), the uniform-weight probability satisfies \(x_a\sim\sqrt{3(a^2-1)}\).

## Assumptions and scope

The kernel variance equals one, both sample points are distinct, and weights are strictly positive; only their ratio matters. Arbitrary translated observations and common Gaussian variance \(\sigma^2>0\) reduce to these assumptions by translating and dividing locations by \(\sigma\). The parameter set for the mixing distribution is unrestricted \(\mathbb R\), not a fixed external support grid. The sole stochastic assertion concerns the independent Gamma weights and the resulting two-observation optimizer; no claim is made for general sample size.

For later steps put \(k_{-}(\theta)=e^{-(\theta+a)^2/2}\) and \(k_{+}(\theta)=e^{-(\theta-a)^2/2}\). All fitted kernel values in the likelihood are strictly positive. Because projection of every \(\theta\notin[-a,a]\) to the closest endpoint of \([-a,a]\) **strictly increases both kernels**, a maximizer may, and necessarily must, be supported in \([-a,a]\). Weak compactness there and continuity of the two fitted values establish existence.

## Proof

**1. The singleton candidate and its exact global sensitivity.** Among one-atom measures, \(\ell_{a,q}(\delta_\theta)=-\{q(\theta+a)^2+(1-q)(\theta-a)^2\}/2\), a strictly concave quadratic with unique maximizer \(\delta_z\), where \(z=a(1-2q)\).

For any \(G\), its directional likelihood derivative when an infinitesimal mass is moved to \(\theta\) is governed by the dual sensitivity

\[
D_G(\theta)=q\frac{k_{-}(\theta)}{\int k_{-}\,dG}+(1-q)\frac{k_{+}(\theta)}{\int k_{+}\,dG}.
\]

Because the log-likelihood is concave in \(G\), \(G\) maximizes the full likelihood **if and only if** \(D_G(\theta)\le1\) for every \(\theta\), with equality on the support of any maximizer. This follows directly by computing the directional derivative toward \(\delta_\theta\), and then using the supporting-hyperplane inequality for the logarithm.

Writing \(t=\theta-z\), direct cancellation of the Gaussian factors gives

\[
D_{\delta_z}(z+t)=e^{-t^2/2}
\bigl[q e^{-2a(1-q)t}+(1-q)e^{2aqt}\bigr].\tag{1}
\]

If \(B\sim\operatorname{Bernoulli}(q)\), the bracket is \(\mathbb E e^{-2at(B-q)}\). The **sharp Kearns--Saul inequality**, with strict equality-characterization proved by Schlemm (2014, Theorem 1.1), says that for \(s\in\mathbb R\) and \(q\ne1/2\),

\[
\log\mathbb E e^{s(B-q)}\le
\frac{1-2q}{4\log((1-q)/q)}s^2,\tag{2}
\]

and equality outside \(s=0\) occurs **only** at \(s=2\log((1-q)/q)\). For \(q=1/2\), the sharp inequality is \(\log\cosh(s/2)\le s^2/8\), with equality only at zero. Substituting \(s=-2at\) in (2) proves from (1) that \(D_{\delta_z}\le1\) everywhere exactly when \(a\le a_{\mathrm c}(q)\). Necessity follows by using the nonzero equality point in (2) (or \(t\to0\) for \(q=1/2\)) whenever \(a>a_{\mathrm c}(q)\). At \(a=a_{\mathrm c}(q)\) and \(q\ne1/2\), the global equality points of \(D_{\delta_z}\) are exactly \(\theta=z\) and \(\theta=-z\), since the nonzero Kearns--Saul equality argument corresponds to \(t=-2z\).

**2. Every optimizer has at most two support atoms.** At any optimum \(G\), its sensitivity \(D_G\) is a strictly positive combination of the two equal-variance Gaussian kernels. It tends to zero at both ends of the line. Its derivative is positive for \(\theta\le-a\) and negative for \(\theta\ge a\). Within \((-a,a)\), write the two positive coefficients as \(A,B\). Its stationary equation is

\[
\log\frac{a-\theta}{a+\theta}+2a\theta=\log\frac{A}{B}.
\]

The derivative of the left side equals \(2a-2a/(a^2-\theta^2)\), which has at most two zeros. The stationary equation therefore has at most three solutions, and \(D_G\) has at most two local maxima, hence at most two *global* maxima. Since the support of \(G\) is contained in these maxima, it has at most two atoms. If \(a>a_{\mathrm c}(q)\), Step 1 excludes every one-atom optimum, hence exactly two distinct, positive-mass atoms occur.

**3. Uniqueness, including the critical equality case.** Strict concavity of \(q\log u+(1-q)\log v\) for \(u,v>0\) shows that any two maximizing measures have the *same ordered fitted-value pair* \((\int k_-dG,\int k_+dG)\), and thus the same dual sensitivity function. This dual function has at most two global maximizers, as just proved. The two kernel-evaluation vectors at different locations are linearly independent: indeed, \(k_-(\theta)/k_+(\theta)=e^{-2a\theta}\) is strictly monotone. Accordingly, a probability measure supported on those two dual maximizers is determined uniquely by its fitted pair. For \(a\le a_{\mathrm c}(q)\), the available maximizer is \(\delta_z\), so it is also unique even at the critical value where a second *dual contact point*, not a second positive-mass mixing atom, occurs. This proves the full deterministic classification.

**4. Nonlocal onset and the local-curvature window.** From (1), the singleton sensitivity obeys

\[
D_{\delta_z}''(z)=4a^2q(1-q)-1.
\]

For \(q\ne1/2\), put \(x=|1-2q|\in(0,1)\). Then \(a_{\mathrm c}(q)^2=\operatorname{arctanh}(x)/x\), while \(a_{\mathrm{loc}}(q)^2=1/(1-x^2)\). The strict integral inequality \(\operatorname{arctanh}(x)=\int_0^x(1-u^2)^{-1}du<x/(1-x^2)\) gives \(a_{\mathrm c}(q)<a_{\mathrm{loc}}(q)\). The global failure of the certificate before its local curvature reverses is therefore real, not merely a numerical observation.

Let \(a\downarrow a_{\mathrm c}(q)\) from above. The optimizers are supported in the common compact interval \([-a,a]\). Every convergent subsequence of their measures must optimize the limiting likelihood, whose unique optimizer from Step 3 is \(\delta_{z_{\mathrm c}}\); thus the full family converges weakly to that point mass. At critical unequal weights, the limiting dual has exactly two *strict, nondegenerate* maxima \(\pm z_{\mathrm c}\). Their curvature is \(4a_{\mathrm c}(q)^2q(1-q)-1<0\), as follows by evaluating (1) at its two equality points. Uniform convergence of the duals with their first two derivatives, together with the at-most-two-maxima argument, forces the two supercritical support points to approach the two distinct limiting maxima. The mass at \(-z_{\mathrm c}\) vanishes by weak convergence of the measures. For \(q=1/2\), the critical dual has only one maximum at the origin, so both support locations coalesce there; uniqueness and reflection symmetry give equal masses.

**5. Exact distribution under independent Gamma reweighting.** For independent \(\operatorname{Gamma}(\alpha,\alpha)\) weights, their normalized first coordinate \(Q\) is \(\operatorname{Beta}(\alpha,\alpha)\). The identity \(a_{\mathrm c}(q)^2=\operatorname{arctanh}(|1-2q|)/|1-2q|\), continuously interpreted as one at \(q=1/2\), is strictly increasing in \(|1-2q|\). Consequently, if \(a\le1\) all weights give one atom; for \(a>1\), the two-atom condition is \(|1-2Q|<x_a\) where \(x_a\) uniquely solves the displayed equation in the Finding. Integrating the symmetric beta density over that central interval gives the stated regularized-beta probability. For \(\alpha=1\), it is the interval length \(x_a\); for \(\alpha=2\), integration of the density \(6q(1-q)\) gives \((3x_a-x_a^3)/2\). Finally \(\operatorname{arctanh}(x)=x+x^3/3+O(x^5)\) gives \(x_a\sim\sqrt{3(a^2-1)}\). \(\square\)

## Verification

The accompanying standalone program `verify.py` executes 29,849 deterministic floating-point diagnostic assertions spanning asymmetric and symmetric likelihood weights. It checks the exact critical contact points, derivatives and curvatures, the strict separation between global and local thresholds, improvement by a tiny second atom immediately above threshold, and the subcritical dual inequality on finite grids. Run `python3 verify.py` in the extracted package directory. The numerical grids are **not** proofs of the global inequality; the infinite claims rest on Schlemm's rigorous Kearns--Saul theorem and the explicit analytical arguments in Steps 1--5.

## Relationship to prior work

Jiang (2026) studies the Gaussian location NPMLE under random positive Gamma likelihood weights and proves high-probability polylogarithmic sparsity in a growing-sample regime (Theorem 1), with exact uniqueness under stated assumptions. The present result provides a **finite, fully exact** support-count phase diagram and its weight-induced probability law at two observations; it does not improve the large-sample sparsity rate. The relevant likelihood definition, Dirichlet normalization and theorem were inspected in Jiang's full version 1, including its introduction, main theorems and supporting discussion.

Schlemm (2014) proves the sharp Kearns--Saul Bernoulli exponential-moment inequality and the strict location of its maximizer. That **pre-existing sharp inequality** is the central nonstandard ingredient in Step 1; no novelty is claimed for it. Polyanskiy and Sellke (2025, Proposition 1.1) review the general Gaussian location-mixture likelihood sensitivity certificate and known one-dimensional optimizer uniqueness, both also prior. The contribution here is the exact identification of **where the singleton certificate succeeds**, its comparison to the different local-curvature threshold, the **two-atom structure with nonlocal onset**, and the resulting exact Beta-reweighted support-count probability, not a rediscovery of those general tools.

## Limitations

All results concern *exact* unrestricted one-dimensional NPMLEs fitted to precisely two distinct observations and a *known common Gaussian variance*. They are not classifications for three or more observations, heteroscedastic kernels, finite grids, penalized estimators or approximate optimizers. The two supercritical atom locations and mixture masses are characterized implicitly via the likelihood/KKT system; no general closed-form formula for them is claimed. The deterministic transition is a mathematical consequence of a known sharp moment-generating-function inequality, so it should not be misconstrued as a new concentration inequality. An older or unindexed treatment of this same NPMLE specialization cannot be ruled out without independent priority examination.

## References

1. H. Jiang, *Polylogarithmic Sparsity of Randomly Reweighted NPMLEs for Gaussian Mixtures*, arXiv:2610.01088v1 (first public submission 2026-10-01), https://arxiv.org/abs/2610.01088.
2. E. Schlemm, *The Kearns--Saul Inequality for Bernoulli and Poisson-binomial Distributions*, arXiv:1405.4496v1 (2014), https://arxiv.org/abs/1405.4496; especially Theorem 1.1 and its proof.
3. Y. Polyanskiy and M. Sellke, *Nonparametric MLE for Gaussian Location Mixtures: Certified Computation and Generic Behavior* (2025), https://people.lids.mit.edu/yp/homepage/data/2025_npmle_support.pdf; especially Proposition 1.1 and the related-work discussion.
4. B. Lindsay, *The geometry of mixture likelihoods: a general theory*, Annals of Statistics 11 (1983), 86--94. Classical likelihood-geometry context, cited through References 1 and 3.
