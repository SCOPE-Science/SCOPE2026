# Sharp weighted-degree bound and bipartite rigidity for graph-Sobolev truncation

## Finding
Let \(G=(V,E,w)\) be any finite undirected graph with \(|V|\ge2\), no loops, and strictly positive weights \(w_{ij}=w_{ji}>0\) on its edges. Fix \(\gamma>0\), equip real signals with
\[
\|f\|_{G,\gamma}^{2}=\sum_{i\in V}f_i^{2}+\gamma\sum_{\{i,j\}\in E}w_{ij}(f_i-f_j)^{2},
\]
and apply coordinatewise positive-part truncation \(R(f)_i=\max\{f_i,0\}\). Write \(L\) for the weighted graph Laplacian, \(A=I+\gamma L\), and \(\Delta=\max_{i\in V}\sum_j w_{ij}\). For every nonempty proper \(S\subset V\), write \(T=V\setminus S\), let \(W_{ST}=(w_{ij})_{i\in S,j\in T}\), and define
\[
\rho(S)=\gamma\left\|A_{SS}^{-1/2}W_{ST}A_{TT}^{-1/2}\right\|_{2\to2}.
\]
All these values are strictly below \(1\). The **exact graph-specific two-point modulus** is
\[
\operatorname{Lip}_{G,\gamma}(R)
=\max\left\{1,\max_{\varnothing\ne S\subsetneq V}\frac{1}{\sqrt{1-\rho(S)^{2}}}\right\}.
\]
In particular, the **sharp universal weighted-degree bound** is
\[
\boxed{\ \operatorname{Lip}_{G,\gamma}(R)
\le \frac{1+\gamma\Delta}{\sqrt{1+2\gamma\Delta}}\ }.
\]
If \(\Delta>0\), equality holds **if and only if** at least one connected component of \(G\) is bipartite and every vertex in that component has weighted degree exactly \(\Delta\). On a connected graph with an edge, equality therefore characterizes weighted-regular bipartite graphs. For every prescribed \(\gamma>0\) and \(\Delta>0\), a two-vertex edge of weight \(\Delta\) attains the bound. Every graph containing an edge has \(\operatorname{Lip}_{G,\gamma}(R)>1\), although \(\|R(f)\|_{G,\gamma}\le\|f\|_{G,\gamma}\) holds for every signal \(f\). The exact two-point modulus is attained by a pair of distinct finite signals within a common open sign orthant.

**Exact irregular-star contrast.** For the unit-weight star with one hub and \(n\ge1\) leaves, the exact modulus specializes to
\[
\boxed{\ \operatorname{Lip}_{K_{1,n},\gamma}(R)
=\left(1+\frac{n\gamma^2}{1+(n+1)\gamma}\right)^{1/2}.\ }
\]
For fixed \(\gamma>0\) this converges to \(\sqrt{1+\gamma}\) as \(n\to\infty\), whereas the universal maximum-degree bound for this same star grows on the order of \(\sqrt{\gamma n/2}\). This demonstrates the substantial role of graph regularity in determining two-point stability.

## Assumptions and scope
All vector spaces are real. Vertex masses are one; edge weights are positive and may vary. A disconnected graph is allowed, as are isolated vertices. The weighted degree is \(d_i=\sum_{j:\{i,j\}\in E}w_{ij}\), so the same \(\Delta\) is used for every component. Each principal submatrix of the positive-definite matrix \(A=I+\gamma L\) is positive definite. The operator norm \(\|\cdot\|_{2\to2}\) is Euclidean spectral norm. On an edgeless graph the exact Lipschitz modulus is \(1\) and the degree bound has equality for trivial reasons; the nontrivial equality characterization assumes \(\Delta>0\).

## Proof
**1. Reduction to coordinate masks.** For any \(S\subseteq V\) let \(D_S\) be the diagonal matrix with diagonal entries one on \(S\) and zero elsewhere. The map \(R\) is linear and equal to \(D_S\) on the open orthant with positive coordinates exactly on \(S\). A line segment between two vectors crosses finitely many coordinate hyperplanes (unless it lies in them; then use continuity), so integrating along the segment gives
\[
\operatorname{Lip}_{G,\gamma}(R)=\max_{S\subseteq V}\|D_S\|_{A\to A},\quad
\|M\|_{A\to A}=\sup_{h\ne0}\frac{\sqrt{h^{\mathsf T}M^{\mathsf T}AMh}}{\sqrt{h^{\mathsf T}Ah}}.
\]
Conversely, for a fixed \(S\), choose a base point strictly inside its open orthant and a maximizing direction for \(D_S\). Two sufficiently close distinct points in that orthant have exactly the ratio \(\|D_S\|_{A\to A}\). Since finitely many masks occur, global attainment follows.

**2. Exact block spectral identity.** For a nontrivial cut \(S,T\), put \(X=A_{SS}\), \(Y=A_{TT}\), and \(B=\gamma W_{ST}\). Relative to the partition, \(A=\left(\begin{smallmatrix}X&-B\\-B^{\mathsf T}&Y\end{smallmatrix}\right)\). For fixed \(u\in\mathbb R^{S}\), minimizing \(\|(u,v)\|_A^{2}\) over \(v\in\mathbb R^{T}\) gives the unique minimizer \(v=Y^{-1}B^{\mathsf T}u\) and denominator \(u^{\mathsf T}(X-BY^{-1}B^{\mathsf T})u\). Consequently,
\[
\|D_S\|_{A\to A}^{2}
=\sup_{u\ne0}\frac{u^{\mathsf T}Xu}{u^{\mathsf T}(X-BY^{-1}B^{\mathsf T})u}
=\frac{1}{1-\|X^{-1/2}BY^{-1/2}\|_{2\to2}^{2}}.
\]
The block Schur complement is positive definite because \(A\) is, proving \(0\le\rho(S)<1\) and the first displayed formula.

**3. Universal weighted-degree estimate.** For a cut define its crossing weighted degrees \(c_i=\sum_{j\in T}w_{ij}\) for \(i\in S\), and \(c_j=\sum_{i\in S}w_{ij}\) for \(j\in T\). The block matrices decompose as
\[
X=I+\gamma\operatorname{diag}(c_i)+\gamma L_{G[S]},\qquad
Y=I+\gamma\operatorname{diag}(c_j)+\gamma L_{G[T]}.
\]
The induced-subgraph Laplacians are positive semidefinite. Weighted edgewise Cauchy–Schwarz yields, for every \(u,v\),
\[
|u^{\mathsf T}W_{ST}v|
\le\bigl(\sum_{i\in S}c_i u_i^2\bigr)^{1/2}
\bigl(\sum_{j\in T}c_j v_j^2\bigr)^{1/2}.
\]
Since \(0\le c_i\le\Delta\), we have the scalar inequality \(c_i\le\frac{\Delta}{1+\gamma\Delta}(1+\gamma c_i)\). Together these imply
\[
\gamma|u^{\mathsf T}W_{ST}v|
\le \frac{\gamma\Delta}{1+\gamma\Delta}
\sqrt{u^{\mathsf T}Xu}\sqrt{v^{\mathsf T}Yv}.
\]
Thus \(\rho(S)\le\gamma\Delta/(1+\gamma\Delta)\). Substitution in the block identity gives precisely the claimed sharp degree bound.

**4. Equality and rigidity.** Suppose \(\Delta>0\) and a nontrivial cut has equality in the bound for \(\rho(S)\). In finite dimensions there exist nonzero vectors \(u,v\) attaining the cross-block norm. Replacing them by their absolute values cannot decrease the nonnegative crossing pairing and cannot increase their within-part quadratic forms, so nonnegative maximizers may be taken. Equality in the degree inequality forces every vertex with \(u_i>0\) or \(v_j>0\) to have crossing weighted degree \(c=\Delta\). Such a vertex has no same-side neighbors, and every neighbor across the cut must have a positive maximizing coefficient: equality in the weighted edge Cauchy–Schwarz condition forces the two edge-indexed vectors to be positive scalar multiples. Iterating along edges shows that the whole connected component containing a positive coordinate has all its vertices on opposite sides of a bipartition, all of weighted degree exactly \(\Delta\). Conversely, if a component is bipartite and weighted \(\Delta\)-regular, the cut separating its parts has \(X=(1+\gamma\Delta)I\) and \(Y=(1+\gamma\Delta)I\) on that component. The crossing weighted adjacency has singular value \(\Delta\), with constant singular vectors on the two sides. Hence \(\rho(S)=\gamma\Delta/(1+\gamma\Delta)\) and the upper bound is attained. Other components do not affect the maximizing direction.

**5. One-point versus two-point behavior.** Since \(t\mapsto\max(t,0)\) is \(1\)-Lipschitz and vanishes at the origin, every individual squared coordinate and every weighted squared edge difference weakly decreases under truncation. This gives \(\|R(f)\|_{G,\gamma}\le\|f\|_{G,\gamma}\). If some edge crosses a cut, \(W_{ST}\ne0\) and \(\rho(S)>0\), so the two-point modulus is strictly larger than \(1\). In particular the failure of two-point nonexpansiveness is not in conflict with the Dirichlet-form normal-contraction property.

**6. Exact star calculation.** Number the hub by \(0\) and the leaves by \(1,\ldots,n\), with every edge of weight one. By cut complementation, take a cut with \(k\) leaves separated from the hub, where \(0\le k\le n\). The off-diagonal block has rank one, and its size is \(k\) copies of \(\gamma\) joining those leaves to the hub. The separated-leaf principal block is \((1+\gamma)I_k\). The other block contains the hub, with diagonal entry \(1+n\gamma\), and the remaining \(n-k\) leaves, each of diagonal entry \(1+\gamma\) and joined to the hub by an entry \(-\gamma\). Its inverse hub-to-hub entry, by eliminating the remaining leaves, is
\[
\left(1+n\gamma-\frac{(n-k)\gamma^2}{1+\gamma}\right)^{-1}
=\frac{1+\gamma}{1+(n+1)\gamma+k\gamma^2}.
\]
Thus
\[
\rho(S)^2=\frac{k\gamma^2}{1+(n+1)\gamma+k\gamma^2},
\qquad
\|D_S\|_{A\to A}^2=1+\frac{k\gamma^2}{1+(n+1)\gamma}.
\]
This is strictly increasing with \(k\), so \(k=n\) yields the asserted star formula. Its limiting value and the different maximum-degree-bound growth follow by elementary division of numerator and denominator by \(n\).

## Verification
Run `python checker.py` with NumPy and SciPy. The self-contained script constructs multiple weighted and unweighted graphs and compares the generalized-eigenvalue mask modulus directly against the independent block-Schur formula for every sign mask, as well as checking the universal degree bound. It also tests equality on bipartite regular graphs, strictness on odd cycles, and the exact star formula by enumerating all masks. The reported computation comprises 3,056 mask comparisons plus the star regression checks. These finite tests are reproducibility diagnostics; the proof above establishes the theorem for all finite graphs and positive edge weights.

## Relationship to prior work
Keller and Lenz (arXiv:0904.2985), in their discussion of regular graph Dirichlet forms and normal contractions, formulate the classical **one-point** inequality \(Q(Cf)\le Q(f)\). Hinz and Teplyaev (arXiv:1511.08499) discuss the analogous property and approximation by finite weighted graph energies. Cai and Wang (arXiv:2006.13318), Lemma 3.3, show that ReLU decreases the Dirichlet energy of an individual graph signal. None of these one-point conclusions implies a two-input Lipschitz constant, much less the exact cut spectral formula, the sharp weighted-degree envelope, or the bipartite weighted-regular equality classification. The previously derived complete-graph truncation modulus covers a single dense graph family and does not imply the universal equality classification. The strengthened Cauchy–Schwarz framework surveyed by Eijkhout and Vassilevski (1991) already covers general block-energy angle estimates; the cut-Schur identity is an elementary specialization, not a claimed discovery. Likewise a classical spectral Kantorovich estimate gives the *numerical shape* of the universal upper bound by combining the eigenvalue interval of \(I+\gamma L\) with a coordinate-projection estimate. The substantive graph-specific statements are the complete weighted-degree equality classification, exact cut-dependent nonlinear modulus, and the explicit irregular-star contrast; these are not stated in the inspected source material.

## Limitations
The exact star calculation illustrates why the sharp *degree-only* bound can be much too large on irregular connected graphs; computing the exact constant for a given graph can require maximization over cuts. The result assumes real scalar signals, a unit-mass vertex \(\ell^2\) term, finite graphs, and coordinatewise positive-part truncation. No corresponding sharp degree-only formula is asserted for arbitrary vertex masses, other nonlinearities, infinite graph domains, or nonquadratic energies. Although three relevant primary full texts and actual database searches were compared, equivalent unindexed formulations in the literature remain possible; mathematical originality has not been independently assessed.

## References
1. M. Keller and D. Lenz, *Dirichlet forms and stochastic completeness of graphs and subgraphs*, arXiv:0904.2985, first submitted 2009-04-20, https://arxiv.org/abs/0904.2985 . Relevant material: regular graph energy and normal contractions in Sections 1–2.
2. M. Hinz and A. Teplyaev, *Closability, regularity, and approximation by graphs for separable bilinear forms*, arXiv:1511.08499, first submitted 2015-11-26, https://arxiv.org/abs/1511.08499 . Relevant material: Sections 1 and 3–5.
3. V. Eijkhout and P. S. Vassilevski, *The Role of the Strengthened Cauchy–Buniakowskii–Schwarz Inequality in Multilevel Methods*, SIAM Review 33(3) (1991), 405–419, DOI:10.1137/1033098. The publicly accessible abstract and bibliographic summary, not its complete article, were read; its general algebraic perspective is acknowledged without any paper-wide noncoverage claim.
4. C. Cai and Y. Wang, *A Note on Over-Smoothing for Graph Neural Networks*, arXiv:2006.13318, first submitted 2020-06-23, https://arxiv.org/abs/2006.13318 . Relevant material: Lemma 3.3 and its proof.
