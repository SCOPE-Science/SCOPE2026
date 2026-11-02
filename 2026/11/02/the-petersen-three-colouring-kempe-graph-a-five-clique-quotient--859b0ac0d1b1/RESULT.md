# The Petersen three-colouring Kempe graph: a five-clique quotient and diameter four

## Finding
Let \(P=\operatorname{KG}(5,2)\), with vertices the ten unordered pairs of \(\{0,1,2,3,4\}\), adjacent when disjoint. Let \(\mathcal K_3(P)\) be the simple graph of all proper vertex colourings \(P\to\{0,1,2\}\), with an edge for a **single** Kempe change: exchanging two colour names on **one connected component** induced by those colours.

**Theorem.** Every colouring has a unique encoding \((c,t;A,B,C)\), where \(c\ne t\) are ground-set labels and \((A,B,C)\) is a permutation of the three named colours. The four pairs containing \(c\) receive \(A\); the three pairs \(\{t,u\}\), for \(u\notin\{c,t\}\), receive \(B\); and the three pairs entirely within \(\{0,1,2,3,4\}\setminus\{c,t\}\) receive \(C\). The complete Kempe-adjacency list for such a state is:

\[
\begin{aligned}
&(c,t;C,B,A),\\
&(c,u;A,C,B) \quad (u\notin\{c,t\}),\\
&(t,c;A,B,C),\quad(t,c;B,A,C).
\end{aligned}
\]

In particular, the graph has **120 vertices, 360 edges, and degree six everywhere**. Quotienting by permutations of the named colours yields the twenty-vertex graph on the ordered pairs \((c,t)\), \(c\ne t\), in which two pairs are adjacent exactly when they have the same first coordinate and different second coordinates, or are mutual reversals. Thus the quotient consists of five \(K_4\) cliques, one for each first coordinate, joined by one reversing edge between each pair of cliques; it has forty edges and diameter three.

The full named-colouring Kempe graph is connected and self-centered, with radius and diameter both four. **Every** colouring has precisely \(6,25,61,27\) other colourings at distances \(1,2,3,4\), respectively. The numbers of unordered distinct colouring pairs at these distances are \(360,1500,3660,1620\). The graph contains no triangles. In sharp contrast, if only proper one-vertex recolourings are permitted, the resulting graph is exactly a disjoint union of **sixty copies of \(K_2\)**.

## Assumptions and scope
All vertices and ground-set elements are individually labelled, the three colours are individually named, and each Kempe move switches exactly one maximal connected component of the subgraph induced by a chosen unordered colour pair. The colour-permutation quotient identifies all six renamings of an otherwise fixed colouring; it does not identify automorphisms of \(P\). Graphs are simple, and loops from null moves are excluded. The graph \(P\) is the ordinary Petersen graph in its two-subset model, and all asserted metrics refer to the fully named \(120\)-vertex graph unless explicitly called quotient metrics.

## Proof
**Encoding and completeness.** An independent vertex set of \(P\) is a pairwise intersecting family of two-subsets of a five-set. It has cardinality at most four, and any size-four such family is one of the five complete stars, consisting of all pairs through one ground-set symbol. To see this directly, start with two edges meeting at \(c\); an intersecting family containing an edge not incident with \(c\) can use at most three edges, since it must meet both those edges. Therefore a four-member intersecting family is a complete star.

Every three-colouring distributes ten vertices among classes of size at most four; consequently one class has size four. Two distinct complete stars intersect, so there cannot be two size-four classes. Let \(c\) be the centre of the unique four-star and \(A\) its colour. The remaining six vertices correspond to the edges of \(K_4\) on the other four symbols. The induced Petersen subgraph on those six vertices is \(3K_2\), consisting of the three pairs of disjoint edges of \(K_4\). Its proper two-colourings choose one edge from each of these three components for one colour. The resulting three-edge family is either a complete three-star centred at a unique \(t\), or a triangle; the complementary family is, respectively, a triangle or a three-star. Hence the other two named colour classes determine a unique second star centre \(t\) with colour \(B\), and a triangle with colour \(C\). Conversely every tuple described in the theorem is proper, so there are exactly \(5\cdot4\cdot3!=120\) states.

**All allowable Kempe moves.** Fix one encoded state and put \(R=\{0,1,2,3,4\}\setminus\{c,t\}\). For the two colours \(B,C\), the induced graph is three disjoint edges: \(\{t,u\}\) is joined solely to \(R\setminus\{u\}\), viewed as a two-subset. Interchanging the colours on any one of those edges changes the secondary centre to \(u\) and exchanges the roles of \(B,C\), giving exactly the three moves \((c,u;A,C,B)\). For the pair \(A,B\), the vertex \(\{c,t\}\) is isolated, while the other six vertices form a single six-cycle: vertices \(\{c,u\}\) and \(\{t,v\}\), with \(u,v\in R\), are adjacent exactly when \(u\ne v\). The two resulting moves give \((t,c;B,A,C)\) and \((t,c;A,B,C)\), respectively. Finally, the \(A,C\) induced graph is connected: \(\{c,t\}\) meets all three triangle vertices by Petersen adjacency, each of which connects to precisely one of the other three \(A\)-vertices. Swapping this one component gives \((c,t;C,B,A)\). This exhausts the three colour pairs and all their connected components, proves the six distinct neighbours, and establishes the displayed transition rule.

**Quotient and exact metric.** Forgetting the colour names leaves the uniquely determined ordered pair \((c,t)\). The transition rule gives exactly the quotient adjacency described above: three neighbours with the same first coordinate and one reversed pair. The five fixed-first-coordinate four-cliques and ten reversing edges give the asserted twenty vertices and forty edges. From a fixed oriented pair, the quotient distance shells have sizes \(1,4,6,9\), so its diameter is three.

For the fully named graph, calculate distances in the six-move rule from the representative \((0,1;0,1,2)\). For \(u,v\) distinct in \(\{2,3,4\}\), the exhaustive shortest-distance census is:

| First two labels | Distance 0 | Distance 1 | Distance 2 | Distance 3 | Distance 4 |
| --- | ---: | ---: | ---: | ---: | ---: |
| \((0,1)\) | 1 | 1 | 1 | 3 | 0 |
| \((0,u)\) | 0 | 3 | 9 | 6 | 0 |
| \((1,0)\) | 0 | 2 | 3 | 1 | 0 |
| \((1,u)\) | 0 | 0 | 6 | 12 | 0 |
| \((u,0)\) | 0 | 0 | 6 | 12 | 0 |
| \((u,1)\) | 0 | 0 | 0 | 15 | 3 |
| \((u,v)\) | 0 | 0 | 0 | 12 | 24 |
| **Total** | **1** | **6** | **25** | **61** | **27** |

Each row includes all six colour permutations for each ordered label pair of the indicated type, with \(u,v\) ranging independently over permitted distinct values. This table is obtained by breadth-first propagation of the six explicit transformations; both standalone included programs reproduce it, one computing the Kempe components from graph edges and one constructing the exact state transitions. The graph automorphisms induced by arbitrary permutations of the five ground labels and the three named colours act transitively on its \(120\) states. Therefore the distance census is the same from every state. The maximum distance of four gives both radius and diameter, and halving \(120\) times each nonzero shell size gives the unordered-pair distribution. Direct counting of common neighbours of adjacent states shows none, so the graph is triangle-free.

**Elementary recolouring contrast.** A Kempe component of size one occurs precisely at the isolated \(\{c,t\}\) vertex in the \(A,B\) two-colour subgraph. It gives exactly one legal one-vertex recolouring from each state, and reversing that recolouring returns to the original. Thus there are sixty disconnected edges, rather than a connected six-regular graph.

## Verification
Two included, standalone, Python-standard-library programs require no external data or dependencies. Run `python verify_direct.py` and `python verify_state_model.py` from the extracted package directory. The first enumerates every assignment of three named colours to the ten Petersen vertices, discards improper assignments, computes all two-colour connected components, builds the full Kempe graph, computes all-pairs shortest-path shells, checks the quotient cliques, and verifies sixty isolated single-recolouring pairs. The second constructs all \(120\) tuples directly, independently forms the six transition rules, checks that they agree with direct component switches, derives the oriented-pair quotient, and verifies the seven-row distance table and every state eccentricity. Both executed successfully on the embedded source files. The mathematical state classification and move derivation show why these finite exhaustive checks cover every case, rather than sampling states.

## Relationship to prior work
Peter Cameron's publicly dated April 12, 2012 discussion of the Petersen chromatic polynomial already records **120** proper named three-colourings and **20** colour-unlabelled partitions. Those previously known counts are not claimed here. A historical Petersen-graph reference by A. E. Brouwer likewise describes the twenty partitions by intersecting stars. Feghali, Johnson and Paulusma (arXiv:1503.03430, first posted March 11, 2015) prove that proper three-colourings of every connected cubic graph other than the tetrahedron and triangular prism are Kempe equivalent, which already implies connectivity here. Their result is not the exact move graph, its quotient, or its shortest-path metric. Work on paths between three-colourings under single-vertex moves treats a different adjacency relation. Subsequent general shortest-Kempe-reconfiguration work for paths and stars does not give the Petersen-specific graph structure.

The contributions established here, relative to these inspected sources, are the exact six-move labelled-state model, the five-clique quotient, the all-state distance distribution and self-centered diameter four, and the explicit contrast with the \(60K_2\) elementary-recolouring graph.

## Limitations
This is a complete result for one canonical finite graph, not a general theorem about all cubic graphs. The verification is exhaustive but was not independently audited by a separate researcher. The historical book literature and unindexed computations could contain equivalent descriptions; the accessible comparisons do not establish absolute first priority. The source results about chromatic counts and Kempe connectivity are explicitly acknowledged and are not novel claims.

## References
1. Peter J. Cameron, *Counting colourings of graphs*, April 12, 2012, https://cameroncounts.wordpress.com/2012/04/12/counting-colourings-of-graphs/ (chromatic polynomial and 120/20 colourings).
2. C. Feghali, M. Johnson, and D. Paulusma, *Kempe Equivalence of Colourings of Cubic Graphs*, arXiv:1503.03430 (first public preprint March 11, 2015), https://arxiv.org/abs/1503.03430 (general connectivity theorem).
3. A. E. Brouwer, *The Petersen graph*, https://aeb.win.tue.nl/graphs/Petersen.html (the Petersen two-subset representation and twenty colour partitions; page date not asserted).
4. L. Cereceda, J. van den Heuvel, and M. Johnson, *Finding Paths Between 3-Colorings*, Journal of Graph Theory 67 (2011), 69–82, https://doi.org/10.1002/jgt.20514 (single-vertex recolouring context).
5. M. Bonamy et al., *Shortest Reconfiguration of Colorings Under Kempe Changes*, STACS 2020, https://doi.org/10.4230/LIPIcs.STACS.2020.35 (general Kempe distance complexity context).
