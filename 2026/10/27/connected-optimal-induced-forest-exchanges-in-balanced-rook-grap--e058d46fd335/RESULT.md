# Connected optimal induced-forest exchanges in balanced rook graphs

## Finding
For every integer \(n\ge2\), let \(R_n=K_n\square K_n=L(K_{n,n})\), the rook graph on an \(n\)-by-\(n\) board. An *induced forest* is a vertex set whose induced subgraph is acyclic. Let \(X_n\) be the graph whose vertices are maximum-cardinality induced forests of \(R_n\); two are adjacent when one selected rook-cell vertex is removed and a different one inserted while preserving maximum cardinality and acyclicity.

**Theorem.** Every maximum induced forest of \(R_n\) has \(2n-1\) vertices and corresponds uniquely to a Hamiltonian path of \(K_{n,n}\). The graph \(X_n\) is connected and vertex-transitive, and
\[
|V(X_n)|=(n!)^2,\qquad \deg(X_n)=4n-5,\qquad
|E(X_n)|=\frac{(n!)^2(4n-5)}2.
\]
Its number of unordered triangles is exactly
\[
\boxed{\#K_3(X_n)=\frac{(n!)^2(2n^2-5)}3.}
\]
In particular, the minimum feedback-vertex-set cardinality in the rook graph is \((n-1)^2\), and every two minimum feedback-vertex sets are joined by a sequence of optimum-preserving one-for-one cell exchanges.

## Assumptions and scope
All graphs are finite, simple and undirected. Board rows and columns are separately labeled \(1,\ldots,n\), with \(n\ge2\). The bijection from rook vertices to edges of \(K_{n,n}\) sends cell \((i,j)\) to its row-column edge. Vertices of \(X_n\) are *sets* of selected rook cells, not oriented walks or colorings; an edge means symmetric difference of size two. A triangle is a three-element set of pairwise adjacent vertices. Connectivity is ordinary graph connectivity; no intermediate nonoptimum configuration is permitted.

## Proof
**1. Optimal forests are Hamilton paths.** Given a cell subset \(S\), let \(H\) be the corresponding edge subgraph of \(K_{n,n}\), retaining its full \(2n\)-vertex set. The rook-induced graph \(R_n[S]\) is the line graph \(L(H)\). If a vertex of \(H\) has degree at least three, its incident edges induce a triangle in \(L(H)\). If \(H\) contains a cycle, the edges along that cycle give a cycle in \(L(H)\). Conversely, when \(H\) is a union of paths and isolated vertices, its line graph is a union of paths and is acyclic. Hence \(R_n[S]\) is a forest if and only if \(H\) is a *linear forest* (an acyclic graph of maximum degree at most two). Every forest on \(2n\) vertices has at most \(2n-1\) edges, with equality only for a spanning tree. An alternating Hamiltonian path in \(K_{n,n}\) realizes \(2n-1\); a tree of maximum degree at most two is necessarily a path. This also proves that every optimum \(S\) arises from a Hamiltonian path.

Each unoriented Hamiltonian path of \(K_{n,n}\) admits exactly one orientation beginning in the row part and ending in the column part. Such a path has the form
\[
P=(\ell_1,r_1,\ell_2,r_2,\ldots,\ell_n,r_n),
\]
where the two subscript orders are independently arbitrary permutations. Consequently \(|V(X_n)|=(n!)^2\). The row- and column-relabeling group acts transitively on these paths, so it acts vertex-transitively on \(X_n\).

**2. Every one-cell exchange.** Number the path edges consecutively \(e_j=\{P_j,P_{j+1}\}\), \(1\le j\le2n-1\). Removing \(e_j\) splits the path into two paths whose endpoints are respectively \(P_1,P_j\) and \(P_{j+1},P_{2n}\). To obtain another Hamilton path by adding one previously unused row-column edge, that edge must join endpoints of these two components. One choice is always available: \(f_0=\{P_1,P_{2n}\}\). For even \(j\), it is the only choice besides restoring \(e_j\). For odd interior \(j\), where \(3\le j\le2n-3\), the two additional available edges are
\[
\{P_1,P_{j+1}\}\quad\text{and}\quad\{P_j,P_{2n}\}.
\]
For the two odd boundary positions \(j=1\) and \(j=2n-1\), the only new choice is \(f_0\), since one nominal alternative coincides with \(f_0\) and the other restores \(e_j\). Thus the number \(q_j\) of replacements after deleting \(e_j\) is one at \(n-1\) even and two boundary positions, and three at the remaining \(n-2\) odd interior positions. Every neighboring edge set determines uniquely both its removed and added edge. It follows that each vertex has degree
\[
(n-1)+2+3(n-2)=4n-5.
\]
Multiplying by the number of vertices and dividing by two gives the asserted edge count.

**3. Exact triangle count.** Fix a Hamilton path \(P\). Every neighbor has edge set \(E(P)-\{e\}+\{f\}\). Two distinct neighbors are adjacent precisely if they have the same removed edge \(e\) or the same added edge \(f\): if both removed and added edges differ, their symmetric difference has four edges. Therefore the number of triangles through \(P\) is the sum of \(\binom{q_e}{2}\) over removed edges and \(\binom{c_f}{2}\) over added edges, where \(c_f\) is the number of admissible removals associated with that added edge. By step 2, the first sum is \(3(n-2)\). The endpoint edge \(f_0\) arises from all \(2n-1\) possible removals. Every other possible added edge connects an endpoint to a distinct nonneighboring internal vertex and arises for exactly one removal. Hence the second sum is \(\binom{2n-1}{2}\). The number of triangles through each vertex is
\[
3(n-2)+\binom{2n-1}{2}=2n^2-5.
\]
Every triangle has three vertices, giving the total formula. This argument also covers \(n=2\), where the odd-interior range is empty.

**4. All optimal forests can be exchanged into one another.** Work with the unique path orientation starting in the row part. For any \(2\le k\le n\), reversing the first \(2k-1\) path vertices changes only one edge: remove \(\ell_k r_k\) and insert \(\ell_1 r_k\). On the two orders this move acts as a reversal of the first \(k\) row entries together with a reversal of the first \(k-1\) column entries. Denote these simultaneous reversals by \(F_k\). The move \(F_2\) is the pure transposition of the first two row entries, with the column order fixed.

Prefix reversals of lengths \(2,\ldots,n\) generate all permutations of an \(n\)-entry list (the elementary prefix-sorting argument moves the required last entry to the front and then into its desired position, successively). Thus the projection of the group generated by the \(F_k\) onto permutations of row positions is the full symmetric group. Conjugating the pure first-two-row transposition \(F_2\) by elements with arbitrary row projections yields *every* pure row transposition. Hence arbitrary row permutations, fixing the columns, are reachable. Cancelling the row part of each \(F_k\) now supplies independent reversals of the first \(k-1\) column entries, so arbitrary permutations of the first \(n-1\) columns, with the last fixed, are reachable.

Finally, reversing the last three path vertices \((r_{n-1},\ell_n,r_n)\) is a single allowed exchange: it removes \(\ell_{n-1}r_{n-1}\) and adds \(\ell_{n-1}r_n\). It interchanges the last two column entries while leaving the row order unchanged. Along with permutations of the first \(n-1\) column entries, this generates all column permutations. Thus both row and column orders may be prescribed arbitrarily by legal single-edge exchanges, so \(X_n\) is connected for all \(n\ge2\).

## Verification
The standalone standard-library checker `rook_forest_verify.py` independently enumerates all subsets of the rook board for \(n=2,3,4\), computes the induced-forest property directly by a disjoint-set cycle test, and verifies the optimum and its multiplicity. For \(n=2,3,4,5\), it constructs every alternating Hamilton path, independently enumerates valid *edge-set exchanges* rather than relying on the replacement classification, and verifies connectedness, degrees, all edges and triangles. It also compares a separate reversal construction at the smallest parameters. The complete computed data are:

| \(n\) | Maximum forest size | Optima | Exchange degree | Exchange edges | Exchange triangles |
|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 4 | 3 | 6 | 4 |
| 3 | 5 | 36 | 7 | 126 | 156 |
| 4 | 7 | 576 | 11 | 3,168 | 5,184 |
| 5 | 9 | 14,400 | 15 | 108,000 | 216,000 |

Run `python3 rook_forest_verify.py` with Python 3.9 or newer. The checker is finite corroboration; the preceding proof establishes the formulas for all \(n\ge2\).

## Relationship to prior work
The induced-forest and feedback-vertex-set framework is classical. Chappell and Pelsmajer [1] study extremal induced forests with degree constraints and bounded treewidth. Bell [2] recognizes line graphs of balanced complete bipartite graphs via Hamilton-path star complements for eigenvalue minus two. These results motivate the line-graph formulation but their identified theorems do not assert the exact optimum-exchange adjacency counts or triangle counts above. The Hamilton-path reconfiguration literature, including Kazazi [3], considers endpoint-rotation (backbite) moves and proves sufficient conditions for connectivity in other graph classes. The square-Hamilton-path and two-thirds minimum-degree conditions stated in [3] do not apply to \(K_{n,n}\); moreover, the present exchange model admits closing the endpoints and reopening an arbitrary path edge, an operation not restricted to one backbite. The unrestricted Hamilton-path enumeration and the scalar induced-forest maximum are elementary reductions and not claimed as independent novelties.

## Limitations
This theorem addresses only balanced rook graphs and ordinary one-for-one changes among maximum induced forests. It does not determine the exchange-graph diameter, its complete cycle spectrum, or unbalanced rectangles. No independent external validation has been performed. The accessible abstract of [3], rather than its inaccessible complete text, supported one part of the literature comparison; unindexed prior computations or an uninspected discussion of \(K_{n,n}\) remain originality risks.

## References
[1] G. G. Chappell and M. J. Pelsmajer, *Maximum Induced Forests in Graphs of Bounded Treewidth*, Electronic Journal of Combinatorics 20(4), P8 (2013), doi:10.37236/3826. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i4p8/pdf/ . First public publication verified 2013-10-28.

[2] F. K. Bell, *Line graphs of bipartite graphs with Hamiltonian paths*, Journal of Graph Theory 43 (2003), 137–149, doi:10.1002/jgt.10107. Publisher first-public date verified 2003-04-21; abstract accessible.

[3] A. Kazazi, *Connectivity of the reconfiguration graph of Hamiltonian paths*, arXiv:2610.05068 (first public 2026-10-04). Accessible abstract: https://arxiv.org/abs/2610.05068 .
