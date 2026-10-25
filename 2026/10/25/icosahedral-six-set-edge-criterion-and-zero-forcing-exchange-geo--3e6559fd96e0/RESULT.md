# Icosahedral six-set edge criterion and zero-forcing exchange geometry

## Finding
Let \(I\) be the ordinary icosahedral graph (the graph of a regular icosahedron), and let \(e_I(S)\) be the number of edges induced by \(S\subseteq V(I)\). Under ordinary zero forcing, its zero-forcing number is \(Z(I)=6\), and a six-vertex set \(S\) is a minimum zero-forcing set **if and only if**
\[
e_I(S)\in\{8,9\}.
\]
There are exactly \(200\) such sets, in three orbits under the \(120\) graph automorphisms, of sizes \(120,60,20\). Exactly \(20\) minimum sets force all vertices in two simultaneous rounds; the other \(180\) need three. The complete ordinary zero-forcing polynomial is
\[
\mathcal Z(I;z)=200z^6+480z^7+450z^8+220z^9+66z^{10}+12z^{11}+z^{12}.
\]
In the minimum-set token-jumping reconfiguration graph \(\mathscr Z(I)\), where one vertex of a minimum set is replaced by one outside it, all \(200\) configurations lie in one connected component. It has \(1320\) edges, radius and diameter both \(6\), and its unordered-pair distance distribution, for distances \(1,\ldots,6\), is
\[
(1320,5160,6300,5010,2010,100).
\]

## Assumptions and scope
Label the vertices \(0,1,\ldots,11\). Vertices \(0\) and \(11\) are poles; vertices \(1,\ldots,5\) form one pentagon, and \(6,\ldots,10\) another. For \(i\in\{0,1,2,3,4\}\), let \(a_i=1+i\) and \(b_i=6+i\), with ring subscripts reduced modulo \(5\). The edges are all \(0a_i\), \(11b_i\), \(a_ia_{i+1}\), \(b_ib_{i+1}\), \(a_ib_i\), and \(a_ib_{i-1}\). Thus the graph is the usual pentagonal antiprism with two pyramidal caps; it has \(12\) vertices, \(30\) edges, and degree \(5\) everywhere.

Initially a subset \(S\) is blue. A blue vertex with exactly one white neighbor turns that neighbor blue. A set is zero forcing if finitely many applications color every vertex. Propagation time is the number of synchronous rounds using all presently possible forces. All sets are vertex-labeled in the graph above. The reconfiguration adjacency is symmetric difference of size \(2\), without any requirement that the removed and added vertices be adjacent in \(I\).

## Proof
**Lower bound.** A vertex of degree \(5\) cannot make its first force unless at least four neighbors and the vertex itself are blue; therefore no starting set of size at most \(4\) can force. If a starting set of size \(5\) permits a first force, it consists of a vertex \(u\) and precisely four of its neighbors. That move produces the closed neighborhood \(N_I[u]\). The five neighbors of \(u\) induce a pentagon. Each of them then has exactly two white neighbors; \(u\) has none. Hence no further force is possible and \(Z(I)\ge6\).

**Six-vertex classification.** The complete finite orbit certificate below represents each six-element subset by the integer \(m(S)=\sum_{v\in S}2^v\). Its columns give the edge count, orbit representative, orbit size, and success. The representative is the smallest integer in its orbit.

| \(e_I(S)\) | Representative and orbit size | Ordinary zero forcing? |
|---:|---|---|
| 10 | \(63:12\) | no |
| 9 | \(95:60,\ 111:20\) | yes |
| 8 | \(123:120\) | yes |
| 7 | \(126:60,\ 243:120,\ 245:30,\ 359:60,\ 371:30\) | no |
| 6 | \(250:30,\ 363:120,\ 365:20,\ 374:120,\ 498:10,\ 726:30,\ 756:10\) | no |
| 5 | \(715:12,\ 723:60\) | no |

The orbit sizes total \(924=\binom{12}{6}\). Every row can be reconstructed without graph-isomorphism software: `verify.py` enumerates every adjacency-preserving permutation by backtracking, obtains exactly \(120\) automorphisms, generates the disjoint orbits of all \(924\) six-subsets, and checks each representative by two equivalent implementations of the color-change rule. Because graph automorphisms preserve induced-edge counts and forcing, this exhaustive finite partition proves the iff criterion and the count \(60+20+120=200\). As explicit witnesses, the representatives \(95\), \(111\), and \(123\) force respectively in \(3\), \(2\), and \(3\) rounds. For \(95\) the newly forced vertex sets are \(\{5,7\}\), then \(\{8,10\}\), then \(\{9,11\}\). For \(111\) they are \(\{4,7,10\}\), then \(\{8,9,11\}\). For \(123\) they are \(\{2\}\), then \(\{7,10\}\), then \(\{8,9,11\}\). All other orbit representatives fail, which is also checked independently for every six-subset.

**All coefficients.** There are exactly \(2^{12}=4096\) initial blue subsets. The two independent forcing algorithms in `verify.py` determine the final color state for each of these subsets and agree on success/failure for every one. Grouping successes by size yields \(200,480,450,220,66,12,1\) at sizes \(6,7,8,9,10,11,12\), and none below six. This is a complete finite enumeration, not a sample extrapolation.

**Reconfiguration.** The same verifier constructs every unordered pair of the \(200\) minimum sets at Hamming distance \(2\). It finds exactly \(1320\) edges; all adjacency decisions are checked a second time by direct pairwise Hamming distances. Breadth-first search from each of the \(200\) vertices reaches all others and finds eccentricity \(6\) for every vertex. Summing source-to-target distances and halving gives the displayed six-entry distribution, whose entries add to \(\binom{200}{2}=19900\). The three minimum-set symmetry orbits have sizes \(20,60,120\) and reconfiguration degrees \(18,16,11\), respectively, consistent with \(2|E|=2640\).

## Verification
Run `python3 verify.py` in the directory containing this file, using Python 3.8 or later; the verifier uses only the standard library. It reconstructs the graph from the explicit edge definition; compares sequential and synchronous forcing on all \(4096\) initial sets; checks the entire \(18\)-orbit classification of six-subsets and all \(120\) automorphisms; verifies the induced-edge criterion, polynomial, orbit sizes, and propagation counts; constructs the full reconfiguration graph in two ways; and performs a breadth-first search from each of its \(200\) vertices. Success ends with `VERIFY_OK`. The explicit orbit table, plus the complete deterministic search logic, provides a finite proof certificate.

## Relationship to prior work
Hogben, Huynh, Kingsley, Meyer, Walker, and Young (arXiv:1410.4191v1; public October 15, 2014) define and investigate ordinary zero-forcing propagation time. Boyer and collaborators (arXiv:1801.08910v1) introduce the zero-forcing polynomial and characterize it for selected graph families. Geneson, Haas, and Hogben's reconfiguration work (arXiv:2009.00220v1) defines the minimum-zero-forcing-set exchange graph and studies its general properties. The inspected texts provide these frameworks, but do not calculate the icosahedral six-set induced-edge criterion, its three optimal symmetry orbits, the displayed polynomial, or this exchange graph's exact metric. These results are not consequences of the papers' general formulas for complete graphs, cycles, trees, or other treated families. Searches for icosahedral forcing counts and equivalent descriptions did not locate a covering statement; absence of a search hit is not a uniqueness guarantee.

## Limitations
The claims concern only the ordinary \(12\)-vertex icosahedral graph, not arbitrary triangulations, geometric icosahedral networks, or other forcing variants. All finite numerical claims rest on auditable exhaustive enumeration. The result does not assert an infinite-family theorem or a general algorithmic complexity improvement. Unindexed computations or graph tables might already contain some counts; independent expert review has not occurred.

## References
1. L. Hogben, M. Huynh, N. Kingsley, S. Meyer, S. Walker, and M. Young, *Propagation time for zero forcing on a graph*, arXiv:1410.4191v1 (October 15, 2014), https://arxiv.org/abs/1410.4191.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (January 26, 2018), https://arxiv.org/abs/1801.08910.
3. J. Geneson, R. Haas, and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1 (September 1, 2020), https://arxiv.org/abs/2009.00220.
