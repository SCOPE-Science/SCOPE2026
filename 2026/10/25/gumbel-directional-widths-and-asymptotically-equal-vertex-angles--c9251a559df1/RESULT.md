# Gumbel directional widths and asymptotically equal vertex angles for bounded-degree symmetric edge polytopes

## Finding

For every sequence of connected simple graphs \(G_n\) on \(n\to\infty\) vertices with maximum degree bounded by a common finite constant, let \(m_n=|E(G_n)|\), and let
\[
P_n=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(G_n)\}\subset H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
The Euclidean metric is inherited from \(\mathbb R^n\). Let \(U_n\) be uniform on the unit sphere of \(H_n\), and let \(W_n=h_{P_n}(U_n)+h_{P_n}(-U_n)\) be the full Euclidean directional width. Write \(\Phi\) for the standard normal distribution function and
\[
b_n=\Phi^{-1}\!\left(1-\frac1{2m_n}\right).
\]
Then
\[
\boxed{\quad b_n\left(\frac{\sqrt{n-1}\,W_n}{2\sqrt2}-b_n\right)\ \Longrightarrow\ \mathcal G,\quad
\mathbb P(\mathcal G\le x)=\exp(-e^{-x}).\quad}
\]
For each oriented root vertex \(v_{ij}=e_i-e_j\) of \(P_n\), let \(\omega_{n,ij}\) be the proportion of intrinsic spherical directions in whose unique support face this vertex is exposed. Uniformly over all the \(2m_n\) oriented root vertices,
\[
\boxed{\quad\max_{\{i,j\}\in E(G_n)}\max_{\pm}\left|2m_n\,\omega_{n,\pm(i,j)}-1\right|\longrightarrow0.\quad}
\]
Thus an asymptotically equal share of the sphere exposes each root even when the graphs have no vertex or edge transitivity.

The bounded-degree assumption is substantive: for the star on \(n\) vertices, if \(c_n=\Phi^{-1}(1-1/(n-1))\), then
\[
\boxed{\quad\frac{\sqrt{n-1}}2W_n-c_n\ \Longrightarrow\ |Z|,\qquad Z\sim N(0,1).\quad}
\]
The centered star law is folded normal, not Gumbel, and its leading width scale differs by a factor of \(\sqrt2\).

## Assumptions and scope

All graphs are deterministic, simple and connected, with \(n\ge3\), and \(\sup_n\Delta(G_n)<\infty\) for the first two conclusions. No regularity, expansion, girth or convergence of edge density is assumed. Connectedness ensures that \(P_n\) is full dimensional in \(H_n\). The star is a separate comparison family with unbounded maximum degree. The convergence is in distribution; no assertion about a uniform-in-graph finite-sample rate or an optimal degree-growth threshold is made.

All signed edge roots are distinct vertices: each has Euclidean norm \(\sqrt2\), and the linear functional given by the root itself strictly favors that root over any other distinct signed edge root.

## Proof

**Step 1: exact spherical Gaussian reduction.** Take independent standard normal coordinates \(g_1,\ldots,g_n\), put \(\bar g=n^{-1}\sum_i g_i\), and set \(R_n=\|g-\bar g\mathbf1\|/\sqrt{n-1}\). The vector \(U_n=(g-\bar g\mathbf1)/\|g-\bar g\mathbf1\|\) is intrinsic Haar-uniform. Define \(Y_e=|g_i-g_j|/\sqrt2\) for each edge \(e=\{i,j\}\), and \(M_n=\max_e Y_e\). Central symmetry gives exactly
\[
\frac{\sqrt{n-1}}{2\sqrt2}W_n=\frac{M_n}{R_n}.
\]
Every \(Y_e\) has the absolute standard-normal law with tail \(p(t)=2[1-\Phi(t)]\). If edges are disjoint, their variables are independent. If distinct edges share one endpoint, the underlying signed standardized Gaussians have correlation of absolute value \(1/2\). For such a pair and \(u>0\), a four-sign union bound on the sum of two signed standard normals yields
\[
\Pr(Y_e\ge u,Y_f\ge u)\le4\exp(-2u^2/3).\tag{1}
\]
Indeed, each sign-pair sum has variance at most \(3\), and simultaneous positive exceedances force that sum to be at least \(2u\).

**Step 2: Poisson extremes.** For any fixed real \(x\), set \(u_n(x)=b_n+x/b_n\). Gaussian tail ratios imply
\[
m_np(u_n(x))\longrightarrow e^{-x},\qquad u_n(x)^2=2\log m_n+O(\log\log m_n).
\]
Let \(N_n(x)=\#\{e:Y_e>u_n(x)\}\). The dependency graph on edge indices joins intersecting original edges and has degree bounded by \(2(\Delta-1)\). In each fixed factorial moment of \(N_n(x)\), the ordered edge tuples with no intersecting pairs contribute \((m_np(u_n(x)))^k+o(1)\). For tuples containing intersections, partition the tuple into connected components in this dependency graph. For each singleton component the joint exceedance probability is \(O(1/m_n)\); for each component of size at least two, bound by (1), namely \(m_n^{-4/3+o(1)}\). Distinct components depend on disjoint sets of underlying Gaussian coordinates and hence are independent. A prescribed component pattern with \(c\) components has only \(O(m_n^c)\) placements because the dependency degree is bounded. Every pattern with a non-singleton component therefore contributes \(o(1)\), and the fixed factorial moments converge to those of a Poisson variable of mean \(e^{-x}\). Hence
\[
\Pr(M_n\le b_n+x/b_n)\longrightarrow\exp(-e^{-x}).\tag{2}
\]
Since \(R_n^2\) is \(\chi^2_{n-1}/(n-1)\), \(R_n=1+O_{\Pr}(n^{-1/2})\); also \(M_n=O_{\Pr}(b_n)\). Connectedness and bounded degree give \(n-1\le m_n\le\Delta n/2\), so \(b_n^2=O(\log n)\). Consequently \(b_nM_n|R_n^{-1}-1|=o_{\Pr}(1)\), and (2) proves the spherical width limit.

**Step 3: uniform normal-cone proportions.** Fix an edge \(e\), and write \(F_e\) for the set of other edges disjoint from \(e\), and \(L_e\) for the at most \(2(\Delta-1)\) neighboring edges. Since \(Y_e\) is independent of \(\{Y_f:f\in F_e\}\), put \(q_e=\Pr(Y_e>\max_{f\in F_e}Y_f)\). For \(v\in(0,m_n)\), define \(t_n(v)\) by \(p(t_n(v))=v/m_n\). The same Poisson argument after removing \(O_\Delta(1)\) edges implies, for fixed \(v>0\),
\[
\Pr\!\left(\max_{f\in F_e}Y_f\le t_n(v)\right)\longrightarrow e^{-v}
\]
uniformly in \(e\). The variable \(m_np(Y_e)\) is uniform on \((0,m_n)\), and therefore
\[
m_nq_e=\int_0^{m_n}\Pr\!\left(\max_{f\in F_e}Y_f\le t_n(v)\right)\,dv\longrightarrow\int_0^\infty e^{-v}\,dv=1.
\]
For domination, the graph induced by \(F_e\) contains a matching with at least \(c_\Delta m_n\) edges, for a positive constant depending only on \(\Delta\). Their Gaussian edge differences are independent, so the integrand is bounded by \((1-v/m_n)^{c_\Delta m_n}\le e^{-c_\Delta v}\). The proof is uniform over the choice of \(e\).

To add back the neighboring competitors, take \(a_n=b_n-3\log\log m_n/b_n\) for sufficiently large \(n\). If \(Y_e\) beats all distant edges but loses to a neighbor, either the distant maximum is below \(a_n\), or both \(Y_e\) and a neighboring \(Y_f\) exceed \(a_n\). The independent matching estimate bounds the first event by \(\exp[-c_\Delta(\log m_n)^3(1+o(1))]=o(1/m_n)\), while (1) bounds the second by \(O_\Delta(m_n^{-4/3}(\log m_n)^{O(1)}))=o(1/m_n)\). It follows that
\[
\sup_{e\in E(G_n)}\left|m_n\Pr(Y_e=M_n)-1\right|\longrightarrow0.
\]
Almost-sure uniqueness follows from continuous Gaussian differences. Reversing the Gaussian vector exchanges the two orientations of each winning edge, each with equal probability. Thus every oriented root has spherical normal-cone angle \(\Pr(Y_e=M_n)/2\), proving the second boxed conclusion.

**Step 4: hub counterregime.** In the star with center coordinate \(g_0\) and \(n-1\) leaves, the largest and the negative of the smallest leaf Gaussian are both \(c_n+o_{\Pr}(1)\). Therefore
\[
\max_{1\le i<n}|g_0-g_i|=c_n+|g_0|+o_{\Pr}(1).
\]
Again \(R_n=1+O_{\Pr}(n^{-1/2})\), and \(c_n/\sqrt n\to0\). The exact Gaussian width representation proves the folded-normal limit.

## Verification

A standalone NumPy/SciPy checker, `geometry_gumbel_checker.py`, regenerates the finite diagnostics in `geometry_gumbel_checks.json`. It compared direct signed-root vertex support calculations with the edge-difference formula in 508 cases, with maximum discrepancy zero at recorded floating precision. At \(n=1400\), simulated distribution functions at normalized zero for paths, cycles and cubic graphs were respectively 0.3804, 0.3539 and 0.3825, versus the Gumbel prediction \(e^{-1}\approx0.3679\); the star yielded 0.0254 against the limiting folded-normal value 0. A separate 130,000-direction simulation of the 72-vertex path gave all edge winning frequencies between 0.01333 and 0.01524, versus \(1/71\approx0.01408\). These finite observations are diagnostics, not proofs of the limits. The proof above is analytical and requires no numerical certificate.

## Relationship to prior work

Chen, Davis and Korchevskaia (2021, arXiv:2107.12315) classify facet and face subgraphs of symmetric edge polytopes; their intrinsic graph-polytope construction supplies the primary geometric setting. D'Alì, Juhnke-Kubitzke, Köhne and Venturello (2022, arXiv:2201.09835) investigate Ehrhart \(\gamma\)-vectors and random-graph regimes. Braun, Bruegge and Kahle (2022, arXiv:2204.07239) investigate facet counts for random graphs and graph ensembles, including hubs. The width fluctuation law and uniform intrinsic spherical root angles here are different invariants: they depend on Gaussian directional exposure rather than the number or combinatorial structure of facets. The Poisson/factorial-moment argument draws on standard extreme-value reasoning but establishes the graph-uniform geometric conclusion with explicit normalization and the contrasting hub law.

## Limitations

The result applies to deterministic simple connected bounded-degree graph sequences in the inherited Euclidean metric. No claim is made for every graph with growing maximum degree, weighted edges, arbitrary affine coordinate changes, or general matroid representations. The arguments prove weak convergence and asymptotic angular proportions, not an optimal finite-sample rate, sharp asymptotic angular correction for any individual edge, or convergence of all moments. More general Gaussian local-dependence extreme-value results may overlap probabilistic subarguments; the novelty assessment concerns the combined precise polytope-width and normal-cone claims, and remains subject to independent bibliographic review.

## References

1. Tianran Chen, Robert Davis and Evgeniia Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, first public version 2021-07-26, https://arxiv.org/abs/2107.12315.
2. Alessio D'Alì, Martina Juhnke-Kubitzke, Daniel Köhne and Lorenzo Venturello, *On the gamma-vector of symmetric edge polytopes*, arXiv:2201.09835, first public version 2022-01-24, https://arxiv.org/abs/2201.09835.
3. Benjamin Braun, Kaitlin Bruegge and Matthew Kahle, *Facets of Random Symmetric Edge Polytopes, Degree Sequences, and Clustering*, arXiv:2204.07239, first public version 2022-04-14, https://arxiv.org/abs/2204.07239.
