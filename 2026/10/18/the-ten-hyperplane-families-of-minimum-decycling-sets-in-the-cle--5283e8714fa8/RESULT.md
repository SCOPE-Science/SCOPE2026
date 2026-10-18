# The ten hyperplane families of minimum decycling sets in the Clebsch graph

## Finding

Let \(C\) be the degree-five Clebsch graph on the sixteen even-parity vectors of \(\mathbb F_2^5\), with two distinct vectors adjacent precisely when they differ in four coordinates. A *feedback vertex set* (or *decycling set*) is a set \(S\subseteq V(C)\) for which the induced graph on \(V(C)\setminus S\) is a forest.

For \(1\le i\le5\) and \(b\in\mathbb F_2\), set
\[
H_{i,b}=\{v\in V(C):v_i=b\}.
\]
Then the minimum feedback vertex sets of \(C\) have cardinality \(7\), and are **exactly**
\[
S_{i,b,x}=H_{i,b}\setminus\{x\},\qquad x\in H_{i,b}.
\]
The representation \((i,b,x)\) is unique. There are exactly \(5\cdot2\cdot8=80\) minimum sets. For each one, its nine-vertex complement induces the tree formed by subdividing every edge of a four-leaf star once.

For an integer \(t\ge1\), let \(R_t(C)\) have the eighty minimum feedback vertex sets as vertices, with an edge between distinct sets if each can be obtained from the other by replacing at most \(t\) selected vertices. Then
\[
R_1(C)=R_2(C)\cong10K_8,
\]
whereas \(R_3(C)\) is connected, 23-regular, has \(920\) edges and diameter \(3\). Every vertex of \(R_3(C)\) has exactly \(1,23,48,8\) vertices at distances \(0,1,2,3\), respectively. Thus **three is the sharp simultaneous-exchange threshold for connectivity**. Under the more restrictive single-vertex token-sliding rule, where the outgoing and incoming vertices must be adjacent in \(C\), the reconfiguration graph is \(40K_2\).

The feedback-vertex statement is equivalently a bootstrap-percolation theorem: at the four-neighbor threshold on this five-regular graph, the minimum contagious sets are exactly the same eighty seven-vertex sets, and each activates the entire graph in three synchronous rounds.

## Assumptions and scope

All graphs are finite, simple, undirected. The term *Clebsch graph* specifically denotes the degree-five, forty-edge version, not its ten-regular complement. The parity condition on \(V(C)\) is \(v_1+\cdots+v_5=0\) in \(\mathbb F_2\). An edge of \(C\) changes precisely four of the five bits. The \(H_{i,b}\) are eight-vertex affine hyperplanes of the even-parity space. The move convention counts the number of vertices removed (equivalently inserted); it requires **both endpoints** of each exchange to be minimum feedback vertex sets, not any particular intermediate order of the individual replacements. Token sliding requires exactly one replacement along an edge of \(C\).

## Proof

**1. Fourier lower bounds for induced forests.** For any \(U\subseteq V(C)\), write \(m=|U|\), \(e(U)=|E(C[U])|\), and
\[
a_i=\sum_{u\in U}(-1)^{u_i},\qquad b_{ij}=\sum_{u\in U}(-1)^{u_i+u_j}\quad(i<j).
\]
The sixteen functions consisting of the constant function, the five coordinate characters and the ten pair-product characters form an orthogonal basis of real-valued functions on the even-parity space. Because an edge changes all but one coordinate, the adjacency eigenvalues on these respective characters are \(5\), \(-3\) and \(1\). Orthogonality gives
\[
m^2+\sum_i a_i^2+\sum_{i<j}b_{ij}^2=16m,
\]
and, by expanding the induced edge count in this basis,
\[
2e(U)=\frac{5m^2-3\sum_i a_i^2+\sum_{i<j}b_{ij}^2}{16}.
\]
Eliminating the \(a_i\) yields the exact identity
\[
\boxed{e(U)=\frac{m^2}{4}-\frac{3m}{2}+\frac18\sum_{i<j}b_{ij}^2.}
\]
For \(m=10\), the last term is nonnegative, so \(e(U)\ge10\). An induced forest on ten vertices can have at most nine edges; hence no induced forest in \(C\) has ten or more vertices.

For \(m=9\), each of the ten numbers \(b_{ij}\) is odd, so its square is at least one. Thus \(e(U)\ge8\). A nine-vertex induced forest necessarily has exactly eight edges, and equality forces \(|b_{ij}|=1\) for all pairs. Parseval then gives
\[
\sum_{i=1}^5a_i^2=16\cdot9-9^2-10=53.
\]
Each \(a_i\) is odd and \(|a_i|\le7\), because either sign-halfspace has just eight ambient vertices. The only unordered five-tuples of odd absolute values obeying the square-sum condition are
\[
(7,1,1,1,1),\quad(5,5,1,1,1),\quad(5,3,3,3,1).
\]
The second pattern is impossible: a coordinate with absolute sum five has seven selected vertices in its majority halfspace, and two such seven-sets would have to intersect in at least five vertices, whereas distinct coordinate halfspaces intersect in exactly four.

The third pattern is impossible as well. If \(|a_i|=5\), exactly two chosen vertices lie outside the majority halfspace for coordinate \(i\). For each of the three coordinates \(j\) with \(|a_j|=3\), its majority halfspace contains six chosen vertices; at most four can lie in the majority halfspace for \(i\). Therefore both of the two exceptional vertices must lie in each of those three majority halfspaces. They agree in coordinate \(i\) and in these three further coordinates. Since both have even parity, they agree in the fifth coordinate too, contradicting that they are distinct.

Consequently \(|a_i|=7\) for some \(i\). All eight vertices of one \(H_{i,b}\) belong to \(U\), together with exactly one vertex \(x\notin H_{i,b}\). Conversely, every such nine-set induces a tree: \(C[H_{i,b}]\) is four disjoint edges, while \(x\) has exactly four neighbors in \(H_{i,b}\), no two of them adjacent (the graph is triangle-free). These four neighbors therefore lie in four different matching edges, giving a four-leaf star with each edge subdivided once. The construction is unique because two distinct coordinate halfspaces intersect in at most four vertices. There are \(5\cdot2\cdot8=80\) such nine-vertex forests. Their seven-vertex complements are therefore all minimum feedback vertex sets.

**2. Costs below three.** If two distinct minima belong to one fixed \(H_{i,b}\), they differ by exchanging the two omitted points, so their cost is one. If their coordinate halfspaces have different indices, these halfspaces meet in exactly four vertices; therefore two associated seven-sets intersect in at most four points and require at least three replacements. The two opposite halfspaces for one index are disjoint and require seven. It follows at once that \(R_1(C)=R_2(C)=10K_8\). Within one hyperplane, its four induced graph edges are the only legal token slides, giving \(40K_2\).

**3. Connectivity, degree and distances at three replacements.** Two seven-sets from different coordinate halfspaces can be adjacent in \(R_3(C)\) exactly when both omitted points lie outside the four-point intersection of their halfspaces. Fix a state \(S_{i,b,x}\). It has seven neighbors in its own eight-state clique. For each \(j\ne i\), exactly one halfspace \(H_{j,c}\) excludes \(x\); in that halfspace exactly four choices of its omitted point are outside \(H_{i,b}\). This adds \(4\cdot4=16\) neighbors. Hence every vertex has degree \(23\), and the edge count is \(80\cdot23/2=920\).

Here is a direct distance argument. Every state arising from a different coordinate \(j\ne i\) is within two steps: if the outgoing omitted point is outside the target halfspace and the target's omitted point is outside the outgoing halfspace, there is already an edge; if exactly one of those fails, adjust that omitted point by one move inside its own clique; if both fail, choose a third coordinate \(k\notin\{i,j\}\) where the two omitted even-parity words agree (one must exist, since they already agree in coordinates \(i,j\) and their Hamming distance is even). The opposite \(k\)-halfspace excludes both omitted points, and a state in that halfspace can be chosen adjacent to both endpoints.

The eight states coming from the opposite halfspace \(H_{i,1-b}\) are not within two steps: a common adjacent intermediate state would have to omit a vertex simultaneously outside both complementary \(i\)-halfspaces, which is impossible. But they are all within three steps. Given omitted vertices \(x\in H_{i,b}\) and \(y\in H_{i,1-b}\), even parity implies that they agree in at least one coordinate \(j\ne i\); choose the \(j\)-halfspace excluding both. One move reaches a suitable state in that halfspace from the first endpoint, one move inside its eight-state clique changes its omitted vertex, and a third reaches the second endpoint. Hence precisely these eight states have distance three. The remaining distance counts follow from the 23 neighbors and the total of 80 states: \((1,23,48,8)\), proving connectivity and diameter three.

**4. Bootstrap interpretation.** At the four-neighbor threshold in a degree-five graph, an inactive vertex becomes active precisely when it has at most one inactive neighbor. Complementing the active set therefore iteratively deletes the vertices of degree at most one from the induced inactive subgraph; it empties exactly when that graph is a forest. For the nine-vertex trees found above, the four leaves, the four degree-two vertices, and then the center disappear in successive rounds. Thus each minimum seven-vertex seed percolates in exactly three rounds.

## Verification

Two independently constructed, standalone Python 3 verifiers accompany this result. `verify_walsh_forest.py` builds the Cayley realization on \(\mathbb F_2^4\), enumerates all sixteen-bit vertex subsets, checks induced acyclicity by leaf-stripping, validates the ten geometric families, and constructs the complete exchange graphs and shortest-path profiles. `verify_parity_tree.py` instead constructs the even-parity five-bit realization, checks acyclicity by graph-depth-first traversal of combinations, and independently compares the resulting families, exchange graphs, and induced-tree degree sequences. Run from the directory containing both programs with `python3 verify_walsh_forest.py` and `python3 verify_parity_tree.py`. The corresponding exact output files are `verification_walsh.json` and `verification_parity.json`.

The finite enumerations exhaust all vertex subsets of cardinalities nine and ten; the spectral argument independently proves the ten-vertex obstruction and the exact nine-vertex classification. All exchange-graph data concern the complete family of eighty minima, not a random sample.

## Relationship to prior work

Morrison and Noel (arXiv:1506.04686, first posted 2015-06-15) study threshold percolation in **ordinary hypercubes**, not the sixteen-vertex folded five-cube or its complete minimum-seed exchange geometry. The distinction matters: quotienting by antipodes changes the graph and its percolation rules. Agrawal, Lokshtanov, Mouawad and Saurabh (arXiv:1510.01557, first posted 2015-10-06) study the general parameterized simultaneous feedback-vertex-set problem, not these Clebsch-specific optimum structures. Bousquet and coauthors (DOI:10.1016/j.tcs.2023.114188) investigate feedback-vertex-set reconfiguration, primarily in planar and subcubic graph classes; their stated structural theorems do not cover this nonplanar degree-five graph. The present theorem supplies an exact geometric classification and a sharp three-exchange threshold, rather than general complexity bounds.

## Limitations

The theorem is specific to the degree-five Clebsch graph. It does not assert a general classification for arbitrary folded cubes, nor does it characterize exchanges under a sequential process in which each *individual* replacement must preserve minimality when three vertices are changed simultaneously. The relationship to classical feedback vertex sets and threshold percolation is standard, while the explicit Clebsch classifications and exchange structure have not received an independent literature or scientific audit. Relevant unindexed tabulations or supplements could contain equivalent results.

## References

1. N. Morrison and J. A. Noel, *Extremal Bounds for Bootstrap Percolation in the Hypercube*, arXiv:1506.04686 (initial public posting 2015-06-15), https://arxiv.org/abs/1506.04686 ; readable full text https://ar5iv.labs.arxiv.org/html/1506.04686 .
2. A. Agrawal, D. Lokshtanov, A. E. Mouawad and S. Saurabh, *Simultaneous Feedback Vertex Set: A Parameterized Perspective*, arXiv:1510.01557 (initial public posting 2015-10-06), https://arxiv.org/abs/1510.01557 .
3. N. Bousquet, F. Hommelsheim, Y. Kobayashi, M. Mühlenthaler and A. Suzuki, *Feedback vertex set reconfiguration in planar graphs*, Theoretical Computer Science 979 (2023), 114188, https://doi.org/10.1016/j.tcs.2023.114188 .
4. E. W. Weisstein, *Clebsch Graph*, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html (basic graph parameters only).
