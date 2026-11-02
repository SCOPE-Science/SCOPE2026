# A birthday bridge and a Gaussian–Rayleigh root-degree law for \(K_{2,n}\)

## Finding

For every integer \(n\ge1\), let \(G=K_{2,n}\), with hubs \(u,v\) and peripheral vertices \(w_1,\ldots,w_n\). Begin with the singleton rooted tree \(\{u\}\). Repeatedly choose **uniformly among graph edges with exactly one endpoint already in the tree**, adjoin the selected edge and its other endpoint, and continue until all vertices are present. Write \(\mathcal T_n\) for the resulting rooted spanning tree, \(D_n=\deg_{\mathcal T_n}(u)\), and \(K_n\) for the number of peripherals acquired before the other hub \(v\) first enters.

With the falling factorial \((n)_k=n(n-1)\cdots(n-k+1)\), the exact finite-size laws are
\[
\Pr(K_n=k)=\frac{k(n)_k}{n^{k+1}}\quad(1\le k\le n),\qquad
D_n\mid(K_n=k)\overset d=k+\operatorname{Bin}(n-k,\tfrac12).
\]
In particular the complete degree probability-generating function is
\[
\mathbb E[z^{D_n}]=\sum_{k=1}^{n}\frac{k(n)_k}{n^{k+1}}z^k
\left(\frac{1+z}{2}\right)^{n-k}.
\]
Writing \(R\) for the Rayleigh random variable with \(\Pr(R>r)=\exp(-r^2/2)\) for \(r\ge0\), and \(G\sim N(0,1)\) independent of \(R\), the joint, non-Gaussian fluctuation law is
\[
\boxed{\left(\frac{K_n}{\sqrt n},\frac{D_n-n/2}{\sqrt n}\right)
\ \Longrightarrow\ \left(R,\frac{R+G}{2}\right).}
\]
Consequently,
\[
\mathbb E D_n=\frac n2+\sqrt{\frac{\pi n}{8}}+o(\sqrt n),\quad
\frac{\operatorname{Var}(D_n)}{n}\longrightarrow\frac{6-\pi}{8},\quad
\Pr(D_n>n/2)\longrightarrow\frac12+\frac{1}{2\sqrt2}.
\]
For comparison, if \(D_n^{\mathrm U}\) is the degree of \(u\) in a **uniformly** sampled spanning tree of the same graph, then
\[
D_n^{\mathrm U}\overset d=1+\operatorname{Bin}(n-1,\tfrac12),
\qquad D_n\succeq_{\mathrm{st}} D_n^{\mathrm U},
\]
with strict stochastic dominance for every \(n\ge2\). In particular, its centered fluctuations converge to \(G/2\), and \(\Pr(D_n^{\mathrm U}>n/2)\to 1/2\).

## Assumptions and scope

The graph is finite, undirected, simple and complete bipartite; \(n\) is an integer at least one. A boundary edge is sampled uniformly at each discrete step, independently given the current tree. The root is one of the two degree-\(n\) vertices. The claimed stochastic comparison is only between this frontier-growth spanning tree and the uniform spanning tree **on this same graph**. No assumption of a uniform distribution over all trees is made for the frontier-growth process.

## Proof

**1. Exact bridge-entry law.** As long as \(v\) is absent and exactly \(k\) peripherals are present, all are attached to \(u\). The tree boundary has \(n-k\) edges from \(u\) to absent peripherals and \(k\) edges from existing peripherals to \(v\), for exactly \(n\) choices. For \(1\le k<n\), the next step adds another peripheral with conditional probability \((n-k)/n\); with probability \(k/n\) it instead adds \(v\). At \(k=n\) it adds \(v\) surely. The first peripheral is compulsory. Therefore, for \(1\le k\le n\),
\[
\Pr(K_n\ge k)=\prod_{j=1}^{k-1}\frac{n-j}{n}=\frac{(n)_k}{n^k},
\quad
\Pr(K_n=k)=\Pr(K_n\ge k)\frac{k}{n}.
\]
The survival law is exactly the classical birthday experiment's number of distinct draws before the first repeat (with the first repeated draw itself excluded). This identification is not claimed as new.

**2. Conditional parent law.** Condition on the full history at the instant \(v\) enters with \(K_n=k\). Each of the remaining \(n-k\) peripheral vertices has one boundary edge incident to \(u\) and one incident to \(v\). The next vertex is therefore uniform among the remaining peripherals, and its incident parent edge is an independent fair choice between \(u\) and \(v\). After that vertex is attached, the corresponding two edges cease to be eligible and the other pairs are unchanged. Iteration gives \(n-k\) independent fair parent choices. Hence the stated conditional binomial representation and generating function, with no approximation.

From conditional expectation and conditional variance,
\[
\mathbb E D_n=\frac{n+\mathbb E K_n}{2},\qquad
\operatorname{Var}(D_n)=\frac{n-\mathbb E K_n+\operatorname{Var}(K_n)}4.
\]

**3. Rayleigh scaling and independent Gaussian noise.** For any \(r\ge0\), set \(k=\lfloor r\sqrt n\rfloor+1\). Expanding the logarithm of the product in part 1 gives
\[
\log\Pr(K_n\ge k)=\sum_{j=0}^{k-1}\log(1-j/n)
=-\frac{k(k-1)}{2n}+O(k^3/n^2)\longrightarrow-r^2/2.
\]
The elementary bound \(\Pr(K_n\ge k)\le \exp[-k(k-1)/(2n)]\) gives bounded moments of every fixed order for \(K_n/\sqrt n\), allowing the first two moments to converge to those of \(R\): \(\mathbb ER=\sqrt{\pi/2}\) and \(\operatorname{Var}R=(4-\pi)/2\).

Let \(B_n\mid K_n\sim\operatorname{Bin}(n-K_n,1/2)\), and set \(Z_n=2(B_n-(n-K_n)/2)/\sqrt n\). Conditional on \(K_n\), its characteristic function is
\[
\mathbb E[e^{itZ_n}\mid K_n]
=\big(\cos(t/\sqrt n)\big)^{n-K_n}\longrightarrow e^{-t^2/2}
\]
in probability, because \(K_n/n\to0\) in probability. Since the conditional characteristic functions are bounded by one, multiplying by \(e^{isK_n/\sqrt n}\) and taking expectations proves joint convergence to independent \(R\) and \(G\). Finally,
\[
\frac{D_n-n/2}{\sqrt n}=\frac{K_n}{2\sqrt n}+\frac{Z_n}{2}.
\]
The mean and variance statements follow from the exact conditional formulas and uniform moment bounds. By continuity of the non-Gaussian limit,
\[
\lim_{n\to\infty}\Pr(D_n>n/2)
=\mathbb E\Phi(R)
=\frac12+\int_0^\infty\!e^{-r^2/2}\frac{e^{-r^2/2}}{\sqrt{2\pi}}\,dr
=\frac12+\frac1{2\sqrt2},
\]
where integration by parts against the Rayleigh density gives the middle equality.

**4. Uniform-tree comparison.** Every spanning tree of \(K_{2,n}\) has a unique peripheral whose two hub edges are included; all other peripherals each have exactly one included edge. Conversely, any one choice of bridging peripheral and any independent assignment of each remaining peripheral to one of the two hubs yields a spanning tree. Thus under the uniform measure the root degree is \(1+\operatorname{Bin}(n-1,1/2)\). To couple with frontier growth, take a realization of \(K_n\) and independent fair coins \(C_2,\ldots,C_n\). Set
\[
D_n=K_n+\sum_{j=K_n+1}^{n}C_j,
\qquad
D_n^{\mathrm U}=1+\sum_{j=2}^{n}C_j.
\]
Both have the required marginal laws and almost surely
\[
D_n-D_n^{\mathrm U}=K_n-1-\sum_{j=2}^{K_n}C_j\ge0.
\]
For \(n\ge2\), \(\Pr(K_n\ge2)>0\) and at least one of those initial fair coins is zero with positive probability, so the stochastic dominance is strict. The uniform-tree normal limit follows from the binomial central limit theorem.

## Verification

Run `python3 check_growth_k2n.py` with the Python standard library. It enumerates all boundary-edge choices exactly with rational probabilities on \(K_{2,n}\) for \(1\le n\le8\), independently checks the closed-form degree distribution, moments and stochastic dominance, verifies birthday-tail recurrences for \(1\le n\le69\), and performs bounded numerical scaling diagnostics. A local replay passed **2,541 exact/computational assertions**. These are finite sanity checks: the all-\(n\) assertions and distributional limit are established by the proof above, not inferred from enumerations or simulations.

## Relationship to prior work

Devroye, Dujmović, Frieze, Mehrabian, Morin and Reed (2017 preprint) define exactly this uniform-boundary-edge tree-growth process on general graphs and study its height and first-passage-percolation representation; the examined source does not present this \(K_{2,n}\) root-degree law. Arratia, Garibaldi and Kilian (2013) explicitly establish the already classical first-birthday-collision Rayleigh law; that component is used, not claimed as novel. Dong and Ge (2021) give spanning-tree counts on complete bipartite graphs for the uniform spanning-tree model; their uniform-tree results do not imply the nonuniform frontier-growth degree law without an additional distributional analysis. The new contribution is the exact bridge-conditioned degree mixture, its joint Gaussian–Rayleigh fluctuation limit and its stochastic comparison to uniform spanning trees. No historical uniqueness claim is made from unsuccessful searches alone.

## Limitations

The result concerns \(K_{2,n}\), a hub root and uniform boundary-edge growth. It neither determines root-degree laws on general \(K_{a,n}\) for \(a\ge3\) nor gives tree-height laws, temporal infection times, stochastic domination for all graph families, or a classification of the entire spanning-tree distribution. The Rayleigh birthday component and the uniform spanning-tree enumeration are established background results. Historical priority for this combined characterization is not independently certified.

## References

1. L. Devroye, V. Dujmović, A. Frieze, A. Mehrabian, P. Morin, B. Reed, *Notes on Growing a Tree in a Graph* (first posted 2017-07-01), https://arxiv.org/abs/1707.00083.
2. R. Arratia, S. Garibaldi, J. Kilian, *Asymptotic distribution for the birthday problem with multiple coincidences, via an embedding of the collision process* (2013), https://arxiv.org/abs/1310.7055.
3. F. Dong, J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest* (first posted 2021-03-09), https://arxiv.org/abs/2103.05294.
4. M. Camarri, J. Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities* (2000), https://doi.org/10.1214/EJP.v5-58.
