# The six-edge bond threshold and a complete learning-dimension classification of theta graphs

## Finding

Let \(G=(V,E)\) be a finite connected simple undirected graph with at least one edge. Its **bond concept family** \(\mathcal B(G)\) consists of the characteristic subsets of \(E\) that are inclusion-minimal disconnecting edge sets. Queries ask whether an edge is in an unknown bond. Bonds are the cocircuits of the graphic matroid; their complements are its hyperplanes. Complementing every concept leaves both VC and Littlestone dimensions unchanged.

Write \(\Theta_{a,b,c}\) for three internally vertex-disjoint paths of positive lengths \(1\le a\le b\le c\) joining the same two endpoints. Assume \(b\ge2\), so the graph is simple. Then

\[
(\operatorname{VCdim}\mathcal B(\Theta_{a,b,c}),\operatorname{Ldim}\mathcal B(\Theta_{a,b,c}))=
\begin{cases}
(3,3),&a\ge2,\\
(2,2),&a=1,\ b=c=2,\\
(2,3),&a=1,\ b\ge2,\ c\ge3.
\end{cases}
\]

Every connected simple graph with at most five edges has equal VC and Littlestone dimensions for its bond family. Among connected simple graphs with **exactly six edges**, the house graph \(\Theta_{1,2,3}\) is, up to graph isomorphism, the **unique** graph with strictly different dimensions; there \(\operatorname{VCdim}=2\) and \(\operatorname{Ldim}=3\). Thus six edges is the sharp first edge threshold for a static–adaptive shattering separation of bond, equivalently graphic-matroid-hyperplane, concepts.

Moreover, all trees and unicyclic connected simple graphs have equal dimensions. For a tree with \(m\) edges the common value is zero if \(m=1\), and one if \(m\ge2\). For a unicyclic graph whose unique cycle has length \(c\ge3\) and with \(b\ge0\) bridges, it is one if \((c,b)=(3,0)\), and two otherwise.

## Assumptions and scope

All graphs are finite, simple, undirected and connected. A bond is an inclusion-minimal *edge* set whose removal disconnects the graph, not necessarily a minimum-cardinality cut and not a minimal *vertex* separator. A support \(S\subseteq E\) is VC-shattered when every binary labeling of the edges in \(S\) is realized by some bond. The Littlestone dimension is the greatest depth of a complete binary edge-query tree with a realizing bond at every leaf; depth zero is allowed. The concept space is the entire collection of bonds, and every edge is a potential query.

For a connected graph, an edge set \(F\) is a bond exactly when \(F=\delta(A)\) for a nonempty proper vertex subset \(A\) such that both induced subgraphs \(G[A]\) and \(G[V\setminus A]\) are connected. This standard bond characterization is independently checked in the supplied program by direct minimal-disconnection enumeration.

Let \(r(G)=|E|-|V|+1\) denote cyclomatic number. For a connected graph, \(r=0\) means a tree and \(r=1\) means unicyclic. We make no claim about all graphs of higher cyclomatic number beyond the sharp smallest-edge classification.

## Proof

**1. Bonds of a theta graph.** Let \(P_a,P_b,P_c\) be the three internally disjoint endpoint-to-endpoint paths, and partition the edges into three blocks \(A,B,C\) of respective sizes \(a,b,c\). Every bond is exactly one of the following forms:

\[
\{x,y,z\},\quad x\in A,\ y\in B,\ z\in C;
\qquad\text{or}\qquad
\{x,x'\}\subseteq A,\ B,\text{ or }C.
\]

To prove this, use the connected-bipartition characterization. If the two common endpoints are in different parts, each path changes parts exactly once: any additional change would isolate an internal run from its assigned endpoint, contradicting connectedness. Thus its cut crosses one edge in each of the three paths. Conversely each such triple separates the endpoints into connected sides. If the endpoints are in the same part, the other connected part must be a nonempty consecutive internal segment on precisely one path; it is separated by exactly two distinct edges of that path. Conversely every such pair isolates an internal segment and leaves the two endpoints connected by the other paths. These cases exhaust all connected bipartitions, and therefore all bonds. In particular,

\[
|\mathcal B(\Theta_{a,b,c})|=abc+\binom a2+\binom b2+\binom c2,
\]

and every bond has at most three edges.

**2. General online upper bound.** For any family of edge sets of cardinality at most \(k\), a complete all-positive branch of depth \(k+1\) is impossible: the queried edges on a complete shattered tree must be distinct along each path, and a concept realizing the all-positive path must contain all of them. Hence the family's Littlestone dimension is at most \(k\). Applied to theta bonds, \(\operatorname{Ldim}\le3\). As always, \(\operatorname{VCdim}\le\operatorname{Ldim}\).

**3. When every path has length at least two.** Fix one distinguished edge in each of the blocks \(A,B,C\). For any prescribed labeling of these three edges, choose the distinguished edge from a block labeled one and some other edge from a block labeled zero. The resulting transversal triple is a bond with exactly the prescribed trace. Thus three edges are VC-shattered and the two dimensions both equal three.

**4. When a direct edge joins the endpoints.** Suppose \(a=1\) and \(b,c\ge2\). Denote the unique edge of \(A\) by \(e\), and choose an edge \(f\) of \(B\). The pair \(\{e,f\}\) is shattered: label \(11\) by a transversal containing both, label \(10\) by a transversal containing \(e\) and another edge of \(B\), label \(01\) by a two-edge bond inside \(B\) containing \(f\), and label \(00\) by a two-edge bond inside \(C\). Thus the VC dimension is at least two. No three-edge support is shattered: to realize an all-one labeling of three selected edges it must itself be a transversal triple, which includes \(e\). But then a labeling selecting its \(B\)-edge and \(C\)-edge while rejecting \(e\) is unrealizable: an edge bond not containing \(e\) has both edges within one block. Hence the VC dimension is exactly two.

If \(b=c=2\), the bond count is \(4+1+1=6\), and the information bound \(\operatorname{Ldim}\le\lfloor\log_2 6\rfloor=2\) shows equality. Otherwise \(c\ge3\); choose two edges of \(B\), three edges of \(C\), and the unique edge of \(A\). These six queries support all ten bond patterns of \(\Theta_{1,2,3}\): six transversal triples, one internal pair on \(B\), and three internal pairs on \(C\). The explicit depth-three tree below uses only those ten patterns and therefore works unchanged for every larger pair of blocks. Consequently \(\operatorname{Ldim}\ge3\), matching the universal upper bound.

**5. Explicit house certificate.** Label the five vertices by \(0,1,2,3,4\) and the six edges as follows, in index order:

\[
(0,1),\quad(0,4),\quad(1,4),\quad(0,3),\quad(2,3),\quad(1,2).
\]

The ten bond masks, with bit \(i\) recording membership of edge \(i\), are

\[
6,11,13,19,21,24,35,37,40,48.
\]

The tree begins by querying edge \(0\). In the zero branch query edge \(3\); its zero child queries edge \(1\) (terminal masks \(48\) and \(6\)) and its one child queries edge \(4\) (terminal masks \(40\) and \(24\)). In the one branch of the root query edge \(1\); its zero child queries edge \(3\) (terminal masks \(21\) and \(13\)) and its one child also queries edge \(3\) (terminal masks \(19\) and \(11\)). In every pair of terminal masks the first is the zero child and the second is the one child. Direct bit inspection verifies all eight root-to-leaf paths. The exact machine-readable tree, including distinct witnesses at its leaves, is in `house_depth3_certificate.json`.

**6. Trees and unicyclic graphs.** In a tree every edge is a bridge, and the bonds are exactly its singleton edges. With at least two edges this class has both dimensions one (every positive branch contains one hypothesis); with one edge there is only one concept and both dimensions are zero. In a connected unicyclic graph, let its cycle have \(c\) edges and let \(b\) edges be bridges. Every bond is either a singleton bridge or any two distinct cycle edges. The claim follows from the unique cycle and minimal disconnection. If \(c=3,b=0\), the concept family has three members and VC dimension one, so Littlestone dimension is one. Otherwise a pair of cycle edges is shattered: two positive by that pair, either one positive by pairing it with another cycle edge, and neither positive by selecting two other cycle edges when \(c\ge4\), or by selecting a singleton bridge when \(b\ge1\). Finally, a positive branch on a cycle-edge query consists of pair bonds through that edge, which form a point-function family on the other cycle edges and have Littlestone dimension at most one; a positive branch on a bridge query has a single hypothesis. No complete depth-three tree exists, establishing equality at two.

**7. Sharp edge threshold and uniqueness.** Any connected graph with at most six edges and at least two independent cycles has at most five vertices, by \(|E|-|V|+1\ge2\). With at most five edges, the only simple connected multicycle graph is \(K_4\) with one edge deleted, which has six bonds and both dimensions two. With six edges, \(K_4\) itself has seven bonds and both dimensions two. The connected five-vertex six-edge graphs have exactly five isomorphism types: the two graphs obtained by attaching a leaf at either a degree-two or a degree-three vertex of \(K_4\) minus one edge; two triangles meeting in one vertex; \(\Theta_{2,2,2}\); and \(\Theta_{1,2,3}\). The first two have seven bonds each, and the bowtie has six; each has a shattered two-edge support and cannot have a depth-three tree by its hypothesis count. The theta cases were determined above. Trees and unicyclic graphs were determined in Step 6. Hence the unique strict-gap graph at the minimum six-edge threshold is \(\Theta_{1,2,3}\), as claimed.

The supplied checker also enumerates every connected labeled simple graph on at most five vertices with at most six edges. It enumerates all 595 such graphs, independently computes their bonds in two ways, evaluates both dimensions exactly, and finds 60 labeled strict-gap graphs, all in the single house-graph isomorphism class. This is a finite corroborating census, not the sole reason the universal theta and unicyclic statements hold.

## Verification

Run `python verify_bond_threshold.py house_depth3_certificate.json` with Python 3 and its standard library. The checker independently computes bonds via connected bipartitions and via inclusion-minimal edge deletions, verifies the explicit eight-leaf tree, computes the two dimensions using exhaustive traces and the exact Littlestone version-space recurrence, and compares direct graph bonds to the theta-block formula on nine parameter triples. It checks the sharp finite edge threshold by enumerating every labeled connected simple graph on two through five vertices with at most six edges, grouping the strict-gap graphs under all relabelings.

All finite assertions were run successfully on the actual files in this package. Finite enumeration does not prove the all-parameter theta theorem; Steps 1–4 provide its proof. The structural classification of minimal six-edge graph types in Step 7 supplies the finite completeness argument, independently corroborated by exhaustive computation.

## Relationship to prior work

Duarte and collaborators, *Computing the Largest Bond and the Maximum Connected Cut of a Graph* (first available preprint dated 2020-07-09, arXiv:2007.04513), provide the graph-theoretic bond characterization and study extrema and computational complexity of bond sizes; their inspected paper does not establish the VC or Littlestone dimensions of the complete bond concept family.

Guingona, Kolesnikov, Nierwinski and Soucy, *Littlestone and VC-dimension of families of zero sets* (first preprint dated 2021-09-10, arXiv:2109.04805), Theorem 3.10, establish equality of the dimensions for the class of **all** zero sets of nonzero linear combinations. In the binary graphic representation, that larger family includes complements of nonminimal cuts as well as matroid hyperplanes. Restricting the family to maximal proper zero sets is not covered by their equality theorem. Indeed, in the house example, the full binary zero-set class has dimensions \((3,3)\), whereas the hyperplane subfamily has dimensions \((2,3)\). This distinction is a substantive part of the claim, not a change of terminology.

The literature and database comparisons included the aliases *minimal edge cut*, *bond*, *graphic cocircuit*, *graphic-matroid hyperplane*, and *maximal proper zero set*, as well as statement-level checks for the theta product-of-paths formula and for stronger all-graphic-matroid learning theorems. No inspected source established the stated theta classification and sharp first edge threshold. Search and access coverage are not a proof of historical uniqueness; priority under a different formulation remains a residual risk.

## Limitations

The theorem concerns inclusion-minimal disconnecting edge sets, not all cuts, minimum-size cuts, oriented graph cuts, or vertex separators. It gives a complete all-length classification for theta graphs and for graphs with at most one cycle, plus the unique first strict-gap graph under the number-of-edges ordering. It does not classify learning dimensions on arbitrary graphs with two or more cycles or prove an unbounded gap. Independent external mathematical audit has not been performed, and historical priority cannot be certified by negative search results.

## References

1. G. L. Duarte, H. Eto, T. Hanaka, Y. Kobayashi, Y. Kobayashi, D. Lokshtanov, L. L. C. Pedrosa, R. C. S. Schouery, and U. S. Souza, *Computing the Largest Bond and the Maximum Connected Cut of a Graph*, arXiv:2007.04513 (first submitted 9 July 2020), https://arxiv.org/abs/2007.04513.
2. V. Guingona, A. Kolesnikov, J. Nierwinski, and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (first submitted 10 September 2021), https://arxiv.org/abs/2109.04805.
3. Self-contained finite checks: `verify_bond_threshold.py` and `house_depth3_certificate.json`, embedded in the same package.
