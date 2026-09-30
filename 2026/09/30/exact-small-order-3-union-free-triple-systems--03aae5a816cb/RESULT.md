# Exact small-order 3-union-free triple systems through nine vertices
## Finding
Let \(U_3(n,3)\) denote the maximum size of a 3-uniform family \(\mathcal F\subseteq\binom{[n]}{3}\) for which the map
\[
\mathcal A\longmapsto \bigcup_{E\in\mathcal A}E
\]
is injective over all nonempty subfamilies \(\mathcal A\subseteq\mathcal F\) with \(1\le |\mathcal A|\le3\). For every integer \(4\le n\le9\),
\[
U_3(n,3)=n-2.
\]
Moreover, up to relabeling, the unique extremal family is a pair-star: for a fixed two-set \(S\subseteq[n]\),
\[
\mathcal F_S=\{S\cup\{x\}:x\in[n]\setminus S\}.
\]
Consequently there are exactly \(\binom n2\) labeled extremal families, namely \(6,10,15,21,28,36\) for \(n=4,5,6,7,8,9\), respectively.
## Assumptions and scope
All hypergraphs are finite, simple, and 3-uniform. The definition above requires distinct unions for every two distinct nonempty edge-subfamilies of cardinality at most three. The claim is only for \(4\le n\le9\); it makes no assertion for \(n\ge10\).
## Proof
For the lower bound, fix a pair \(S\). Every subfamily of \(\mathcal F_S\) is determined by its set of outside vertices: if \(\mathcal A\subseteq\mathcal F_S\), then
\[
\bigcup_{E\in\mathcal A}E=S\cup X_{\mathcal A},
\]
where \(X_{\mathcal A}\subseteq[n]\setminus S\) is precisely the set of third vertices appearing in \(\mathcal A\). Thus different nonempty subfamilies of size at most three have different unions, proving \(U_3(n,3)\ge n-2\).

The upper bound and equality classification are finite exact statements. Because 3-union-freeness is hereditary under deleting edges, it is enough to rule out a family of exactly \(n-1\) edges. By vertex relabeling, every nonempty candidate has a distinguished first edge \(\{0,1,2\}\). An exact depth-first search then adds triples in lexicographic order. At any node it stores every union already realized by a one-, two-, or three-edge subfamily. When a new edge \(e\) is proposed, the only newly created unions are \(e\), \(e\cup E_i\), and \(e\cup E_i\cup E_j\); the branch is rejected if any two of these collide or if any collides with a previously stored union. This criterion is exactly equivalent to preserving 3-union-freeness after inserting \(e\), so the search is exhaustive by induction on the number of selected edges.

For each \(n=4,5,6,7,8,9\), the search finds no family of \(n-1\) edges containing \(\{0,1,2\}\), hence no such family at all. It also enumerates exactly three \((n-2)\)-edge extremal families containing \(\{0,1,2\}\). The three pair-stars centered at \(\{0,1\}\), \(\{0,2\}\), and \(\{1,2\}\) are already three such families, so they exhaust the fixed-edge equality cases. Double-counting incidences between labeled extremal families and their edges gives
\[
N_n(n-2)=\binom n3\cdot3,
\]
and therefore \(N_n=\binom n2\). Since there are exactly \(\binom n2\) pair-stars, every labeled extremal family is a pair-star.
## Verification
The file `artifacts/verify_unionfree.py` implements the exact union-collision search described above and emits `VERIFY_OK` together with the per-order census. A separately implemented C++ program, `artifacts/crosscheck_unionfree.cpp`, repeats the search with independently written state handling and emits `CROSSCHECK_OK`. Both implementations agree on the optimum, the number of fixed-edge extremals, and the pair-star classification for every \(n=4,\ldots,9\).

The recorded primary output gives fixed-edge upper-search node counts \(3,11,66,643,7009,127221\) and labeled extremal counts \(6,10,15,21,28,36\). These counts are not used as assumptions in the proof; they are reproducibility data for the exact finite verification.
## Relationship to prior work
Liu, Shangguan, and Zhang study uniform union-free hypergraphs and explicitly leave the regime \(U_3(n,3)\) outside their general asymptotic theorem; they also recall the known superlinear lower bound \(U_3(n,3)=\Omega(n^{5/3})\). The present result therefore supplies exact initial conditions in an exceptional regime whose eventual behavior is much larger than the pair-star construction.

A nearby constant-weight coding problem is the 2-cover-free, or 2-disjunct, condition on triples. It is necessary but not sufficient for 3-union-freeness: if an edge is contained in the union of two other edges, those two edges and all three have the same union. The converse implication fails. Thus a maximum-size theorem for 2-cover-free triple families does not itself determine the stricter 3-union-free optimum or its equality classification. For example, the seven lines of the Fano plane form a 2-cover-free family; several distinct three-line subfamilies have union equal to its seven-point ground set, so it is not 3-union-free. This distinguishes the conditions without claiming that a weaker condition is stronger.
## Limitations
The upper bounds and classifications for \(4\le n\le9\) are computer-assisted finite proofs, albeit with two independent exact implementations. No claim is made for \(n\ge10\), and the computation does not address the asymptotic problem. The literature comparison is best-of-knowledge rather than a formal exhaustive bibliographic proof; an obscure older small-order table could in principle exist despite targeted searches under union-free, separable-code, and uniquely-decodable terminology.
## References
1. M. Liu, C. Shangguan, and C. Zhang, “Asymptotically sharp bounds for cancellative and union-free hypergraphs,” arXiv:2411.07908v1, first public 2024-11-12.
2. M. Liu, C. Shangguan, and C. Zhang, “Sharp bounds for uniform union-free hypergraphs,” arXiv:2605.11949v1, first public 2026-05-12 (later versions titled “Sharp asymptotic bounds for uniform union-free hypergraphs”).
