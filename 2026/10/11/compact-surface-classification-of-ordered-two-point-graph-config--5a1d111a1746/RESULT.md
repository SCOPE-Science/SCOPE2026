# Compact-surface classification of ordered two-point graph configuration complexes

## Finding
Let \(G\) be a finite connected simple graph on at least three vertices. The ordered two-point Abrams cubical complex \(D^{\mathrm{ord}}_2(G)\) is a compact topological surface, with boundary permitted, **if and only if** one of the following holds:

1. \(G=C_n\) for any \(n\ge5\).
2. \(G=K_5\setminus M_r\), where \(M_r\) is a matching of \(r\in\{0,1,2\}\) edges.
3. \(G=C_6+S\), where \(S\) is a nonempty subset of the three opposite chords in a hexagon. Up to isomorphism the three cases are \(|S|=1,2,3\).

All the resulting surfaces are connected and orientable. Their genus \(g\) and number \(b\) of boundary circles are, respectively:

| Graph | Genus \(g\) | Boundary circles \(b\) |
| --- | ---: | ---: |
| \(C_n\), \(n\ge5\) | 0 | 2 |
| \(K_5\setminus M_0\) | 6 | 0 |
| \(K_5\setminus M_1\) | 4 | 4 |
| \(K_5\setminus M_2\) | 4 | 2 |
| \(C_6\) plus 1 opposite chord | 2 | 2 |
| \(C_6\) plus 2 opposite chords | 2 | 4 |
| \(C_6\) plus 3 opposite chords | 4 | 0 |

The two closed exceptional surfaces arise from \(K_5\) and \(K_{3,3}\). The other noncyclic examples supply additional boundary surfaces, and no other connected simple graphs give surfaces of this cubical type.

## Assumptions and scope
Regard each edge and vertex of \(G\) as a closed cell. The cubical complex \(D^{\mathrm{ord}}_2(G)\) has one cell \(\sigma\times\tau\) for each **ordered** pair of open graph cells whose closures are disjoint. Two-dimensional cells are squares indexed by ordered disjoint edge pairs; one-dimensional cells arise from an edge disjoint from a vertex. Its vertices are all ordered distinct vertex pairs \((u,v)\). A topological surface here means a compact 2-dimensional manifold in which boundary points have half-disc neighborhoods. Every 0-cell therefore must have a link homeomorphic to a circle or closed interval. We do not identify the complex with its unordered quotient.

## Proof
**Exact vertex links.** At an ordered vertex \((u,v)\) with \(u\ne v\), the link has tagged left vertices \(N(u)\setminus\{v\}\), tagged right vertices \(N(v)\setminus\{u\}\), and a link edge between left \(x\) and right \(y\) exactly when \(x\ne y\). Consequently, the link is a complete bipartite graph with the matching edges corresponding to common neighbors deleted. The cubical complex is a 2-manifold with boundary precisely when every such link is one connected path containing an edge or one cycle. This is the standard vertex-link criterion for regular square complexes; interiors of edges and squares then also have the required neighborhoods.

**Uniform bound on the graph order.** Every graph vertex has degree at least two: if \(u\) is a leaf with neighbor \(v\), the link at \((u,v)\) has an empty side. If a vertex \(w\) has degree at least five, choose one of its neighbors \(v\); because \(v\) has degree at least two, the link at \((w,v)\) contains a right vertex with at least \(\deg(w)-2\ge3\) neighbors, contradicting the path-or-cycle criterion. If \(w\) has degree four and has any nonneighbor \(v\), then the link at \((w,v)\) again has a right vertex of degree at least three. Thus a degree-four vertex must be universal, forcing exactly five vertices. Therefore **if \(G\) has at least six vertices, all degrees are two or three**.

Suppose there are at least seven vertices and some degree-three vertex \(w\). Put \(U=N(w)\), so \(|U|=3\), and \(B=V(G)\setminus U\). For any \(v\in B\setminus\{w\}\), the link at \((w,v)\) forces \(N(v)\subseteq U\): a neighbor outside \(U\) would have degree three in that link. Also \(N(w)=U\), hence \(B\) is independent. Each vertex in \(B\) has degree at least two, whereas each of the three vertices of \(U\) has degree at most three. Counting the cross-edges gives \(2(|V(G)|-3)\le9\); thus \(|V(G)|\le7\).

In the only remaining case \(|V(G)|=7\), there are four vertices in \(B\) and eight or nine cross-edges. If there are eight, all four vertices of \(B\) have two-element neighborhoods in the three-element set \(U\). Two therefore have the same neighborhood, and their mutual ordered-pair link is \(K_{2,2}\) minus two disjoint edges, hence disconnected. If there are nine, exactly one vertex of \(B\) has degree three and the other three have degree two. Their two-element neighborhoods must be the three distinct two-element subsets of \(U\), otherwise the same disconnected-link obstruction applies. This uses all three possible edges at each vertex of \(U\), so \(U\) is independent and any two different vertices of \(U\) share exactly two of their three neighbors. Their mutual link is \(K_{3,3}\) minus two disjoint edges; it contains vertices of degree three and is not a path or cycle. Both cases contradict the manifold condition. Hence every valid graph with at least seven vertices has degree two everywhere, and so is a cycle.

**Exact finite remainder.** For graph orders \(3\) through \(6\), the standalone script `verify.py` enumerates **all** labeled simple graphs, checks connectedness and the exact vertex-link criterion for every ordered distinct vertex pair, and independently compares the accepted masks with the full isomorphism orbits of the claimed graphs. It checks all \(8,64,1024,32768\) labeled graphs of these orders, respectively. It finds \(0,0,38,340\) valid labeled graphs; the full accepted-mask sets equal the asserted graph families, with no additional cases. Thus the finite remainder is exhaustive, not sampled.

**Surface types.** The same standalone checker constructs every vertex, edge, square and incidence of the resulting cubical surface. It verifies square-orientation compatibility across every internal edge, the connectedness of the 1-skeleton, and that boundary edges form disjoint simple cycles. The exact Euler characteristic \(\chi\) and boundary-circle count \(b\) then give \(g=(2-b-\chi)/2\). The resulting counts are displayed in the finding table. For any cycle \(C_n\) with \(n\ge5\), an ordered collision-free pair is characterized by the cyclic order of the two particles; the two complementary directed arc lengths define a circular coordinate and an interval coordinate, giving an annulus. Equivalently, the square complex is an orientable cyclic strip with exactly two boundary circuits and Euler characteristic zero. This establishes the cyclic row for all \(n\ge5\), beyond the finite computer checks. Together these steps establish the full theorem.

## Verification
Run `python3 verify.py` from the directory containing the file. It has no nonstandard dependencies, downloads or external datasets. It exhaustively checks all simple labeled graphs through six vertices, reconstructs the asserted isomorphism classes, and reports `VERIFY_OK`. Its accepted-mask SHA-256 fingerprints are `3d3c4dddbac9be13f7632d6aa36fe9286647e131885b479037a1fd5c19aad221` at five vertices and `45e5e4777df59c275914b0ed2fd07b67b83165cf3d41c72c7c9e005827b2c411` at six vertices. It also reconstructs the cells and boundary cycles for every exceptional type and for cycles of lengths five, seven and eight. Exhaustive finite checks are used only for the orders that remain after the analytic bound, not to infer the all-orders conclusion from experiments.

## Relationship to prior work
Murray and Wilcher's 2026 study *Locally Euclidean Discretized Graph Configuration Spaces* gives a classification for **closed** manifolds in Abrams' discretized graph-configuration setting. The present theorem is about surfaces **with boundary allowed**, and adds the boundary-circle and genus types along with an exclusion argument for all possible graph orders. The abstract and thesis description expressly exclude boundary from their classification; nevertheless, their full proof and appendices were not obtainable in this check, so possible incidental overlap is a residual originality risk.

Abrams and Ghrist studied discretized graph braids and the closed examples arising from \(K_5\) and \(K_{3,3}\). Maciążek and Sawicki explain the Abrams cubical model in their graph-configuration-space work. These provide definitions and precedents, not a demonstrated classification of all ordered two-point **boundary** surfaces, their graph types and their genera.

## Limitations
This is a statement about the unsubdivided **ordered Abrams cubical complex** for finite connected simple graphs, not about arbitrary continuous configuration spaces on nonsufficiently-subdivided graphs, unordered particle quotients, graphs with loops or multiple edges, disconnected graphs, or configurations of three or more particles. The finite-checker proof covers exactly graphs of orders three through six; larger orders are settled by the symbolic graph-degree argument. Full text of the directly relevant Murray--Wilcher preprint was unavailable, leaving a specific residual overlap risk despite its explicit closed-manifold scope. The May 2026 master's-thesis record carries only an issue month; its precise date of first public exposure was not verified. The dated source used for the eligibility of this research direction is the 2026-07-09 arXiv posting.

## References
1. Justin Murray and Zach Wilcher, *Locally Euclidean Discretized Graph Configuration Spaces*, arXiv:2607.08810 (first arXiv posting July 9, 2026). https://arxiv.org/abs/2607.08810
2. Zach Wilcher, *Locally Euclidean discretized graph configuration spaces*, master's thesis, Ball State University, issue date May 2026. https://hdl.handle.net/20.500.14291/204667
3. Aaron Abrams and Robert Ghrist, *Finding topology in a factory: configuration spaces*, arXiv:math/0009118 (2000). https://arxiv.org/abs/math/0009118
4. Tomasz Maciążek and Adam Sawicki, *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics 371 (2019), Abrams discrete-model exposition. https://doi.org/10.1007/s00220-019-03583-5
