# Minimum zero forcing sets and maximum nullity of cubed broom trees

## Finding

For integers \(t\ge2\) and \(\ell\ge2\), let \(B_{t,\ell}\) be the tree consisting of a path \(v_0v_1\cdots v_\ell\) and \(t\) additional, distinct pendant vertices \(a_1,\ldots,a_t\), each adjacent to \(v_0\). Put \(H_{t,\ell}=B_{t,\ell}^{3}\), the ordinary third graph power, with adjacency between distinct vertices precisely when their distance in the tree is at most three. Then

\[
Z(H_{t,\ell})=M(H_{t,\ell})=t+2.
\]

The exact number \(N_{t,\ell}\) of distinct minimum zero forcing subsets, with all vertices distinguished, is

\[
N_{t,\ell}=\begin{cases}
t+3,&\ell=2,\\
4t+3,&\ell\ge3.
\end{cases}
\]

In particular, the multiplicity is independent of the handle length for every \(\ell\ge3\). The minimum sets are completely classified below.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled at the vertices specified above. A zero forcing process begins with a black set \(S\); a black vertex having exactly one white neighbor may color it black. A zero forcing set eventually colors all vertices. Its minimum size is \(Z(H)\). For a graph \(H\), let \(M(H)\) denote the maximum nullity among real symmetric matrices whose nonzero off-diagonal entries occur exactly on edges of \(H\); the diagonal is unrestricted. We use the standard inequality \(M(H)\le Z(H)\). No claim is made for different graph powers or brooms with more than one long arm.

For \(\ell\ge3\), every minimum zero forcing set is exactly one of the following two disjoint kinds:

1. **All brush vertices:** the whole set \(\{a_1,\ldots,a_t\}\), together with any two distinct vertices of \(\{v_0,v_1,v_2\}\) (three sets).
2. **All but one brush vertex:** choose an omitted \(a_i\), and select three path vertices, either all of \(\{v_0,v_1,v_2\}\), or \(v_\ell\) and any two distinct vertices of \(\{v_{\ell-3},v_{\ell-2},v_{\ell-1}\}\) (four sets for each omitted brush vertex).

For \(\ell=2\), the graph is complete on \(t+3\) vertices; its minimum sets are precisely all complements of individual vertices.

## Proof

**Geometry and the size bound.** In \(H_{t,\ell}\), the brush vertices form a clique of true twins: each \(a_i\) is adjacent to all the other brush vertices and to exactly \(v_0,v_1,v_2\) among path vertices. Also \(v_jv_k\) is an edge exactly when \(1\le|j-k|\le3\). For an algebraic lower bound valid also at \(\ell=2\), put \(r=\ell-1\) and let \(e_0,\ldots,e_{r-1}\) be an orthonormal basis for \(\mathbb R^r\). For indices \(0\le i\le\ell+1\), define

\[
w_i=\sum_{h=\max(0,i-3)}^{\min(i,\ell-2)}e_h.
\]

Assign \(w_0\) to every \(a_i\), and \(w_{j+1}\) to \(v_j\) for \(0\le j\le\ell\). Every assigned vector is nonzero. The intervals of basis coordinates in \(w_i\) and \(w_j\) intersect exactly when \(|i-j|\le3\). Thus the Gram matrix of these assigned vectors has positive off-diagonal entries exactly at the edges of \(H_{t,\ell}\). The vectors \(w_0,\ldots,w_{r-1}\) are linearly independent: their coordinate matrices are upper triangular with diagonal one. Hence the Gram matrix has rank exactly \(r=\ell-1\) and nullity \((t+\ell+1)-(\ell-1)=t+2\). Consequently

\[
Z(H_{t,\ell})\ge M(H_{t,\ell})\ge t+2.
\]

**Forcing constructions.** Suppose \(\ell\ge3\). Start by coloring all brush vertices and any two of \(v_0,v_1,v_2\). A black brush vertex forces the third of these path vertices; next, for every \(3\le j\le\ell\), vertex \(v_{j-3}\) forces \(v_j\). All of its other neighbors are already black at that moment.

Alternatively, omit one \(a_i\) and color all other brush vertices plus \(v_0,v_1,v_2\). A black brush vertex forces the omitted one, and the same forward path-forcing sequence completes the process.

For the remaining configurations, omit one \(a_i\) and initially color the other brush vertices, \(v_\ell\), and two of \(v_{\ell-3},v_{\ell-2},v_{\ell-1}\). First \(v_\ell\) forces the missing predecessor. Then in descending order \(j=\ell-4,\ell-5,\ldots,0\), the vertex \(v_{j+3}\) forces \(v_j\): it has no brush neighbors since \(j+3\ge3\), and its other path neighbors are black. Once \(v_0,v_1,v_2\) are black, a brush vertex forces the omitted \(a_i\). These constructions use \(t+2\) vertices, proving \(Z=M=t+2\).

**Necessity and exact classification.** If two brush vertices initially remain white, neither can ever turn black: every neighbor that could force one is also adjacent to the other. Hence every zero forcing set contains at least \(t-1\) brush vertices. At the minimum size \(t+2\), there are only two possibilities: \(t\) brush vertices and two path vertices, or \(t-1\) brush vertices and three path vertices.

In the former case, no initially black path vertex can force: it has at least three path neighbors (since \(\ell\ge3\)) and at most one other initially black path neighbor. Thus the first force must come from a brush vertex, whose path neighbors are exactly \(v_0,v_1,v_2\); it has exactly one white neighbor if and only if the initial pair of path vertices is two of these three. This gives exactly the first family.

In the latter case, an initially black path vertex from \(v_0,v_1,v_2\) cannot force, because it has an initially white brush neighbor and at least one initially white path neighbor. Every internal path vertex \(v_j\) with \(3\le j<\ell\) has at least four path neighbors but at most two other initially black path vertices, and so cannot force. The only possible first forcing vertices are brush vertices or the path endpoint \(v_\ell\). A brush vertex has the sole white brush vertex and the three path vertices \(v_0,v_1,v_2\) as neighbors, and can force initially exactly when all these three path vertices are black. The endpoint \(v_\ell\) has precisely three path neighbors \(v_{\ell-3},v_{\ell-2},v_{\ell-1}\), and can force initially exactly when it is black and two of those three neighbors are black. The four permitted path triples exhaust the second family. The forcing constructions above prove each is valid. Therefore the count is \(3+t(1+3)=4t+3\).

When \(\ell=2\), all vertices have pairwise tree-distance at most three, so \(H_{t,2}=K_{t+3}\). Every complement of one vertex and no smaller set zero forces a complete graph, giving \(Z=M=t+2\) and precisely \(t+3\) minimum sets. This closes all boundary cases.

## Verification

The accompanying standalone script `verify.py` constructs the original broom by edges, obtains its third power using breadth-first search, enumerates every vertex subset of cardinalities \(t+1\) and \(t+2\), and implements the one-neighbor forcing rule. It separately checks the predicted family and exact Gram matrix support/rank for each pair \(2\le t\le5\), \(2\le\ell\le9\), a total of 32 parameter pairs. Expected output is in `verify_output.txt`. These checks are finite corroboration only; the unrestricted result is proved above.

## Relationship to prior work

Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker (2026, arXiv:2610.03892) study graph-power zero forcing. Their Proposition 7 gives exact values for powers of paths; Proposition 9 gives upper bounds for spiders with **equal** arm lengths, with a conjecture concerning sharpness. The present objects have \(t\) unit arms and a single arbitrary-length handle, and the principal new assertion is the classification/count of all minimum forcing sets in their cubes. The familiar maximum-nullity inequality is used, not claimed new.

DeAlba and coauthors (2012) prove path-power minimum-rank results and address strict powers and squares of trees; Chang and Lin (2013) determine the square-of-tree case. These theorems do not enumerate the minimum zero forcing sets of the present third powers. A true-twin substitution or path-power reformulation alone does not supply the exact exhaustive first-move classification above.

## Limitations

No classification is asserted for arbitrary spiders, fourth or higher powers, general graph families, or all cardinality coefficients. Publication-priority searches and primary-text comparisons cannot exclude unindexed prior work; independent mathematical review has not been performed. Computational checks cover only the stated finite ranges.

## References

1. A. Abiad, M. Flagg, S. Ghasemi Nezhad, S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892, first available 2026-10-02. https://arxiv.org/abs/2610.03892
2. L. M. DeAlba, J. Grout, S. Kirkland, J. J. McDonald, A. Yielding, *Minimum Rank of Powers of Trees*, Electronic Journal of Linear Algebra 23 (2012), 151–163. https://journals.uwyo.edu/index.php/ela/article/download/1023/1023/1023
3. G. J. Chang, J. C.-H. Lin, *Minimum Rank of Powers of Cycles and Trees* (2013), https://www-math.nsysu.edu.tw/~chlin/Publications/Articles/GJpower.pdf
4. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648.
