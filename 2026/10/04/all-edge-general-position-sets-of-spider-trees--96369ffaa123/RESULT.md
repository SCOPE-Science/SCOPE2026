# All edge general-position sets of spider trees
## Finding
Let \(T\) be a spider tree with center \(c\), \(k\ge 3\) arms \(A_1,\ldots,A_k\), and positive arm lengths \(\ell_1,\ldots,\ell_k\). For \(X\subseteq E(T)\), write \(a_i=|X\cap E(A_i)|\). Then \(X\) is an edge general-position set if and only if either \(a_i\le 1\) for every \(i\), or there is a unique \(i\) with \(a_i=2\) and \(a_j=0\) for every \(j\ne i\). Consequently the size enumerator is \[P_T(z)=\prod_{i=1}^k(1+\ell_i z)+z^2\sum_{i=1}^k\binom{\ell_i}{2}.\] The inclusion-maximal edge general-position sets are exactly the sets containing one edge from every arm, together with the two-edge subsets contained in a single arm. Hence \(\operatorname{gp}_{\rm e}(T)=k\), there are \(\prod_i\ell_i\) maximum sets, and the total number of inclusion-maximal sets is \(\prod_i\ell_i+\sum_i\binom{\ell_i}{2}\).

## Assumptions and scope
A spider tree is a finite tree with a distinguished center \(c\) of degree \(k\ge 3\) such that deleting \(c\) leaves \(k\) paths. The corresponding center-to-leaf paths are the arms \(A_1,\ldots,A_k\), and \(\ell_i=|E(A_i)|\ge 1\). An edge set is in edge general position when no geodesic contains three of its edges.

## Proof
Because \(T\) is a tree, every pair of vertices has a unique geodesic.

Let \(X\subseteq E(T)\) and put \(a_i=|X\cap E(A_i)|\). First, \(a_i\le 2\) for every \(i\): if one arm contained three selected edges, the unique path between suitable vertices beyond the first and third selected edges would be a geodesic containing all three.

Next, for distinct arms \(A_i,A_j\), the unique path joining a vertex beyond the selected edges of \(A_i\) to a vertex beyond the selected edges of \(A_j\) passes through the center and contains every selected edge from those two arms. Hence
\[
a_i+a_j\le 2
\]
for all distinct \(i,j\).

These inequalities give exactly two possibilities. Either every \(a_i\le 1\), or some \(a_i=2\), in which case \(a_j=0\) for every \(j\ne i\). Conversely, each of these two patterns is edge general position: a geodesic uses edges from at most two arms, so in the first case it contains at most two selected edges, while in the second case all selected edges are the two edges in one arm.

For the size enumerator, sets of the first type are obtained independently by choosing no edge or one of the \(\ell_i\) edges from each arm, giving
\[
\prod_{i=1}^k(1+\ell_i z).
\]
The second type contributes exactly \(\sum_i\binom{\ell_i}{2}\) additional two-edge sets, yielding the stated formula.

For maximality, a set with at most one edge per arm is inclusion-maximal exactly when every arm contributes one edge. A two-edge set contained in one arm is automatically inclusion-maximal, because adding any third edge either creates three selected edges in that arm or creates a geodesic containing the two selected arm edges and the new edge in another arm. No other maximal patterns exist by the classification.

Therefore every maximum set chooses one edge from each of the \(k\) arms, so its size is \(k\) and the number of maximum sets is \(\prod_i\ell_i\). Counting both maximal types gives the final maximal-set formula.

## Verification
An independent checker constructs each spider as an ordinary graph, reconstructs its unique shortest paths, tests every edge subset directly against the definition, and then tests inclusion-maximality. It verifies the enumerator and maximal-set classification for all checked spider types with three to five arms, arm lengths from one through four, and at most ten edges in total. The all-orders statement is proved symbolically above.

## Relationship to prior work
Manuel, Prabha, and Klavžar introduced edge general position and proved that for an arbitrary tree the edge general-position number equals the number of leaves. For a spider this gives the maximum cardinality \(k\), but it does not classify all feasible edge sets, count maximum sets, or describe all inclusion-maximal sets. Tian, Klavžar, and Tan later revisited extremal edge general-position sets, including trees and block graphs, without giving this spider all-set enumerator in the inspected material.

Targeted searches for spider edge general-position sets, edge general-position enumerators, and polynomial refinements did not locate an equivalent classification. The present result refines the known tree extremal value to a complete feasible-set and maximal-set description on the basic one-branch-vertex tree family.

## Limitations
The formula is specific to spider trees. General trees can have geodesics crossing several branching vertices, so the arm-count reduction used here does not directly extend. The finite checker is corroborative only and does not replace the proof. Literature search cannot exclude differently phrased or non-indexed prior work.

## References
1. P. Manuel, R. Prabha, S. Klavžar, “Edge general position problem,” arXiv:2105.04292, later published in Bulletin of the Malaysian Mathematical Sciences Society, DOI 10.1007/s40840-022-01319-8.
2. J. Tian, S. Klavžar, E. Tan, “Extremal edge general position sets in some graphs,” arXiv:2302.01587, Graphs and Combinatorics 40 (2024), Article 40, DOI 10.1007/s00373-024-02770-z.
