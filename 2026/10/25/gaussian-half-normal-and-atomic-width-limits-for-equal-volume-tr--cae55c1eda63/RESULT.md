# Gaussian, half-normal, and atomic width limits for equal-volume tree symmetric-edge polytopes

## Finding

Let \(T\) be a tree on \(N\ge 3\) labeled vertices, and let its symmetric-edge polytope be
\[
Q_T=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(T)\}\subset H_N=\{x\in\mathbb R^N:\sum_i x_i=0\}.
\]
Widths and volume below use the intrinsic Euclidean metric on \(H_N\). Write \(W_T=\max_{x\in Q_T}\langle x,U\rangle-\min_{x\in Q_T}\langle x,U\rangle\) for \(U\) uniformly distributed on the unit sphere of \(H_N\). Every such \((N-1)\)-polytope has the same volume
\[
\operatorname{Vol}_{N-1}(Q_T)=\frac{2^{N-1}\sqrt N}{(N-1)!}.
\]

Put \(b_k=\Phi^{-1}(1-1/k)\), \(k\ge2\), for the standard normal distribution function \(\Phi\), and let \(\Lambda(x)=\exp(-e^{-x})\) be the standard Gumbel distribution function.

**Sparse-degree regime.** For any trees \(T_N\) with \(m=N-1\) edges and maximal degree
\[
\Delta_N=o\!\left(\frac{m^{1/3}}{(\log m)^{2/3}}\right),
\]
the random angular widths have the universal limit
\[
 b_{2m}\left(\frac{\sqrt N}{2\sqrt2}W_{T_N}-b_{2m}\right)
 \ \Longrightarrow\ \Lambda.
\]
In particular this holds for all sequences of uniformly bounded-degree trees, including paths.

**Broom phase transition.** Let \(B_{n,\ell}\) be the tree with one hub, \(n\) pendant leaves, and one additional path of \(\ell\) edges rooted at the hub. Assume \(n\to\infty\) and \(\ell=\ell_n\ge1\), and define
\[
 c_n=\sqrt2\,b_{2\ell_n}-b_n,\qquad N_n=n+\ell_n+1.
\]
When \(c_n\to s\in\mathbb R\),
\[
 \frac{\sqrt{N_n}}2 W_{B_{n,\ell_n}}-b_n
 \ \Longrightarrow\ \max\{|Z|,s\}, \qquad Z\sim N(0,1).
\]
When \(s>0\), this limit has an atom at \(s\) of mass exactly \(2\Phi(s)-1\), together with the half-normal tail above \(s\). When \(c_n\to-\infty\), the limit in the preceding display is simply \(|Z|\). When \(c_n\to+\infty\), the path instead dominates and
\[
 b_{2\ell_n}\left(\frac{\sqrt{N_n}}{2\sqrt2}W_{B_{n,\ell_n}}-b_{2\ell_n}\right)
 \ \Longrightarrow\ \Lambda.
\]
For each prescribed \(s\in\mathbb R\), the explicitly chosen integer sequence
\[
 \ell_n=\left\lfloor\frac1{2\,\overline\Phi((b_n+s)/\sqrt2)}\right\rfloor,
 \qquad \overline\Phi=1-\Phi,
\]
(restricted to sufficiently large \(n\)) realizes \(c_n\to s\); thus every critical law, including the atomic ones, occurs within this equal-volume family. In particular, \(\ell_n=\lfloor n^\alpha\rfloor\) gives the half-normal regime for \(0<\alpha\le\tfrac12\), and the Gumbel regime for \(\alpha>\tfrac12\).

## Assumptions and scope

Graphs are finite, simple, labeled, and connected. Every angular direction is Haar-uniform on the intrinsic sphere; widths use the Euclidean metric inherited from \(\mathbb R^N\), not a coordinate-transformed cube metric. All limits involve growing dimension. In the broom definition the additional path's nonhub vertices are disjoint from the \(n\) pendant leaves. The stated normal quantiles are defined when their indices exceed two; all limit assertions concern sufficiently large indices. The Gumbel regime has a different normalization from the star/critical regime.

## Proof

**1. Exact common volume and support representation.** Choose any orientation of the tree edges and assemble the \(N\times(N-1)\) incidence matrix \(B\) with columns \(e_i-e_j\). Because a tree has no cycles, its columns are linearly independent. Each maximal square minor obtained by deleting one row is \(\pm1\); Cauchy–Binet therefore gives \(\det(B^TB)=N\). The image under \(B\) of the standard \((N-1)\)-crosspolytope is precisely \(Q_T\), so the intrinsic volume is \(\frac{2^{N-1}}{(N-1)!}\sqrt{\det(B^TB)}\), as claimed. Central symmetry gives \(W_T=2\max_{\{i,j\}\in E(T)}|U_i-U_j|\).

Let \(G_1,\ldots,G_N\) be independent standard Gaussians, \(\overline G=N^{-1}\sum_iG_i\), \(R_N=\|G-\overline G\mathbf1\|_2\). Orthogonal Gaussian rotation symmetry gives the exact identity in distribution
\[
 W_T=\frac2{R_N}\max_{\{i,j\}\in E(T)}|G_i-G_j|.
\]
Moreover \(R_N/\sqrt N=1+O_{\mathbb P}(N^{-1/2})\), because \(R_N^2\) has the chi-square distribution with \(N-1\) degrees of freedom. For every tree with \(N-1\) edges, the Gaussian union bound gives \(\max_{ij\in E(T)}|G_i-G_j|=O_{\mathbb P}(\sqrt{\log N})\). Consequently replacing \(R_N\) by \(\sqrt N\) incurs \(O_{\mathbb P}(\sqrt{\log N/N})\) before multiplication by any extreme-value quantile, and \(O_{\mathbb P}(\log N/\sqrt N)=o_{\mathbb P}(1)\) afterward.

**2. Uniform Gumbel law at sufficiently sparse degree.** Put \(X_e=(G_i-G_j)/\sqrt2\) for each oriented edge \(e=ij\). These variables have unit variance. Disjoint edges depend on disjoint Gaussians and are independent. Distinct incident edges have correlation of absolute value \(1/2\). Fix \(x\in\mathbb R\), set \(u=b_{2m}+x/b_{2m}\), and let \(I_e=\mathbf1\{|X_e|>u\}\). The exceedance count has mean \(\lambda_m=2m\overline\Phi(u)\to e^{-x}\), by the usual normal-tail ratio (Mills' estimate).

Use the local-dependence Poisson inequality of Arratia–Goldstein–Gordon, with the neighborhood of an edge consisting of all edges sharing either endpoint, including itself. It has cardinality at most \(2\Delta_N-1\), and the independent-outside-neighborhood term vanishes exactly. Writing \(p=2\overline\Phi(u)=O(1/m)\), its first error term is bounded by \(m(2\Delta_N-1)p^2=O(\Delta_N/m)\).

For incident distinct edges, each of the four sign choices \(a,b\in\{\pm1\}\) has \(\operatorname{Var}(aX_e+bX_f)\le 3\); the joint event \(aX_e>u,bX_f>u\) therefore has probability at most \(\exp(-2u^2/3)\) by a one-dimensional Gaussian Chernoff bound. Thus
\[
 \mathbb P(|X_e|>u,|X_f|>u)
 \le4e^{-2u^2/3}
 =O\!\left(m^{-4/3}(\log m)^{2/3}\right).
\]
The second Poisson error term is \(O(\Delta_N m^{-1/3}(\log m)^{2/3})=o(1)\). It follows that \(\Pr(\max_e|X_e|\le u)\to e^{-e^{-x}}\). The Gaussian radius replacement above proves the angular-width assertion.

**3. Star limit.** Write \(G_0\) for the hub Gaussian and \(G_1,\ldots,G_n\) for its leaf Gaussians. The two normal sample extrema obey \(\max_{1\le i\le n}G_i=b_n+o_{\mathbb P}(1)\) and \(\min_{1\le i\le n}G_i=-b_n+o_{\mathbb P}(1)\). Therefore the maximum absolute difference across hub-to-leaf edges is
\[
 S_n=\max\big\{\max_iG_i-G_0,\,G_0-\min_iG_i\big\}
 =b_n+|G_0|+o_{\mathbb P}(1).
\]

**4. Path and crossover.** The \(\ell\) path edges, including the hub-to-first-path edge, have the same dependence structure as any ordinary path. When \(\ell\to\infty\), part 2 gives
\[
 P_\ell=\max_{\text{path edges}}|G_i-G_j|
 =\sqrt2\,b_{2\ell}+O_{\mathbb P}(1/b_{2\ell}),
\]
and the centered, scaled Gumbel law. If \(\ell\) stays bounded, \(P_\ell=O_{\mathbb P}(1)\). The full broom Gaussian edge maximum is **exactly** \(\max(S_n,P_\ell)\). The joint limits are not assumed independent: since \(P_\ell-\sqrt2b_{2\ell}\to0\) in probability, the maximum theorem and Slutsky's lemma directly give \(\max\{|Z|,s\}\) for finite \(s\), and the half-normal law when \(c_n\to-\infty\). For \(c_n\to+\infty\), the star event \(S_n>P_\ell\) has probability tending to zero, so the path's own finer Gumbel law transfers unchanged. The chi-square radius correction is negligible under both normalizations.

For the explicit critical sequence, put \(q_n=(b_n+s)/\sqrt2\). Since \(q_n\to\infty\), choosing \(\ell_n=\lfloor(2\overline\Phi(q_n))^{-1}\rfloor\) yields \(\overline\Phi(b_{2\ell_n})/\overline\Phi(q_n)\to1\), so normal-tail inversion gives \(b_{2\ell_n}-q_n\to0\). Finally \(b_n\sim\sqrt{2\log n}\), giving \(\sqrt2b_{2n^\alpha}-b_n=(2\sqrt\alpha-\sqrt2)\sqrt{\log n}+o(\sqrt{\log n})\) for fixed positive \(\alpha\), and at \(\alpha=1/2\) the difference tends to zero. For \(s>0\), the distribution function of \(\max(|Z|,s)\) jumps at \(s\) by \(\Pr(|Z|\le s)=2\Phi(s)-1\). This completes every claimed case.

## Verification

A standalone Python checker, `verification.py`, checks tree incidence Gram determinants exactly up to size fourteen; directly compares polytope-vertex support with the Gaussian edge-maximum representation; verifies the shared-edge covariance pattern; and checks twelve finite-parameter realizations of the critical quantile relation. It also prints illustrative Monte Carlo discrepancies and explicitly does not treat those slow-convergence simulations as proofs. Reproduce using Python, NumPy and SciPy by executing `python verification.py`. The all-dimensional claims follow from the preceding analytical argument, not from enumeration or simulation.

## Relationship to prior work

Chen–Davis–Korchevskaia establish the symmetric-edge-polytope graph–facet framework, while Chen–Korchevskaia study contractions and subdivisions. Those structural theorems do not give the Haar-direction width laws of this result. Bibinger studies Gumbel limits of maxima of independent half-normal-related variables; the edge differences here are dependent, with a hub producing the half-normal regime. Arratia–Goldstein–Gordon provide the standard Poisson approximation inequality used in the bounded-degree proof. The use of Gaussian spherical normalization, Mills' ratio, and the Chen–Stein method is standard. The new assertion here is their geometrically motivated combination into a precise three-regime and atomic crossover law on the fixed-volume class of tree symmetric-edge polytopes. A relevant published result for *graphical zonotopes* concerns width variance, a different convex body and statistic, not this limiting width law.

## Limitations

The degree-growth condition is a sufficient condition for the Gumbel regime; necessity or a sharp classification of arbitrary tree sequences is not asserted. The critical broom limit has an atom even though every finite-dimensional angular-width distribution is continuous; it is a weak limit, not a pointwise atom at finite dimension. The stated asymptotics are for intrinsic Haar-uniform directions, not arbitrary nonuniform sampling. The analysis is not a claim of prior-art exclusion in every unindexed Gaussian-extremes reference. Independent mathematical assessment remains to be done.

## References

1. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315v1 (first publicly available 26 July 2021), https://arxiv.org/abs/2107.12315.
2. T. Chen, E. Korchevskaia, *Graph edge contraction and subdivisions for adjacency polytopes*, arXiv:1912.02841, https://arxiv.org/abs/1912.02841.
3. M. Bibinger, *Gumbel convergence of the maximum of convoluted half-normally distributed random variables*, arXiv:2103.14525v1, https://arxiv.org/abs/2103.14525.
4. R. Arratia, L. Goldstein, L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method*, Annals of Probability **17** (1989), 9–25, doi:10.1214/aop/1176991491.
