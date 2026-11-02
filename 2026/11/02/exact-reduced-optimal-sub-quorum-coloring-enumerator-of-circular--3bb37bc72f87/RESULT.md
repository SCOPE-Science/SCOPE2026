# Exact reduced-optimal sub-quorum coloring enumerator of circular ladders

## Finding
For each integer \(n\ge3\), let \(G_n=C_n\square K_2\) have two labelled cyclic rows and labelled rungs. A *sub-quorum coloring* is a partial vertex coloring in which each colored vertex has its own color on at least half the colored vertices of its closed neighborhood. A coloring is *reduced* if all nonempty color classes are singletons or pairs. Distinct colorings are identified only by permutation of color names; vertex labels remain fixed.

The maximum number of colors is \(\psi_{\mathrm{sq}}(G_n)=n\). Let \(a_n\) count reduced colorings that use this maximum. Their exact enumerator is
\[
\sum_{n\ge1} a_nz^n=-z\frac{d}{dz}\log\left[(1-z^2)^2 D_5(z)D_7(z)\right],
\]
where
\[
D_5(z)=1+z-z^2+z^4-z^5,\qquad D_7(z)=1-2z-3z^2+2z^3+2z^4-2z^6-z^7.
\]
Only coefficients from \(n=3\) onward count simple circular ladders. The first six counts are \(16,65,151,434,1177,3225\) for \(n=3,4,5,6,7,8\), respectively.

## Assumptions and scope
All graphs are finite, simple and undirected. Index cyclic columns by \(i\in\mathbb Z/n\mathbb Z\), and rows by \(r\in\{0,1\}\). The edge set consists of horizontal edges from column \(i\) to \(i+1\) in each row, together with the two-row rung at each column. The color names are not counted: equivalently, a coloring is an unlabelled set partition of its colored support into color classes. A size-two color class in an optimal coloring must be an edge, since otherwise splitting it into two colors preserves all local conditions and improves the color count.

For an optimal coloring, let \(T\) be its singleton-colored vertices. Choose one edge from each nonsingleton connected color class, giving a matching \(M\). The published representative-pair lemma gives \(\psi_{\mathrm{sq}}(G)\le\max(|T|+|M|)\), where \(T\cap V(M)=\varnothing\) and every \(t\in T\) has at most one neighbor in \(T\cup V(M)\). For a cubic graph, every such pair is itself a reduced sub-quorum coloring: give each singleton and matched edge its own color. The singleton has at most one other colored neighbor; both endpoints of each matched edge have at least two of at most four colored closed-neighborhood vertices in their own color.

## Proof
**Step 1: a sharp cyclic bound.** Fix any feasible pair \((T,M)\) as above. In each column, write the status of each row vertex as \(U\) if unused, \(T\) if a singleton, \(L\) if matched to the previous column, \(R\) if matched to the next column, or \(V\) if matched vertically. A column consists either of two non-\(V\) symbols or the pair \((V,V)\); hence there are exactly \(17\) types.

For column \(i\), define its *color contribution* \(w_i\) to be the number of symbols \(T\) plus the number of symbols \(R\) plus one if its type is \((V,V)\). Every matched horizontal edge is charged once to its left column, every matched vertical edge once to its column, and every singleton once. Thus \(\sum_i w_i=|T|+|M|\), with \(w_i\in\{0,1,2\}\).

If \(w_i=2\), that column has type \((T,T)\), \((T,R)\), \((R,T)\), or \((R,R)\). A singleton having the other rung vertex colored must have both horizontal neighbors uncolored. An \(R\)-vertex must match an \(L\)-vertex in the next column. Consequently the immediate next column has type \((U,U)\), \((U,L)\), \((L,U)\), or \((L,L)\), respectively; in every case \(w_{i+1}=0\). The mapping from columns of weight two to their successor columns of weight zero is injective even cyclically, so \(\sum_i w_i\le n\). Conversely, coloring both endpoints of each rung with their own shared color gives \(n\) colors and is sub-quorum, since each closed neighborhood has two vertices of that color among four colored vertices. Hence \(\psi_{\mathrm{sq}}(G_n)=n\).

Equality holds precisely when every weight-zero column is immediately preceded by a weight-two column: the forward implication above always holds, and equality of the total to \(n\) is equivalent to equality of the numbers of weight-zero and weight-two columns.

**Step 2: finite transfer model.** Let \(\mathcal A\) comprise the \(17\) column types. Two types \(a,b\) are horizontally compatible when in each row the right-match symbol \(R\) appears in \(a\) if and only if the left-match symbol \(L\) appears in \(b\). An ordered pair \((a,b)\) of compatible types is a transfer state. There are exactly \(119\) such states.

There is an edge from \((a,b)\) to \((b,c)\) exactly when \(a,b\) and \(b,c\) are horizontally compatible, each singleton symbol in \(b\) sees at most one colored vertex among its partner in column \(b\) and its two horizontal neighbors in \(a,c\), and either \(w(b)>0\) or \(w(a)=2\). These purely local constraints encode respectively matching consistency, the singleton sub-quorum condition, and the equality criterion from Step 1. A closed transfer walk of length \(n\) corresponds bijectively to one reduced optimal coloring of the labelled \(G_n\). (One fixed starting column is used; quotienting by rotation would be incorrect.) Therefore \(a_n=\operatorname{tr}(B^n)\), where \(B\) is the explicit zero-one adjacency matrix of this \(119\)-state graph.

**Step 3: exact transfer spectrum.** The transfer digraph has three cyclic strongly connected components, of sizes \(49\), \(2\) and \(2\); all remaining components are acyclic. The two size-two components have characteristic polynomial \(x^2-1\). The size-\(49\) component has characteristic polynomial
\[
x^{37}(x^5+x^4-x^3+x-1)(x^7-2x^6-3x^5+2x^4+2x^3-2x-1).
\]
These are **exact finite integer identities**, not fitted recurrences. The standalone verifier reconstructs the \(17\) types, all \(119\) states and all transfer edges, determines their cyclic components, and independently computes their full characteristic polynomials via Newton identities from integer traces. Thus
\[
\det(I-zB)=(1-z^2)^2D_5(z)D_7(z).
\]
Finally, the formal trace-determinant identity \(\sum_{n\ge1}\operatorname{tr}(B^n)z^n=-z\frac{d}{dz}\log\det(I-zB)\) proves the enumerator for every \(n\ge3\).

## Verification
Run `python3 verify.py` (Python standard library only) in a directory containing the provided standalone script. It checks all \(17\) types, \(119\) states and \(343\) locally admissible transitions of the reduced transfer; confirms the three cyclic components and their exact characteristic polynomials; recomputes the series coefficients; and independently enumerates **all** pairs of matchings and singleton sets directly on the original labelled graph for \(n=3,4,5,6\), evaluating the closed-neighborhood inequalities before counting. The direct counts are \(16,65,151,434\). The infinite result follows from the transfer bijection and exact finite characteristic-polynomial identity, not from fitting the small cases.

## Relationship to prior work
Ma, Sahbi, and Zhang, *Sub-quorum colorings of graphs*, arXiv:2609.25128v4, provide the subcubic representative framework (Lemma 2.4 and Theorem 3.3), universal cubic bounds (Corollary 3.4), and the exact maximum for **open** two-row ladders \(P_2\square P_n\) (Theorem 7.3). The maximum-color assertion for cyclic ladders is a straightforward cyclic refinement of that ladder argument and is **not proposed as an independent novelty**. The new statement assessed here is the complete rational generating function for the reduced optimal colorings on **closed** two-row ladders, a counting theorem not implied by the published maximum-only result. The 2013 foundational work *Quorum Colorings of Graphs* introduced the parameter. Allagan's arXiv:2601.03488 studies ordinary **domination** of prisms, not this local-support coloring enumerator.

## Limitations
The coefficients count only optimal sub-quorum colorings whose color classes have size at most two. Optimal colorings with larger classes may exist but are not enumerated. Colors are unlabelled, vertices and cyclic columns are labelled; the result does not count dihedral orbits. The transfer calculation is exact and self-contained but has not been independently audited. Although the closest relevant paper's full current manuscript was examined and published-record searches found no identical enumeration, earlier differently phrased results cannot be ruled out.

## References
1. Haobo Ma, Rafik Sahbi, Wenlin Zhang, *Sub-quorum colorings of graphs*, arXiv:2609.25128v4 (2026); first version publicly available September 20, 2026. https://arxiv.org/pdf/2609.25128v4
2. S. M. Hedetniemi, S. T. Hedetniemi, R. C. Laskar, and H. M. Mulder, *Quorum Colorings of Graphs*, 2013.
3. Julian Allagan, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, arXiv:2601.03488 (2026). https://arxiv.org/abs/2601.03488
