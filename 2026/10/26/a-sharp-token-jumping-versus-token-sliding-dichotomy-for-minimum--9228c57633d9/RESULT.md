# A sharp token-jumping versus token-sliding dichotomy for minimum zero forcing in the Möbius–Kantor graph

## Finding

Let \(G\) be the Möbius–Kantor graph \(GP(8,3)\). For ordinary zero forcing, \(Z(G)=6\), and \(G\) has exactly \(1704\) minimum zero forcing sets. Let \(J(G)\) be the graph whose vertices are minimum zero forcing sets, with two sets adjacent when one selected vertex is replaced by an arbitrary unselected vertex. Let \(T(G)\) impose the additional condition that the departing and arriving vertices be adjacent in \(G\). Then \(J(G)\) is connected, has \(16560\) edges, and has both radius and diameter exactly \(6\). Every vertex of \(J(G)\) has eccentricity \(6\). By contrast, \(T(G)\) has no edges: its \(1704\) vertices are all isolated. Therefore any two optimal forcing configurations require at most six unrestricted single-vertex replacements, with six sometimes necessary, whereas no nontrivial replacement of a single vertex along an edge preserves optimality.

## Assumptions and scope

All graphs are finite, simple, undirected. Label the sixteen vertices \(u_i=i\) and \(v_i=8+i\), where \(i\in\{0,\ldots,7\}\). Edges are precisely \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), with subscripts modulo eight. An initially blue set \(B\) *forces* all of \(G\) if repeated application of the rule “a blue vertex with exactly one white neighbor makes that neighbor blue” eventually makes all vertices blue. The minimum cardinality of such a set is \(Z(G)\). A token jump replaces \(a\in B\) by any \(b\notin B\), requiring the resulting set also to be minimum zero forcing; a token slide additionally requires \(ab\in E(G)\). Both reconfiguration graphs are simple undirected graphs on actual labeled six-subsets (not symmetry-orbit quotients).

## Proof

The finite theorem follows by exhaustive enumeration with finite search bounds and independent implementations. For a subset \(B\) represented by a sixteen-bit mask, define a closure operator: at every round, for each presently blue vertex with precisely one white neighbor, add that neighbor to the next blue set, simultaneously; terminate when a round changes nothing. A seed forces precisely when the resulting mask has sixteen bits. This criterion is exact: every round consists of legal forces (simultaneous forces may be sequentially applied; a target already colored is harmless), and if the process halts short of all vertices then there is no legal force left. Also, arbitrary sequential legal-force scheduling yields the same terminal closure. This is the usual confluence of ordinary zero forcing.

The finite loop in `check_gp.py` tests every \(\binom{16}{k}\) subset, for all integers \(0\le k\le6\), using this exact mask criterion. It finds no forcing set for any \(k<6\), and precisely \(1704\) for \(k=6\). Thus both the lower bound and attainability are exhaustive rather than inferred from sampling.

For each pair of these \(1704\) six-subsets, token jumping is permitted exactly when their symmetric difference consists of two vertices. This is tested via every ordered removal–addition pair, with lookup in the verified list; token sliding additionally checks adjacency of those two vertices in the displayed \(GP(8,3)\) edge set. The exhaustive construction finds exactly \(16560\) unordered jumping edges and no sliding edges. The entire jumping degree distribution is \(16:240,17:96,18:336,19:192,20:288,21:192,22:240,24:120\), whose degree sum is \(33120\), independently confirming the stated edge count.

A breadth-first search from **every** one of the \(1704\) minimum sets reaches all \(1704\) vertices, and every such BFS has maximum distance precisely \(6\). BFS computes graph distances exactly by induction on path length. Hence the jumping graph is connected, has radius and diameter six, and every configuration has eccentricity six. For an explicit sharpness witness, the six-set \(\{0,1,2,3,4,5\}\) is at distance six from \(\{6,7,8,9,10,13\}\). The following is an actual six-step path of valid minimum sets:

\[
\begin{aligned}
&\{0,1,2,3,4,5\}\\
&\to\{1,2,3,4,5,6\}\\
&\to\{2,3,4,5,6,7\}\\
&\to\{3,4,5,6,7,9\}\\
&\to\{4,5,6,7,8,9\}\\
&\to\{5,6,7,8,9,13\}\\
&\to\{6,7,8,9,10,13\}.
\end{aligned}
\]

`check_lcf.py` implements a genuinely different graph encoding: a Hamiltonian sixteen-cycle and alternating chords of lengths \(\pm5\), namely LCF notation `[5,-5]^8`. It checks an explicit isomorphism with the preceding graph; enumerates forcing sets using sequential one-force-at-a-time updates; builds token-jump edges by buckets of five-element intersections; and independently computes shortest paths from every configuration. Its results agree on all stated invariants, including the complete absence of token slides.

## Verification

With Python 3 standard library only, execute `python3 check_gp.py` and `python3 check_lcf.py`. Compare the printed JSON to the included files `gp_output.json` and `lcf_output.json`. Both programs contain assertions for exhaustive counts, graph representation, exchange adjacency and diameter. The principal program also asserts the six-step explicit witness. Runtime and memory requirements are modest for enumeration on sixteen vertices; no external downloads or packages are needed. A complete finite enumeration is a proof only for the specifically defined sixteen-vertex graph, and the result makes no infinite-family extrapolation.

## Relationship to prior work

The AIM Minimum Rank–Special Graphs Work Group introduced ordinary zero forcing in *Zero forcing sets and the minimum rank of graphs* (first available online 26 November 2007); this supplies the definition and standard context, not the present sixteen-vertex classification. Geneson, Haas and Hogben introduce the minimum-zero-forcing-set reconfiguration graph with precisely the token-jumping edge relation studied here, and obtain general and family-specific results, but do not determine the Möbius–Kantor graph's enumerator or exchange geometry. Rashidi, Poursalavati and Tavakkoli treat generalized Petersen zero-forcing numbers; their exact statement for \(GP(n,3)\) assumes \(n\ge12\) and therefore does not cover \(GP(8,3)\). Positive-semidefinite and skew zero forcing use different force rules and cannot determine ordinary forcing configurations without an additional implication. Other analyses of the Möbius–Kantor graph's matching, independence or cut complexes do not compute these forcing-set and reconfiguration invariants. The Möbius *ladder* is a different graph from the Möbius–Kantor graph. The present result concerns the contrast of two legitimate local-move models, not just a zero-forcing number.

## Limitations

The theorem is specific to \(GP(8,3)\); it does not establish a general phenomenon for generalized Petersen graphs. The verification is exhaustive finite computation in two independently written programs, not an external independent scientific audit. An unindexed enumeration of the same forcing-set family or equivalent reconfiguration statement might exist; publication priority is not independently certified. The finite computations do not claim uniqueness of a forcing sequence or an algorithmic complexity bound for larger graphs.

## References

1. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra Appl. 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009. First online: 2007-11-26. Full text: https://draganstevanovic.wordpress.com/wp-content/uploads/2012/09/published-version2.pdf.
2. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (2020). Full text: https://arxiv.org/abs/2009.00220.
3. S. Rashidi, N. Shajareh Poursalavati and M. Tavakkoli, *Computing the zero forcing number for generalized Petersen graphs*, J. Algebra Comb. Discrete Appl. 7 (2020), 183–193. DOI: 10.13069/jacodesmath.729465. Full text: https://dergipark.org.tr/tr/download/article-file/1078628.
4. *Reconfiguration of Minimum PSD Forcing Sets and Minimum Skew Forcing Sets*, arXiv:2501.03642 (2025). Full text: https://arxiv.org/html/2501.03642v1.
5. NetworkX documentation, *moebius_kantor_graph*, graph representation and LCF form: https://networkx.org/documentation/stable/reference/generated/networkx.generators.small.moebius_kantor_graph.html.
