# Sharp two-site maximum-independent-set exchange distinguishes the Shrikhande and rook graphs

## Finding

Let \(S\) denote the Shrikhande graph and \(R=K_4\square K_4\) the four-by-four rook graph, the two strongly regular graphs with parameters \((16,6,2,2)\). Their maximum independent sets have size four. Define \(X_2(G)\) to have these sets as vertices and to join different sets \(I,J\) when \(|I\cap J|=2\); a step replaces two selected vertices by two others, with a valid maximum independent set at both endpoints. Define \(X_1(G)\) by \(|I\cap J|=3\).

**Theorem.** Both \(X_1(S)\) and \(X_1(R)\) have no edges. The two-site graphs are connected, and
\[
X_2(S)\cong D(\operatorname{Sub}(K_4)),\qquad X_2(R)\cong\operatorname{Cay}(S_4,\mathcal T),
\]
where \(D(\operatorname{Sub}(K_4))\) replaces each edge of \(K_4\) by *two* distinct length-two paths (not by a parallel edge), and \(\mathcal T\) is the six-transposition generating set. The Shrikhande graph has 16 configurations, 24 exchanges, degree multiset \(6^4,2^{12}\), radius 3 and diameter 4. The rook graph has 24 configurations, 72 exchanges, constant degree 6, and radius and diameter 3. Both exchange graphs are bipartite. Therefore the smallest simultaneous-exchange budget giving connectedness is exactly two for both graphs.

## Assumptions and scope

Graphs are simple and finite. An independent set of size four is an optimal configuration; intermediate states with three selected vertices are *not* allowed. The exchange cost counts simultaneous removal of exactly two tokens followed by insertion of two at unoccupied sites. No restriction requires moving tokens along underlying graph edges. Label \(V(S)=\mathbb Z_4^2\), with adjacency exactly when the coordinate difference is in \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\). Label \(V(R)=\{0,1,2,3\}^2\), with two squares adjacent when they have equal first or equal second coordinate.

## Proof

**Maximum size and complete configurations.** Both graphs are 6-regular with least adjacency eigenvalue \(-2\). The ratio bound yields \(\alpha\le16\cdot2/(6+2)=4\). Independent 4-sets exist in both graphs. In the rook graph, an independent 4-set occupies each row and each column exactly once; it is the graph of a permutation \(\pi\in S_4\). Thus there are exactly 24.

For Shrikhande, there are precisely nine nonneighbors of the zero vertex. The unordered triples of those nine vertices that form an independent set are exactly
\[
\begin{array}{c}
\{(0,2),(2,0),(2,2)\},\quad\{(0,2),(2,1),(2,3)\},\\
\{(1,2),(2,0),(3,2)\},\quad\{(1,3),(2,2),(3,1)\}.
\end{array}
\]
This is an exhaustive check of the \(\binom93=84\) triples using the stated six differences, also performed by the two included checkers. Adding zero gives four order-four subgroups \(H_0,H_1,H_2,H_3\) of \(\mathbb Z_4^2\), where
\[
H_0=2\mathbb Z_4^2,\quad H_1=\langle(2,1)\rangle,\quad H_2=\langle(1,2)\rangle,\quad H_3=\langle(1,3)\rangle.
\]
Every independent 4-set may be translated so that it contains zero, hence is a coset of one of these subgroups; conversely, all their cosets are independent. There are four cosets of each subgroup, so exactly 16 states.

**The Shrikhande exchange graph.** The intersection \(H_0\cap H_i\) has size two for \(i>0\), while \(H_i\cap H_j\) has size one for distinct \(i,j>0\). Two cosets of a common subgroup are disjoint; two cosets of different subgroups have intersection either empty or a coset of the subgroup intersection. Therefore the only intersections of size two occur between a coset of \(H_0\) and a coset of one of \(H_1,H_2,H_3\). Any such cyclic coset meets exactly two \(H_0\)-cosets in two vertices each. For each of the six unordered pairs of \(H_0\)-cosets, exactly two cyclic cosets meet that pair, because each nonzero coset in \(\mathbb Z_4^2/H_0\) corresponds to exactly one of the three order-four cyclic subgroups. These are the two degree-two subdivisions for each original edge of \(K_4\). The four \(H_0\)-cosets have degree six, the other twelve have degree two, and there are 24 exchange edges. The doubled subdivision is connected and bipartite; its radius is 3 and diameter is 4, by considering hub-to-hub paths and paths between subdivision vertices on disjoint edges.

**The rook exchange graph.** The corresponding permutations intersect in the number of positions where they agree. Two distinct permutations cannot agree at exactly three positions, and they agree in exactly two positions precisely when their quotient is a transposition. Thus \(X_2(R)\) is the transposition Cayley graph on \(S_4\). Its connectedness follows because transpositions generate \(S_4\); parity gives bipartiteness; its word metric is \(4-c(\sigma)\), where \(c(\sigma)\) counts cycles including fixed points. The largest such distance is three. Both one-site graphs are edgeless, and the asserted minimum exchange threshold follows.

## Verification

Run `python3 verify_bruteforce.py` and `python3 verify_algebra.py` with Python 3 and its standard library. The first constructs the two 16-vertex underlying graphs, checks by exhaustive enumeration that no independent 5-sets exist, lists all independent 4-sets, constructs each complete exchange graph, and computes all graph distances and bipartiteness. The second uses subgroup cosets and independent permutation matrices, and separately checks the doubled-subdivision incidence and transposition Cayley structure. Both programs use only standard-library modules. The outputs are deterministic. The exhaustive computations are limited to the two named graphs; the theorem is finite, so no larger-order extrapolation is claimed.

## Relationship to prior work

Peeters's 1993 research memorandum, published in the *European Journal of Combinatorics* in 1997, already describes the 4-coclique split in the Shrikhande graph (four sub-3-net configurations and twelve 3-net-line configurations). The 16-state census and two types are **not** claimed as new. The ratio bound and the permutation encoding for the rook graph are also elementary established facts. Bonsma, Kamiński and Wrochna (arXiv:1403.0359v1, first submitted 2014-03-03 UTC) study ordinary one-token independent-set reconfiguration, not the simultaneous 2-for-2 exchange. Existing published independence-complex comparisons distinguish the same cospectral pair by homotopy type, not the exact exchange graphs. The proposed addition is the sharp budget-two exchange geometry and the explicit contrast of its two full reconfiguration graphs.

## Limitations

This result is confined to the two strongly regular graphs with parameters \((16,6,2,2)\); it gives no theorem for larger Doob or Hamming graphs. The structure depends on allowing *simultaneous* two-site replacements without retaining independence after the first removal/insertion. Earlier literature describing 4-cocliques could imply parts of the present exchange geometry after an additional intersection analysis; exact equivalent descriptions in unindexed configuration literature remain an originality risk. The Peeters antecedent has a verified public *year* (1993), but no publicly verified first day; the `first_public_date` metadata records the earliest verified exact UTC date among inspected independently date-stamped methodological sources (2014-03-03), not a claim that no earlier undated precursor exists. Independent scholarly validation has not been performed.

## References

1. R. Peeters, *Strongly regular graphs that are locally a disjoint union of hexagons*, Tilburg research memorandum FEW 625 (1993), and *European Journal of Combinatorics* 18 (1997), 579–588. https://research.tilburguniversity.edu/en/publications/strongly-regular-graphs-that-are-locally-a-disjoint-union-of-hexa-2 ; https://paperzz.com/doc/7134087/strongly-regular-graphs-that-are-locally-a-disjoint-union...
2. A. E. Brouwer and H. Van Maldeghem, *Strongly Regular Graphs*, online monograph, section on Shrikhande and the rook graph. https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf
3. P. Bonsma, M. Kamiński, M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1, 2014-03-03. https://arxiv.org/abs/1403.0359
4. *Independence complexes of the Shrikhande and 4×4 rook graphs have different sphere-wedge homotopy types*, published-finding corpus entry, 2026-10-11, database identifier `2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187` (summary consulted; full text not accessible).
