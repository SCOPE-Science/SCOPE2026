# Sharp stochastic and Euclidean mean-width protection by matching edge deletions

## Finding

For integers \(n\ge4\) and \(1\le k\le\lfloor n/2\rfloor\), let \(F\) be any \(k\)-edge subset of the complete graph on \(n\) labeled vertices. Write \(G=K_n\setminus F\) and
\[
P_G=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(G)\}\subset H_n,
\qquad H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
The Euclidean structure on \(H_n\) is inherited from \(\mathbb R^n\). Define intrinsic mean width by \(w(P)=\mathbb E_{U}[h_P(U)+h_P(-U)]\), with \(U\) uniform on the unit sphere of \(H_n\) and \(h_P\) the support function.

Let \(Z_1,\ldots,Z_n\) be independent standard Gaussians, with strict order statistics \(Z_{(1)}<\cdots<Z_{(n)}\). Put
\[
D_n=\min\{Z_{(2)}-Z_{(1)},\ Z_{(n)}-Z_{(n-1)}\},\qquad
\eta_n=\mathbb E D_n>0,\qquad
 a_{n-1}=\sqrt2\,\frac{\Gamma(n/2)}{\Gamma((n-1)/2)}.
\]
Then the sharp inequality is
\[
\boxed{w(P_G)\le w(P_{K_n})-\frac{4k\eta_n}{n(n-1)a_{n-1}}.}
\]
**Equality holds if and only if \(F\) is a matching.** Thus removing \(k\) pairwise-disjoint edges uniquely maximizes intrinsic Euclidean mean width among all ways to remove \(k\) edges, up to graph relabeling.

The conclusion strengthens to a distributional statement. Given independent identically distributed continuous real scores \(X_1,\ldots,X_n\), define the nonnegative support loss
\[
\Delta_F(X)=\max_iX_i-\min_iX_i-\max_{\{i,j\}\in E(G)}|X_i-X_j|.
\]
Let \(D(X)\) be the lesser of the top and bottom consecutive spacings of their order statistics. For \(B\) independent of \(D(X)\), with \(\Pr(B=1)=2k/[n(n-1)]\),
\[
\boxed{\Delta_F(X)\ \succeq_{\rm st}\ B D(X),}
\]
where stochastic domination means larger upper-tail probabilities at every threshold. For every matching \(F\) there is **equality in distribution**. For nonmatchings the inequality in expected loss is strict whenever the score law has a density positive on an interval and finite first moment.

The universal Gaussian constant has the exact convergent integral, writing \(\phi\) and \(\Phi\) for the standard normal density and distribution function,
\[
\eta_n=n(n-1)\int_0^\infty\!\int_{-\infty}^\infty\!\int_{x+2t}^\infty
\phi(x)\phi(y)[\Phi(y-t)-\Phi(x+t)]^{n-2}\,dy\,dx\,dt.
\]
Furthermore, for \(u_n=\Phi^{-1}(1-1/n)\),
\[
 u_n\eta_n\longrightarrow\frac12,
\qquad
w(P_{K_n})-w(P_{K_n\setminus M_k})\sim
\frac{2k}{n^{5/2}\sqrt{2\log n}}
\]
uniformly for any choice of integer \(1\le k=k(n)\le\lfloor n/2\rfloor\), where \(M_k\) is a matching with \(k\) edges. In particular, for even \(n\) and a perfect matching,
\[
\lim_{n\to\infty}n^{3/2}\sqrt{2\log n}\,[w(P_{K_n})-w(P_{K_n\setminus M_{n/2}})]=1.
\]

## Assumptions and scope

The graph has \(n\ge4\) vertices and \(1\le k\le\lfloor n/2\rfloor\) deleted edges. Under these assumptions \(G\) remains connected (a disconnected graph formed by deleting edges of \(K_n\) requires at least \(n-1\) deletions), so \(P_G\) is full-dimensional inside the \((n-1)\)-dimensional space \(H_n\). Gaussian scores have variance one. The stochastic comparison extends to any atomless independent identically distributed scalar scores; the strict *expectation* assertion assumes finite first moment and positive density on an interval. All widths are intrinsic, not widths normalized in ambient \(\mathbb R^n\).

## Proof

**1. A pointwise extremal-spacing bound.** Fix \(n\) distinct scores and let \(i_+\) and \(i_-\) label their maximum and minimum. The full-graph support is \(R=X_{(n)}-X_{(1)}\). If \(\{i_+,i_-\}\) survives, the support loss is zero. Otherwise, each surviving edge fails to connect the two extremes and loses at least one of the endpoint spacings. Therefore
\[
\Delta_F(X)\ge\mathbf1_{\{\{i_+,i_-\}\in F\}}D(X).
\]
If \(F\) is a matching and the extremes form a deleted edge, then both \(\{i_+,i_{\mathrm{second\ min}}\}\) and \(\{i_{\mathrm{second\ max}},i_-\}\) survive: each extreme is incident to precisely one deleted edge. Their score differences are respectively \(R-(X_{(2)}-X_{(1)})\) and \(R-(X_{(n)}-X_{(n-1)})\). One attains \(R-D(X)\), proving equality pointwise for matchings.

**2. Exchangeable labels and strictness.** For identically distributed continuous scores, their sorting permutation is uniform on \(n!\) possibilities and independent of the ordered values. Hence the unordered extreme pair belongs to \(F\) with probability \(k/\binom n2=2k/[n(n-1)]\), independently of \(D(X)\). This proves the stochastic bound and equality law. If \(F\) is not a matching, it contains edges \(\{u,v\}\) and \(\{u,w\}\) sharing \(u\). There is a positive-probability open set of score assignments with \(u\) largest, \(v\) smallest, \(w\) second smallest, and bottom spacing strictly smaller than top spacing. The unique potential remaining edge attaining loss \(D(X)\) would connect \(u\) to \(w\), but it too was removed. The inequality is strict on that open set. If the score density is positive on an interval, such an open set can be chosen within that interval; finiteness of the first moment then gives strict expectation.

**3. Spherical width normalization.** Let \(Z=(Z_i)\), \(\Pi_HZ\) its orthogonal projection onto \(H_n\), and \(U=\Pi_HZ/\|\Pi_HZ\|\). By Gaussian rotational invariance, \(U\) is uniform on the unit sphere, independent of \(\|\Pi_HZ\|\sim\chi_{n-1}\). For every edge root the projection leaves coordinate differences unchanged, giving \(h_{P_G}(Z)=h_{P_G}(\Pi_HZ)\). Since \(P_G\) is centrally symmetric,
\[
 w(P_G)=\frac{2}{a_{n-1}}\mathbb E\max_{ij\in E(G)}|Z_i-Z_j|.
\]
Subtract the full-graph expression, apply Step 2 with \(\mathbb E\Delta_F(Z)\ge 2k\eta_n/[n(n-1)]\), and use its equality and strictness conclusions.

**4. Exact integral.** By layer cake, \(\eta_n=\int_0^\infty\Pr(D_n>t)\,dt\). For both endpoint spacings to exceed \(t\), there must be one observation \(x\) at the minimum, one \(y\) at the maximum, and all other \(n-2\) observations in \((x+t,y-t)\). Choosing their ordered labels in \(n(n-1)\) ways and integrating their joint density gives the displayed triple integral. Tonelli's theorem applies to its nonnegative integrand.

**5. Extreme-value limit and expectations.** Write \(u=u_n\). Mills' ratio gives, for every fixed real \(s\),
\[
 n\Pr(Z>u+s/u)\longrightarrow e^{-s},\qquad
 n\Pr(Z<-u-s/u)\longrightarrow e^{-s}.
\]
For disjoint upper and lower extreme intervals, multinomial rare-event counts converge jointly to independent Poisson counts. Hence the two centered-scaled extreme point processes converge to independent Poisson processes with intensity \(e^{-s}\,ds\). The spacing between the two largest points of such a process has an \(\operatorname{Exp}(1)\) law: under the transformation \(t=e^{-s}\), its two smallest arrival times are \(E_1\) and \(E_1+E_2\), with independent unit exponentials, and \(\Pr(\log((E_1+E_2)/E_1)>v)=e^{-v}\). Thus
\[
 (u(Z_{(n)}-Z_{(n-1)}),u(Z_{(2)}-Z_{(1)}))
 \ \Longrightarrow\ (E_+,E_-),
\]
with independent unit exponentials.

To pass to expectations, condition on the second-largest value \(V=Z_{(n-1)}\). The largest point above \(V\) follows the normal upper tail conditional on exceeding \(V\). On \(V\ge u/2\), the increasing Gaussian hazard rate, bounded below by \(V\), gives
\[
\Pr\{u(Z_{(n)}-V)>s\mid V\}\le e^{-s/2}\quad(s\ge0).
\]
The exceptional probability \(\Pr(V<u/2)\) is \(\Pr(\operatorname{Bin}(n,\overline\Phi(u/2))\le1)\), which decays faster than any inverse polynomial because \(n\overline\Phi(u/2)=n^{3/4+o(1)}\). Cauchy--Schwarz and \(\mathbb E\max_i|Z_i|^2=O(\log n)\) show that the exceptional contribution to the first moment of the scaled spacing vanishes. The same holds at the lower extreme. Therefore the scaled lesser gap is uniformly integrable and \(u\eta_n\to\mathbb E\min(E_+,E_-)=1/2\). Finally \(u_n\sim\sqrt{2\log n}\) and \(a_{n-1}\sim\sqrt n\), yielding the stated uniform-in-\(k\) asymptotic.

## Verification

The included executable `check.py` uses only Python's standard library. From the actual embedded source, run `python3 check.py`. It exhaustively checks all deleted-edge sets with \(1\le k\le\lfloor n/2\rfloor\) and all score-label permutations for \(n=4,5,6\), verifies exact pointwise bounds, matching equality, and strictly larger average losses for nonmatchings. It also checks the \(\operatorname{Uniform}[0,1]\) specialization by seeded simulation. These finite checks are consistency tests; the infinite statements follow from Steps 1--5.

As an additional exact distribution-free benchmark, for independent uniform scores the \(n+1\) adjacent spacings including the boundary gaps have the Dirichlet\((1,\ldots,1)\) law. Hence \(\Pr(D(X)>t)=(1-2t)^n\) for \(0\le t\le1/2\), \(\mathbb ED(X)=1/[2(n+1)]\), and a deleted matching has expected (unnormalized) support loss \(k/[n(n-1)(n+1)]\).

## Relationship to prior work

D'Alì, Juhnke-Kubitzke, Köhne and Venturello define these symmetric edge polytopes and study their \(h^*\)- and \(\gamma\)-vectors and random-graph face behavior. Their paper supplies the primary geometry family and its MSC ownership, not an extremal result for Euclidean mean width under edge deletion. Braun, Bruegge and Kahle analyze facet counts of random symmetric edge polytopes; Ohsugi and Tsuchiya investigate matching generating polynomials and enumerative invariants; D'Alì et al., *Many faces of symmetric edge polytopes*, investigate facets, triangulations and volume. None of those inspected results implies the present support-loss stochastic bound or unique deletion extremizer. Kabluchko, Litvak and Zaporozhets establish the general Gaussian mean-width representation and study regular simplices/crosspolytopes, but not this graph-edge deletion optimization. The Gaussian width normalization used here is standard; the full distributional deletion inequality and sharp graph-extremizer classification are the specific claim.

## Limitations

The theorem addresses Euclidean mean width of the specified standard root-coordinate realization, not all affine realizations or arbitrary edge weights. It does not claim classification for more than \(\lfloor n/2\rfloor\) missing edges, nor exact mean width for every nonmatching deletion pattern. The limiting formula concerns Gaussian-score spherical widths; the universal stochastic inequality has a broader score-law domain. The finite code does not certify the Poisson limit or the infinite classification. An earlier equivalent result under stochastic range, forbidden-pair order statistics, or graph-root-polytope terminology cannot be ruled out without a comprehensive independent bibliographic audit. Independent mathematical validation has not been performed.

## References

1. A. D'Alì, M. Juhnke-Kubitzke, D. Köhne and L. Venturello, *On the gamma-vector of symmetric edge polytopes*, arXiv:2201.09835 (first publicly posted 2022-01-24), https://arxiv.org/abs/2201.09835 . Primary MSC2020 52B20.
2. B. Braun, C. Bruegge and M. Kahle, *Facets of Random Symmetric Edge Polytopes, Degree Sequences, and Clustering*, arXiv:2204.07239 (2022), https://arxiv.org/abs/2204.07239 .
3. H. Ohsugi and A. Tsuchiya, *Symmetric edge polytopes and matching generating polynomials*, arXiv:2008.08621 (2020), https://arxiv.org/abs/2008.08621 .
4. A. D'Alì et al., *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (2019), https://arxiv.org/abs/1910.05193 .
5. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (2015), https://arxiv.org/abs/1511.08479 .
