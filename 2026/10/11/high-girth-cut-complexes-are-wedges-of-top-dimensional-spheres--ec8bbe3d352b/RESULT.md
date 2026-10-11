# High-girth cut complexes are wedges of top-dimensional spheres
## Finding
Let \(G=(V,E)\) be a finite simple graph with \(N=|V|\). For an integer \(k\ge3\) with \(N\ge k+4\), suppose that \(G\) contains no cycle with at most \(k+1\) edges. Define \(c_k(G)\) as the number of \(k\)-element subsets \(U\subseteq V\) for which \(G[U]\) is connected. The ordinary \(k\)-cut complex \(\Delta_k(G)\) has as its facets the sets \(V\setminus U\) for which \(G[U]\) is disconnected. Then
\[
\Delta_k(G)\simeq\bigvee^{\binom{N-1}{k-1}-c_k(G)}S^{N-k-1}.
\]
The multiplicity is a nonnegative integer; zero spheres means a point. In particular the complete integral homology is torsion-free, vanishes in reduced degrees except \(N-k-1\), and in that degree is free of the displayed rank. No connectedness assumption on \(G\) is required.

For \(k=4\), the connected four-subsets are precisely induced paths with four vertices and induced three-leaf stars. Consequently, for every graph of girth at least six,
\[
c_4(G)=\sum_{uv\in E}(\deg(u)-1)(\deg(v)-1)+\sum_{v\in V}\binom{\deg(v)}{3}.
\]
Thus this degree-based formula and the first display determine the homotopy type of all four-cut complexes in the stated range. For a chain of two hexagons given by parallel five-vertex paths and rungs at positions \(0,2,4\), \(N=10\), \(c_4=20\), and \(\Delta_4\simeq\bigvee^{64}S^5\). For a chain of three hexagons (parallel seven-vertex paths, rungs at \(0,2,4,6\)), \(N=14\), \(c_4=34\), and \(\Delta_4\simeq\bigvee^{252}S^9\).

## Assumptions and scope
Girth means the minimum number of edges in a cycle; forests have infinite girth. All graphs are finite, simple and undirected, and need not be connected. The inequalities \(k\ge3\) and \(N\ge k+4\) make \(d=N-k-1\ge3\), the connectivity range used to promote homology to homotopy. The condition \(\operatorname{girth}(G)\ge k+2\) is equivalent to saying every induced subgraph on at most \(k+1\) vertices is a forest.

The Alexander dual of a simplicial complex \(K\) on \(V\) is \(K^*=\{A\subseteq V: V\setminus A\notin K\}\). We take the empty face as usual and use integral reduced homology and cohomology. The complement of a disconnected \(k\)-set is a facet only for the *ordinary* cut complex, not the total cut complex whose complements must be independent.

## Proof
**1. Every potential codimension-one cut face occurs.** Consider any \((k+1)\)-subset \(W\subseteq V\). By girth, \(G[W]\) is a forest. There is a vertex \(w\in W\) whose removal leaves \(G[W\setminus\{w\}]\) disconnected. Indeed, when the forest is connected, remove a nonleaf vertex (one exists because \(k+1\ge4\)); when it is disconnected, choose a vertex that leaves at least two components nonempty. Hence every subset of \(V\) of size \(N-k-1\) belongs to \(\Delta_k(G)\). Because all facets have size \(N-k\), \(\Delta_k(G)\) is the complete \((N-k-2)\)-skeleton plus some \((N-k-1)\)-simplices. In particular it is simply connected since \(N-k-2\ge2\).

**2. Identify the dual.** Let \(L=\Delta_k(G)^*\). Every subset of \(V\) of size at most \(k-1\) belongs to \(L\), because its complement is too large to be a face of \(\Delta_k(G)\). A \(k\)-subset \(U\) belongs to \(L\) exactly when \(G[U]\) is connected, because its complement is a cut-complex facet exactly in the disconnected case. No larger set belongs to \(L\), by Step 1. Therefore
\[
L=\operatorname{skel}_{k-2}(\sigma^{N-1})\cup\{\text{the \((k-1)\)-simplices on connected \(k\)-sets}\}.
\]
The union includes all their subfaces.

**3. Every upper simplex has a private free face.** Fix a connected \(k\)-set \(U\). Because \(G[U]\) is a connected induced subgraph with fewer than \(k+2\) vertices and the girth bound holds, \(G[U]\) is a tree. Choose any vertex \(v\in U\) of degree at least two in this tree and put \(S=U\setminus\{v\}\). The forest \(G[S]\) has at least two nonempty connected components. Suppose another connected \(k\)-set of the form \(S\cup\{z\}\), with \(z\notin U\), existed. Then \(z\) would have a neighbor in every component of \(G[S]\). Select two components and the unique tree paths within \(U\) between those neighbors and \(v\). Joining them through \(z\) creates a simple cycle entirely inside \(U\cup\{z\}\), hence of length at most \(k+1\), contradicting the girth bound. Therefore the \((k-2)\)-simplex \(S\) lies in exactly one \((k-1)\)-simplex of \(L\), namely \(U\). These private faces are distinct for different \(U\). Pairing each \(U\) with its private \(S\) gives \(c_k(G)\) consecutive elementary simplicial collapses of \(L\); no other upper simplex contains any chosen \(S\).

**4. Exact integral dual homology.** Let \(F=\operatorname{skel}_{k-2}(\sigma^{N-1})\). This full skeleton is \((k-3)\)-connected and has \(\widetilde H_{k-2}(F;\mathbb Z)\cong\mathbb Z^{\binom{N-1}{k-1}}\) and no other reduced integral homology. Attaching the \(c_k(G)\) top simplices to \(F\) gives a cellular boundary map from \(\mathbb Z^{c_k(G)}\) to the \((k-2)\)-chains of \(F\). For each column, the private face from Step 3 has signed coefficient \(\pm1\) and coefficient zero in every other column. Thus this map is a split injection: it contains a \(c_k(G)\)-by-\(c_k(G)\) diagonal unit minor. Since its image lies in the cycle group, the quotient of the cycle group by the image is torsion-free. It follows that \(\widetilde H_{k-2}(L;\mathbb Z)\cong\mathbb Z^{\binom{N-1}{k-1}-c_k(G)}\), and all other reduced integral homology groups of \(L\) vanish. The universal coefficient theorem gives the identical free cohomology group in degree \(k-2\), with all other reduced cohomology zero.

**5. Duality and homotopy.** Combinatorial Alexander duality supplies \(\widetilde H_i(\Delta_k(G);\mathbb Z)\cong\widetilde H^{N-i-3}(L;\mathbb Z)\). Thus the only possibly nonzero reduced integral homology of \(\Delta_k(G)\) is in degree \(d=N-k-1\), where its rank is \(\binom{N-1}{k-1}-c_k(G)\). By Step 1, \(\Delta_k(G)\) is simply connected. The Hurewicz theorem implies that this space is \((d-1)\)-connected and that its degree-\(d\) homotopy group is free of this rank. Represent a basis by maps from \(d\)-spheres. Their wedge induces an isomorphism on every integral homology group, so the homology version of Whitehead's theorem for simply connected CW complexes makes it a homotopy equivalence. If the rank is zero, the same argument shows contractibility.

**6. Four-vertex formula.** In a graph with girth at least six, every induced connected four-set is a four-vertex tree. A star on four vertices is uniquely specified by choosing three neighbors of its center, giving \(\sum_v\binom{\deg(v)}3\). A path on four vertices has a unique middle edge \(uv\); choosing one other neighbor of each endpoint gives \((\deg(u)-1)(\deg(v)-1)\) paths. No identification or extra chord is possible without a triangle or four-cycle. Summing gives the formula.

## Verification
The standalone runnable standard-library file `verify.py` checks the hypotheses, connected-set enumeration, and private-free-face uniqueness by exhaustive vertex-subset enumeration. It constructs the Alexander dual up to dimension \(k-1\), computes mod-two simplicial boundary ranks directly, and compares its reduced Betti ranks with the formula. For \(k=4\) it also checks the independent degree-count formula. The program checks 23 graph/parameter pairs: cycles, paths, hexagonal chains, a theta graph with overlapping cycles, the Petersen graph, the Heawood graph, and an edgeless graph, and returns `VERIFY_OK 23 complete finite graph/parameter checks` under Python 3. The infinite-family proof rests on Steps 1–6, not on these finite checks. The signed unit-minor argument is integral and is not inferred from mod-two computations.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue, *Topology of Cut Complexes of Graphs* (arXiv:2304.13675), Proposition 6.2, established the same complete lower skeleton under the no-short-cycles condition; Theorem 6.1 gave the Euler characteristic and restricted torsion-free homology to at most the top two dimensions. Their separate theorems treat forests, cycles, and \(k=2\) triangle-free connected graphs, but do not assert this top-dimensional homotopy classification for arbitrary graphs and \(k\ge3\). The private-free-face argument in Step 3 forces the lower-degree homology to vanish and upgrades the conclusion to homotopy.

Bayer et al., *Topology of Cut Complexes II* (arXiv:2407.08158), treats disjoint unions, squared paths and rectangular square grids; its four-cut grid cases have four-cycles and do not establish the above high-girth theorem. Chandrakar, *On Shellability of 3-Cut Complexes of Hexagonal Grid Graphs* (arXiv:2512.21755, originally public December 25, 2025), proves three-cut shellability and asks in Question 5.1 about larger cut sizes for hexagonal chains. The present result answers the homotopy question for four-cuts of such chains and all other sufficiently large girth-six graphs; **it does not answer that shellability question**. Previously known forest, cycle, and three-cut special cases are not claimed as new.

## Limitations
The bound \(N\ge k+4\) is used to ensure simple connectivity and to justify the final sphere-wedge conclusion; the smaller dimensions are not classified here. The method uses girth at least \(k+2\), not merely triangle-free or bipartite graphs. It does not prove shellability, a specific shelling order, equivariant homotopy equivalence, or conclusions about total cut complexes. Neither database searches nor this proof establish priority over unpublished or unindexed work; independent validation has not been performed.

## References
1. Himanshu Chandrakar, *On Shellability of 3-Cut Complexes of Hexagonal Grid Graphs*, arXiv:2512.21755, first posted December 25, 2025. Section 5, Question 5.1.
2. Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, Section 6, especially Theorem 6.1 and Proposition 6.2; Section 7 on forests and cycles.
3. Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Sheila Sundaram, and Lei Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, Sections 4–5.
4. A. Hatcher, *Algebraic Topology*, 2002, for standard Alexander duality, Hurewicz and Whitehead theorems.
