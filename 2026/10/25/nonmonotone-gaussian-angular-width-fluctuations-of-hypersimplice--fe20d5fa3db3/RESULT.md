# Nonmonotone Gaussian angular-width fluctuations of hypersimplices

## Finding
For integers \(n\ge 2\) and \(1\le k\le\lfloor n/2\rfloor\), consider the hypersimplex
\[
\Delta_{n,k}=\operatorname{conv}\{\mathbf 1_S:S\subseteq\{1,\dots,n\},\ |S|=k\}
\]
in its intrinsic affine hyperplane. Let \(W_{n,k}\) be the Euclidean length of its orthogonal projection on a line whose direction is Haar-uniform in \(\mathbf 1^\perp\). Define
\[
\alpha_n=k/n,\quad z_n=\Phi^{-1}(1-\alpha_n),\quad
\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2},\quad
\overline\Phi(z)=1-\Phi(z),
\]
and the explicitly computable positive function
\[
V(z)=2\big[(1+z^2)\overline\Phi(z)-z\varphi(z)\big]
 -4\big[\varphi(z)-z\overline\Phi(z)\big]^2-2\varphi(z)^2.
\]
For **every** sequence with \(\alpha_n\in[\varepsilon,1/2]\), where \(\varepsilon>0\) is fixed, including sequences with no limiting rank fraction,
\[
\boxed{\quad
\frac{W_{n,k}-2\sqrt n\,\varphi(z_n)}{\sqrt{V(z_n)}}
\ \Longrightarrow\ N(0,1).\quad}
\]
In particular, if \(\alpha_n\to\alpha\in(0,1/2]\), the unstandardized centered widths converge to a centered Gaussian with variance \(V(\Phi^{-1}(1-\alpha))\).

The angular fluctuation variance profile is **not monotone** in the hypersimplex rank fraction. In the variable \(z=\Phi^{-1}(1-\alpha)\), its exact strict inequalities include
\[
\boxed{\quad V(1/2)>V(1)<V(3/2)>V(2).\quad}
\]
Thus the dense-rank variance displays both a decrease–increase and an increase–decrease as one moves from balanced toward sparser ranks. These inequalities are certified by rational intervals, not inferred from plotted decimals. At the balanced endpoint the exact identity is
\[
V(0)=1-3/\pi.
\]

## Assumptions and scope
The ambient Euclidean metric is the one induced from \(\mathbb R^n\) on the \((n-1)\)-dimensional hyperplane \(\sum_i x_i=k\); directions lie on the unit sphere in its parallel linear subspace \(\mathbf1^\perp\). No ambient-sphere projection or extra normalization of vertices is used. The asymptotic theorem requires \(\inf_n k/n>0\) and \(k\le n/2\). Complementation of incidence vectors gives the same width for ranks \(k\) and \(n-k\). The claim does **not** treat ranks with \(k/n\to0\), for which extreme-order-statistic regimes require different scaling. The displayed \(V\) is the variance of the Gaussian *limit law*, not a separately proved formula for finite-dimensional \(\operatorname{Var}(W_{n,k})\).

## Proof
**Exact support representation.** Take independent standard normal variables \(G_1,\ldots,G_n\), write \(\overline G=n^{-1}\sum_iG_i\), and \(R_n=(\sum_i(G_i-\overline G)^2)^{1/2}\). Orthogonal projection of the Gaussian vector onto \(\mathbf1^\perp\), followed by normalization, is Haar-uniform on the intrinsic sphere. Since translating all coordinates by the same scalar does not change a top-minus-bottom rank sum, we have the exact distributional identity
\[
W_{n,k}\ \stackrel d=\
\frac{\sum_{j=n-k+1}^{n}G_{(j)}-\sum_{j=1}^kG_{(j)}}{R_n},
\]
where \(G_{(1)}\le\cdots\le G_{(n)}\). This identity follows directly by maximizing and minimizing the linear functional over incidence vectors; the denominator is strictly positive almost surely for \(n\ge2\).

**Uniform trimmed-sum linearization.** Set \(z=z_n\). The sum of the top \(k\) values equals
\[
\min_{t\in\mathbb R}\left[kt+\sum_{i=1}^n(G_i-t)_+\right]
\]
and the minimizing \(t\) is a sample \((1-\alpha_n)\)-quantile. With \(\alpha_n\in[\varepsilon,1/2]\), the deterministic quantiles \(z_n\) stay in the compact interval \([0,\Phi^{-1}(1-\varepsilon)]\). Uniform positive lower bounds on the normal density there, together with the binomial-count concentration or the elementary quantile argument, imply \(t-z_n=O_{\mathbb P}(n^{-1/2})\), uniformly along any such rank sequence. Evaluating the convex objective at \(z_n\) instead of its minimizer therefore introduces only \(O_{\mathbb P}(1)\) error: its slope fluctuates at order \(O_{\mathbb P}(\sqrt n)\) and its curvature is order \(n\) locally. Apply the same argument to \(-G_i\). Writing \(H_z(g)=(|g|-z)_+\), the numerator becomes
\[
2kz_n+\sum_{i=1}^nH_{z_n}(G_i)+O_{\mathbb P}(1)
=2n\varphi(z_n)+\sum_{i=1}^n\big[H_{z_n}(G_i)-\mathbb EH_{z_n}(G_i)\big]+O_{\mathbb P}(1),
\]
because \(\mathbb EH_z(G)=2[\varphi(z)-z\overline\Phi(z)]\) and \(k=n\overline\Phi(z_n)\) exactly.

**Spherical normalization and covariance.** Standard Gaussian laws of large numbers and Taylor expansion give
\[
R_n=\sqrt n+\frac1{2\sqrt n}\sum_{i=1}^n(G_i^2-1)+o_{\mathbb P}(1).
\]
Dividing the preceding numerator by \(R_n\) yields
\[
W_{n,k}-2\sqrt n\,\varphi(z_n)
=\frac1{\sqrt n}\sum_{i=1}^n\psi_{z_n}(G_i)+o_{\mathbb P}(1),
\]
where
\[
\psi_z(g)=H_z(g)-2[\varphi(z)-z\overline\Phi(z)]-\varphi(z)(g^2-1).
\]
The required Gaussian integrals are
\[
\mathbb E[H_z(G)^2]=2[(1+z^2)\overline\Phi(z)-z\varphi(z)],
\quad \mathbb E[H_z(G)(G^2-1)]=2\varphi(z),
\quad \operatorname{Var}(G^2-1)=2.
\]
They imply \(\operatorname{Var}(\psi_z(G))=V(z)\). For each finite \(z\ge0\), \(V(z)>0\), since \(H_z(g)\) is not an affine function of \(g^2\) almost surely. On compact \(z\)-intervals its moments of order three are bounded and \(V\) has a positive lower bound. The triangular-array Lindeberg theorem applied to \(\psi_{z_n}(G_i)\), together with Slutsky's lemma, proves the standardized assertion even for oscillating \(\alpha_n\).

**Certified nonmonotonicity.** The supplied standalone checker uses rational Taylor bounds for \(e^{-z^2/2}\) and \(\int_0^z e^{-t^2/2}\,dt\), the alternating Machin formula for \(\pi\), and rational square-root enclosures to bracket \(V\) at four rational arguments. The resulting rigorous enclosures, rounded outward here to six decimal places, are
\[
\begin{aligned}
0.014884&<V(1/2)<0.014885,\\
0.005814&<V(1)<0.005815,\\
0.008708&<V(3/2)<0.008709,\\
0.005419&<V(2)<0.005420.
\end{aligned}
\]
They prove all asserted strict inequalities. Setting \(z=0\) in the explicit formula gives \(1-3/\pi\).

## Verification
Run `python3 CHECK.py` in a Python 3 standard-library environment. It verifies the alternating-series error brackets with exact rational arithmetic, checks the three strict differences with non-overlapping intervals, and independently enumerates support extrema for fixed rational vectors on small hypersimplices. The checker verifies the stated numeric certificates and exact finite representation; the asymptotic central limit theorem is established analytically above, not by finite experimentation.

## Relationship to prior work
The hypersimplex incidence-vector realization is standard; Martínez-Sandoval and Padrol analyze its projections preserving vertices and skeleta, rather than the Haar-angular length law. Kabluchko, Litvak, and Zaporozhets prove a Gaussian projection-width limit for regular cubes, simplices, and crosspolytopes; their cube calculation supplies the balanced endpoint \(V(0)=1-3/\pi\), which is not claimed as new. Standard L-statistic and quantile asymptotic theory supplies the trimmed-sum linearization mechanism. The contribution assessed here is its explicitly normalized all-dense-rank hypersimplex specialization and the rationally certified nonmonotone variance profile. Existing broad results may make the Gaussian limit a corollary after further calculation; no direct covering angular-width rank-profile result was identified in the inspected sources.

## Limitations
This is a limiting law for positive-proportion ranks, not a finite-dimensional variance identity or a statement about sparse or fixed ranks. The strict four-point inequalities show nonmonotonicity but do not locate or count all critical points. The first two cited primary papers were read in their freely accessible versions for their geometric object and projection-width results. Broader order-statistic literature may contain an equivalent studentized L-statistic statement, and this remains a bibliographic risk. No independent validation has been performed.

## References
1. L. Martínez-Sandoval and A. Padrol, *The convex dimension of hypergraphs and the hypersimplicial Van Kampen–Flores theorem*, arXiv:1909.01189, first posted 2019-09-03. https://arxiv.org/abs/1909.01189
2. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, 2015. https://arxiv.org/abs/1511.08479
3. A. W. van der Vaart, *Asymptotic Statistics*, Cambridge University Press, 1998, Chapter 22 (L-statistics and sample-quantile methods).
