# High-girth neighborhood complexes collapse to explicit graph wedges
## Finding
Let \(G\) be a finite connected simple graph with \(n\) vertices, \(m\) edges, minimum degree at least \(2\), and girth at least \(5\). Then the Lovász neighborhood complex \(\mathcal N(G)\) simplicially collapses to a graph. If \(G\) is non-bipartite, then \(\mathcal N(G)\simeq \bigvee^{2m-2n+1}S^1\). If \(G\) is bipartite, then \(\mathcal N(G)\) has exactly two connected components and each is homotopy equivalent to \(\bigvee^{m-n+1}S^1\).

Equivalently, the entire positive-dimensional homotopy of the ordinary open-neighborhood complex is determined by the two graph counts \(n=|V(G)|\) and \(m=|E(G)|\), together with bipartiteness, throughout this high-girth class.

## Assumptions and scope
The graph \(G\) is finite, connected, simple, has minimum degree at least \(2\), and has no cycles of length \(3\) or \(4\). The Lovász neighborhood complex is
\[
\mathcal N(G)=\{{\sigma\subseteq V(G):\sigma\ne\varnothing\text{{ and }}\sigma\subseteq N_G(v)\text{{ for some }}v\in V(G)\}}.
\]
The result concerns ordinary open neighborhoods. It does not assert the same formula for closed-neighborhood complexes, graphs with leaves, or graphs containing triangles or quadrangles.

## Proof
For each vertex \(v\), write \(\Delta_v\) for the simplex on \(N_G(v)\). Since \(\deg(v)\ge2\), choose two distinct vertices of \(N_G(v)\). If \(N_G(v)\subseteq N_G(w)\) for distinct \(v,w\), those two vertices would be common neighbors of \(v\) and \(w\), producing a four-cycle. Hence every \(\Delta_v\) is a maximal simplex of \(\mathcal N(G)\). The same argument shows
\[
|N_G(v)\cap N_G(w)|\le1
\]
for distinct \(v,w\). Thus different maximal simplices meet only in vertices.

Fix a center \(c_v\in N_G(v)\). Inside \(\Delta_v\), order the nonempty subsets \(\sigma\subseteq N_G(v)\setminus\{c_v\}\) with \(|\sigma|\ge2\) by decreasing cardinality. Successively collapse each pair
\[
(\sigma,\;\sigma\cup\{c_v\}).
\]
At the moment this pair is used, every larger coface has already been removed, so \(\sigma\) is free and \(\sigma\cup\{c_v\}\) is its unique remaining coface. This collapses \(\Delta_v\), relative to all of its vertices, onto the star tree with center \(c_v\) and vertex set \(N_G(v)\). Because distinct \(\Delta_v\) meet only in vertices and no vertex is removed, these local collapse sequences concatenate globally.

Let \(H\) be the resulting graph. The star contributed by \(v\) has exactly \(\deg(v)-1\) edges. No edge can occur in two different stars, because that would give two common neighbors to two distinct vertices and hence a four-cycle. Therefore
\[
|E(H)|=\sum_{v\in V(G)}(\deg(v)-1)=2m-n.
\]

Two vertices of \(H\) lie in the same connected component exactly when they are joined in \(G\) by an even-length walk. Indeed, each edge of \(H\) joins two vertices with a common neighbor in \(G\), while within the star associated to any vertex \(v\), all vertices of \(N_G(v)\) are connected. Since \(G\) is connected, the even-walk relation has one class when \(G\) is non-bipartite and two classes, the bipartition classes, when \(G\) is bipartite.

If \(G\) is non-bipartite, \(H\) is connected and its cycle rank is
\[
(2m-n)-n+1=2m-2n+1.
\]
A connected graph of cycle rank \(r\) is homotopy equivalent to \(\bigvee^r S^1\), proving the first case.

Now suppose \(G\) has bipartition \(A\sqcup B\). The component of \(H\) on \(A\) receives one star from every vertex of \(B\), so it has
\[
\sum_{b\in B}(\deg(b)-1)=m-|B|
\]
edges and \(|A|\) vertices. Its cycle rank is therefore \(m-|B|-|A|+1=m-n+1\). The component on \(B\) has the same rank by symmetry. This proves the bipartite case.

## Verification
The standalone `verify.py` reconstructs the neighborhood complex and executes the stated elementary collapse order for six independent examples satisfying the hypotheses: \(C_5\), \(C_6\), the Petersen graph, the Heawood graph, and two irregular graphs obtained from pairs of cycles joined by a bridge. It checks that every proposed free face has exactly one remaining strict coface, that the terminal complex is one-dimensional, and that its component cycle ranks agree with the theorem. The replay is finite corroboration of the local collapse mechanism; the all-parameter conclusion is established by the proof above rather than by enumeration.

## Relationship to prior work
Kozlov's 2005 paper gives the standard neighborhood-complex framework and proves simple-homotopy equivalence with \(\operatorname{{Hom}}(K_2,G)\), but it does not state this girth-based collapse or the exact rank formulas. Shukla's later theorem shows that for connected graphs of maximum degree at most \(3\), each neighborhood-complex component is contractible or a wedge of circles (apart from named exceptions). The present statement uses a different hypothesis: girth at least \(5\) and minimum degree at least \(2\), with no upper degree bound, and it gives the exact number of circle summands directly from \(n\) and \(m\).

A previously checked special case for incidence graphs of Steiner \(2\)-designs is subsumed by the bipartite formula, but that special case does not imply the present theorem for arbitrary high-girth graphs, including irregular and non-bipartite graphs.

## Limitations
The girth assumption is used twice: it prevents distinct neighborhood facets from sharing an edge and prevents one nontrivial neighborhood from being contained in another. With triangles or quadrangles, the independent facetwise collapses can fail and higher-dimensional homotopy can occur. The minimum-degree assumption excludes leaf neighborhoods, which can be non-maximal and require separate folding behavior. No claim is made about optimality of these hypotheses.

## References
1. Dmitry N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613v1, first public 2005-03-28; primary MSC 57Q10.
2. Samir Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v2, first public 2018-02-13.
