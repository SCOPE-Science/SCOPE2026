# Complementary induced paths and optimal decycling exchanges in the icosahedral graph

## Finding
For the twelve-vertex icosahedral graph \(I\), the decycling number (minimum feedback vertex-set size) equals the previously known value \(6\). The exact family of minimum feedback vertex sets consists of **60** six-sets. Each minimum set \(S\) has the stronger property
\[
I[S]\cong P_6\cong I[V(I)\setminus S],
\]
so every optimum partitions the vertices into two complementary **induced** six-vertex paths, and every such complementary induced-path bipartition produces two minimum feedback vertex sets (one for each side).

The exchange graph \(\mathcal R(I)\) has these sixty minimum sets as vertices and joins \(S,T\) when \(|S\setminus T|=|T\setminus S|=1\). It is connected, four-regular and bipartite, with exactly \(120\) edges and
\[
\operatorname{radius}(\mathcal R(I))=\operatorname{diameter}(\mathcal R(I))=6.
\]
Every admissible single-vertex replacement moves between adjacent vertices of the original graph. Thus token jumping and token sliding give **exactly the same** optimum reconfiguration graph. Complementary minimum sets have graph distance six.

For all ordered optimum pairs \((S,T)\), the exact distribution by overlap size \(r=|S\cap T|\) and exchange distance \(d\) is:

| \(r\) | \(d\) | Ordered pairs |
|---:|---:|---:|
| 0 | 6 | 60 |
| 1 | 5 | 240 |
| 2 | 4 | 720 |
| 2 | 5 | 300 |
| 3 | 3 | 720 |
| 3 | 4 | 240 |
| 4 | 2 | 720 |
| 4 | 3 | 300 |
| 5 | 1 | 240 |
| 6 | 0 | 60 |

Every distance is either \(6-r\) or \(7-r\). Precisely \(840\) ordered pairs, equivalently \(420\) unordered pairs, require the one-exchange detour relative to the basic overlap lower bound. This is an exact finite theorem, not an asymptotic assertion.

## Assumptions and scope
All graphs are finite, simple, undirected. Give the icosahedral graph vertices \(\{N,S\}\cup\{U_i,L_i:i\in\mathbb Z/5\mathbb Z\}\). Its edges are precisely \(NU_i,SL_i,U_iU_{i+1},L_iL_{i+1},U_iL_i,U_iL_{i-1}\) for each \(i\in\mathbb Z/5\mathbb Z\). The letters \(N\) and \(S\) denote the opposite poles, not variables for feedback sets. The graph has 12 vertices, 30 edges and degree five at every vertex.

A feedback vertex set \(S_0\subseteq V(I)\) is any vertex subset for which \(I[V(I)\setminus S_0]\) is a forest. A minimum set has cardinality \(\nabla(I)\). A token jump replaces one selected vertex by one unselected vertex while retaining the minimum feedback vertex-set property; a token slide imposes adjacency of the exchanged vertices in \(I\). Exchange distance means shortest-path distance in the finite optimum reconfiguration graph.

## Proof
**Minimum-cardinality lower bound.** Since \(I\) is five-regular with twelve vertices and thirty edges, deleting a set \(S_0\) of size \(k\) leaves precisely \(30-5k+e_I(S_0)\) edges on \(12-k\) remaining vertices, where \(e_I(S_0)\) counts edges induced by \(S_0\). If the remainder is a nonempty forest, it has at most \(11-k\) edges. Thus \(19+e_I(S_0)\le4k\). Consequently \(k\ge5\). Equality \(k=5\) would require \(e_I(S_0)\le1\), and then five selected vertices contain an independent four-set. But the independence number of \(I\) is three: selecting either pole excludes its five adjacent ring vertices, leaving at most two choices from the other five-cycle; without poles, an independent four-set would need two vertices from each ring, and two nonconsecutive upper-ring vertices exclude four of the five lower-ring vertices. Hence \(k\ne5\), so \(\nabla(I)\ge6\).

**Existence.** In the ring labeling, the set \(\{N,U_0,U_2,L_0,L_2,L_3\}\) has six vertices and leaves an induced six-vertex path; this is also checked directly by the standalone verifier. Thus \(\nabla(I)=6\). The scalar equality is also Theorem 12 of Ma–Ma–Ren (2024) and is not the new contribution.

**Complete finite classification.** The two attached independently constructed checkers enumerate every possible six-subset of a twelve-vertex graph: \(\binom{12}{6}=924\) candidate masks. The ring-based checker additionally evaluates all \(2^{12}=4096\) vertex subsets, verifying no smaller feedback set. The second checker uses a different exact-coordinate graph construction and verifies all smaller subsets independently. Both find exactly sixty minimum sets. Each checks that *both* its selected and unselected six-vertex induced graphs are connected, have five edges and degree multiset \(\{1,1,2,2,2,2\}\), proving each is isomorphic to the simple path \(P_6\). These tests are exhaustive because all possible subsets of the relevant size are enumerated, not sampled.

**Exchange certificate and shortest paths.** For every ordered pair of the sixty minimum sets, the first verifier constructs all one-for-one replacements directly. The second constructs the same optimum-replacement relation using pairwise symmetric differences. They independently obtain sixty reconfiguration vertices, 120 undirected edges and degree four throughout. Each checks adjacency in \(I\) for every exchange, establishing equality of the token-jumping and token-sliding graphs, and verifies connectivity and bipartiteness. Complete breadth-first searches from **each** of the sixty configurations establish eccentricity six at every vertex and the displayed exact intersection-distance counts. The elementary overlap bound \(d(S,T)\ge6-|S\cap T|\) holds because one exchange can insert at most one target vertex, so the distance counts show exactly when the bound is sharp and when one extra step is necessary. Both independently verify the radius and diameter, and the ring checker explicitly verifies the complement-distance assertion for every optimum configuration.

## Verification
Run the following independent Python 3 standard-library programs from the directory containing these files:

```
python3 verify_icosahedron_rings.py
python3 verify_icosahedron_coordinates.py
```

The first program constructs the graph as two pentagonal rings and poles. The second constructs the vertices as cyclic permutations of \((0,\pm1,\pm\varphi)\), using the exact algebraic ring \(\mathbb Z[\varphi]\) and \(\varphi^2=\varphi+1\) to test squared distance four. Its coordinate system, induced-forest test, subset enumeration and exchange-graph construction are independent of the ring implementation. Both computations were executed directly from the embedded scripts; the output files reproduce the findings and report successful assertions. No graph-library dependency or random sampling is required.

## Relationship to prior work
Bau (2007) surveys the decycling/feedback vertex-set invariant, its general edge-count bounds and induced-forest duality, without an optimum-set enumeration on the icosahedron. Ma, Ma and Ren (2024), Theorem 12, explicitly prove \(\nabla(I)=6\) and exhibit one six-vertex deletion, but do not classify the sixty optimum configurations, their complementary induced paths or the reconfiguration graph. The analysis of sliding and jumping in Demaine et al. (2014) concerns independent sets (chiefly on trees), not minimum feedback vertex sets of the icosahedron. Related published mathematical-record results on the icosahedral neighborhood complex and Čech persistence concern different invariants and do not imply the exact exchange geometry. Historical unpublished enumerations might overlap; no independent priority certification is asserted.

## Limitations
The theorem is specific to the simple twelve-vertex icosahedral graph and does not extrapolate to all triangulations, Platonic solids, or general feedback vertex-set reconfiguration. The numerical classification uses complete finite computer enumeration from the supplied standalone source code; no completely noncomputational proof of the exchange distance table is claimed. The status is a self-review only; independent external audit or validation has not been performed. Identical or stronger facts may occur in unindexed literature.

## References
1. S. Bau, *The Decycling Number of Graphs*, arXiv:math/0703544v1, first public 2007-03-19, https://arxiv.org/pdf/math/0703544.
2. D. Ma, M. Ma and H. Ren, *The decycling number of a planar graph covered by \(K_4\)-subgraphs*, Discussiones Mathematicae Graph Theory 44 (2024), 459–473, doi:10.7151/dmgt.2455; Theorem 12 on the icosahedron, https://www.researchgate.net/publication/360513333_The_decycling_number_of_a_planar_graph_covered_by_K4-subgraphs.
3. E. D. Demaine et al., *Linear-Time Algorithm for Sliding Tokens on Trees*, arXiv:1406.6576, first public 2014-06-25, https://arxiv.org/pdf/1406.6576.
