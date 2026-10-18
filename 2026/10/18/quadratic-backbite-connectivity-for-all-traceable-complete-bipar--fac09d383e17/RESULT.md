# Quadratic backbite connectivity for all traceable complete bipartite graphs
## Finding
Let \(R(G)\) be the reconfiguration graph whose vertices are **unoriented** Hamiltonian paths of a finite simple graph \(G\), with two paths adjacent when a single endpoint backbite transforms one into the other. For every \(n\ge1\), both \(R(K_{n,n})\) and \(R(K_{n,n+1})\) are connected. Quantitatively, for \(n\ge2\),
\[
\operatorname{diam}R(K_{n,n})\le6n(n-1),
\]
and for \(n\ge3\),
\[
\operatorname{diam}R(K_{n,n+1})\le15n^2-9n.
\]
The exceptional \(R(K_{2,3})\) is connected with diameter \(3\). When \(n=1\), each corresponding graph has one unoriented Hamiltonian path. A complete bipartite graph with two nonempty sides admits a Hamiltonian path if and only if the side sizes differ by at most one. Thus the connectivity statement covers **all** traceable complete bipartite graphs.

## Assumptions and scope
A *backbite* on a Hamiltonian path \((v_1,\ldots,v_N)\) joins one endpoint, say \(v_1\), to an internal vertex \(v_i\), with \(i\ge3\), by a graph edge and removes the path edge \(v_{i-1}v_i\). Equivalently it replaces the oriented path by \((v_{i-1},\ldots,v_1,v_i,\ldots,v_N)\). The symmetric operation is permitted from the right endpoint. Reversed words define the same unoriented path. Distances count legal single backbites, not informal adjacent swaps. All graphs are finite, simple and have two nonempty bipartition classes, and the stated upper bounds are not claimed to be optimal.

Write the two classes as \(X\) and \(Y\). A permutation pair \((x_1\cdots x_n,y_1\cdots y_m)\) specifies an alternating oriented Hamiltonian path. Let \(P_j\) denote a backbite at the left endpoint reversing the first \(2j-1\) vertices, and \(S_j\) a right-end backbite reversing the last \(2j-1\) vertices. Indices begin at one; compositions of operations below are applied from left to right. Each generator with \(2\le j\le n\) is a permitted backbite and is an involution.

## Proof
**Balanced sides.** Canonically orient every undirected Hamiltonian path in \(K_{n,n}\) to begin in \(X\), so its vertex word is \((x_1,y_1,\ldots,x_n,y_n)\). The endpoint operations on the corresponding permutation pair are
\[
P_j:(x_1\cdots x_n,y_1\cdots y_n)\mapsto
(\operatorname{rev}(x_1\cdots x_j)x_{j+1}\cdots x_n,
 \operatorname{rev}(y_1\cdots y_{j-1})y_j\cdots y_n),
\]
\[
S_j:(x_1\cdots x_n,y_1\cdots y_n)\mapsto
(x_1\cdots x_{n-j+1}\operatorname{rev}(x_{n-j+2}\cdots x_n),
 y_1\cdots y_{n-j}\operatorname{rev}(y_{n-j+1}\cdots y_n)).
\]
These are direct reversals of alternating path segments. The composition \(P_jP_2P_j\) swaps **only** \(x_{j-1}\) and \(x_j\), for every \(2\le j\le n\). Similarly \(S_jS_2S_j\) swaps **only** \(y_{n-j+1}\) and \(y_{n-j+2}\). To see these identities, note that \(P_2\) reverses exactly the first two entries of the \(X\)-permutation and fixes the \(Y\)-permutation; conjugation by the length-\(j\) prefix reversal transports that transposition to positions \((j-1,j)\), while the other prefix reversal is canceled. The right-side identity is symmetric. Therefore all adjacent transpositions of the two component permutations occur as words of three backbites. Sorting both permutations needs at most \(2\binom n2=n(n-1)\) adjacent transpositions. Hence any oriented Hamiltonian path reaches one canonical path in at most \(3n(n-1)\) moves. Concatenating two such routes proves the first diameter bound.

**One extra vertex.** In \(K_{n,n+1}\), orient paths to begin in the larger class \(Y\), giving \((y_1,x_1,y_2,x_2,\ldots,y_n,x_n,y_{n+1})\). The generators \(P_j\) and \(S_j\), for \(2\le j\le n\), respectively reverse the first \(j\) and last \(j\) entries of the \(Y\)-permutation, and the first \(j-1\) and last \(j-1\) entries of the \(X\)-permutation. Thus \(P_2\) swaps \(y_1,y_2\) without changing \(X\), and \(S_2\) swaps \(y_n,y_{n+1}\) without changing \(X\). For \(2\le j\le n\), the triple \(P_jP_2P_j\) swaps only \(y_{j-1},y_j\); likewise \(S_jS_2S_j\) swaps only \(y_{n-j+2},y_{n-j+3}\). Accordingly all adjacent \(Y\)-transpositions cost at most three backbites.

For \(n\ge3\), the single move \(P_3\) swaps \(x_1,x_2\) and simultaneously exchanges \(y_1,y_3\). Cancel that latter exchange using the three available pure adjacent \(Y\)-swaps \((1,2)(2,3)(1,2)\), giving a pure transposition of \(x_1,x_2\) of cost at most \(1+3\cdot3=10\). For every \(2\le i\le n-2\), conjugating that pure transposition by \(P_{i+2}\) yields a pure transposition of \(x_i,x_{i+1}\), at most twelve moves: conjugation transports the first-two \(X\)-positions to \((i,i+1)\), while the \(Y\)-part cancels. Finally \(S_3\) interchanges the last two \(X\)-entries and a pair of \(Y\)-entries separated by one position. Cancel the latter by three pure adjacent \(Y\)-swaps, costing at most ten. Hence each adjacent \(X\)-transposition costs at most twelve, independently of the other class. Sorting both permutations to fixed orders uses no more than
\[
12\binom n2+3\binom{n+1}2=\frac{15n^2-9n}{2}
\]
backbites per oriented path, and twice this many between arbitrary oriented paths. The unoriented reconfiguration graph is a quotient of this connected oriented move graph, so the asserted diameter bound follows.

**Small orders.** If \(n=2\) and the side sizes are \(2,3\), the two permitted endpoint moves \(P_2,S_2\) independently swap the two left or two right adjacent \(Y\)-positions, yielding a six-vertex connected component for each of the two fixed \(X\)-orders. Reversal of the entire alternating path exchanges the two \(X\)-orders; therefore the unoriented state graph is connected. Its diameter is exactly three because the six canonical unordered paths are naturally labeled by permutations of the three \(Y\)-vertices and the two endpoint moves realize the two adjacent transpositions, giving the six-cycle Cayley graph. The \(n=1\) cases have a unique unoriented path. Finally every path in a bipartite graph alternates sides, so all-vertex paths require side sizes differing by at most one; conversely any such complete bipartite graph has an alternating Hamiltonian path. This proves all assertions.

## Verification
A standalone exact checker (`verify.py`) constructs the backbite permutations, independently enumerates backbite neighbors from actual alternating vertex words, tests their agreement, checks the pure adjacent-transposition macros for a range of parameters, and verifies constructive sorting and the resulting length bounds on deterministic sample states. Exhaustive finite tests are corroborative only; the unrestricted theorem is proved by the explicitly displayed generator identities and sorting argument.

## Relationship to prior work
Kazazi's October 2026 work introduced the Hamiltonian-path reconfiguration setting and proved connectedness whenever a graph contains the square of a spanning Hamiltonian path, or has minimum degree at least about two-thirds of its order; it conjectured connectedness under the half-order minimum-degree condition. Neither established sufficient condition applies to balanced complete bipartite graphs: a Hamiltonian-path square necessarily has edges within a bipartition class, and their minimum degree falls below the published two-thirds threshold. The balanced family here lies exactly at the conjectured half-order boundary, while the one-extra-vertex family has a similar extremal alternating structure. Takaoka's earlier Hamiltonian **cycle** reconfiguration theorem uses two-edge switches rather than endpoint backbites, so neither adjacency nor conclusion subsumes this result. A published bipermutahedron reversal-distance calculation concerns a polytope's adjacent-word swaps and singleton transfers, not endpoint rotations of Hamiltonian paths. The exact classification and explicit quadratic backbite bounds are not entailed by those results.

## Limitations
The theorem applies to complete bipartite graphs with nonempty sides and a Hamiltonian path; it does not address general graphs or all graphs meeting the half-degree conjecture. The bounds are constructive upper bounds, not asserted sharp distances. Originality comparisons cover the cited primary work and related identifiable formulations, but unindexed equivalent literature cannot be ruled out by search alone. No independent scientific review is asserted.

## References
1. Albi Kazazi, *Connectivity of the reconfiguration graph of Hamiltonian paths*, arXiv:2610.05068v1 (first public version 4 October 2026), Theorem 1.1, Corollary 1.2 and Conjecture 7.8.
2. Asahi Takaoka, *Complexity of Hamiltonian Cycle Reconfiguration*, Algorithms 11(9), 140 (2018), DOI: 10.3390/a11090140.
3. Federico Ardila, *The bipermutahedron*, arXiv:2008.02295 (first public version 5 August 2020); contextual graph of ordered bipermutations with different edge operations.
