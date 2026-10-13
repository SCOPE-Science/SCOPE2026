# Bivariate enumeration of independent dominating sets in central graphs of triangle-free graphs

## Finding

Let \(G\) be a finite connected simple triangle-free graph with \(n\ge3\) vertices and \(m\ge2\) edges. The central graph \(\mathsf C(G)\) is formed by replacing every original edge with a path of length two and joining every pair of original vertices that were nonadjacent in \(G\).

Write \(w_{uv}\) for the subdivision vertex associated with \(uv\in E(G)\), let \(d(v)=d_G(v)\), and define
\[
\ell(v)=|\{u\in N_G(v):d(u)=1\}|.
\]
Let \(\mathcal I(\mathsf C(G))\) denote the family of all independent dominating sets, equivalently all maximal independent sets. The following bivariate polynomial also records the number of selected **original** vertices:
\[
\mathcal M_G(x,y)=\sum_{D\in\mathcal I(\mathsf C(G))}x^{|D|}y^{|D\cap V(G)|}.
\]

**Theorem.** Every set in \(\mathcal I(\mathsf C(G))\) has exactly one of the three forms
\[
\{w_e:e\in E(G)\},
\]
\[
\{v\}\cup\{w_e:e\in E(G-v)\},\qquad \ell(v)=0,
\]
or
\[
\{u,v\}\cup\{w_e:e\in E(G-\{u,v\})\},\qquad uv\in E(G).
\]
All listed sets are independent dominating sets, and no others occur. Consequently,
\[
\boxed{
\mathcal M_G(x,y)=x^m+
 y\sum_{v:\,\ell(v)=0}x^{m+1-d(v)}+
 y^2\sum_{uv\in E(G)}x^{m+3-d(u)-d(v)}.
}
\]

The ordinary independent-domination polynomial of \(\mathsf C(G)\) is \(\mathcal M_G(x,1)\). In particular, the **total number of maximal independent sets** is exactly
\[
\boxed{1+m+|\{v:\ell(v)=0\}|\le n+m+1,}
\]
with equality if and only if \(\delta(G)\ge2\). Thus all maximal independent sets of this potentially large central graph can be listed using at most one object per original vertex or edge, plus one extra object.

The term of \(y\)-degree two retains the original graph's entire edge degree-sum histogram: for any integer \(s\),
\[
[x^{m+3-s}y^2]\mathcal M_G(x,y)
=|\{uv\in E(G):d(u)+d(v)=s\}|.
\]
The term of \(y\)-degree one similarly retains the degree histogram restricted to vertices with no leaf neighbor.

Let
\[
D_*=\max_{uv\in E(G)}(d(u)+d(v)).
\]
The previously known minimum independent-domination number is
\[
i(\mathsf C(G))=m+3-D_*.
\]
The new coefficient-level refinement counts all minimum sets:
\[
\boxed{
\begin{aligned}
N_{\min}(G)={}&|\{uv\in E(G):d(u)+d(v)=D_*\}|\\
&+|\{v:\ell(v)=0,\ d(v)=D_*-2\}|\\
&+\mathbf 1_{D_*=3}.
\end{aligned}}
\]
The last term accounts for the all-subdivision set in the exceptional lowest-edge-degree-sum case.

As an illustration of finer information not captured by the degree sequence alone, let \(T_{2,2,1}\) and \(T_{3,1,1}\) be the six-vertex trees with one degree-three vertex and three pendent arms of the indicated lengths. Both have degree multiset \(\{3,2,2,1,1,1\}\), but
\[
\mathcal M_{T_{2,2,1}}(x,1)=2x^3+x^4+6x^5,
\]
whereas
\[
\mathcal M_{T_{3,1,1}}(x,1)=x^3+4x^4+5x^5.
\]
In particular, their central graphs have \(9\) and \(10\) maximal independent sets.

## Assumptions and scope

All graphs are finite, loopless, simple, and undirected. The input \(G\) is connected and triangle-free, with at least three vertices. A maximal independent set is exactly an independent dominating set. The central graph is defined by one subdivision vertex for each edge of \(G\), and an edge between original vertices precisely when they are nonadjacent in \(G\).

The bivariate variable \(y\) counts the original vertices in a selected set, marking the construction's original/subdivision partition. For \(n\ge4\) this partition is intrinsic to \(\mathsf C(G)\), because original vertices have degree \(n-1\) in \(\mathsf C(G)\) while subdivision vertices have degree two. The distinction is marked by construction in the order-three boundary case.

The theorem does not claim a formula for arbitrary graphs containing triangles, nor for central iterates beyond the first. The scalar formula for \(i(\mathsf C(G))\) is existing literature, not new here.

## Proof

Write \(D\) for an arbitrary independent dominating set of \(\mathsf C(G)\), and put \(S=D\cap V(G)\). Two original vertices are adjacent in the central graph precisely when they were nonadjacent in \(G\). Independence of \(D\) therefore forces \(S\) to be a clique of \(G\). Since \(G\) is triangle-free,
\[
|S|\in\{0,1,2\}.
\]
If \(|S|=2\), its two vertices are the endpoints of an original edge.

For each edge \(e=uv\in E(G)\), the subdivision vertex \(w_e\) has exactly the two original vertices \(u,v\) as neighbors. If \(u\) or \(v\) belongs to \(S\), independence forbids \(w_e\) from belonging to \(D\). If neither belongs to \(S\), domination forces \(w_e\in D\), since neither of its only two neighbors is selected. Thus the entire subdivision part of \(D\) is uniquely forced:
\[
\boxed{D=S\cup\{w_e:e\in E(G-S)\}.}
\]

Consider an unselected original vertex \(v\in V(G)\setminus S\). It is dominated by a selected original vertex if and only if some \(u\in S\) is **not** adjacent to \(v\) in \(G\). Otherwise, it is dominated by a selected subdivision vertex exactly when \(v\) has a neighbor in \(V(G)\setminus S\). It is therefore undominated exactly when
\[
N_G(v)=S.
\]
Thus a forced set of the displayed form dominates the whole central graph if and only if
\[
\{v\in V(G)\setminus S:N_G(v)=S\}=\varnothing.
\]

When \(S=\varnothing\), this holds because the connected graph \(G\) has no isolated vertex. When \(S=\{u\}\), a vertex with neighborhood exactly \(\{u\}\) is precisely a degree-one neighbor of \(u\). Hence this case is feasible exactly when \(\ell(u)=0\). Finally, when \(S=\{u,v\}\) and \(uv\in E(G)\), any vertex with neighborhood exactly \(\{u,v\}\) would form a triangle with \(u,v\), contradicting triangle-freeness. Thus **every** edge choice is feasible. This proves the exhaustive and nonoverlapping classification.

The size of the forced set equals \(|S|+|E(G-S)|\). For \(S=\varnothing\), this is \(m\). For a singleton \(S=\{v\}\), deleting \(v\) removes \(d(v)\) edges, giving \(m+1-d(v)\). For an edge \(S=\{u,v\}\), deleting its endpoints removes \(d(u)+d(v)-1\) edges, giving \(m+3-d(u)-d(v)\). Since \(|S|\) is precisely the \(y\)-exponent, adding one monomial per allowed \(S\) proves the bivariate formula.

The coefficient interpretation of edge degree-sums follows immediately from the \(y^2\) summand. Putting \(x=y=1\) gives exactly one set of type zero, one for every vertex with no degree-one neighbor, and one for every original edge. Consequently the total count is at most \(n+m+1\); equality means every vertex has \(\ell(v)=0\), equivalent for a connected graph to the absence of leaves.

For completeness, we derive the minimum-count refinement while distinguishing its known scalar value. Since \(m\ge2\) and \(G\) is connected, \(D_*\ge3\), so the all-subdivision set has size
\[
m\ge m+3-D_*.
\]
If \(\ell(v)=0\), every neighbor of \(v\) has degree at least two. Choosing any neighbor \(u\), we have
\[
D_*\ge d(v)+d(u)\ge d(v)+2,
\]
and hence
\[
m+1-d(v)\ge m+3-D_*.
\]
The edge-type sets achieve size \(m+3-D_*\) exactly on edges attaining the maximum degree-sum \(D_*\). The singleton-type sets tie exactly when \(d(v)=D_*-2\), and the type-zero set ties exactly when \(D_*=3\). Adding these three disjoint contributions gives the displayed formula for \(N_{\min}(G)\).

For the two six-vertex trees, their degree multiset is the same but their edge-degree-sum and leaf-neighbor profiles differ. Substitution into the exact formula yields the two stated polynomials, completing the proof. \(\square\)

## Verification

The standalone script `artifacts/verify.py` constructs each central graph from its defining edges, enumerates vertex subsets directly, checks independence and domination using adjacency, and records both the size and the number of original vertices for each valid subset.

It independently computes the theorem's bivariate polynomial solely from degrees, leaf-neighbor counts, and edge degree sums. All coefficients agree for each of the \(88\) connected triangle-free unlabeled graphs of orders three through seven in the NetworkX graph atlas. The same run checks the independent minimum-size count, the total number of maximal independent sets, and the two distinguishable spider examples.

Verified replay output:

`ALL CHECKS PASSED; connected_triangle_free_atlas_graphs=88; subsets_examined=3098568; original_orders=3..7; bivariate_polynomials=yes; minimum_counts=yes; spider_profiles=2`

The exhaustive test is finite corroboration. The theorem for all connected triangle-free graphs is established by the structural proof, not inferred from enumeration. The test used NetworkX version `3.6.1`.

## Relationship to prior work

Cabrera-Martínez, López-Carmona, Rios-Villamar, and Serrano-Díaz (first public 14 September 2026) prove a general optimization formula for the **minimum size** of an independent dominating set of a central graph (Theorem 2.1). Their Theorem 2.2 specializes it to the triangle-free case and yields the known scalar
\[
i(\mathsf C(G))=m+3-D_*.
\]
Their proof already uses original cliques and forced subdivision vertices when analyzing minimum sets. The present theorem explicitly strengthens the quantifier to **every** independent dominating set, obtains a complete one-to-one classification, and enumerates every size and original-vertex count. The minimum cardinality itself is fully credited to that paper.

Shivaswamy, Soner, and Alwardi (2014) define the independent dominating polynomial and determine it for several standard families and operations, including stars, complete bipartite graphs, spiders, and friendship graphs. Their directly inspected full paper does not give central-graph polynomial formulas; examples for a graph \(G\) are not examples for its central graph \(\mathsf C(G)\).

Published related work on **higher iterated** central graphs determines independent-domination numbers at iterates at least three, and separate work determines **total** domination of central graphs. Neither supplies an independent-domination all-set polynomial at the first central iterate. Targeted database and literature searches under maximal-independent-set, polynomial, central graph, degree-sum, triangle-free, and leaf-neighbor terminology did not locate a covering statement.

## Limitations

The structural theorem assumes that the original graph is connected and triangle-free; dropping these conditions changes the list of admissible original cliques. The polynomial records distinguished original-vertex counts, which must be marked if the central graph has original and subdivision vertices of the same degree (the order-three case).

The minimum cardinality formula itself is previously published. The originality claim is restricted to the universal all-set bijection for triangle-free originals, the bivariate polynomial, its edge degree-sum coefficient recovery, the linear complete census, and its exact minimum multiplicities. Searches do not prove absolute novelty; equivalent results under poorly indexed maximal-independent-set terminology remain a residual risk.

The finite computer checks through order seven are not a proof for arbitrary order. No independent external audit is asserted.

## References

1. A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar, and A. Serrano-Díaz, *Independent domination in central graphs*, arXiv:2609.16357v1, first public 2026-09-14, primary MSC \(05C69\). https://arxiv.org/abs/2609.16357
2. P. M. Shivaswamy, N. D. Soner, and A. Alwardi, *Independent Dominating Polynomial in Graphs*, International Journal of Scientific and Innovative Mathematical Research 2(9) (2014), 757–763. https://arcjournals.org/article/7207
3. *Independent domination of higher iterated central graphs*, published-finding corpus, 2026-09-17, https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-iterated-central-graph-independent-domination--7dc2104ad847
4. *Exact vertex-cover formula for total domination of central graphs*, published-finding corpus, 2026-09-20, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-exact-total-domination-formula-central-graphs--f6679e0fe594
