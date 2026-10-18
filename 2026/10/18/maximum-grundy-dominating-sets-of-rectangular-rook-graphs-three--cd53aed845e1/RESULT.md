# Maximum Grundy dominating sets of rectangular rook graphs: three forest types and exact counts

## Finding
Let \(m,n\ge2\) be integers, and let \(R_{m,n}=K_m\square K_n\) be the rook graph on the \(m\times n\) labeled board. A *legal dominating sequence* is an ordering \((v_1,\ldots,v_t)\) of distinct vertices such that each closed neighborhood \(N[v_i]\) contains a vertex not in the earlier closed neighborhoods, and the union of all closed neighborhoods is the vertex set. A *maximum Grundy dominating set* is the unordered support of such a sequence having maximum possible length. We count supports, not orderings.

The Grundy domination number is \(\gamma_{\rm gr}(R_{m,n})=m+n-2\). Let \(g_{m,n}\) count distinct maximum Grundy dominating sets. Write \(S(a,b)\) for a Stirling number of the second kind, with \(S(0,0)=1\) and \(S(a,b)=0\) for \(b>a\). Define
\[
\begin{aligned}
A_{m,n}&=m(m-1)^{n-1}\bigl(n^{m-2}-n!S(m-2,n)\bigr),\\
B_{m,n}&=n(n-1)^{m-1}\bigl(m^{n-2}-m!S(n-2,m)\bigr),\\
C_{m,n}&=mn(m-1)^{n-2}(n-1)^{m-2}.
\end{aligned}
\]
Then for every \(m,n\ge2\) except \((m,n)=(2,2)\),
\[
\boxed{g_{m,n}=A_{m,n}+B_{m,n}+C_{m,n}.}
\]
The exceptional value is \(g_{2,2}=6\). More precisely, maximum sets are in bijection with the three spanning-forest types described below, and the summands count those three disjoint types (apart from a two-to-one parametrization of type C when \(m=n=2\)).

## Assumptions and scope
Rows and columns are individually labeled, the graph is finite and simple, and \(m,n\ge2\). Associate each rook-graph vertex \((r,c)\) with the edge \(rc\) of the complete bipartite graph \(K_{m,n}\), whose partite sets are the row labels and column labels. For an unordered rook-graph set \(D\), let \(F(D)\) be the corresponding bipartite edge set. A leaf means degree one in the selected edge subgraph, not in the complete bipartite graph.

The three types are:

1. **A:** Exactly one row label is absent from \(F(D)\); the selected edges form a tree spanning the other \(m-1\) rows and **all \(n\) columns**, and at least one column is a leaf.
2. **B:** Exactly one column label is absent; the selected edges form a tree spanning **all \(m\) rows** and the other \(n-1\) columns, and at least one row is a leaf.
3. **C:** All row and column labels occur; the edges form a tree spanning \(m-1\) rows and \(n-1\) columns, plus a disjoint single edge joining the omitted row and omitted column. Thus there are two components, one being a single edge. When \(m=n=2\), both components are single edges.

## Proof
**1. The length bound and structure of every maximum sequence.** After selecting any set of rook positions, let \(U\) be the set of row labels occurring and \(W\) the set of column labels occurring. The already dominated cells are *exactly* those whose row belongs to \(U\) or whose column belongs to \(W\). In particular, a prefix is dominating if and only if \(U\) includes every row or \(W\) includes every column. While both sides have an unrepresented label, the next position is legal precisely when it introduces at least one new label (row or column).

For a legal dominating sequence of length \(t\ge2\), its first \(t-1\) positions cannot already dominate. Their row and column supports therefore have sizes at most \(m-1\) and \(n-1\). The first selected edge introduces two labels; each of the remaining \(t-2\) prefix edges introduces at least one. Consequently \(2+(t-2)\le(m-1)+(n-1)\), so \(t\le m+n-2\). Equality is attained by choosing positions along one fixed column in \(m-1\) different rows, then choosing a position in each of the remaining \(n-1\) columns in one of those rows. Hence \(\gamma_{\rm gr}(R_{m,n})=m+n-2\).

In an extremal sequence, immediately before its last choice there are exactly \(m-1\) represented rows and \(n-1\) represented columns. Every choice after the first and before the last must have introduced **exactly one** new label. Therefore the first \(m+n-3\) chosen edges form a tree spanning the represented \(m-1\) row and \(n-1\) column labels: the first edge connects two labels, and every subsequent edge joins one new label to the existing component. The last edge introduces either (i) just a column, (ii) just a row, or (iii) both. In the three cases it respectively attaches a leaf column, attaches a leaf row, or forms a detached edge. These are exactly types A, B and C.

Conversely, any type-A or type-B tree with a leaf on the fully represented side can be ordered by first growing the tree *after deleting that leaf*, then taking the leaf edge last. Growth is possible by an arbitrary rooted-tree exploration, starting with one edge; every subsequent edge introduces one new label and so is legal while neither side is fully represented. The last leaf edge makes one entire side represented, completing domination. For type C, grow the larger tree similarly and choose the detached edge last; that edge introduces both previously missing labels and completes domination. All three types have \(m+n-2\) edges, proving the claimed exact classification.

**2. Bipartite tree count with a specified leaf-side condition.** For positive integers \(a,b\), the following degree-enumerating identity holds for spanning trees \(T\) of the labeled bipartite graph \(K_{a,b}\):
\[
\sum_T\ \prod_{i=1}^{a}x_i^{\deg_T(u_i)-1}\prod_{j=1}^{b}y_j^{\deg_T(v_j)-1}
=\bigl(\sum_{i=1}^{a}x_i\bigr)^{b-1}\bigl(\sum_{j=1}^{b}y_j\bigr)^{a-1}.
\]
For completeness, weight edge \(u_iv_j\) by \(x_i y_j\), put \(X=\sum_i x_i\) and \(Y=\sum_j y_j\), and apply the weighted matrix-tree theorem. After deleting the row and column of \(v_b\), the Laplacian cofactor has row-side block \(Y\operatorname{diag}(x_i)\), column-side block \(X\operatorname{diag}(y_j)\) for \(j<b\), and cross-block entries \(-x_i y_j\). Its Schur complement is \(X\bigl(\operatorname{diag}(y_j)_{j<b}-yy^{\mathsf T}/Y\bigr)\), with determinant \(X^{b-1}(\prod_{j<b}y_j)y_b/Y\). Multiplying by the row-block determinant \(Y^a\prod_i x_i\), then dividing by \(\prod_i x_i\prod_j y_j\), gives the stated identity. The polynomial identity extends to zero weights by continuity.

Setting every variable to one gives \(a^{b-1}b^{a-1}\) labeled bipartite spanning trees. Fixing all \(x_i=1\), a column has degree one precisely when its exponent of \(y_j\) is zero. Thus trees *without* any column leaf correspond to words of length \(a-1\) over \(b\) letters that use every letter. There are \(b!S(a-1,b)\) such words. Hence the number of trees with at least one column leaf equals
\[
\boxed{a^{b-1}\bigl(b^{a-1}-b!S(a-1,b)\bigr).}
\]
The analogous formula for trees with at least one row leaf follows by interchanging \(a,b\).

**3. Count the three disjoint types.** For type A, choose the missing row in \(m\) ways and apply the preceding leaf-column formula with \(a=m-1,b=n\), yielding \(A_{m,n}\). For type B, choose the missing column in \(n\) ways and apply the symmetric leaf-row formula with \(a=m,b=n-1\), yielding \(B_{m,n}\). For type C, choose the row and column endpoints of the detached edge in \(mn\) ways; the remaining labels support \((m-1)^{n-2}(n-1)^{m-2}\) spanning trees. Except when \(m=n=2\), the single-edge component is uniquely identifiable, so this gives \(C_{m,n}\). In the exceptional \(2\times2\) case the two components are both edges, and the \(mn=4\) parametrizations describe just two perfect matchings; together with two type-A sets and two type-B sets, this gives \(g_{2,2}=6\). The three support patterns are disjoint, completing the proof.

## Verification
A standalone Python verifier, `verify.py`, uses the rook graph's **actual closed neighborhoods** and searches for a legal ordering of every candidate set of the theoretical maximum size. It independently compares membership to the three forest conditions and checks the closed formulas by exhaustive enumeration for nine boards: \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4)\). Its captured stdout is `verification_output.txt`. The count totals are respectively \(6,20,34,52,74,108,564,2400,4752\). Run `python3 verify.py` in a directory containing the extracted file. The proof, not the finite tests, establishes all dimensions.

## Relationship to prior work
Brešar et al., *Dominating sequences in grid-like and toroidal graphs* (arXiv:1607.00248v1, §3), explicitly exhibit a Grundy dominating sequence of length \(m+n-2\) in Cartesian products of complete graphs; **that lower-bound construction is not new**. The paper does not classify all maximum unordered supports or count them. Brešar, Pandey and Sharma, *Computation of Grundy dominating sequences in (co-)bipartite graphs* (arXiv:2310.10566v1), establish complexity results and a chain-graph algorithm but do not provide this rook-graph count. Mertens, *Domination Polynomial of the Rook Graph* (arXiv:2401.00716v1), enumerates **all dominating sets**, viewing rook placements as edges of a complete bipartite graph, but does not impose or enumerate the maximum-length sequential legality constraint. Our count is a proper refinement: for instance, on \(R_{3,3}\), there are \(108\) maximum Grundy supports of size \(4\), versus \(117\) arbitrary dominating sets of size \(4\) in the published polynomial.

## Limitations
The result counts unordered supports, not the number of legal orderings of each support. It applies only to Cartesian products of two nontrivial complete graphs and does not classify optimizers for other products. Finite enumeration cannot establish historical novelty or the unrestricted mathematical theorem. The relation to potentially unindexed equivalent characterizations remains an originality risk.

## References
1. B. Brešar, C. Bujtás, T. Gologranc, S. Klavžar, G. Košmrlj, B. Patkós, Z. Tuza and M. Vizer, *Dominating sequences in grid-like and toroidal graphs*, arXiv:1607.00248v1 (2016), especially Section 3. https://arxiv.org/abs/1607.00248
2. B. Brešar, A. Pandey and G. Sharma, *Computation of Grundy dominating sequences in (co-)bipartite graphs*, arXiv:2310.10566v1 (2023). https://arxiv.org/abs/2310.10566
3. S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716v1 (2024). https://arxiv.org/abs/2401.00716
4. B. Brešar and T. Dravec, *Graphs with unique Grundy dominating sets*, arXiv:2103.10172v1 (2021). https://arxiv.org/abs/2103.10172
