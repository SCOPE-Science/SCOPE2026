# The octagon-flip threshold for Nauru perfect matchings

## Finding

Let \(H=GP(12,5)\) be the Nauru graph. For an even integer \(\ell\), let \(\mathcal F_{\ell}(H)\) be the simple graph whose vertices are all perfect matchings of \(H\), with two matchings adjacent precisely when their symmetric difference is **one simple cycle of exactly \(\ell\) edges**. Equivalently, one may replace the selected edges of a matching along an alternating \(\ell\)-cycle by its unselected edges; no moves of other lengths are allowed.

**Theorem.** The Nauru graph has \(120\) perfect matchings, and the first even flip length giving a connected configuration graph is \(\ell=8\). More precisely:

* \(\mathcal F_4(H)\) has no edges, because \(H\) contains no quadrilateral.
* \(\mathcal F_6(H)\) has \(192\) edges and thirteen connected components: nine isolated vertices, three components of size \(18\), and one component of size \(57\).
* \(\mathcal F_8(H)\) has \(414\) edges and is connected, with radius \(4\) and diameter exactly \(6\). The eccentricity distribution is \(72\) vertices of eccentricity \(4\), \(42\) of eccentricity \(5\), and \(6\) of eccentricity \(6\).

Therefore any two Nauru perfect matchings are joined by at most six *octagon-only* flips, some require exactly six, and hexagon-only flips do not connect the configuration space. The known number \(120\) of perfect matchings is a baseline, not part of the novelty claim.

## Assumptions and scope

Write the vertex set as \(\{u_i,v_i:i\in\mathbb Z/12\mathbb Z\}\), with undirected edges
\[
\{u_i,u_{i+1}\},\quad \{u_i,v_i\},\quad \{v_i,v_{i+5}\}
\qquad (i\in\mathbb Z/12\mathbb Z).
\]
The indices are reduced modulo \(12\). Every vertex has degree \(3\), and the resulting graph is simple, connected, bipartite and has \(24\) vertices and \(36\) edges. A perfect matching consists of \(12\) pairwise disjoint edges covering all \(24\) vertices. Graph distance in \(\mathcal F_8(H)\) counts octagon-only flips, not unrestricted alternating-cycle moves. There is no claim about a general family of generalized Petersen graphs.

## Proof

**Lemma 1 (complete matching enumeration).** Fix any total order of the vertices. Recursively take the least uncovered vertex, try every incident edge to a still-uncovered neighbor, and mark both endpoints covered. At a leaf all vertices are covered. Every output is a perfect matching. Conversely, any perfect matching contains exactly one edge incident to the least uncovered vertex, so induction on the uncovered set shows that the recursion visits that matching exactly once. On the explicit \(36\)-edge graph above, the fully specified recurrence in either `verify.py` or `verify_alt.cpp` has exactly \(120\) leaves (distinct perfect matchings).

**Lemma 2 (complete move characterization).** If \(M\) and \(N\) are perfect matchings, each vertex in \(M\mathbin{\triangle}N\) has degree either zero or two, and its nontrivial components are vertex-disjoint, even, \(M\)-alternating cycles. Thus \(M,N\) differ by one legal \(\ell\)-flip if and only if their symmetric difference has exactly \(\ell\) edges and is connected on its nonisolated vertices. Conversely, for any simple \(\ell\)-cycle with exactly \(\ell/2\) edges in \(M\), disjointness of matching edges forces these edges to alternate; \(M\mathbin{\triangle}C\) is then another perfect matching. These two tests are equivalent and exhaustive.

**Lemma 3 (finite transition census).** A simple-cycle depth-first enumeration using the least cycle vertex as root and one of the two traversal orientations counts no four-cycles, exactly \(12\) hexagons and exactly \(54\) octagons. For each of the \(120\) matchings, testing all these cycles using Lemma 2 produces respectively \(0\), \(192\) and \(414\) undirected flip edges. Flood-fill of the complete hexagon graph yields components with sizes \(1\) (nine times), \(18\) (three times), and \(57\) (once). Flood-fill of the complete octagon graph visits all \(120\) vertices. Breadth-first search from each of its \(120\) states gives eccentricities \(4\) (\(72\) times), \(5\) (\(42\) times), and \(6\) (\(6\) times). The attached programs perform all finite steps, make these comparisons as hard assertions, and fail if any count differs.

The enumeration of cycles in the first implementation is independent of the enumeration of **matching pairs** in the second. The latter compares every one of the \(\binom{120}{2}=7140\) unordered matching pairs, checks that the symmetric difference consists of a *single* cycle of the given length, and rebuilds the same transition graphs without using a list of graph cycles. Both algorithms include every possible matching and every possible legal move, by Lemmas 1 and 2. They agree on all component and distance claims. In particular the octagon graph's eccentricity-six vertices give lower-bound witnesses, while connectivity and maximum eccentricity six give the upper bound. This proves the theorem.

## Verification

Run `python3 verify.py` and, independently, `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt` in a directory containing the two supplied files. The Python program enumerates simple cycles and flips each matching along matching-alternating cycles. The C++ program instead enumerates every unordered matching pair and inspects its symmetric difference. Both test the zero four-cycle layer, the full hexagon component census, the octagon connectivity, and all \(120\) octagon eccentricities. They return `ALL_VERIFY_OK` and `INDEPENDENT_VERIFY_OK` respectively. `VERIFICATION.md` records observed check outputs and exact limits.

## Relationship to prior work

Csikvári studied the number of perfect matchings in vertex-transitive bipartite graphs; this supplies archival context for the canonical cubic bipartite example, but not its fixed-cycle exchange geometry. Ito, Kakimura, Kamiyama, Kobayashi and Okamoto studied shortest perfect-matching reconfiguration when **any** alternating cycle may be flipped. Their unrestricted adjacency does not imply fixed-length octagon connectivity, its sharp six-to-eight threshold, or a length-eight distance bound. Bonamy and coauthors studied alternating **quadrilateral** flips; the Nauru graph has no quadrilaterals, making that model edgeless here. A separate exact Nauru anti-forcing and two-factor census already establishes the \(120\) baseline and matching structural statistics, but does not state or imply the thirteen hexagon components or the octagon-flip metric without a further exchange-graph analysis.

## Limitations

This is an exact finite-graph statement proved by exhaustive enumeration with transparent completeness arguments, not an infinite-family theorem. The eccentricity and component claims depend on the executions of the included self-contained verifiers; no formal proof-assistant certificate or independent scholarly audit is claimed. Literature outside the inspected, accessible sources could contain an equivalent result under another graph name or flip convention. In particular **octagon-only** flips must not be conflated with flips of *up to* eight edges or unrestricted alternating-cycle flips.

## References

1. P. Csikvári, *Matchings in vertex-transitive bipartite graphs*, arXiv:1407.5409, publicly available 2014-07-21, https://arxiv.org/abs/1407.5409 (archival primary source; primary 2010 MSC 05C35).
2. T. Ito, N. Kakimura, N. Kamiyama, Y. Kobayashi and Y. Okamoto, *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*, arXiv:1907.01700, https://arxiv.org/abs/1907.01700.
3. M. Bonamy, N. Bousquet, M. Heinrich, T. Ito, Y. Kobayashi, A. Mary, M. Mühlenthaler and K. Wasa, *The Perfect Matching Reconfiguration Problem*, arXiv:1904.06184, https://arxiv.org/abs/1904.06184.
4. E. W. Weisstein, *Nauru Graph*, MathWorld, https://mathworld.wolfram.com/NauruGraph.html (graph aliases and defining parameters, not exchange statistics).
