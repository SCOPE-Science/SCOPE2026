# Conditional geodesic attachment profiles in uniform labeled trees

## Finding

Let \(T_n\) be a uniformly random tree on \(\{1,\ldots,n\}\), and fix distinct marked vertices \(u,v\). Conditional on their graph distance \(D_n=k\), write their unique path, oriented from \(u\) to \(v\), as \(v_0,v_1,\ldots,v_k\). Define the **excess-degree profile** \(E_i\) by subtracting the number of path edges at each vertex:
\[
E_i=\deg_{T_n}(v_i)-\deg_{P}(v_i),\qquad 0\le i\le k.
\]
Thus \(E_i\) counts edges leaving the specified path at its \(i\)-th vertex, not all vertices in the off-path subtrees. Put \(\ell=k+1\), \(m=n-k-2\), and \(R=\sum_{i=0}^{k}E_i\).

**Finite exact law.** For every \(n\ge3\), \(1\le k\le n-2\), and complex \(z_i\),
\[
\boxed{\mathbb E\!\left[\prod_{i=0}^k z_i^{E_i}\mid D_n=k\right]
=\left(\frac{\sum_{i=0}^k z_i}{\ell}\right)
\left(1+\frac{\sum_{i=0}^k(z_i-1)}n\right)^m.}
\tag{1}
\]
In particular, conditional on \(D_n=k\),
\[
\boxed{R\overset{\mathrm d}{=}1+\operatorname{Bin}\!\left(m,\frac\ell n\right),\qquad
(E_0,\ldots,E_k)\mid(R=r)\sim\operatorname{Multinomial}\!\left(r;\frac1\ell,\ldots,\frac1\ell\right).}
\tag{2}
\]
At the boundary \(k=n-1\), all excess degrees and \(R\) are identically zero. For any distinct indices \(i,j\) and \(1\le k\le n-2\),
\[
\boxed{\operatorname{Cov}(E_i,E_j\mid D_n=k)
=-\frac1{\ell^2}-\frac{m}{n^2}<0.}
\tag{3}
\]

**Whole-path Gaussian limit.** Consider any sequence of integers \(n\to\infty\), \(1\le k=k_n\le n-2\), such that \(\ell_n=k_n+1\to\infty\),
\[
\frac{k_n}{n}\longrightarrow\theta\in[0,1],\qquad
\mu_n:=1+\frac{(n-k_n-2)(k_n+1)}n\longrightarrow\infty.
\tag{4}
\]
For \(0\le t\le1\), let \(C_n(t)=\sum_{0\le i<\lfloor t\ell_n\rfloor}E_i\). Then, conditional on \(D_n=k_n\), in the Skorokhod space \(D[0,1]\),
\[
\boxed{\left(\frac{C_n(t)-t\mu_n}{\sqrt{\mu_n}}\right)_{0\le t\le1}
\ \Longrightarrow\ \left(B(t)+t\sqrt{1-\theta}\,Z\right)_{0\le t\le1},}
\tag{5}
\]
where \(B\) is a standard Brownian bridge and \(Z\) is an independent standard normal variable. The limiting process is centered Gaussian with covariance
\[
\boxed{\operatorname{Cov}(G_\theta(s),G_\theta(t))=\min(s,t)-\theta st.}
\tag{6}
\]
For sublinear but diverging path length (\(\theta=0\)), the limit is standard Brownian motion. If \(k_n/n\to1\) while \(n-k_n\to\infty\), the limit is a standard Brownian bridge. Every intermediate \(0<\theta<1\) gives the specified continuous interpolation. The parameter \(\mu_n\to\infty\) is essential: a path leaving only finitely many vertices outside has no such Gaussian profile limit.

## Assumptions and scope

Trees are labeled and uniformly distributed over all \(n^{n-2}\) choices. Conditioning on \(D_n=k\) is well-defined for every \(1\le k\le n-1\). The orientation of the unique path is from the first fixed marked vertex to the second. The random profile counts direct off-path edges, **not** the sizes of descendant components or the total number of off-path vertices.

For \(n=2\), the unique tree is a spanning path and the excess profile is zero; the theorem's finite nonboundary formula applies from \(n=3\). In the functional statement, \(\theta=1\) is allowed only along sequences with \(\mu_n\to\infty\). Brownian motion and Brownian bridge are standard continuous Gaussian processes, and \(D[0,1]\) carries the \(J_1\) topology.

## Proof

**1. Weighted extension count.** For positive or formal vertex variables \(x_w\), the weighted Cayley identity is
\[
\sum_{T\text{ tree on }[n]}\prod_{\{a,b\}\in E(T)}x_ax_b
=\left(\prod_{w=1}^n x_w\right)\left(\sum_{w=1}^n x_w\right)^{n-2}.
\tag{7}
\]
For any fixed forest \(F\) with \(c\ge2\) connected components \(A_1,\ldots,A_c\), contract those components. An edge between contracted components \(A_p,A_q\) has total possible weight \((\sum_{a\in A_p}x_a)(\sum_{b\in A_q}x_b)\). Applying (7) to the contracted graph and retaining the prescribed edges of \(F\) yields
\[
\sum_{T\supset F}\prod_{\{a,b\}\in E(T)}x_ax_b
=\left(\prod_{\{a,b\}\in E(F)}x_ax_b\right)
\left(\sum_w x_w\right)^{c-2}\prod_{p=1}^c\left(\sum_{w\in A_p}x_w\right).
\tag{8}
\]
The contraction identity is an exact polynomial identity: a contracted tree together with one chosen original edge for every contracted edge uniquely reconstructs a full tree containing \(F\).

Fix a possible labeled path \(P\) of length \(k\) from \(u\) to \(v\). Set \(x_{v_i}=z_i\) along this path and all other \(x_w=1\). The components of \(P\) plus isolated vertices number \(c=n-k\); one has size \(\ell=k+1\) and the other \(n-\ell\) are singletons. Substituting in (8), then dividing by the value at every \(z_i=1\), gives exactly (1) for \(k\le n-2\). All ordered lists of intermediate vertices yield the same conditional polynomial. Since a tree has a unique path joining \(u\) and \(v\), averaging over path labels establishes the formula conditional merely on \(D_n=k\). For \(k=n-1\), the prescribed path already spans the tree, so no off-path edges exist.

**2. Binomial–multinomial representation and covariance.** The first factor in (1) is the probability-generating function of a single ball assigned uniformly among the \(\ell\) path sites. The second factor is the generating function of \(m\) independent trials, each landing at each particular path site with probability \(1/n\), or outside the path with probability \((n-\ell)/n\). This proves the distributional representation. The number of these latter trials landing anywhere on the path is \(\operatorname{Bin}(m,\ell/n)\), and conditioning on this number leaves independent uniform site labels. Adding the compulsory first uniform ball gives (2).

For distinct sites, the indicators of occupation by the same ball have covariance \(-1/\ell^2\) for the compulsory ball and \(-1/n^2\) for each further trial. Different trials are independent. This proves (3), including strictness. The variance of the total is
\[
\operatorname{Var}(R\mid D_n=k)=m\frac\ell n\left(1-\frac\ell n\right).
\tag{9}
\]

**3. Functional interpolation.** Under (4), put \(p_n=\ell_n/n\). Formula (2) gives \(R=1+\operatorname{Bin}(m,p_n)\) with \(\mathbb E R=\mu_n\) and
\[
\frac{\operatorname{Var}(R)}{\mu_n}
=\frac{\mu_n-1}{\mu_n}(1-p_n)\longrightarrow1-\theta.
\tag{10}
\]
Hence \(R/\mu_n\to1\) in probability. For \(\theta<1\), the standard triangular-array binomial central limit theorem gives \((R-\mu_n)/\sqrt{\mu_n}\Rightarrow\sqrt{1-\theta}\,Z\); when \(\theta=1\), the same convergence to zero follows directly from (10) and Chebyshev's inequality.

Given \(R=r\), the \(r\) attachment locations are independent uniform samples from the \(\ell_n\) ordered sites. Coupling each discrete site with the corresponding interval of a uniform \([0,1]\) point shows that its centered cumulative empirical process, divided by \(\sqrt r\), converges to a Brownian bridge by the empirical-process invariance principle. The coupling changes the centering by at most \(r/\ell_n\); after division by \(\sqrt{\mu_n}\) this is negligible, because \(\mu_n\le\ell_n+1\) and \(\ell_n\to\infty\). Since \(R/\mu_n\to1\), the random-index empirical bridge still converges to \(B\), asymptotically independently of \((R-\mu_n)/\sqrt{\mu_n}\); conditional sample-location laws do not otherwise depend on \(R\). Finally,
\[
C_n(t)-t\mu_n=[C_n(t)-tR]+t(R-\mu_n).
\]
Combining the bridge limit with (10) yields (5). Independence gives (6), so \(\theta=0\) yields Brownian-motion covariance and \(\theta=1\) the Brownian-bridge covariance. All convergences hold as processes with continuous limits, not merely at finitely many times.

## Verification

The accompanying standard-library Python program `verify.py` reconstructs every labeled tree from every Prüfer sequence through eight vertices. For each tree it finds the oriented path between two fixed labels by breadth-first search and records the entire off-path incident-degree vector. Exact rational comparisons against (1) and its multinomial coefficients, the distance count, the total attachment mean, and the pair covariance cover 280,392 trees and 487 assertions. Running `python verify.py` reproduces these finite checks.

Finite enumeration checks the finite exact law on small instances but does not prove the theorem for unrestricted \(n\). Equation (8), the categorical representation, and the functional central limit argument prove the general statements.

## Relationship to prior work

The weighted Cayley identity and the classical Moon–Pitman forest-extension enumeration underpin the exact calculation and are not asserted to be new. Earlier published work establishes the marginal conditional endpoint-degree distribution of a uniform labeled tree given the separation between fixed vertices; a marginal does not specify the complete profile along the intervening path.

Białas and Oleś (2010), and the expanded derivation in Oleś (2012), give asymptotic two-point degree correlations at fixed vertex separation in ensembles of random trees. Their uniform-tree specialization covers the limiting endpoint covariance \(-1/(k+1)^2\) for fixed \(k\). Neither that fixed-separation two-point law nor the classical forest count by itself states the entire random-length geodesic attachment empirical-process limit (5) with its macroscopic-length interpolation. The present contribution is the **whole-path conditional process description and its Gaussian interpolation**, not a claim to have originated Cayley's identity, standard multinomial sampling, Brownian bridges, or fixed-distance endpoint correlations.

Devroye and Janson (2008/2011) study path counts and distance profiles in conditioned Galton–Watson trees. Their topic is related but distinct from the conditional excess-degree empirical profile here.

## Limitations

Only uniform labeled trees are treated. The theorem describes direct side-edge incidences; it does not determine the sizes, shapes, or dependence of attached off-path subtrees. The Gaussian limits condition on distances that may be rare for a uniformly sampled tree; they are conditional statements and do not assert unconditional Brownian limits. The limit assumes diverging mean side incidence count and does not apply to an almost spanning path leaving only finitely many vertices off it.

A broad weighted forest enumeration implies the finite generating polynomial after specialization; thus that polynomial alone is not claimed as an independent advance. The possibility that a prior spine-decomposition or general conditioned-tree process theorem already implies the functional interpolation under alternate notation remains a historical-priority risk.

## References

1. J. Pitman, *Coalescent Random Forests*, University of California Berkeley Statistics Technical Report 457, first posted 1996-09-01, Sections 2 and 5. https://statistics.berkeley.edu/tech-reports/457
2. P. Białas and A. K. Oleś, “Long-range disassortative correlations in generic random trees,” arXiv:0909.2764 (first posted 2009-09-15), *Physical Review E* 81 (2010), 041136. https://arxiv.org/abs/0909.2764
3. A. K. Oleś, *Correlations in Random Graphs*, doctoral thesis, Jagiellonian University, Kraków (2012), Chapter 3, Sections 3.2–3.3, equations (3.34)–(3.37). https://fais.uj.edu.pl/documents/41628/ee7e15df-3c10-4e2b-8547-100653fbbdd0
4. L. Devroye and S. Janson, “Distances between pairs of vertices and vertical profile in conditioned Galton–Watson trees,” arXiv:0812.3326 (first posted 2008-12-17), *Random Structures & Algorithms* 38 (2011), 381–395. https://arxiv.org/abs/0812.3326
