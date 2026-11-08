# A near-square exception for Grundy total domination of rook graphs

## Finding
For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\). A *total dominating sequence* is an ordered sequence of distinct vertices in which each chosen vertex has an open neighbor not adjacent to any earlier chosen vertex. Its last selected set must totally dominate the graph. Write \(\gamma_{\mathrm{gr}}^t\) for the maximum length of such a sequence.

Then the **exact all-order formula** is
\[
\gamma_{\mathrm{gr}}^t(R_{m,n})=\begin{cases}
2m-2,&n=m,\\
2m,&n=m+1,\\
m+n-2,&n\ge m+2.
\end{cases}
\]
In particular, increasing the longer board dimension by one from a square increases the parameter by two, while every subsequent increase beyond the immediately rectangular case increases it by at most one.

Via the published identity \(\gamma_{\mathrm{gr}}^t(G)=|V(G)|-Z^-(G)\), this is equivalently an exact formula for skew zero forcing of rook graphs:
\[
Z^-(R_{m,n})=\begin{cases}
mn-2m+2,&n=m,\\
mn-2m,&n=m+1,\\
mn-m-n+2,&n\ge m+2.
\end{cases}
\]
The two formulations are one invariant theorem under the established duality.

## Assumptions and scope
All graphs are finite, simple, undirected and without loops. The squares of an \(m\)-by-\(n\) board are the vertices of \(R_{m,n}\), and two distinct squares are adjacent exactly when they have the same row or the same column. Thus each square identifies an edge of the complete bipartite graph \(K_{m,n}\). The stated formula applies to every integer \(m,n\ge2\), after interchanging dimensions to arrange \(m\le n\). The open-neighborhood convention is essential: this is *not* the closed-neighborhood Grundy domination number.

## Proof
**Undominated-edge lemma.** For any prefix of a legal sequence, let \(H\subseteq K_{m,n}\) have exactly the already selected edges, and let \(A\) and \(B\) be the sets of vertices (rows and columns) untouched by \(H\). An edge of \(K_{m,n}\), viewed as a vertex of its line graph, is not yet dominated if and only if either (i) both its endpoints belong to \(A\cup B\) (one in each part), or (ii) it is the unique edge in an isolated \(K_2\)-component of \(H\). Indeed, all other edges share an endpoint with a *different* selected edge. Consequently the undominated set is the disjoint union of the \(|A||B|\) edges between untouched vertices and the \(q\) isolated-edge components of \(H\).

**Forest lemma.** Every legal prefix has acyclic selected-edge graph \(H\). For an added edge with at least one untouched endpoint, it cannot create a cycle. If both endpoints were already touched, the new edge cannot dominate an edge joining two untouched vertices. Legality therefore requires adjacency to some previously undominated isolated selected edge. The new edge joins that isolated edge's component to another component; it cannot lie within a single existing component. This again cannot create a cycle. Induction starts from the empty forest.

**Upper bound.** A legal total dominating sequence must eventually touch every row or every column, since otherwise an edge between untouched vertices is undominated. Let \(t\) be the first index at which one whole part is touched. The two parts cannot first become fully touched *simultaneously*: immediately before such a move there would be one untouched vertex in each part and the only edge between them would be selected by the move; that edge is not adjacent to itself, and the move is disjoint from every previously undominated isolated selected edge, so it would not be legal.

At index \(t\), let \(s\) be the number of touched vertices of \(K_{m,n}\), \(c\) the number of nonempty (edge-bearing) components of \(H\), and \(q\le c\) the number of components consisting of one edge. By the forest lemma, \(t=s-c\). From this point onward, no undominated edge lies between two untouched vertices. Every subsequent legal choice must eliminate at least one of the \(q\) isolated-edge components; none can be created by such a move, which necessarily touches a selected edge. There are therefore at most \(q\) remaining moves, and the full length \(\ell\) satisfies
\[
\ell\le s-c+q\le s.
\]
If the rows are first fully touched while \(b\ge1\) columns remain untouched, then \(s=m+n-b\). For \(b\ge2\) we obtain \(\ell\le m+n-2\). For \(b=1\), \(\ell\le m+n-1\); equality requires \(c=q\), meaning that \(H\) is a matching. Since a matching touches equally many row and column vertices, equality is possible only if \(m=n-1\), equivalently \(n=m+1\). Thus, unless \(n=m+1\), the stronger bound \(m+n-2\) holds.

If the columns are first fully touched, and \(a\ge1\) rows remain untouched, then \(s=m+n-a\). For \(a\ge2\) we obtain \(\ell\le m+n-2\). For \(a=1\), equality with \(m+n-1\) would again require a matching, now touching \(m-1\) rows and \(n\) columns. This would imply \(m-1=n\), contrary to \(m\le n\). Hence this case also has \(\ell\le m+n-2\). In the exceptional case \(n=m+1\), the first-row bound gives \(\ell\le2m\). Combining cases proves every asserted upper bound.

**Sharp constructions.** If \(n=m\) or \(n\ge m+2\), first select the squares
\[
(1,1),(1,2),\ldots,(1,n-1)
\]
and then
\[
(2,1),(3,1),\ldots,(m,1).
\]
Every step is legal: while the columns are being added, untouched rows supply new neighbors; while the rows are being added, untouched column \(n\) supplies new neighbors. The \(m+n-2\) selected edges form one nontrivial connected tree meeting every row, so no undominated vertices remain.

If \(n=m+1\), first select a bipartite matching
\[
(1,1),(2,2),\ldots,(m,m)
\]
then choose
\[
(1,m+1),(2,m+1),\ldots,(m,m+1).
\]
Each of the initial \(m\) steps is legal because an untouched column remains and the first untouched-row/column rectangle shrinks; the second block is legal because each step dominates the previously undominated matching edge in its row. The resulting sequence has \(2m\) vertices and totally dominates. This completes the proof for all parameters, including \(m=2\).

## Verification
Two standalone, independently structured exhaustive programs are supplied. `check_coverage.py` does dynamic programming on the union of dominated open neighborhoods, checks every board with \(2\le m\le6\), \(m\le n\le8\), and \(mn\le42\), and explicitly verifies both extremal constructions. `check_selected.py` instead performs dynamic programming on exact sets of already selected squares, recomputing dominated neighborhoods from those sets; it checks nine boards through the \(4\)-by-\(5\) board. Both programs assert the formula against their exhaustive results. Reference outputs are `coverage_output.txt` and `selected_output.txt`. These finite computations are corroboration only; the preceding symbolic proof covers all dimensions.

## Relationship to prior work
Brešar, Henning and Rall (first posted January 27, 2016) introduced and studied longest total dominating sequences, proving general bounds and characterizations. Their inspected main results on trees, complete multipartite graphs and general regular graphs do not give the present formula for line graphs of complete bipartite graphs.

Brešar and collaborators (first posted December 23, 2017) studied Grundy total domination of graph products. Their inspected Cartesian-product section treats paths and cycles rather than the Cartesian product of two complete graphs. Their introduction also records Lin's exact equivalence between Grundy total domination and skew zero forcing, used only to translate the present calculation.

Abiad and collaborators (2022), Lemma 3.5, give \(Z^+(K_r\square K_r)=(r-1)^2+1\), the positive-semidefinite forcing number, not the skew forcing number calculated here. Existing ordinary and positive-semidefinite zero-forcing formulas do not themselves determine the open-neighborhood greedy maximum. The square instance of the present skew result agrees numerically with their positive-semidefinite value, while the adjacent rectangular instance exhibits a one-unit difference from the familiar \(mn-m-n+2\) line-graph expression.

## Limitations
The result is restricted to Cartesian products of two complete graphs with both factors nontrivial. It gives the extremal length but does not classify *all* longest ordered sequences or their reconfiguration graph. The symbolic proof is independent of finite enumeration. Historical priority remains subject to unindexed articles and unpublished tables; absence of a matching search result is not a proof of uniqueness.

## References
- B. Brešar, M. A. Henning and D. F. Rall, *Total Dominating Sequences in Graphs*, arXiv:1601.07525v1, January 27, 2016. https://arxiv.org/abs/1601.07525
- B. Brešar, C. Bujtás, T. Gologranc, S. Klavžar, G. Košmrlj, T. Marc, B. Patkós, Z. Tuza and M. Vizer, *On Grundy Total Domination Number in Product Graphs*, arXiv:1712.08780v1, December 23, 2017. https://arxiv.org/abs/1712.08780
- A. Abiad, B. Brimkov, J. Breen, T. R. Cameron, H. Gupta and R. R. Villagrán, *Constructions of Cospectral Graphs with Different Zero Forcing Numbers*, Electron. J. Linear Algebra **38** (2022), 280–294, DOI:10.13001/ela.2022.6737.
