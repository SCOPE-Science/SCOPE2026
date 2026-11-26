# End-local rigidity and a sharp exchange-disconnection threshold for three-row grids

## Finding

Let \(G_n=P_n\square P_3\), with vertices \((c,r)\), where \(0\le c<n\), \(0\le r<3\), and adjacency by unit change of one coordinate. A set \(B\) is *zero forcing* if, starting with exactly \(B\) blue, repeated application of the rule “a blue vertex with exactly one white neighbor makes that neighbor blue” eventually blues every vertex. Let \(\mathcal Z(G_n)\) be the *minimum-zero-forcing-set exchange graph*: its vertices are the minimum zero forcing sets and two are adjacent exactly when their symmetric difference has size two.

**Theorem.** For every \(n\ge5\), \(Z(G_n)=3\), and the 26 minimum zero forcing sets are exactly 13 explicitly listed end-local triples \(\mathcal L\) and their reflections across the middle of the grid. Every set in \(\mathcal L\) is supported in the first three columns; every reflected set is supported in the last three columns. Moreover,
\[
  \mathcal Z(G_n)\cong F\sqcup F,
  \qquad |V(F)|=13,\quad |E(F)|=24,\quad
  \operatorname{rad}(F)=3,\quad\operatorname{diam}(F)=5.
\]
The 13-vertex graph \(F\) is defined explicitly below by an edge list, independent of \(n\). The exchange graph is therefore disconnected for every \(n\ge5\). The change is sharp: for \(n=4\), it has 26 vertices, 56 edges, is connected, has radius four and diameter six; for \(n=3\), it has 20 vertices, 44 edges, is connected, has radius three and diameter four.

## Assumptions and scope

All graphs are finite, simple and undirected. Both dimensions of the Cartesian grid are paths, not cycles. The statements concern ordinary zero forcing (neither positive-semidefinite nor skew forcing) and **token jumping between minimum sets**, not adding extra initially blue vertices. The principal structural theorem covers every integer \(n\ge5\); the two smaller boundary cases are exact finite calculations. No claim is made for a fourth or larger row width.

For compact coordinates write \(cr\) for vertex \((c,r)\) **only in the following displayed, explicitly defined table**; thus \(00,01,02\) are the three vertices of the leftmost column. The following numbered triples constitute \(\mathcal L\):

| Index | Initial blue vertices | Rounds to blue all of columns 0, 1, 2 |
| ---: | :--- | ---: |
| 0 | 00, 01, 02 | 2 |
| 1 | 00, 01, 11 | 3 |
| 2 | 00, 01, 20 | 5 |
| 3 | 00, 02, 10 | 3 |
| 4 | 00, 02, 12 | 3 |
| 5 | 00, 10, 11 | 4 |
| 6 | 00, 10, 20 | 4 |
| 7 | 01, 02, 11 | 3 |
| 8 | 01, 02, 22 | 5 |
| 9 | 02, 11, 12 | 4 |
| 10 | 02, 12, 22 | 4 |
| 11 | 10, 11, 20 | 5 |
| 12 | 11, 12, 22 | 5 |

Let \(F\) have vertex set \(\{0,\dots,12\}\). Its 24 unordered edges, in lexicographic order, are
\[
\begin{gathered}
(0,1),(0,2),(0,3),(0,4),(0,7),(0,8),(1,2),(1,5),\\
(1,7),(2,6),(3,4),(3,5),(3,6),(4,9),(4,10),(5,6),\\
(5,11),(6,11),(7,8),(7,9),(8,10),(9,10),(9,12),(10,12).
\end{gathered}
\]
Each parenthesized pair is an undirected edge joining the two numbered configurations.

## Proof

**1. Optimum cardinality.** The first column is a zero forcing set of three vertices: each blue column forces the entire next column in parallel. Conversely, suppose that at most two vertices are initially blue. A first force cannot be made by a vertex of degree three or four: that would require the forcing vertex and at least two additional blue neighbors. A first force must therefore come from a corner of degree two together with one of its neighbors. With exactly those two initial vertices, the first force produces a blue set of three vertices supported in the first two columns or their right-hand reflection, and every blue vertex then has zero or at least two white neighbors. For \(n\ge3\), the process is frozen before the graph is blue. Thus \(Z(G_n)=3\).

**2. End-locality.** Take a three-element zero forcing set \(B\) for \(n\ge5\). Every first force is made either by a blue corner with one blue neighbor, or by a blue degree-three vertex with two blue neighbors. Degree-four vertices cannot force initially.

If a first force comes from a degree-three vertex, all three elements of \(B\) are the source and two of its neighbors. A degree-three vertex is either the middle vertex of an end column or one of the upper/lower vertices of a non-end column. The end-column case places \(B\) in its first two columns. In the upper/lower case, at column \(c\), if \(2\le c\le n-3\), direct inspection of the three possible pairs of initially blue neighbors shows that the first force is the **only** force: either a horizontal triple forces its middle-row vertex, or a horizontal/vertical corner-shaped triple forces the remaining horizontal neighbor, and all blue vertices thereafter have zero or at least two white neighbors. Hence a *successful* three-blue configuration admitting a degree-three initial force must be supported in columns \(0,1,2\) or \(n-3,n-2,n-1\).

It remains to consider first forces from a corner. If \(B\) includes a left corner and one of its neighbors, those two alone produce at most one new blue vertex before freezing. When the remaining element of \(B\) lies outside columns \(0,1,2\), it is not adjacent to the resulting left-end blue three-set, and cannot itself force: it has at least two white neighbors (for \(n\ge5\)). Thus that configuration fails. The same holds at the right end. If a corner is blue without a blue neighbor, it cannot be the initial source; a possible initial degree-three source has already been covered, and any initial source at the opposite corner is covered by the same two-seed argument. Therefore **every** three-element zero forcing set lies entirely in one of the two three-column end regions.

**3. The finite boundary test is sufficient for every width.** For each of the \(\binom{9}{3}=84\) initial triples in columns \(0,1,2\), test the color-change rule in \(G_5\) by simultaneous rounds. Stop at the first of the following: the first three columns are full; there are no legal targets; a force into column \(4\) is possible before the first three columns are full. The last outcome does not occur: `verify_local_boundary.py` enumerates all 84 triples, checks that the 13 listed triples fill columns \(0,1,2\) in the displayed numbers of rounds while column \(3\) is still entirely white, and checks that the other 71 stall with no blue vertex past column \(3\). Simultaneous rounds are valid because each still-white target of a round is still the unique white neighbor of its source after any of the round's other targets have turned blue.

All blue sources of the histories used in this test are in columns \(0,1,2,3\); their neighbor sets in \(G_n\) and \(G_5\) are identical for every \(n\ge5\). In each of the 71 stalled cases the final blue set is therefore closed in \(G_n\) as well. No forcing order from the seed can escape that set: a first force to a vertex outside the set would also be legal with the entire closed set blue. In each of the 13 successful cases the finite history works unchanged and each fully blue column then forces the next one. Reflection gives precisely the right-end family. The two families are disjoint: for \(n=5\) they share only a supporting column and each triple contains at most one vertex there; for \(n\ge6\) the supports are disjoint.

**4. Exchange graph and sharp cutoff.** Two triples are adjacent precisely when they have two vertices in common. Apply this rule to the numbered 13 triples to obtain the displayed 24 edges of \(F\). Between left and right families there are no edges: for \(n\ge6\) their supporting columns are disjoint, while at \(n=5\) they can share at most one vertex in the middle column. Direct breadth-first search on the explicit 13-vertex edge list gives connectivity, radius three and diameter five. Hence \(\mathcal Z(G_n)=F\sqcup F\). The exceptional small widths \(n=3,4\) are exhaustively checked by both independent methods in the verification package; those statements require no extrapolation.

## Verification

`verify_local_boundary.py` checks the 84 local outcomes needed in Step 3, including that every rejected triple stalls before column \(4\) is touched. `verify_structural.py` constructs the graphs by Cartesian-coordinate adjacency, enumerates the same 84 possible left-end triples on five columns, checks their complete zero-forcing closures, and checks the column-three-free histories and the 24-edge exchange graph. It also exhaustively tests every initial triple on widths 3 through 12, recording base counts and graph radii/diameters. `verify_masks.py` uses separate row-major integer bitmasks and checks all one- and two-element sets, all triples, all exchanges, components and diameters for widths 3 through 10. Each program runs as `python3 filename.py` with only the Python standard library, and each terminates with `VERIFY_OK` if every assertion holds. All infinite-width conclusions additionally use the preceding proof; testing finitely many widths alone would not establish them.

## Relationship to prior work

The Cartesian-grid minimum size was established earlier. Chilakamarri, Dean, Kang and Yi [1, §3] discuss rectangular grids and credit the AIM Minimum Rank–Special Graphs Work Group [4] for \(Z(P_s\square P_t)=\min(s,t)\) when \(s,t\ge2\). That formula gives the optimum cardinality three here, not the 26-set classification. Geneson, Haas and Hogben [2, §3] study minimum-zero-forcing-set exchange graphs and give disconnected examples, including one obtained by adding leaves to \(K_r\square P_3\). The present result gives the exact exchange-component cutoff for the unadorned three-row rectangular grid.

## Limitations

The exchange rule does not allow temporary extra blue vertices. The component is characterized as an explicit thirteen-vertex graph, not by a new abstract graph-isomorphism name. The computations independently verify small instances and the local table; no infinite proof is inferred solely from numerical experiments. Independent external scientific validation has not been performed.

## References

1. K. B. Chilakamarri, N. Dean, C. X. Kang and E. Yi, *Iteration Index of a Zero Forcing Set in a Graph*, arXiv:1105.1492 (first posted 2011-05-08). https://arxiv.org/abs/1105.1492
2. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (first posted 2020-09-01). https://arxiv.org/abs/2009.00220
3. L. Hogben, M. Huynh, N. Kingsley, S. Meyer, S. Walker and M. Young, *Propagation time for zero forcing on a graph*, arXiv:1410.4191 (first posted 2014-10-15). https://arxiv.org/abs/1410.4191
4. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648.
