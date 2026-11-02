# Maximum induced matchings of the Pappus graph recover its line graph

## Finding
Let \(P\) be the eighteen-vertex Pappus graph, realized as the point-line incidence graph of the nine-point affine plane \(\operatorname{AG}(2,3)\) after removing one parallel class. An *induced matching* is a set of edges with no shared endpoints and no other graph edge between endpoints of distinct selected edges. Let \(\mathcal M\) be the set of maximum induced matchings of \(P\). For \(M,N\in\mathcal M\), join \(M\) and \(N\) when \(|M\setminus N|=|N\setminus M|=2\). Then

\[
\nu_s(P)=5,\qquad |\mathcal M|=27,\qquad \mathcal E_2(P)\cong L(P).
\]

In particular, the two-edge-replacement graph \(\mathcal E_2(P)\) is connected, four-regular, has \(54\) edges and \(18\) edge-disjoint triangles (each edge belongs to exactly one triangle). Its all-source shortest-path profile, at distances \(0,1,2,3,4\), is

\[
(1,4,8,12,2).
\]

It has radius and diameter \(4\). Its unordered-pair distance counts at distances \(1,2,3,4\) are \((54,108,162,27)\). Among the \(351\) unordered pairs of distinct maximum matchings, the intersection/distance pairs \((|M\cap N|,d(M,N))\) occur exactly as follows:

\[
(3,1):54,\quad(1,2):108,\quad(0,3):162,\quad(0,4):27.
\]

Consequently a single-edge replacement never connects distinct optimal matchings; two-edge replacement is the sharp mobility threshold. For every pair,

\[
\left\lceil\frac{5-|M\cap N|}{2}\right\rceil
\le d(M,N)\le
\left\lceil\frac{5-|M\cap N|}{2}\right\rceil+1,
\]

and exactly \(27\) unordered pairs require the extra step.

## Assumptions and scope
Use \(\mathbb F_3=\{0,1,2\}\). The nine point vertices are \((x,y)\in\mathbb F_3^2\), and the nine line vertices are \(L_{s,b}=\{(x,sx+b):x\in\mathbb F_3\}\), for \(s,b\in\mathbb F_3\). A point and a line are adjacent precisely when the point lies on the line. The omitted parallel class consists of the vertical lines. Distinct edges in the two-replacement graph must each have cardinality five and intersect in three edges; no intermediate nonmaximum configurations are allowed. The claim is for this fixed graph, not for arbitrary affine planes or arbitrary incidence graphs.

## Proof
**Maximum size.** If an induced matching contains \(r\) point-line flags, the \(r\) selected points are incident to exactly one selected line each, hence to two of the \(9-r\) unselected lines each. Counting those incidences gives \(2r\le3(9-r)\), so \(r\le5\).

**Complete classification.** Let \(S\) be the selected five point vertices of a size-five induced matching. For each \(p\in S\), its selected line must meet \(S\) only in \(p\), so every selected point requires a tangent among the three allowed line directions. Classify \(S\) by the occupancies of the three vertical columns. The only possible profiles are \((3,2,0)\), \((3,1,1)\), and \((2,2,1)\). In the first profile, each selected point in the column containing two selected points has no tangent, because every nonvertical line through it meets the full column. In the second, each singleton-column point has no tangent for the same reason. In the third, translate so that the unique point in the singleton column is \((0,0)\). Write the missing points of the other two columns as \((1,a)\) and \((2,b)\). A line of slope \(s\) through \((0,0)\) is a tangent only if its other two points are missing, which forces \(a=s\) and \(b=2s=-s\). Hence \(a+b=0\). The five selected points are then exactly the union of the two nonvertical lines through \((0,0)\) of slopes distinct from \(s\). Conversely, whenever \(S=A\cup B\) for two intersecting allowed lines of different slopes, each point has exactly one tangent among the nine allowed lines: the intersection point has the third-direction line, and either other point of \(A\) (respectively \(B\)) has the parallel to \(B\) (respectively \(A\)). These five tangent flags form an induced matching. Therefore every maximum is obtained uniquely from an unordered pair \(A,B\) of intersecting allowed lines. There are \(\binom32\cdot3^2=27\) such pairs.

**Canonical flags and local exchange.** For each incident point-line flag \(e=(p,C)\), let \(A,B\) be the other two allowed lines through \(p\), and let \(M_e\) be the five tangent flags of \(A\cup B\). Its distinguished flag is \(e\), and the preceding classification proves that \(e\mapsto M_e\) is a bijection from the \(27\) flags onto \(\mathcal M\). The affine transformations \(x\mapsto\delta x+\eta\), \(y\mapsto\alpha y+\beta x+\gamma\), where \(\delta,\alpha\in\mathbb F_3^\times\), act transitively on flags. It is therefore enough to examine \(e=((0,0),L_{0,0})\). Its matching consists of the flags

\[
((0,0),L_{0,0}),\ ((1,1),L_{2,2}),\ ((1,2),L_{1,1}),\ ((2,1),L_{1,2}),\ ((2,2),L_{2,1}).
\]

The following exact table lists \(|M_e\cap M_f|\) for every flag \(f=((x,y),L_{s,y-sx})\), with columns \(s=0,1,2\):

| \((x,y)\) | \(s=0\) | \(s=1\) | \(s=2\) |
|---|---:|---:|---:|
| \((0,0)\) | 5 | 0 | 0 |
| \((0,1)\) | 0 | 1 | 1 |
| \((0,2)\) | 0 | 1 | 1 |
| \((1,0)\) | 0 | 0 | 0 |
| \((1,1)\) | 1 | 0 | 3 |
| \((1,2)\) | 1 | 3 | 0 |
| \((2,0)\) | 0 | 0 | 0 |
| \((2,1)\) | 1 | 3 | 0 |
| \((2,2)\) | 1 | 0 | 3 |

Each entry follows from the displayed five-flag construction and the three possible slopes. Thus every \(M_e\) has four two-edge-exchange neighbours, and the only possible intersections of distinct maxima are \(0,1,3\); in particular there are no one-edge exchanges. The four neighbours of \(M_e\) induce exactly two disjoint edges. By flag transitivity every exchange edge lies in exactly one triangle, and every exchange vertex lies in exactly two triangles. Hence there are \(27\cdot2/3=18\) triangles.

**Recovering the original graph from triangles.** Label a noncollinear triple of points, one in each vertical column, by \(a=(a_0,a_1,a_2)\) and the points \((i,a_i)\) for \(i=0,1,2\). Noncollinearity is exactly \(a_0+a_1+a_2\ne0\) in \(\mathbb F_3\); there are \(18\) such triples. For each \(i\), let \(e_i\) be the flag at \((i,a_i)\) whose line is parallel to the side joining the other two points. The three maxima \(M_{e_0},M_{e_1},M_{e_2}\) form a triangle in the exchange graph, as can be checked for \(a=(0,1,1)\) using the table. Every other noncollinear triple is its image under a shear, translation and nonzero scaling of the \(y\)-coordinate, so these are exactly the \(18\) triangles.

Let \(H\) be the graph whose vertices are these triangles, adjacent when they share a maximum matching. The two colour classes consist of the \(9\) triples with sum \(2\), and the \(9\) triples with sum \(1\). An edge from a sum-\(2\) triple \(a\) to a sum-\(1\) triple \(b\) exists exactly when \(b\) is obtained by adding \(1\) to two coordinates of \(a\) and leaving the third fixed. This follows because a shared flag must have the same point and the same slope parallel to the opposite side. Using the first two coordinates to label each colour class by \((r,s)\in\mathbb F_3^2\), the neighbour set of a sum-\(1\) vertex \((r,s)\) is exactly

\[
\{(r,s-1),(r-1,s),(r-1,s-1)\}.
\]

The nine sum-\(1\) vertices split into three parallel classes according to \(r-s\). Lines in the same class have disjoint three-point neighbourhoods; lines in different classes have exactly one common neighbour. Indeed the six nonzero differences of the three offsets \((0,1),(1,0),(1,1)\) are precisely the six vectors other than \((1,1)\) and \((2,2)\). Thus \(H\) is a three-net of order \(3\). Every three-net of order \(3\) is the unique Latin-square configuration of order \(3\), hence is the affine plane of order \(3\) with one parallel class removed. Therefore \(H\cong P\). Each maximum matching lies in exactly two triangles, and these two triangles share an edge of \(H\); every edge of \(H\) arises this way. Two maximum matchings are adjacent precisely when their corresponding edges of \(H\) share a triangle vertex. Consequently \(\mathcal E_2(P)\cong L(H)\cong L(P)\).

**Distance assertion.** In the explicit \(27\)-edge model of \(H\) above, breadth-first enumeration from each of its \(27\) edges, taking adjacency to mean a shared endpoint, produces the same distance profile \((1,4,8,12,2)\). Both independent scripts provide executable, exhaustive breadth-first checks, including the overlap/distance joint distribution. The upper distance bound and its \(27\) exact exceptions follow by comparison with the elementary lower bound \(\lceil(5-|M\cap N|)/2\rceil\).

## Verification
Run `python affine_certificate.py` and `python lcf_certificate.py` with Python 3; they use only the standard library. The first enumerates all \(\binom{27}{5}=80{,}730\) five-flag subsets in the affine incidence model, independently recovers the underlying graph from its \(18\) exchange triangles, and computes every shortest path. The second constructs the Pappus graph from the distinct Hamiltonian LCF specification `[5,7,-7,7,-7,-5]^3`, enumerates all *maximal* independent cliques in the edge-compatibility graph by pivoted backtracking, independently finds exactly \(27\) maxima of size \(5\), and computes the complete distance distribution. It separately verifies the triangle-graph isomorphism. Both programs assert all numerical conclusions rather than merely printing them. The full optimum bound and geometric classification have the elementary proof above; the finite scripts independently verify their instance.

## Relationship to prior work
The classical Pappus graph's affine-plane realization and distance-regular description are standard (A. E. Brouwer, *Pappus graph*). Nguyen (arXiv:1407.7604, July 29, 2014) and Joos (arXiv:1407.8336, July 31, 2014) study general sharp lower bounds on induced matching sizes in bounded-degree graphs, not this Pappus-specific optimum classification or its two-replacement line-graph self-recovery. Work on the ordinary matching complex of the Pappus graph concerns a different object: ordinary matchings need not be induced, and its homology does not determine this reconfiguration graph. Earlier numerical graph-reconfiguration results for other configurations likewise do not imply the present self-line-graph theorem. Exact equivalence under older strong-matching or configuration terminology remains a historical-priority risk.

## Limitations
The theorem is for the specific order-three affine net and does not assert an analogous result for larger nets. The distance calculations are exhaustive for the finite graph and are not proposed as an infinite-family formula. Although relevant accessible full texts and indexed records were checked, an equivalent unindexed or inaccessible historical classification is possible. The result has not undergone independent scholarly audit.

## References
- A. E. Brouwer, *Pappus graph*, https://aeb.win.tue.nl/graphs/Pappus.html (graph realization, intersection array and spectrum).
- V. H. Nguyen, *Induced matchings in graphs of degree at most 4*, arXiv:1407.7604, first posted July 29, 2014, https://arxiv.org/abs/1407.7604.
- F. Joos, *Induced Matchings in Graphs of Maximum Degree 4*, arXiv:1407.8336, first posted July 31, 2014, https://arxiv.org/abs/1407.8336.
- K. K. Dabrowski, M. Demange and V. V. Lozin, *New results on maximum induced matchings in bipartite graphs and beyond*, Theoretical Computer Science 478 (2013), 33–40, DOI:10.1016/j.tcs.2013.01.027 (abstract accessible; full article not verified in this review).
