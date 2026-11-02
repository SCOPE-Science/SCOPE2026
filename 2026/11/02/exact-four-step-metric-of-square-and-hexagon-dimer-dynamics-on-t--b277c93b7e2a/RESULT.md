# Exact four-step metric of square-and-hexagon dimer dynamics on the tesseract

## Finding
Let \(Q_4\) denote the graph on \(\{0,1\}^4\) with edges between bitstrings of Hamming distance one. Form the graph \(\mathcal F_{4,6}(Q_4)\) whose vertices are **all perfect matchings** of \(Q_4\), with two distinct matchings adjacent precisely when their symmetric difference is the edge set of a *single simple alternating cycle* of length four or six. Every state of this graph has eccentricity **four**. Hence the graph is connected and is self-centered with
\[
\operatorname{rad}\mathcal F_{4,6}(Q_4)=\operatorname{diam}\mathcal F_{4,6}(Q_4)=4.
\]
There are exactly 272 states, 1,984 unordered move edges (768 supported on squares and 1,216 on six-cycles), and the complete unordered-pair distance enumerator is
\[
\sum_{\{M,N\}}z^{d(M,N)}=1984z+10784z^2+19568z^3+4520z^4.
\]
Thus precisely 4,520 unordered pairs require four moves; all other distinct pairs require one to three moves. These are exact, finite results for the labelled four-dimensional unit hypercube, not asymptotic claims about arbitrary boxes.

## Assumptions and scope
Each of the sixteen graph vertices is represented by an integer in \(\{0,\ldots,15\}\), whose four-bit expansion specifies the coordinate vector. Its neighbours are the integers obtained by toggling exactly one bit. A perfect matching is a set of eight disjoint graph edges covering all sixteen vertices exactly once. A switch along a simple cycle is legal if the matching contains one of the two alternating edge sets; its replacement by the complementary set remains a perfect matching. The move graph is simple, undirected, and unweighted; a move along a square and a move along a hexagon each cost one. A six-cycle move is permitted regardless of whether it lies in a single three-dimensional coordinate face; all simple six-cycles of \(Q_4\) are included. The distance enumerator uses unordered distinct pairs.

## Proof
The proof is an exhaustive finite derivation, with its complete state and adjacency certificate in `certificate.json` and a standalone exact checker in `verify_cycle.py`.

**Completeness of states.** Recursively choose the smallest vertex not yet matched. Branch over every neighbour of this vertex that is still available, record that edge, and recurse after deleting its endpoints. Any perfect matching contains exactly one edge incident with that smallest vertex, so induction on the number of unmatched vertices proves that this procedure constructs every perfect matching exactly once. Sorting the resulting edge sets gives 272 distinct matchings. An independent enumeration, `verify_bipartite.py`, instead selects one neighbour for each even-parity bitstring, with no odd-parity neighbour repeated, and obtains exactly the identical set of 272 states.

**Completeness of moves.** A depth-first enumeration visits all simple cycles of lengths four and six. Cycles are represented by their edge sets, removing duplicates arising from changing the starting point or reversal. There are exactly 24 square cycles and 128 simple hexagons. For each perfect matching \(M\), and each cycle \(C\) in this exhaustive list, test whether \(|M\cap C|=|C|/2\). Because \(M\) is a matching, this condition requires an alternating selection covering every vertex of \(C\); consequently \(M\triangle C\) is a perfect matching and is precisely the legal switch. Conversely, every legal switch is found by the simple-cycle list and this incidence test. Edge sets of distinct cycles of the two prescribed lengths cannot induce the same adjacent pair: their symmetric difference is uniquely determined. The generated adjacency is symmetric and has 768 square edges and 1,216 additional hexagon edges. As an independent cross-check, for each unordered pair of the 272 states, the second verifier constructs its symmetric difference and tests whether it is exactly one connected two-regular component on four or six edges. This independently produces precisely the same two adjacency matrices.

**Metric.** Starting from each one of the 272 states, run ordinary breadth-first search in the union adjacency graph. Breadth-first search discovers vertices at minimum graph distance by induction on the queue layer. Every search reaches all 272 states and has maximum layer exactly four. Counting unordered pairs at each layer gives exactly 1,984, 10,784, 19,568 and 4,520 pairs at distances one, two, three and four respectively. The four figures sum to \(\binom{272}{2}=36,856\), so no pairs are omitted. Since each source has a vertex at distance four and none farther, every eccentricity is four; hence both radius and diameter are four. A concrete distance-four witness consists of the matchings

`[(0,1),(2,3),(4,5),(6,7),(8,9),(10,11),(12,13),(14,15)]`

and

`[(0,1),(2,6),(3,11),(4,12),(5,7),(8,10),(9,13),(14,15)]`.

The cited independent verifier checks every state, move and all 36,856 unordered distances, not just this witness.

## Verification
Run `python3 verify_cycle.py certificate.json` and `python3 verify_bipartite.py certificate.json` in the directory containing all three supplied files. The first checker independently recomputes all matchings, cycle lists, moves and all-source distance histograms, then compares its deterministically serialized certificate byte-for-byte with `certificate.json`. The second checker reconstructs the 272 matchings via even-to-odd assignments, tests every one of the 36,856 matching pairs by symmetric difference, builds the adjacency graph independently, runs its own 272 breadth-first searches, and checks the claimed complete distance histogram. Both scripts require only Python's standard library. `certificate.json` embeds the full sorted matching list, both adjacency lists and numerical totals. Thus the certificate provides a complete reproducible finite proof rather than a non-exhaustive sample of computations.

## Relationship to prior work
Milet and Saldanha introduced flip-and-trit local domino dynamics in three-dimensional duplex regions (first publicly posted in April 2014); their graph and domain are distinct from the exact four-dimensional matching metric here. Klivans and Saldanha, Example 2.2, already counted **272** domino tilings of the four-dimensional \(2\times2\times2\times2\) box and gave the square-flip component sizes \(264,1,1,1,1,1,1,1,1\). Those numbers and the existence of frozen square-flip configurations are **not novel claims** here. Their Theorem 3 addresses the twist parity of flips and trits. Hartarsky, Lichev and Toninelli subsequently proved general non-isolation results for short local moves and an ergodicity theorem allowing cycles of length at most twelve in \(Q_4\), with the corresponding general diameter bound 24. Combined previous work can already substantially constrain the connectivity of the four-or-six move graph; connectivity alone is not asserted as a new principle. The contribution here is the **sharp exact metric under precisely four- and six-cycle moves**, including the self-centered eccentricity four and full pair-distance distribution. Bonamy and collaborators studied the computational complexity of perfect-matching reconfiguration by square flips on general graphs, a different move set.

## Limitations
This is an exactly enumerated theorem for \(Q_4\) alone. It provides no asymptotic mixing-time estimate, no analogous metric formula for higher-dimensional hypercubes, and no lower bound on full-dimensional dimer Markov-chain mixing times. Historical tables or unpublished exhaustive studies might independently have recorded the same numbers; a negative literature search cannot establish absolute priority. No independent scholarly audit or external mathematical certification has been conducted.

## References
1. P. H. Milet and N. C. Saldanha, *Flip invariance for domino tilings of three-dimensional regions with two floors*, arXiv:1404.6509 (first posted 2014-04-25), https://arxiv.org/html/1404.6509v2.
2. C. Klivans and N. C. Saldanha, *Domino tilings and flips in dimensions 4 and higher*, arXiv:2007.08474 (first posted 2020-07-16), Example 2.2 and Theorem 3, https://arxiv.org/html/2007.08474v2.
3. I. Hartarsky, L. Lichev and F. Toninelli, *Local dimer dynamics in higher dimensions*, arXiv:2304.10930 (first posted 2023-04-21), Theorems 5 and 6, https://arxiv.org/html/2304.10930v2.
4. M. Bonamy et al., *The perfect matching reconfiguration problem*, arXiv:1904.06184 (first posted 2019-04-12), https://arxiv.org/html/1904.06184v1.
