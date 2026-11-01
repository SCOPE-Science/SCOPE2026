# Three parity components in four-tuplings of cyclic eight-polytope boundaries

## Finding
For every integer \(n\ge9\), let \(X_n=\partial C(n,8)\) be the simplicial boundary of the cyclic eight-polytope with linearly ordered vertices \(0,1,\ldots,n-1\), and write \(Y_n=D^4(X_n)\) for its four-tupling. Put
\[
F_n=\frac{n(n-5)(n-6)(n-7)}{24}.
\]
If \(n\) is odd, then
\[
|Y_n|\simeq\bigvee^{35F_n-\binom{n}{4}+1}S^1.
\]
If \(n=2m\) is even, there are exactly three connected components. For a four-subset \(T\) of the vertex labels, let \(k(T)\) be its number of even labels, and put \(j(T)=\min(k(T),4-k(T))\). The three components consist precisely of the vertices with \(j(T)=0,1,2\), respectively, and their integral homotopy types are
\[
\begin{aligned}
Y_{n,0}&\simeq\bigvee^{F_n-2\binom{m}{4}+1}S^1,\\
Y_{n,1}&\simeq\bigvee^{16F_n-2m\binom{m}{3}+1}S^1,\\
Y_{n,2}&\simeq\bigvee^{18F_n-\binom{m}{2}^{2}+1}S^1.
\end{aligned}
\]
Thus a natural family of simplicial seven-spheres has four-tuplings with three connected components for every even \(n\ge10\), but connected four-tuplings for every odd \(n\ge9\). For example, at \(n=10\) the three circle ranks are \(16,301,351\).

## Assumptions and scope
The four-tupling \(D^4(X)\) has one vertex for each four-element face \(T\) of \(X\), and an edge for each unordered pair \(\{T,U\}\) of disjoint four-element faces whose union is an eight-element facet of \(X\). There are no higher-dimensional faces when \(X\) has no faces with twelve vertices. The cyclic polytope is defined by \(n\) strictly increasing points on the moment curve \(t\mapsto(t,t^2,\ldots,t^8)\). All four-element subsets are faces by four-neighborliness, and its facets are precisely unions of four pairwise disjoint edges of the cyclic graph \(C_n\), with cyclic labels. The latter is the even-dimensional form of Gale's evenness criterion; the endpoint edge is \(\{n-1,0\}\).

## Proof
**1. Graph and facet count.** Every vertex of \(Y_n\) is one of the \(\binom n4\) four-subsets. As \(X_n\) has no faces of size twelve, \(Y_n\) is one-dimensional. An eight-vertex facet of \(X_n\) gives exactly \(\binom84/2=35\) edges of \(Y_n\), each uniquely identified by the union of its two endpoints. The number of ways to choose four nonincident edges on a cycle of length \(n\) equals
\[
\frac{n}{n-4}\binom{n-4}{4}=F_n.
\]
Hence the graph has \(\binom n4\) vertices and \(35F_n\) edges.

**2. A connectedness lemma for path facets.** Let \(H_n\) be the graph on the four-subsets of \(\{0,\ldots,n-1\}\) with edges corresponding to complements inside unions of four pairwise disjoint **path** edges \(\{i,i+1\}\), with \(0\le i<n-1\). For every \(n\ge10\), \(H_n\) has precisely three components, labeled by \(j(T)=\min(k(T),4-k(T))\in\{0,1,2\}\). Every path edge has one even and one odd endpoint, so the parity count on complementary four-subsets satisfies \(k(T)+k(U)=4\). Thus no edge crosses these three classes.

For the base \(n=10\), the complete finite graph is reconstructed by `verify.py`: it has 210 vertices, 15 path facets, 525 edges, and its breadth-first search yields precisely one component of each parity class, of sizes 10, 100 and 100. The base certificate does not rely on data files, sampled faces or unverified rank calculations.

For the inductive step, the copy of \(H_{n-1}\) on four-subsets avoiding \(n-1\) is a subgraph of \(H_n\). Take any new four-subset \(T\) containing \(n-1\). Force the edge \(\{n-2,n-1\}\) into a four-edge matching; the remaining at most three marked vertices of \(T\) belong to the path on \(\{0,\ldots,n-3\}\), which has \(n-2\ge9\) vertices. They can all be covered by three mutually disjoint path edges. Indeed, on a path with \(N\ge9\) vertices and a set of at most three marked vertices, choose a perfect matching if \(N\) is even; if \(N\) is odd, choose an unmarked even-indexed vertex, delete it, and perfectly match both resulting even-length subpaths. In either case choose the edges of this matching incident to the marked vertices and add arbitrary remaining matching edges until there are three. The resulting four-edge matching covers \(T\); its complementary four-subset \(U\) avoids \(n-1\), and \(\{T,U\}\) is an edge. Thus every newly added vertex joins an old component of its parity class, and induction proves the lemma.

**3. Cyclic wrap and the component classification.** For even \(n\), the additional wrap edge \(\{n-1,0\}\) has one endpoint of each parity. Every cyclic facet therefore also has four even and four odd vertices, so no new edge can cross the three classes. Since \(H_n\) is a subgraph, these three classes are connected and are exactly the components of \(Y_n\).

For odd \(n\ge11\), the wrap edge has two even endpoints. Consider the facet made of the four disjoint cycle edges \(\{n-1,0\}\), \(\{1,2\}\), \(\{3,4\}\), and \(\{5,6\}\). It has five even and three odd vertices. Among its complementary four-subsets are an edge between parity counts four and one (joining classes zero and one), and an edge between counts three and two (joining classes one and two). The already-connected classes of \(H_n\) therefore merge into a single connected component of \(Y_n\). The exceptional odd value \(n=9\) is also connected: \(X_9\) is the boundary of an eight-simplex and \(Y_9\) is the Kneser graph on disjoint four-subsets of a nine-set. Two four-subsets differing in one vertex have the same four-element disjoint complement, producing a length-two path; such one-vertex exchanges connect all four-subsets.

**4. Ranks of the circles.** The homotopy type of a finite connected graph is a wedge of \(E-V+1\) circles. In the odd case, use the global vertex and edge totals from step 1. In the even case write \(n=2m\). The vertex counts of the three parity classes are
\[
V_0=2\binom m4,\qquad V_1=2m\binom m3,\qquad V_2=\binom m2^2.
\]
Each cyclic facet has four even and four odd labels. Its 35 edges divide into exactly one edge of class zero, 16 edges of class one, and 18 edges of class two: selecting a four-subset with \(k=0\), \(k=1\), or \(k=2\) even vertices gives the respective binomial counts \(1\), \(4\cdot4\), and \(\binom42^2/2\). Thus \(E_0=F_n\), \(E_1=16F_n\), and \(E_2=18F_n\), and the stated ranks are \(E_j-V_j+1\). This proves the integral homotopy classification.

## Verification
Run `python3 verify.py` using Python 3 and only its standard library. The checker constructs path and cyclic facet sets from disjoint consecutive edges; independently reconstructs cyclic facets from Gale's evenness condition for \(9\le n\le14\); checks all face/edge counts, every component's parity class and exact Betti ranks for \(9\le n\le17\); and verifies the complete 210-vertex induction base. It also exhaustively confirms the auxiliary three-marked-vertex matching-cover lemma on paths with 9 through 16 vertices. The script has no downloaded dependencies. Infinite-range validity is established by the written induction, not by finite numerical extrapolation.

## Relationship to prior work
Lesh, Schreiner and Wahl introduced \(r\)-tupling and proved general weak Cohen–Macaulay connectivity bounds [1, Definition 2.1 and Theorem A]. For the seven-sphere \(X_n\) and \(r=4\), that theorem yields only weak Cohen–Macaulay dimension zero and does not determine the number of components or their fundamental-group ranks. Gale's evenness criterion supplies the cyclic-polytope facets [2]. The graph here is not the full four-uniform hypergraph matching complex of a simplex: its edges are restricted to unions that are facets of a cyclic eight-polytope. The exact three-component parity split and the uniform circle-rank formulas are not consequences of those cited results.

## Limitations
The result concerns the four-tupling of the boundary of the cyclic eight-polytope, not arbitrary seven-dimensional simplicial spheres or all \(r\)-tuplings. It determines ordinary integral homotopy types, not the full equivariant homotopy representation under cyclic or dihedral automorphisms. Computational checks verify the finite base and samples only; they are not a substitute for the induction. An equivalent uncatalogued computation may exist.

## References
[1] K. Lesh, B. Schreiner and N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436, first posted 2025-06-12; Definition 2.1, Theorem A, and Sections 2–3. https://arxiv.org/abs/2506.10436

[2] G. M. Ziegler, *Lectures on Polytopes*, Springer, 1995, p. 14 (Gale's evenness criterion); see also D. Gale, *Neighborly and cyclic polytopes*, in *Convexity*, Proceedings of Symposia in Pure Mathematics 7, 1963, pp. 225–233.
