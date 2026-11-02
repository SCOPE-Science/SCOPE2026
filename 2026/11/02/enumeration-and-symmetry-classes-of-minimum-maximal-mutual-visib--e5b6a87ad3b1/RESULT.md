# Enumeration and symmetry classes of minimum maximal mutual-visibility sets in rook graphs

## Finding
For integers \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n\), with a vertex for each square of an \(m\)-by-\(n\) array and adjacency when two squares share a row or a column. A mutual-visibility set is a subset \(S\) such that every two vertices in \(S\) can be joined by a shortest path with no internal vertex in \(S\). It is *inclusion-maximal* if no additional vertex can be adjoined while preserving this property. Write \(\mu^-(R_{m,n})\) for the least possible size of an inclusion-maximal mutual-visibility set.

**Enumeration theorem.** Every minimum-cardinality inclusion-maximal mutual-visibility set has \(m+n-1\) vertices. Such sets are in bijection with spanning trees of \(K_{m,n}\) of diameter at most four, or equivalently spanning trees having a vertex adjacent to the entire opposite part. Their exact labeled count is
\[
\boxed{N_{m,n}=m n^{m-1}+n m^{n-1}-mn.}
\]
For \(a,b\ge0\), write \(p_{\le b}(a)\) for the number of integer partitions of \(a\) into at most \(b\) parts, including zeros for unused parts. Under independent permutations of the two coordinate sets, the number of distinct minimum-set orbits is
\[
\boxed{U_{m,n}=p_{\le n}(m-1)+p_{\le m}(n-1)-1.}
\]
Under the full automorphism group of the rook graph, the orbit count is \(U_{m,n}\) when \(m\ne n\); for equal factor orders it is
\[
\boxed{U_{n,n}^{\mathrm{full}}=p_{\le n}(n-1)=p(n-1).}
\]
The labeled set count and symmetry classification are the asserted enumerative contributions; the minimum cardinality was previously established.

## Assumptions and scope
All graphs are finite, simple, and undirected. Integers \(m,n\) are at least two. Rook squares are individually labeled by row and column. A spanning tree is regarded as a subgraph on the fixed two-part vertex set of \(K_{m,n}\); 'diameter' is measured in that tree. The smallest maximal cardinality is taken among maximal sets, not all mutually visible sets. Symmetry means permutations of row and column labels; when the factor orders agree, interchange of the two factors is also allowed.

## Proof
**1. Conversion to bipartite saturation.** Represent a rook square \((i,j)\) by an edge \(ij\) of the complete bipartite graph with \(m\) row vertices and \(n\) column vertices. Distinct rook squares sharing a row or column are adjacent and hence mutually visible directly. Squares in different rows and columns are at distance two, and their only two shortest paths have as internal squares the other two corners of their rectangular \(2\)-by-\(2\) array. Therefore all selected pairs are mutually visible precisely when the corresponding root edge set contains no four-cycle. Inclusion maximality is precisely saturation for a four-cycle relative to all the edges of \(K_{m,n}\): inserting any missing root edge must create a four-cycle.

**2. The minimum-size layer.** Every four-cycle-saturated spanning bipartite subgraph is connected. Otherwise choose a row vertex and a column vertex in different components; their missing joining edge cannot complete a cycle. Hence every saturated graph has at least \(m+n-1\) edges. This bound is attained, for example, by joining one fixed row vertex to every column and each remaining row vertex to any fixed column. Thus \(\mu^-(R_{m,n})=m+n-1\). Any saturated graph attaining this bound is connected with exactly one fewer edge than vertices, hence a tree.

**3. Characterization of the optimum trees.** If a nonedge joins opposite parts in a tree, adding it creates a four-cycle exactly when its endpoints are at tree distance three: a tree has a unique path between any two vertices, and the added edge closes a cycle of length one plus that distance. An edge already present has distance one. Thus an optimum tree is saturated if and only if every opposite-part pair is at distance at most three. All such distances are odd. This is equivalent to tree diameter at most four: a path of length at least five contains an opposite-part pair at distance five, whereas a diameter-four tree has all opposite-part distances one or three.

A tree of diameter at most four has a central vertex of eccentricity at most two (the midpoint of a longest path). Every vertex in the opposite bipartition is at an odd distance from that center, therefore at distance one. Conversely, if a tree has a vertex adjacent to every vertex on the opposite side, every other vertex on the center's own side must have degree exactly one (otherwise a four-cycle occurs). The resulting tree has diameter at most four and is saturated. This proves the claimed bijection and structural equivalences.

**4. Labeled counting.** Choose a universal row vertex in \(m\) ways. It is connected to all \(n\) columns. Each other row vertex must choose exactly one column as parent, independently; there are \(n^{m-1}\) choices. This generates all row-centered optimum trees exactly once within this family, since two distinct universal rows would form a four-cycle when \(n\ge2\). The column-centered family analogously has \(n m^{n-1}\) members. A tree lies in both families exactly when it is a double-star, specified by the ordered choice of a row center and a column center. There are exactly \(mn\) such double-stars. Inclusion-exclusion yields \(N_{m,n}=m n^{m-1}+n m^{n-1}-mn\).

**5. Unlabeled classification.** In a row-centered optimum tree, each column has some number of pendent row neighbors besides the central row. These \(n\) nonnegative integers sum to \(m-1\). Independent permutations of rows and columns preserve exactly the unordered multiset, and any two assignments with the same multiset are equivalent; hence there are \(p_{\le n}(m-1)\) row-centered types. There are analogously \(p_{\le m}(n-1)\) column-centered types. The unique type simultaneously represented in both descriptions is the double-star. This yields \(U_{m,n}\). If \(m=n\), interchanging the factors identifies every row-centered type with its corresponding column-centered type, leaving \(p_{\le n}(n-1)\) full-symmetry types. No factor interchange is an automorphism when \(m\ne n\), because maximal row cliques and maximal column cliques have different sizes (in the \(2\)-factor cases, the same conclusion follows from the unique Cartesian-factor decomposition).

## Verification
The attached standalone `verify.py` checks the *original shortest-path definition*, not merely the spanning-tree characterization. It exhaustively enumerates every \((m+n-1)\)-element rook-square subset for nine boards: \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)\). It verifies inclusion maximality by explicitly attempting to insert each omitted square, compares the counts with the exact formula, and independently confirms the existence of a universal root vertex. On eight of those boards it also canonicalizes configurations under separate row/column permutations to verify the integer-partition orbit counts, including full factor-swap orbits on the three balanced boards. All checks end with `VERIFY_OK`; 145180 candidate subsets are examined. This is a finite consistency check, not the proof of the all-parameter result.

The classical spanning-tree number of \(K_{m,n}\) is \(m^{n-1}n^{m-1}\). Thus, as a corollary, the proportion of its spanning trees that give minimum maximal mutual-visibility configurations is exactly
\[
\frac{m n^{m-1}+n m^{n-1}-mn}{m^{n-1}n^{m-1}}.
\]
In particular for \(m=n=r\), this proportion equals \(2r^{2-r}-r^{4-2r}\), and tends to zero rapidly as \(r\to\infty\).

## Relationship to prior work
Brešar and Yero [1] introduced the lower mutual-visibility invariant, proved the scalar optimum \(m+n-1\) for Cartesian products of complete graphs, and explained the conversion to four-cycle-saturated bipartite subgraphs. Bryant and Fu [2, Section 2, especially Lemmas 2.1–2.3] independently studied such saturated bipartite graphs earlier, proving the minimum size and describing examples. Their page 264 also observes that every nonedge in a saturated bipartite graph is connected by a path of length three. Consequently the structural reduction to small-diameter *trees* is close to, and deducible from, their framework. Neither inspected article states the present labeled enumeration or the two symmetry-type formulas. The exhaustive count and orbit classification, rather than the previously known minimum or the basic reduction, constitute the claimed contribution. Dong and Ge [3] count general spanning trees subject to a prescribed forest, rather than optimum saturated trees as a class.

## Limitations
No universal statement about larger inclusion-maximal mutual-visibility sets is made; those correspond to possibly cyclic four-cycle-saturated subgraphs. The unlabeled formulas distinguish whether factor exchange is allowed. The minimum size and general four-cycle-saturation correspondence are previous results, not new claims. The structural small-diameter characterization is a short corollary of classical saturation properties. An earlier unindexed enumeration of these diameter-four bipartite trees or their orbits could supersede the asserted enumerative novelty. The verification covers finite boards and does not replace the proof; independent audit has not been conducted.

## References
[1] B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, first public arXiv submission 6 July 2023, arXiv:2307.02951. https://arxiv.org/abs/2307.02951 .

[2] D. E. Bryant and H.-L. Fu, *C4-saturated bipartite graphs*, Discrete Mathematics 259 (2002), 263–268. Open manuscript: https://ir.lib.nycu.edu.tw/bitstream/11536/28302/1/000180085900019.pdf .

[3] F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, Journal of Graph Theory 101 (2022), 79–94, first arXiv submission March 2021, arXiv:2103.05294. https://arxiv.org/abs/2103.05294 .
