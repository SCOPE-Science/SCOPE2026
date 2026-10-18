# Geodesic-poset volume law and a counting-complexity barrier for Lipschitz dual balls

## Finding

Let \(G=(V,E,\ell)\) be a finite connected, simple, undirected graph with positive edge lengths, with distinct terminals \(u,v\). Suppose **every edge belongs to at least one shortest \(u\)-to-\(v\) path**. Write \(N=|V|\ge 3\), \(d=N-1\), \(L=d_G(u,v)\), and \(\ell_*=\min_{e\in E}\ell_e\). Orient each edge toward increasing distance from \(u\), and let \(P\) be the reachability poset on \(V\setminus\{u,v\}\). Denote its number of linear extensions by \(e(P)\).

For \(0\le t\le L\), define the anchored Lipschitz ball
\[
 B_G(t)=\bigl\{f\in\mathbb R^{V}:f(u)=0,\ |f(b)-f(a)|\le \ell_{ab}\ (ab\in E),\ |f(v)|\le t\bigr\},
\]
and let \(W_G(t)\) be its \(d\)-dimensional Lebesgue volume in the coordinates \((f(x))_{x\ne u}\). Equivalently, the last constraint adjoins a terminal edge of length \(t\), and for \(t>0\) this is the Lipschitz dual unit ball of the induced shortest-path metric.

**Exact cap law.** For every real \(\varepsilon\) satisfying \(0\le\varepsilon\le\min\{L,2\ell_*\}\),
\[
\boxed{W_G(L)-W_G(L-\varepsilon)=\frac{2e(P)}{d!}\,\varepsilon^d.}
\]
In particular, the first \(d-1\) left derivatives at the redundancy threshold \(t=L\) vanish. The nonzero exact degree-\(d\) coefficient records the entire geodesic reachability poset's linear-extension count.

**Restricted complexity consequence.** There is a polynomial-time construction from every nonempty height-two poset \(P\), with \(n\) elements and no isolated elements, to a connected unweighted bipartite graph \(H_P\) of diameter exactly \(3\), with terminals at distance \(3\), for which
\[
\boxed{\operatorname{vol}B_{H_P}(3)-\operatorname{vol}B_{H_P}(2)=\frac{2e(P)}{(n+1)!}.}
\]
Therefore exact evaluation of this **volume difference** is \(\#\mathrm P\)-hard under polynomial-time counting reductions even for this restricted graph class and a single length-\(2\) terminal shortcut. No \(\#\mathrm P\)-membership assertion is made for volume evaluation.

## Assumptions and scope

All graph weights are strictly positive, all graphs finite and simple, and volumes use anchored vertex coordinates rather than the Euclidean measure in the zero-sum hyperplane. The geometric cap law requires each *original* edge to lie on a shortest terminal path. It does not apply without modification to extraneous edges or vertices. The bound \(\varepsilon\le 2\ell_*\) ensures the upper half of each Lipschitz edge inequality is inactive in the cap; it need not be sharp for a particular graph. The theorem concerns real Lipschitz dual balls. For the complexity consequence, the input consists of an explicitly represented height-two poset and the output is an exact rational volume difference.

## Proof

**1. Geodesic orientation.** Define \(\phi(x)=d_G(u,x)\). An edge \(ab\) lying on a shortest \(u\)-to-\(v\) path has, after orienting it \(a\to b\),
\[
 \phi(b)-\phi(a)=\ell_{ab}>0.
\]
Consequently the orientation is acyclic, every vertex lies on a directed terminal path, and its endpoints are the unique source \(u\) and sink \(v\). In particular \(\phi(u)=0\), \(\phi(v)=L\), and reachability of internal vertices defines a finite poset \(P\).

**2. A top cap is an order-polytope cone.** Since the edge constraints alone imply \(|f(v)|\le L\), the part removed by imposing \(|f(v)|\le L-\varepsilon\) is the union (up to measure-zero boundaries) of the positive and negative terminal caps. Central symmetry makes their volumes equal. On the positive cap, use
\[
  s=L-f(v),\qquad z_x=\phi(x)-f(x),\quad z_u=0,\quad z_v=s.
\]
Here \(0\le s\le\varepsilon\). Along every directed edge \(a\to b\), the Lipschitz inequality becomes
\[
 0\le z_b-z_a\le 2\ell_{ab}.
\]
Directed terminal paths force \(0\le z_x\le s\) for every internal vertex. As \(s\le\varepsilon\le2\ell_*\), the upper edge bounds are automatic. The remaining conditions are precisely
\[
 z_a\le z_b\quad\text{when }a\le_P b,
 \qquad 0\le z_x\le s\quad(x\in P).
\]
Thus each fixed-\(s\) section is exactly \(s\mathcal O(P)\), where \(\mathcal O(P)\) is Stanley's order polytope. This affine change of vertex coordinates has absolute Jacobian one: the internal coordinates are translated and sign-reversed, and the terminal variable is changed from \(f(v)\) to \(s\). Therefore the positive cap volume is
\[
 \int_0^{\varepsilon}s^{N-2}\operatorname{vol}_{N-2}(\mathcal O(P))\,ds.
\]
Stanley's elementary linear-extension triangulation gives \(\operatorname{vol}_{N-2}(\mathcal O(P))=e(P)/(N-2)!\). Integrating and doubling proves the exact formula \(2e(P)\varepsilon^{N-1}/(N-1)!\) on the full stated range. At \(\varepsilon=0\) the equality holds by continuity. Since \(e(P)>0\), the degree-\(d\) coefficient is nonzero.

**3. Bipartite diameter-three realization.** Let \(P\) be a height-two poset without isolated elements. Partition its elements into the minimal set \(A\) and maximal set \(B\); these are disjoint and every vertex has a comparable partner. Make an unweighted graph on \(A\cup B\cup\{u,v\}\) with exactly the edges \(ua\) for \(a\in A\), \(ab\) whenever \(a<_P b\), and \(bv\) for \(b\in B\). Its vertex bipartition is \((\{u\}\cup B, A\cup\{v\})\). Every edge belongs to an \(u,a,b,v\) path of length \(3\), and no shorter terminal path exists, so \(d(u,v)=3\). Two vertices within \(A\) have distance at most \(2\) via \(u\); likewise within \(B\) via \(v\). Any pair in opposite layers has distance at most \(3\): if not adjacent, it can travel via a comparable partner and one terminal. Distances from \(u\) or \(v\) are at most \(3\). Hence the graph diameter is exactly \(3\), and its reachability order on internal vertices is precisely \(P\). Here \(N=n+2\), \(d=n+1\), \(L=3\), and \(\ell_*=1\). Taking \(\varepsilon=1\) proves the displayed volume-difference identity.

**4. Counting reduction.** Dittmer and Pak proved that computing \(e(P)\) for height-two posets is \(\#\mathrm P\)-complete. Removing \(k\) isolated elements from such a poset with \(n\) elements leaves \(m=n-k\) elements and multiplies extension count by \(n!/m!\), so restriction to posets without isolates preserves \(\#\mathrm P\)-hardness. The graph construction has \(n+2\) vertices and at most quadratic many edges, with unit weights and a single optional shortcut of length \(2\). An oracle for the exact volume difference recovers \(e(P)=(n+1)!\Delta/2\) using polynomial-bit rational arithmetic. This is the asserted polynomial-time counting reduction.

## Verification

The accompanying `verify_caps.py` independently enumerates integer-valued feasible vertex potentials for \(14\) small cases and extracts the leading Ehrhart coefficient by exact forward differences. It includes arbitrary weighted geodesic-poset lifts and three unit-edge height-two constructions. The computed cap differences equal \(2e(P)/(n+1)!\) in every case using `fractions.Fraction`, with no floating-point tolerances. This is finite corroboration; the infinite-family proof is the exact coordinate argument above. Run with `python3 verify_caps.py`.

## Relationship to prior work

Stanley's order-polytope triangulation already establishes the linear-extension volume formula; no novelty is claimed for that identity. Sanyal and Stump's first poset-hypersimplex identifies another order-polytope section (Corollary 5.2); their result supplies related convex-geometric context, not the stated symmetric metric-graph terminal-cap law or restricted counting reduction. Dittmer and Pak's hardness theorem supplies the counting-complexity input rather than a new complexity classification of posets. Alexander and coauthors study the volume products and structure of finite Lipschitz-free spaces, rather than the terminal-edge cap response. A previously recorded complete-bipartite, one-stretched-edge volume response is an explicit special case: its factor \((p-1)!(q-1)!\) is the extension count of a two-chain-level internal order. The present claim adds arbitrary geodesic reachability posets and a restrictive \(\#\mathrm P\)-hardness realization; the earlier specialized formula is not presented as new.

## Limitations

The cap identity is local to the stated interval near terminal-edge redundancy; it does not evaluate the entire volume for arbitrary shortcuts. The constructed complexity result concerns an exact rational difference, not randomized approximation, additive error, or individual unrestricted full-volume evaluation. A general-purpose or differently named existing result could subsume the displayed cap law; the bibliography and comparison cannot certify universal absence from the literature.

## References

- R. P. Stanley, *Two Poset Polytopes*, Discrete & Computational Geometry **1** (1986), 9–23. Classical order-polytope volume triangulation.
- R. Sanyal and C. Stump, *Lipschitz Polytopes of Posets and Permutation Statistics*, arXiv:1703.10586v1 (first public version, 2017-03-30), especially Corollary 5.2. https://arxiv.org/abs/1703.10586
- S. Dittmer and I. Pak, *Counting Linear Extensions of Restricted Posets*, arXiv:1802.06312v1 (first public version, 2018-02-17), Theorem 1.1. https://arxiv.org/abs/1802.06312
- M. Alexander, M. Fradelizi, L. C. García-Lirola, and A. Zvavitch, *Geometry and Volume Product of Finite Dimensional Lipschitz-Free Spaces*, arXiv:1911.10642v1 (first public version, 2019-11-24). https://arxiv.org/abs/1911.10642
