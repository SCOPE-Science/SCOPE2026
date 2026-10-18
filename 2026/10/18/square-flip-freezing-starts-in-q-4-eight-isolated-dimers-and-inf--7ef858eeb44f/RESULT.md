# Square-flip freezing starts in \(Q_4\)

## Finding
Let \(Q_d\) be the graph on \(\{0,1\}^d\) with edges between words of Hamming distance one. Let \(\mathcal F_d\) be the graph whose vertices are *unordered perfect matchings* of \(Q_d\), with an edge precisely when two matching edge sets differ by exchanging the two opposite matched edges of a coordinate four-cycle (a **square flip**). Vertices of \(Q_d\) are labeled, and no quotient by geometric symmetry is taken.

The square-flip graph \(\mathcal F_2\) is \(K_2\), and \(\mathcal F_3\) is connected with nine vertices and twelve edges. The next dimension exhibits a sharp change:
\[
|V(\mathcal F_4)|=272,\qquad |E(\mathcal F_4)|=768,\qquad
\mathcal F_4=G_{264}\sqcup8K_1.
\]
The graph \(G_{264}\) is connected with 264 vertices and 768 edges, radius seven, and diameter eight. Among its vertices, 252 have eccentricity seven and twelve have eccentricity eight. The eight isolated matchings form one orbit under the 384 coordinate-permutation and bit-translation automorphisms of \(Q_4\). The full degree distribution of \(\mathcal F_4\) is
\[
(0:8),\ (3:32),\ (4:12),\ (5:96),\ (6:48),\ (8:72),\ (12:4).
\]
Furthermore, for **every integer** \(d\ge4\), the number of perfect matchings of \(Q_d\) admitting no square flip is at least
\[
2^{2^{d-4}}.
\]
Thus four is the smallest dimension in which a hypercube perfect matching can be frozen under square flips. The infinite bound is constructive, not extrapolated from the four-dimensional census.

## Assumptions and scope
A perfect matching consists of disjoint unoriented graph edges covering all vertices exactly once. The 4-cycle of a flip must be induced by varying exactly two binary coordinates and fixing all other coordinates. In \(Q_d\), every graph 4-cycle has this form. Flips on cycles of length six or more and global automorphism moves are **not allowed**. A matching is *frozen* if it contains no two opposite edges of any coordinate square, i.e. if it is an isolated vertex of \(\mathcal F_d\). A labeled matching is counted once, independent of the order of its edges. For the quantitative finite classification the domain is exactly \(d=2,3,4\); for the lower bound the domain is all integers \(d\ge4\).

## Proof
**Exhaustive finite base and exact graph construction.** Encode a vertex \(v\in\{0,1\}^d\) as its integer binary word, with coordinate \(j\) flipped by XOR with \(2^j\). Two independent exhaustive generators recover all perfect matchings for \(d=2,3,4\). The first selects the least uncovered vertex and pairs it in turn with each uncovered neighbor; the uniquely specified partner in any matching proves coverage and absence of duplicates. The second assigns each even-parity vertex injectively to one adjacent odd-parity vertex, rejecting repeats; bipartiteness makes this equivalent to all perfect matchings with a different recursion. The generator sets agree exactly and give counts \(2,9,272\).

For each pair of coordinate directions, fixing all remaining coordinates gives exactly one square. Testing which opposite edge pair is in each matching generates every legal square flip and no other move. An independent check considers every pair of distinct matched edges and both reconnections of their four endpoints, retaining those for which both new edges belong to \(Q_d\); the two move sets agree for every state. Undirected adjacency is checked in both directions. Components are found by breadth-first search, and within the large four-dimensional component shortest paths are computed by breadth-first search from *every* vertex. This exhaustive, terminating graph computation gives the counts, degree sequence, and distances in the Finding. A further exhaustive application of all \(2^4\cdot4!=384\) cube automorphisms to one frozen matching gives exactly the set of all eight frozen matchings, hence the claimed orbit.

**Explicit four-dimensional frozen seeds.** The 16 vertices of \(Q_4\) are the integer bit words \(0,1,\ldots,15\). The following four perfect matchings are written as sets of unordered vertex pairs:

- \(A\): \((0,1),(2,6),(3,11),(4,12),(5,7),(8,10),(9,13),(14,15)\).
- \(B\): \((0,2),(1,9),(3,7),(4,5),(6,14),(8,12),(10,11),(13,15)\).
- \(C\): \((0,4),(1,3),(2,10),(5,13),(6,7),(8,9),(11,15),(12,14)\).
- \(D\): \((0,8),(1,5),(2,3),(4,6),(7,15),(9,11),(10,14),(12,13)\).

For each list, all sixteen vertices occur once and every displayed edge differs in exactly one bit. Inspecting the twenty-four coordinate squares verifies that none contains two opposite edges from any one matching. Inspection of the four cross-pairs also verifies
\[
A\cap C=A\cap D=B\cap C=B\cap D=\varnothing
\]
(as sets of edges), although the pairs within \(\{A,B\}\) or within \(\{C,D\}\) need not be disjoint. Both statements are asserted again by the executable finite checker and follow directly from the displayed lists.

**Inductive slice construction in arbitrary dimension.** Fix \(d\ge4\), split the coordinates into the first four and the remaining \(d-4\). Each word \(t\in\{0,1\}^{d-4}\) defines a disjoint 4-cube slice. If \(t\) has even Hamming-weight parity, fill its slice with either \(A\) or \(B\); if \(t\) has odd parity, fill it with either \(C\) or \(D\). Every slice independently contributes a perfect matching on its sixteen vertices, and none uses a crossing edge, so their union is a perfect matching of the entire \(Q_d\). Choices are independent across all \(2^{d-4}\) slices; the four base matchings are distinct, so the resulting global matchings are distinct. Their number is \(2^{2^{d-4}}\).

To prove all these global matchings frozen, consider an arbitrary coordinate square. If both varying coordinates are among the first four, it lies in one slice and no two opposite matching edges occur because its chosen base is frozen. If both varying coordinates are among the last \(d-4\), all four square edges cross slices, while no matched edge crosses any slice. If exactly one varying coordinate is among the first four, the only potentially matched opposite pair consists of the *same* four-dimensional edge in two slices indexed by \(t\) and \(t'\) differing in one bit. These two slice indices have opposite parity; thus one base is in \(\{A,B\}\) and the other in \(\{C,D\}\). Cross-disjointness forbids that common edge. In all three cases there is no legal square flip. This proves the infinite bound. The previously exhausted \(d=2,3\) cases have no frozen matching, giving the exact first dimension \(d=4\). All quantifiers and the smallest dimensions are accounted for.

## Verification
Execute `python3 verify_hypercube_flips.py` with Python 3.9 or newer. This standalone standard-library program regenerates all states using two different backtracking methods, verifies both independent legal-move descriptions, checks the complete finite component structure and the all-source distance statistics, enumerates the full 384-element automorphism group, discovers and verifies the explicit cross-disjoint quartet, and checks all four variants of the construction in dimension five. The included `verify_output.txt` is the exact output of a successful full run; running the extracted program again reproduces it byte-for-byte. The finite checker supplements, but is not substituted for, the separate symbolic slice proof in arbitrary dimension.

## Relationship to prior work
Fink's papers on matching graphs of hypercubes [1,2] use a substantially different adjacency: a pair of perfect matchings is adjacent when their union forms a **spanning Hamiltonian cycle**. Fink's connectivity theorem for that global operation does not imply connectivity under a single local coordinate-square flip, and is consistent with the eight frozen states above. The standard count of 272 perfect matchings of \(Q_4\) is previously tabulated [4], so that scalar is not proposed as new.

Milet and Saldanha [5] establish the square-flip rule and disconnectedness in three-dimensional two-floor boxes, but do not classify the graph of perfect matchings of a unit hypercube. The more directly related study by Hartarsky, Lichev and Toninelli [3] defines \(D_\ell\) using alternating cycles of length at most \(2\ell\). Its Theorems 5 and 6 provide degree/ergodicity statements on unit hypercubes with **cycles longer than four** allowed; for example, allowing cycles up to length six can release a square-frozen \(Q_4\) matching. Those results do not determine the four-cycle-only graph \(D_2(Q_4)\), its eight isolates, or this explicit infinite frozen-matching lower bound. The inspected full papers and targeted database searches did not locate an equivalent complete square-flip classification; this is a best-knowledge literature distinction, not proof that unindexed work does not exist. This theorem uses the same natural local operation as lattice dimer “plaquette flips,” but imposes the exact finite hypercube geometry and moves.

## Limitations
The exact degree sequence, component count, symmetry orbit and metric pertain only to the four-dimensional hypercube. The infinite-family statement proves a lower bound, not an exact enumeration or classification of all frozen matchings in higher dimensions; it does not claim that the nonfrozen states are connected there. The base calculation relies on finite exhaustive software whose full recursions are given for reproducibility, not external independent validation. The literature comparison leaves possible unindexed numerical tables or an equivalent construction under different terminology. No independent audit has been performed.

## References
1. J. Fink, *Matching graphs of hypercubes and complete bipartite graphs*, Electronic Notes in Discrete Mathematics, 2007; DOI 10.1016/j.endm.2007.07.059. Author-accessible conference manuscript: https://kam.mff.cuni.cz/~fink/publications/eurocomb07.pdf.
2. J. Fink, *Connectivity of matching graph of hypercube*, SIAM Journal on Discrete Mathematics, 2009; DOI 10.1137/070697288. Author manuscript: https://kam.mff.cuni.cz/~fink/publications/kreweras2.pdf.
3. I. Hartarsky, L. Lichev and F. Toninelli, *Local dimer dynamics in higher dimensions*, arXiv:2304.10930 (first public version 21 April 2023), Theorems 5 and 6, https://arxiv.org/abs/2304.10930.
4. OEIS A005271, number of perfect matchings of hypercubes, https://oeis.org/A005271.
5. P. H. Milet and N. C. Saldanha, *Flip invariance for domino tilings of three-dimensional regions with two floors*, arXiv:1404.6509 (first public version 25 April 2014), https://arxiv.org/abs/1404.6509.
