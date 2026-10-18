# Three sampling limits and rare-collision localization for complete-bipartite graph associahedra

## Finding
Let \(p,q\ge1\), put \(n=p+q\), and let \(P_{p,q}\) be the standard graph associahedron of the complete bipartite graph \(K_{p,q}\), realized as the Minkowski sum of the coordinate simplices associated with all nonempty connected induced subsets. Sample exposed vertices by an isotropic Gaussian direction in its intrinsic Euclidean affine hull. A search-tree vertex has a **handle** of successive eliminated vertices and \(r\ge1\) unordered terminal leaves, all of the same bipartition color. Its Gaussian normal-cone probability is exactly
\[
\alpha_r=\frac{r!}{n!}.
\]
The number of vertices with this probability is
\[
N_{p,q}(r)=(n-r-1)!\left(p\binom qr\mathbf1_{r\le q}+q\binom pr\mathbf1_{r\le p}\right),
\qquad1\le r\le\max(p,q).
\tag{1}
\]
Consequently, the exact independent-Gaussian exposed-vertex collision probability is
\[
C_{p,q}=\frac{1}{(n!)^2}\sum_{r=1}^{\max(p,q)}N_{p,q}(r)(r!)^2.
\tag{2}
\]

For the balanced infinite family \(p=q=m\to\infty\), let \(R_m\) denote the number of terminal leaves of a sampled vertex, and write \(V_m\) for its total number of vertices. **Three sampling procedures produce three different limiting laws:**

1. Under one isotropic Gaussian objective,
\[
\Pr(R_m=r)\longrightarrow2^{-r},\qquad r=1,2,\ldots.
\tag{3}
\]
2. For a vertex chosen uniformly among all \(V_m\) vertices,
\[
\frac{V_m}{(2m)!}\longrightarrow e^{1/2}-1,
\qquad
\Pr(R_m=r)\longrightarrow\frac{2^{-r}}{r!(e^{1/2}-1)},
\quad r\ge1.
\tag{4}
\]
The latter is a positive Poisson variable of parameter \(1/2\), conditioned not to vanish.
3. Condition two independent Gaussian objectives on exposing the **same** vertex, and set \(D_m=m-R_m\) for that common vertex. Then
\[
C_{m,m}\sim\frac{2e(m!)^3}{((2m)!)^2},
\qquad
\Pr(D_m=k\mid\text{collision})\longrightarrow\frac{e^{-1}}{k!},
\quad k\ge0.
\tag{5}
\]
Thus a typical Gaussian-exposed vertex has a bounded number of leaves, whereas rare collisions concentrate on vertices having all but a bounded number of the \(m\) available terminal leaves. The collision-conditioned deficit tends to Poisson of parameter \(1\). In particular, comparison with uniform independent vertex sampling gives
\[
V_m C_{m,m}\sim2e(e^{1/2}-1)\frac{(m!)^3}{(2m)!}\longrightarrow\infty;
\]
two Gaussian directions collide increasingly more often than two uniformly sampled vertices relative to their respective sample spaces.

## Assumptions and scope
The vertex set of \(K_{p,q}\) is partitioned into two labeled, nonempty sets \(A,B\) with \(|A|=p\) and \(|B|=q\). A **tube** is a nonempty set \(S\subseteq A\sqcup B\) whose induced subgraph is connected; equivalently \(S\) is a singleton or intersects both \(A\) and \(B\). Write \(\Delta_S=\operatorname{conv}\{e_i:i\in S\}\). The polytope is
\[
P_{p,q}=\sum_{S:\,S\text{ a tube}}\Delta_S
\quad\subseteq\mathbb R^n.
\]
It lies in an affine translate of the hyperplane \(H=\{x:\sum_i x_i=0\}\). All Euclidean direction probabilities use the induced Euclidean inner product on \(H\). By isotropy, the direction of an independent standard Gaussian \(g\in\mathbb R^n\) after orthogonal projection to \(H\) is uniform on the sphere in \(H\); subtracting the common coordinate average does not change any coordinate ordering. Gaussian ties have probability zero.

A graph search tree is constructed recursively by selecting a root and then selecting a search tree for each connected component remaining after its removal. For \(K_{p,q}\), the induced remainder remains connected as long as both colors are present. At the first elimination of the final point from one color, the remaining \(r\) points of the opposite color form isolated terminal children. The resulting rooted tree has an ordered handle and unordered terminal leaves (a broom). The \(r\) terminal leaves are not ordered as tree vertices. This description also covers the case \(r=1\).

The integer \(m\) tends to infinity through positive integers. The limiting laws in (3)–(5) concern these specified sampling measures, not uniformly chosen random faces or intrinsic volumes of general, differently realized associahedra. A positive weighted sum of the connected simplices has the same nested normal fan; nevertheless the claim is stated for the displayed standard realization.

## Proof
**Step 1: Normal cones and permutation fibers.** For any Gaussian vector with distinct coordinates, the unique maximizer on \(\Delta_S\) is \(e_i\), where \(i\) has the largest coordinate among points of \(S\). Therefore the maximizer on \(P_{p,q}\) is the sum of these chosen simplex vertices. The established graph-associahedron nested-fan/search-tree correspondence identifies the common maximizer with the recursive selection of the maximum-coordinate root from each remaining connected component. In a biclique the recursion has exactly the broom form described above. All \(n!\) coordinate orders are equiprobable.

Fix a labeled broom with ordered handle and unordered terminal leaf set of cardinality \(r\). Exactly \(r!\) strict coordinate orders give that search tree: the handle must occur first in its fixed order, and the last \(r\) positions can be permuted arbitrarily. The nested fan distinguishes different search trees. Hence the normal-cone probability is \(r!/n!\), establishing the individual-angle assertion.

**Step 2: Exact multiplicities.** Suppose the color \(A\) is exhausted first, so \(r\) surviving leaves come from \(B\). Choose those leaves in \(\binom qr\) ways. The final handle entry must be any of the \(p\) members of \(A\). All remaining \(n-r-1\) handle entries can be ordered in \((n-r-1)!\) ways. This gives \(p\binom qr(n-r-1)!\) labeled brooms. Exchanging colors adds \(q\binom pr(n-r-1)!\). The cases are disjoint because the final handle vertex has opposite color to every remaining leaf. This yields (1), including all endpoint cases.

Every direction selects exactly one vertex, and the normal cones partition the sphere up to measure zero. Thus
\[
\sum_r N_{p,q}(r)r!=n!.
\]
For two independent Gaussian objectives, sum the squares of the vertex probabilities to obtain (2).

**Step 3: Ordinary sampling limits.** With \(p=q=m\), equation (1) becomes
\[
N_m(r)=2m\binom mr(2m-r-1)!,\qquad 1\le r\le m.
\tag{6}
\]
For each fixed positive \(r\), the probability of \(R_m=r\) under Gaussian selection is
\[
\frac{N_m(r)r!}{(2m)!}
=\frac{2m\,m!\,(2m-r-1)!}{(m-r)!(2m)!}
\longrightarrow2^{-r}.
\]
The candidate limit sums to one, proving convergence in distribution on positive integers; indeed convergence of all point masses to a probability distribution yields tightness.

For uniform vertex sampling,
\[
\frac{N_m(r)}{(2m)!}
=\frac1{r!}\frac{N_m(r)r!}{(2m)!}
\longrightarrow\frac{2^{-r}}{r!}.
\]
The summands are bounded by \(1/r!\), independently of \(m\), since \(N_m(r)r!/(2m)!\le1\). Dominated convergence over positive integers implies
\[
\lim_{m\to\infty}\frac{V_m}{(2m)!}
=\sum_{r\ge1}\frac{2^{-r}}{r!}=e^{1/2}-1.
\]
Dividing the individual vertex-count mass by the total proves (4).

**Step 4: Collision localization at the opposite endpoint.** Parameterize the second moment in (2) using \(r=m-k\) for \(0\le k\le m-1\). From (6), direct factorial cancellation yields
\[
C_{m,m}=\frac{2(m!)^3}{((2m)!)^2}
\sum_{k=0}^{m-1}a_m(k),
\qquad
a_m(k)=\frac{(m+k-1)!(m-k)!}{(m-1)!m!k!}.
\tag{7}
\]
In particular \(a_m(0)=1\), and for fixed \(k\ge0\), \(a_m(k)\to1/k!\). The ratio of consecutive summands is exactly
\[
\frac{a_m(k+1)}{a_m(k)}
=\frac{m+k}{(m-k)(k+1)}
\qquad(0\le k\le m-2).
\tag{8}
\]
For \(0\le k\le\lfloor m/2\rfloor-1\) this is at most \(3/(k+1)\), whence \(a_m(k)\le3^k/k!\) in that range. For \(\lfloor m/2\rfloor\le k\le m-2\), the ratio is at most one because this condition is equivalent to \(m-k-2\ge0\). Therefore the entire tail from \(\lfloor m/2\rfloor\) onward is bounded by
\[
m\,\frac{3^{\lfloor m/2\rfloor}}{\lfloor m/2\rfloor!}\longrightarrow0.
\]
The first segment is dominated by the summable factorial majorant \(3^k/k!\); consequently
\[
\sum_{k=0}^{m-1}a_m(k)\longrightarrow\sum_{k=0}^{\infty}\frac1{k!}=e.
\]
This proves the collision asymptotic in (5), with no inference from finite numerical experiments. Conditional on a collision, the probability of deficit \(k\) is exactly \(a_m(k)/\sum_j a_m(j)\), proving its Poisson limit.

## Verification
The standalone Python-standard-library script `check_angles.py` independently enumerates all strict coordinate orders for \((p,q)=(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3),(3,4)\). For each order it computes (i) the maximizing vertex directly by adding winners of all connected simplices, and (ii) its recursive broom search tree. It asserts equality of their equivalence classes, bijective distinct vertices, all multiplicities in (1), every \(r!\) permutation fiber, total cone mass one, and the collision formula (2), using exact rational arithmetic. No random samples or floating-point tests are used for these assertions. For \((p,q)=(3,4)\), for example, it computes exactly \(3702\) vertices and collision probability \(11/22050\).

As separate *illustrative* finite consistency checks, it evaluates the scaled sum in (7) for \(m=5,10,20,50\). They do not certify any infinite limit. The convergence, including the small-probability collision tail, is proved analytically in Step 4. Reproduce by running `python check_angles.py` from the package directory using Python 3, without third-party libraries; successful execution prints `ALL EXACT CHECKS PASSED`.

## Relationship to prior work
The polytope construction, nested normal fan, correspondence of graph-associahedron vertices with graph search trees, and fact that biclique search trees are brooms are established in the literature and are **not** presented as new. Cardinal, Pournin and Valencia-Pabon analyze diameters of these polytopes, including bicliques, rather than Euclidean Gaussian normal-cone angles. General braid-fan and deformation theory makes the permutation-fiber interpretation available in principle.

The further finite classification of vertex eccentricities for \(K_{4,4}\) records the same labeled broom types and their counts in that one case. It determines shortest-path distances in the flip graph, not normal-cone probabilities, balanced-family collision asymptotics, or their two different Poisson regimes. In particular, the distributions in (3)–(5) are asymptotic statements for all \(m\), not a restatement of a finite table. The mathematical contribution asserted here is the complete family-specific angular census together with the quantitatively different ordinary and collision-conditioned sampling limits.

## Limitations
The three sampling limits are proved for the balanced complete-bipartite family. No collision asymptotics are asserted for arbitrary nonbalanced growth paths, and no angles of individual lower-dimensional faces are classified. They rely on the standard nested-fan realization and on independent isotropic Gaussian directions; an arbitrary anisotropic directional measure need not obey the same laws. A bibliographic possibility remains that equivalent balanced asymptotics were published under random elimination-tree, braid-fan, or poset linear-extension terminology without being recovered in the checked literature.

## References
1. J. Cardinal, L. Pournin and M. Valencia-Pabon, *Diameter estimates for graph associahedra*, arXiv:2106.16130, first public 2021-06-30, Sections 1.1–1.2 and 6. https://arxiv.org/abs/2106.16130
2. V. Pilaud and coauthors, *Celebrating Loday's associahedron*, *Archiv der Mathematik* (2023), Sections 2 and 4 on braid/nested fans and simplex-sum realizations. https://doi.org/10.1007/s00013-023-01895-6
3. A. Gargantini, A. Pastine and P. Torres, *Effect of graph operations on graph associahedra*, arXiv:2406.06317, first public 2024-06-10; Section 4 concerns biclique flip distances, not Gaussian angles. https://arxiv.org/abs/2406.06317
