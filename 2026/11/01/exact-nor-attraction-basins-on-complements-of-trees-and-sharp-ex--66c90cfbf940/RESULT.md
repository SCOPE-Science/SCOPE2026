# Exact NOR attraction basins on complements of trees and sharp extremizers

## Finding

**Theorem.** Let \(T\) be any finite simple tree with \(n\ge4\) vertices, let \(G=\overline T\) be its simple graph complement, and let a synchronous binary open-neighborhood NOR update act on subsets \(S\subseteq V(T)\) by
\[
 F(S)=\{v\in V(T):N_G(v)\cap S=\varnothing\}.
\]
Write \(d_v=\deg_T(v)\), let \(L=\{v:d_v=1\}\) be the leaves, and put \(I=V(T)\setminus L\). For an eventual periodic orbit \(\mathcal O\), its **basin** \(\mathcal B(\mathcal O)\) comprises every initial subset whose forward orbit eventually enters \(\mathcal O\), including the periodic states themselves.

Every state becomes periodic after at most one update, and this upper bound is attained for every \(n\ge4\). There are exactly \(n-1\) fixed configurations, corresponding to the edges of \(T\). More precisely, the entire orbit and attraction-basin classification is as follows.

**Nonstar trees.** If \(T\not\cong K_{1,n-1}\), every edge \(uv\in E(T)\) yields the fixed configuration \(\{u,v\}\), with
\[
 |\mathcal B(\{u,v\})|=1+\mathbf1_{\{d_u=1\}}+\mathbf1_{\{d_v=1\}}.
\]
There are exactly \(|I|+1\) primitive two-cycle orbits: one \(\mathcal U_T=\{\varnothing,V(T)\}\), and one \(\mathcal O_v=\big\{\{v\},N_T[v]\big\}\) for each \(v\in I\). Their exact basin sizes are
\[
 |\mathcal B(\mathcal O_v)|=2^{d_v+1}-2d_v-1,\qquad
 |\mathcal B(\mathcal U_T)|=2^n-2n+1-\sum_{v\in I}(2^{d_v+1}-2d_v-2).
\]
The total number of periodic states is \(n+2|I|+1\).

**Stars.** If \(T\cong K_{1,n-1}\), with center \(c\), the \(n-1\) edge configurations \(\{c,u\}\) are fixed, each with basin size two. There is just one primitive two-cycle, \(\mathcal U_T=\big\{\{c\},V(T)\big\}\), with
\[
 |\mathcal B(\mathcal U_T)|=2^n-2n+2.
\]
The number of periodic states is \(n+1\).

**Sharp structural extremizers.** In every tree with \(n\ge4\), \(\mathcal U_T\) is the *unique orbit with the largest basin*. Writing \(B_T=|\mathcal B(\mathcal U_T)|\),
\[
 \boxed{2^{n-1}-3\ \le B_T\ \le 2^n-2n+2.}
\]
Equality on the left holds exactly for the **broom**, namely the tree whose degree sequence is \((n-2,2,1,\ldots,1)\); equality on the right holds exactly for the star. Among nonstar trees, the sharper bound is
\[
 \boxed{2^{n-1}-3\ \le B_T\ \le 2^n-4n+5,}
\]
where equality on the right holds exactly for the path \(P_n\). At \(n=4\) the broom and path coincide. In all trees, the total number of initial states eventually reaching *any* fixed point is exactly \(n-1+|L|\). Hence uniform random initial states have fixation probability \((n-1+|L|)/2^n\), even though the recurrent set may contain many distinct cycles.

## Assumptions and scope

The underlying tree is finite, connected, simple, undirected, and has at least four vertices; states are binary, updates are simultaneous and deterministic, and **only open neighbors in the complement graph** are consulted. An isolated vertex of \(G\) updates to one, using the usual empty-product convention. Temporal phases are counted as one primitive two-cycle orbit, but all labelled initial configurations are counted separately. The bounds compare trees of the same labelled vertex count, independent of vertex labels; no random-tree model is assumed.

The stated theorem is not for self-inclusive NOR, asynchronous updates, directed graphs, arbitrary Boolean thresholds, or complements of graphs containing cycles. In particular, the isolated-vertex convention matters for complements of stars.

## Proof

**1. A symmetric antitone closure identity.** For any finite simple undirected graph \(G\), the map \(F(S)=\{v:N_G(v)\cap S=\varnothing\}\) is antitone. Symmetry gives \(S\subseteq F^2(S)\): if \(v\in S\) then each \(u\in F(S)\) is a nonneighbor of \(v\), hence \(v\in F^2(S)\). Applying antitonicity yields \(F^3(S)\subseteq F(S)\). Applying the same inflation to \(F(S)\) gives the reverse inclusion. Thus \(F^3=F\), so every image state is periodic with least period one or two. This universal fact supplies only the time bound, not the tree-specific classification or basin counts.

**2. Closed-neighborhood intersection for the tree.** Since \(N_G(v)=V(T)\setminus N_T[v]\),
\[
 F(S)=\{v:S\subseteq N_T[v]\}.
\]
For two distinct tree vertices \(u,v\), the sets \(N_T[u]\cap N_T[v]\) are \(\{u,v\}\) when \(u,v\) are adjacent, the singleton middle vertex when their distance is two, and empty otherwise. The first case uses the absence of triangles and the second the absence of four-cycles. Consequently, no three-element set can have two distinct common closed-neighborhood centers. Directly:
\[
 F(\varnothing)=V(T),\qquad F(\{v\})=N_T[v],\qquad F(\{u,v\})=
 \begin{cases}
  \{u,v\},&uv\in E(T),\\
  \{w\},&\operatorname{dist}_T(u,v)=2\text{ with middle }w,\\
  \varnothing,&\operatorname{dist}_T(u,v)\ge3.
 \end{cases}
\]
For \(|S|\ge3\), the image is either empty or a singleton \(\{v\}\), with the latter occurring exactly when \(S\subseteq N_T[v]\).

**3. Periodic configurations.** When \(T\) is not a star, it has no universal vertex, so \(F(V(T))=\varnothing\). Each edge pair \(\{u,v\}\) is fixed. Each nonleaf \(v\) has \(|N_T[v]|\ge3\), so the preceding intersection property gives \(F(N_T[v])=\{v\}\), and \(F(\{v\})=N_T[v]\). A leaf singleton instead maps to its edge pair, already fixed. These exhaust the possible outputs in step 2 and hence all periodic states by \(F^3=F\). For a star, its center \(c\) is universal in \(T\), so \(F(V(T))=\{c\}\). Its complement consists of an isolated center and a clique on the leaves: the clique output is all leaves from the empty clique support, the same singleton from a singleton support, and empty from any support of at least two leaves. This proves the stated star classification.

**4. Exact inverse fibers and basins.** Assume first that \(T\) is not a star. The inverse fiber of \(V(T)\) is just \(\{\varnothing\}\). For every nonleaf \(v\), the inverse fiber of \(N_T[v]\) consists of the single state \(\{v\}\); indeed all other possibilities from step 2 have smaller images or are the whole vertex set. For an edge \(uv\), the inverse fiber of \(\{u,v\}\) contains that pair and, if present, the singleton corresponding to its leaf endpoint. Its size is therefore \(1+\mathbf1_{\{d_u=1\}}+\mathbf1_{\{d_v=1\}}\).

For an internal vertex \(v\) of degree \(d\), the inverse fiber of \(\{v\}\) consists of (i) subsets of \(N_T[v]\) of size at least three, and (ii) pairs of distinct neighbors of \(v\). These families are disjoint and have total size
\[
 \sum_{j=3}^{d+1}\binom{d+1}{j}+\binom d2
 =2^{d+1}-2d-2.
\]
Every other initial state maps to the empty set. There are \(|I|\) singleton nonleaf fibers, \(|I|\) one-element inverse fibers of large closed stars, and edge fibers totalling \((n-1)+|L|\). The inverse fiber of \(\varnothing\) consequently has size
\[
 2^n-\bigl[1+|I|+(n-1)+|L|+\sum_{v\in I}(2^{d_v+1}-2d_v-2)\bigr]
 =2^n-2n-\sum_{v\in I}(2^{d_v+1}-2d_v-2).
\]
Since every state is periodic immediately after one update, the basin of a fixed point equals its inverse fiber, and the basin of a two-cycle equals the union of the two phase fibers. Adding those phase-fiber counts proves all nonstar formulas. For a star, the isolated center in the complement has unrestricted initial bit; each fixed singleton-leaf clique state therefore has two predecessors. The remaining \(2^n-2(n-1)\) states enter its only two-cycle. The fixed-basin total in either case is the sum \((n-1)+|L|\).

**5. Sharp extremal basins.** For nonstar trees set \(e_v=d_v-1\ge0\), so \(\sum_v e_v=n-2\), with at least two positive terms. Put \(\psi(e)=2^{e+2}-2e-4\), where \(\psi(0)=0\). Its discrete increments are \(\psi(e+1)-\psi(e)=2^{e+2}-2\), strictly increasing with \(e\). Thus under the fixed excess sum, \(\sum_v\psi(e_v)\) is minimized uniquely when every positive excess equals one, which is the path degree sequence, and maximized uniquely when the positive excesses are \(n-3\) and one, which is the broom degree sequence. Their respective values are \(2(n-2)\) and \(2^{n-1}-2n+4\). Substitution into the basin formula yields exactly the nonstar bounds, with the asserted equality cases. The star has strictly greater distinguished-basin size than even the path upper bound, establishing the global bound and equality case.

Finally a nonstar tree has \(d_v\le n-2\), so every non-universal two-cycle basin is at most \(2^{n-1}-2n+3\). Its distinguished basin is at least \(2^{n-1}-3\), strictly larger for \(n\ge4\). All fixed basins have size at most two. For a star its unique two-cycle basin is strictly larger than its fixed basins. Thus the distinguished orbit is always the unique largest-basin orbit.

## Verification

Two separately implemented exhaustive state-space checkers are supplied. `check_trees.py` enumerates every nonisomorphic tree of orders \(4\) through \(11\), constructs the complement-neighborhood transition table, traces each initial state until periodic, and compares the resulting orbit-basin dictionary with the theorem's formulas. It examined 433 trees and 621,696 initial configurations. `check_labeled.cpp` enumerates every labelled tree through seven vertices using Prüfer sequences and, for each one, evaluates every initial state directly; it additionally checks 100 seeded labelled trees at each order from eight through twelve. It examined 18,744 trees and 3,032,096 configurations. Both report PASS, including the sharp extremal basin counts at all Python-tested orders. These finite checks corroborate but do not replace the all-orders argument above.

The checker outputs, full source and exact compilation/replay instructions are embedded with this result; no external scientific certificate or independent mathematical audit is claimed.

## Relationship to prior work

For loopless symmetric negative conjunctive networks, the known correspondence between fixed points and maximal independent sets is explicitly recorded by Aracena, Richard and Salinas, arXiv:1507.06141, Proposition 1. Applied to the complement of a tree, it already explains why the fixed configurations correspond to tree edges. The present claim **does not** assert that this correspondence or the eventual-period-one-or-two restriction is new. Rather, it determines *each* primitive orbit, *each* basin cardinality, and the sharp tree-degree extremizers of the uniquely largest basin.

The open-access survey of Aledo, Martínez and Valverde (2015) reviews Boolean maxterm/minterm periodicity. Its homogeneous NOR convention includes a vertex's own state, unlike the present **open-neighborhood** map. Its general period discussion therefore is not a covering tree-complement basin classification. The 2020 article by Aledo and collaborators concerns periodic-point bounds and exact formulas for the self-inclusive homogeneous maxterm/minterm systems; it gives no tree-complement basin or sharp path/broom extremal formula. A related 2012 article of Aledo, Martínez, Pelayo and Valverde could not be inspected in full because full text could not be retrieved from available lawful sources. The 2015 survey's statement of its model limits the apparent risk, but unavailable primary content remains an explicit historical overlap uncertainty.

## Limitations

The results concern labelled initial states and deterministic simultaneous, **open-neighbor** NOR only. The family restriction to complements of trees is essential to the pairwise closed-neighborhood intersection step. The displayed fixed-point count and general short-period property are established background; originality is asserted only for the *complete family-specific basin census and extremal consequence*, subject to possible overlap with unindexed or inaccessible literature. Computational exhaustion is finite and cannot prove the theorem for all \(n\). The supplied proof is self-contained; independent review has not been performed.

## References

1. J. Aracena, A. Richard and L. Salinas, *Fixed points in conjunctive networks and maximal independent sets in graph contractions*, arXiv:1507.06141 (first posted 22 July 2015), especially Section 1, equation (2), and Proposition 1.
2. J. A. Aledo, S. Martínez and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics 2015, article 594294, first published 24 March 2015, DOI:10.1155/2015/594294.
3. J. A. Aledo, S. Martínez, F. L. Pelayo and J. C. Valverde, *Parallel discrete dynamical systems on maxterm and minterm Boolean functions*, Mathematical and Computer Modelling 55 (2012), 666–671, DOI:10.1016/j.mcm.2011.08.040. Full text was unavailable for this comparison.
4. J. A. Aledo, A. Barzanouni, G. Malekbala, L. Sharifan and J. C. Valverde, *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity 2020, article 9708347, DOI:10.1155/2020/9708347.
