# Edge-open-packing rigidity in the Heawood and Desargues incidence graphs

## Finding
Let \(H\) be the Heawood graph, the point-line incidence graph of the Fano plane, and let \(D\) be the Desargues graph, the bipartite inclusion graph between the two-element and three-element subsets of a five-element set. An **edge-open packing** is an edge set such that no two selected edges have a *distinct third edge* joining an endpoint of one to an endpoint of the other; equivalently, its endpoint-induced subgraph is a disjoint union of stars. Write \(\rho_e^o\) for the maximum size of such a packing.

**Theorem.** The exact values and complete extremal configurations are
\[
\rho_e^o(H)=6,\qquad \rho_e^o(D)=9.
\]
The Heawood graph has exactly **14** maximum packings: each is three vertex-disjoint induced \(K_{1,2}\) stars, with the three centers either the three points on one Fano line or the three lines through one Fano point. Their six selected edges are uniquely forced by the centers. The Desargues graph has exactly **20** maximum packings: each comprises one induced \(K_{1,3}\) and three induced \(K_{1,2}\) stars, with all four centers in the same bipartition class. Every choice of the center of the \(K_{1,3}\) determines one maximum packing, and there are no others. In each graph, its maximum packings form a single automorphism orbit.

Both values are exactly one below the cubic bound \(|E(G)|/3\), which here is respectively \(7\) and \(10\). The result includes the full extremizer counts and structural classifications, not only the two numerical values.

## Assumptions and scope
All graphs are finite, simple and undirected. The Fano plane has seven points and seven lines; any two points lie on exactly one line, and two distinct lines intersect in exactly one point. The Heawood graph has \(14\) vertices and \(21\) edges, each vertex having degree \(3\). For the Desargues graph, denote by \(L\) the ten two-subsets and by \(R\) the ten three-subsets of \([5]\), with \(A\in L\) adjacent to \(B\in R\) precisely when \(A\subset B\). It is also cubic, with \(20\) vertices and \(30\) edges. Complementation in \([5]\) interchanges its two vertex classes and preserves adjacency.

A packing of size \(s\) whose induced star forest has \(c\) components has exactly \(s+c\) incident vertices. Its components are stars with one, two, or three edges because both graphs are cubic. Crucially, there are no graph edges between distinct induced star components.

## Proof
### 1. A divisibility refinement of the cubic upper bound
In any cubic graph on \(N\) vertices, let \(B\) be an edge-open packing of \(s\) edges inducing \(c\) stars on an endpoint set \(U\). We have \(|U|=s+c\) and exactly \(s\) edges inside \(U\). Thus the number of edges incident to \(U\), counting each edge once, is
\[
3|U|-s=2s+3c\le \frac{3N}{2}.
\]
Every star has at most three edges, so \(s\le3c\). Therefore \(s\le N/2\), and equality forces \(s=3c=N/2\), in particular \(6\mid N\). For \(N=14\) and \(N=20\), equality is impossible and hence \(s\le6\) and \(s\le9\), respectively. This is an upper bound only; the constructive classifications below establish sharpness.

### 2. Complete classification for the Heawood graph
Suppose \(s=6\). The incident-edge inequality gives \(2\le c\le3\). If \(c=2\), the packing consists of two full \(K_{1,3}\) stars. The distance between their centers would be at least four: distances one, two, and three respectively create a center-to-center edge, a shared leaf, or an edge between leaves. But the incidence graph of the Fano plane has diameter three. Therefore \(c=3\), with three \(K_{1,2}\) stars.

Two centers on opposite bipartition sides are impossible. An incident point and line would be adjacent. For a nonincident point \(p\) and line \(\ell\), the three lines through \(p\) meet \(\ell\) in three different points. The induced incidence between their respective neighborhoods is a perfect matching of size three; any choice of two neighbors on both sides includes a matched pair, creating an edge between the putative star components. Consequently the three centers all are points or all are lines.

Consider three point centers \(p,q,r\). Each center must have two lines not incident to either of the other two centers. If the three points are noncollinear, the two joining lines through \(p\) are distinct, so only one of the three lines through \(p\) is private—impossible. Hence the three centers are collinear. Conversely, if they lie on a Fano line, each center has exactly two other incident lines and selecting those six point-line edges produces three mutually nonadjacent \(K_{1,2}\) stars. There are seven possible common lines, and every choice forces exactly one packing. Interchanging points and lines gives seven additional packings centered at the three lines through a point. This proves the value, all \(14\) extremizers, and transitivity under Fano-plane symmetries together with point-line duality.

### 3. Complete classification for the Desargues graph
For \(s=9\), the incident-edge inequality forces \(c=3\) or \(c=4\). We use the following direct inclusion observations. A two-subset \(A\) and a three-subset \(B\) are incident if \(|A\cap B|=2\); when \(|A\cap B|=1\), precisely two of the three two-subsets of \(B\) are contained in one of the three three-subsets containing \(A\). Consequently a full three-edge star centered at \(A\) forbids a two-edge star centered at such a \(B\). An opposite-side center supporting a two-edge star alongside the full star at \(A\) must therefore be the unique complementary three-subset \(B=[5]\setminus A\). Dually the same assertion holds with the two sides interchanged.

If \(c=3\), all components are three-edge stars. Any two full-star centers on opposite sides must be complementary by the preceding observation. Three centers cannot mix sides, since the opposite-side complement of a fixed center is unique. If all are two-subsets, their pairwise neighborhoods are disjoint only if the two-subsets are pairwise disjoint; three such pairs cannot fit inside a five-set. If all are three-subsets, complementation gives the same contradiction. Hence \(c\ne3\).

For \(c=4\), star edge counts must be either \((3,3,2,1)\) or \((3,2,2,2)\). The first option is impossible: two full-star centers in the same part are complementary-disjoint in the appropriate two-subset representation, leaving no possible two-edge-star center on that side, while on the opposite side a two-edge-star center would have to be simultaneously complementary to both. If the two full-star centers are on opposite sides, they must be complements; a further two-edge center on either side is forced either to be incident to the opposite full center or to conflict with one of its selected leaves. Thus any nine-edge packing has a unique full star and three two-edge stars.

Suppose the full star center is a two-subset \(A\). At most one of the other centers can lie in the three-subset class, and it would have to be \(A^c\). Any further two-subset center must be disjoint from \(A\) and hence contained in \(A^c\), making it adjacent to that opposite-side center. Thus all four centers are two-subsets. Because the full star uses all three neighbors of \(A\), each of the other centers must be disjoint from \(A\). They are exactly the three two-subsets \(C\subset A^c\). The star at \(A\) uses its three supersets \(A\cup\{x\}\) for \(x\in A^c\); each remaining center \(C\subset A^c\) has exactly two available three-subset leaves \(C\cup\{a\}\) for \(a\in A\). The third candidate leaf, namely \(A^c\), is adjacent to all three smaller centers and cannot be selected. These forced choices form an induced disjoint union of one \(K_{1,3}\) and three \(K_{1,2}\), giving nine edges.

Every one of the ten two-subsets \(A\) yields exactly one packing. Complementation in \([5]\) gives the ten corresponding packings with the full-star center on the three-subset side. Thus exactly \(20\) packings exist. Permutations of \([5]\) act transitively on the first ten, and complementation exchanges the two classes, proving that all twenty lie in one automorphism orbit.

## Verification
The accompanying `verify.py` builds both incidence graphs without graph-theory packages, tests compatibility of every pair of graph edges directly from the definition, and exhaustively enumerates maximal cliques of the compatibility graphs by a pivoted Bron–Kerbosch recurrence. It separately counts fixed-size cliques using a non-pivot recursion, checks induced-star profiles, and verifies that natural automorphism actions generate the complete extremizer sets. The exact output in `verification_output.txt` reports:

* Heawood: maximal-clique size histogram \(\{3:14,6:14\}\), fourteen maximum packings of size six, profile \((2,2,2)\), one orbit under \(336\) explicit automorphisms.
* Desargues: maximal-clique size histogram \(\{5:132,6:105,8:30,9:20\}\), twenty maximum packings of size nine, profile \((2,2,2,3)\), one orbit under \(240\) explicit automorphisms.

The mathematical upper bounds and structural classifications above are self-contained; exhaustive computation is an independent finite check of both finite graphs, not an extrapolation to other orders or graph families. Run with `python3 verify.py` on a Python version supporting `int.bit_count` (Python 3.8 can instead use `bin(x).count('1')` in the one parity check).

## Relationship to prior work
Chelladurai, Kalimuthu and Soundararajan introduced edge-open packing and its graph-coloring interpretation. Brešar and Samadi established general extremal bounds and characterized equality in \(\rho_e^o(G)\le |E(G)|/\delta(G)\); their characterization does not determine the two strictly sub-extremal values or extremizer multiplicities here. Brešar, Dravec, Hedžet and Samadi studied product and hypercube edge-open packing; those results do not specify the two incidence graphs. Pandey and Santra later gave general necessary-and-sufficient tests for arbitrary prescribed packing size, but not closed values or complete maximum-set censuses for either graph. Searches also used the aliases “induced star forest,” “injective edge-color class,” “Fano incidence graph,” and “middle levels graph.”

The equality obstruction in Section 1 is related to, and weaker than, the 2024 general equality characterization. Novelty asserted here is restricted to the **two sharp near-equality values and their complete structural and orbit classifications**; neither the general cubic bound nor the EOP definition is claimed as new.

## Limitations
The theorem applies only to the Heawood and Desargues graphs. It does not classify other cubic bipartite incidence graphs, other generalized Petersen graphs, or other levels of Boolean-lattice inclusion graphs. The extremal counts are counts of distinct edge sets in the specified labeled realizations, not counts modulo isomorphism; each count corresponds to a single orbit. An unindexed equivalent description under induced-star-forest or injective-edge-coloring terminology could affect historical priority, notwithstanding the explicitly compared works.

## References
1. G. Chelladurai, K. Kalimuthu and S. Soundararajan, “Edge open packing sets in graphs,” *RAIRO Operations Research* 56 (2022), 3765–3776. DOI: 10.1051/ro/2022171. https://www.numdam.org/articles/10.1051/ro/2022171/
2. B. Brešar and B. Samadi, “Edge open packing: complexity, algorithmic aspects, and bounds,” arXiv:2403.00750v1 (public 2024-03-01). https://arxiv.org/pdf/2403.00750
3. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, “Induced matching vs edge open packing: trees and product graphs,” arXiv:2406.04020v2 (first public 2024-06-06). https://arxiv.org/pdf/2406.04020
4. A. Pandey and K. Santra, “Edge open packing: further characterizations,” arXiv:2508.01935v1 (2025). https://arxiv.org/pdf/2508.01935
