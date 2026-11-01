# Parity and fundamental groups of cyclic six-polytope three-tuplings

## Finding

For every integer \(n\ge 7\), let \(X_n=\partial C(n,6)\) be the boundary of the six-dimensional cyclic polytope with vertices labeled \(0,\ldots,n-1\) in moment-curve order, and let \(Y_n=D^{3}(X_n)\) be its ordinary simplicial three-tupling. Define
\[
F_n=\frac{n(n-4)(n-5)}6.
\]
If \(n\) is odd, \(Y_n\) is connected and
\[
|Y_n|\simeq\bigvee^{\,10F_n-\binom n3+1} S^1.
\]
If \(n=2m\) is even (thus \(m\ge4\)), it has **exactly two** connected components, with integral homotopy types
\[
|Y_{n,0}|\simeq\bigvee^{\,F_n-2\binom m3+1}S^1,\qquad
|Y_{n,1}|\simeq\bigvee^{\,9F_n-2m\binom m2+1}S^1.
\]
Here \(Y_{n,0}\) consists of triple-vertices whose number of even labels is \(0\) or \(3\); \(Y_{n,1}\) consists of those with \(1\) or \(2\) even labels. In particular, \(Y_7\simeq\bigvee^{36}S^1\) and the two components of \(Y_8\) are \(\bigvee^9S^1\) and \(\bigvee^{97}S^1\).

## Assumptions and scope

The three-tupling \(D^3(X)\) has the triangles (three-vertex faces) of \(X\) as its vertices. A pair of distinct triangle-vertices is joined by an edge exactly if the triangles are disjoint and their six-vertex union is a facet of \(X\). Since \(X_n\) has dimension five, \(Y_n\) is a graph and has no higher-dimensional simplices. The cyclic polytope is three-neighborly; therefore all \(\binom n3\) triples are vertices of \(Y_n\). A wedge of zero circles means a point (although none of the displayed multiplicities is zero in the stated domain).

## Proof

**1. Facet description.** Gale's evenness criterion for \(C(n,6)\) says that a six-set is a facet precisely when, in the cyclic order of the \(n\) labels, it is a union of three pairwise vertex-disjoint edges of the cycle \(C_n\). Indeed, relative to any two missing labels, an even number of selected labels must intervene; the runs of selected labels between successive missing labels are therefore even and can be paired consecutively. Conversely such pairings satisfy evenness. There is a missing label since \(n\ge7\). The induced subgraph of a proper six-subset in \(C_n\) is a union of paths and has at most one perfect matching; hence the three-edge matching corresponding to each facet is unique.

**2. Connectivity for paths.** Let \(H_q\) be the graph whose vertices are all three-subsets of \(\{0,\ldots,q-1\}\) and whose edges join complementary three-subsets of six-vertex unions of three disjoint edges in the path \(P_q\). Every such six-set has three even and three odd labels. Thus any edge exchanges the numbers \(0\leftrightarrow3\) or \(1\leftrightarrow2\) of even labels. Hence the two classes \(\{0,3\}\) and \(\{1,2\}\) cannot be connected to each other.

The finite base \(H_8\) is exhaustive: the ten possible three-edge matchings of \(P_8\) give 100 graph edges on 56 triple-vertices; breadth-first searches from \(\{0,2,4\}\) and \(\{0,1,2\}\) reach respectively 8 and 48 vertices, without overlap. These exhaust all 56 triples, so exactly the two parity classes are connected. The complete base calculation is reproducible in `verify.py` and has no randomized step.

To pass from \(H_q\) to \(H_{q+1}\), for \(q\ge8\), retain the old path as a subgraph. Every new triple \(T\) contains the new terminal vertex \(q\). Include the terminal path edge \(\{q-1,q\}\) in a three-edge matching. We need only choose two disjoint edges of the remaining path on \(0,\ldots,q-2\) covering the at most two elements of \(T\) outside \(\{q-1,q\}\). Such edges always exist: in any path on at least five vertices, any set of at most two marked vertices is contained in the vertex set of a two-edge matching. For an even-length path, select edges from its perfect matching; for an odd-length path, delete an unmarked even-indexed vertex (one exists since at least three such indices are available), perfectly match each resulting even-length side, and select or complete to two matching edges. The residual path here has \(q-1\ge7\) vertices. The complementary triple in this six-set is an *old* vertex adjacent to \(T\). As parity class is preserved, every new vertex attaches to the correct old connected component. By induction, \(H_q\) has exactly the two parity-class components for every \(q\ge8\).

**3. Restore the cyclic edge.** For even \(n\ge8\), the added edge \(\{n-1,0\}\) joins odd and even labels. Every three-edge matching of \(C_n\) therefore still has three vertices of each parity. Thus no added edge of \(Y_n\) can bridge the two classes, while \(H_n\) already connects each one. There are exactly two components.

For odd \(n\ge9\), the wrap edge \(\{n-1,0\}\) has two even endpoints. Together with \(\{1,2\}\) and \(\{3,4\}\), it forms a three-edge matching with six-set \(\{n-1,0,1,2,3,4\}\). The complementary triples \(\{n-1,0,2\}\) and \(\{1,3,4\}\) have respectively three and one even elements, so this single extra edge connects the two components of \(H_n\). The only remaining odd case is \(n=7\), where direct enumeration gives 35 triple-vertices, 70 edges and one connected component (also verified in `verify.py`). Thus all odd cases are connected.

**4. Exact circle counts.** Three-edge matchings of \(C_n\) are in bijection with its facets, and their number is
\[
F_n=\frac{n}{n-3}\binom{n-3}3=\frac{n(n-4)(n-5)}6.
\]
Each facet supports precisely \(\frac12\binom63=10\) complementary triple-pair edges. No graph edge is counted twice, since its union uniquely determines the facet. Therefore \(Y_n\) has \(\binom n3\) vertices and \(10F_n\) edges. In the connected odd case its circle rank is \(10F_n-\binom n3+1\).

When \(n=2m\) is even, every facet has three even and three odd labels. Of the ten complementary partitions, exactly one pairs an all-even triple with an all-odd triple, and the other nine pair a one-even with a two-even triple. Thus the two components have respectively \(F_n\) and \(9F_n\) edges, and their vertex counts are \(2\binom m3\) and \(2m\binom m2\). Since a finite connected graph is homotopy equivalent to a wedge of \(E-V+1\) circles, the two displayed homotopy formulas follow. All calculations are integral and describe full ordinary homotopy types, not only rational Betti numbers.

## Verification

Run `python3 verify.py` using the Python standard library. It reconstructs all path and cycle three-matching facets; checks the complete two-component \(H_8\) base and the connected \(C_7\) base; independently compares facet sets against Gale evenness for \(7\le n\le16\); checks complete cycle component and rank formulas for \(7\le n\le22\); and checks the new-terminal-vertex path covering property for \(8\le q\le28\). The terminal message is `ALL_VERIFY_OK`. The induction in the proof—not the finite parameter test—establishes the unbounded cases.

## Relationship to prior work

Lesh, Schreiner and Wahl introduced the general \(r\)-tupling construction and prove connectivity bounds in *The double of a simplicial complex*, arXiv:2506.10436, first version posted June 12, 2025. Their Theorem A gives a weak Cohen–Macaulay lower bound; it does not calculate the components or circle ranks here. Gale's classical evenness criterion identifies cyclic-polytope facets. Existing calculations of the *double* of cyclic four- and six-polytope boundaries, and the *four-tupling* of cyclic eight-polytope boundaries, address different constructions and do not imply this three-tupling result. The present theorem treats the intermediate odd block size and isolates its two-component parity obstruction.

## Limitations

The theorem concerns the specific six-dimensional cyclic-polytope boundary, with three-tupling and \(n\ge7\). It does not classify arbitrary even-dimensional cyclic polytopes, arbitrary block size, or equivariant homotopy actions. The literature comparison cannot rule out uncatalogued equivalent calculations. The finite base cases and large-parameter verification are exhaustive for the reported ranges, but their numerical extent alone is not an infinite proof.

## References

1. K. Lesh, B. Schreiner and N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436 (first public version: June 12, 2025). https://arxiv.org/abs/2506.10436
2. D. Gale, the evenness characterization of faces of cyclic polytopes; see the standard statement in *Cyclic polytope*, Gale evenness section, https://en.wikipedia.org/wiki/Cyclic_polytope
3. R. Cordovil and P. Duchet, *Cyclic Polytopes and Oriented Matroids*, European Journal of Combinatorics, 2000 (combinatorial context for Gale's condition).
