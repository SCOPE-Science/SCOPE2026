# Square-switch components of perfect matchings of the five-cube

## Finding

Let \(Q_5\) be the graph on binary words of length five, where an edge changes exactly one coordinate. Let \(\mathcal F_4(Q_5)\) have one vertex for every perfect matching of \(Q_5\); two matchings are adjacent precisely when their symmetric difference is the four edges of a square of \(Q_5\). This move is an **alternating-square flip**, not an unrestricted alternating-even-cycle flip.

There are \(589{,}185\) matchings, a previously known static count. The new exact square-flip component census is

\[
\mathcal F_4(Q_5)\cong 120K_1\;\sqcup\;80C_4\;\sqcup\;G_{99{,}280}\;\sqcup\;G_{489{,}465},
\]

where \(G_{99{,}280}\) and \(G_{489{,}465}\) denote **connected** graphs of the displayed orders (not specified by further isomorphism classifications). The reconfiguration graph has exactly \(3{,}219{,}360\) edges and \(202\) connected components. The two large components have, respectively, \(359{,}680\) and \(2{,}859{,}360\) edges; each four-vertex component is a four-cycle. The \(120\) isolated matchings form one orbit under the coordinate-permutation/bit-translation automorphism group of \(Q_5\); the \(80\) four-cycle components also form one orbit. The reconfiguration graph is bipartite.

## Assumptions and scope

The vertex labels are the integers \(0,\ldots,31\), interpreted as five-bit words. The graph has \(80\) edges and \(80\) coordinate squares. A matching covers all \(32\) graph vertices, so contains exactly \(16\) edges. A square-flip replaces the two opposite matching edges of one coordinate square by its two other edges. Only four-edge symmetric differences are allowed. All counts are for **labeled** matchings; no symmetry quotient is taken when counting states or edges. The theorem concerns only the finite graph \(Q_5\); it makes no claim for arbitrary dimension.

## Proof

The proof is an exhaustive, fully specified finite enumeration, certified by the two complete standalone programs shipped with this result. The points establishing completeness are as follows.

1. Partition the graph into the \(16\) even-weight vertices \(E=(e_0,\ldots,e_{15})\) and the \(16\) odd-weight vertices \(O=(o_0,\ldots,o_{15})\). Every perfect matching is uniquely represented by a bijection \(p\colon\{0,\ldots,15\}\to\{0,\ldots,15\}\), with \(e_i\) joined to \(o_{p(i)}\), subject to the necessary and sufficient adjacency condition \(\operatorname{wt}(e_i\oplus o_{p(i)})=1\). The C++ verifier enumerates every such bijection by recursively assigning the next even vertex to every currently unused adjacent odd vertex. Thus **each perfect matching appears exactly once**. It obtains \(589{,}185\) distinct states.

2. A square-flip on one of these matchings necessarily interchanges exactly two odd partners \(p(i)\) and \(p(j)\). Conversely, if both cross edges \(e_i o_{p(j)}\) and \(e_j o_{p(i)}\) exist, the four edges on those two even and two odd vertices form an alternating four-cycle, so that interchange is a legal square-flip. Therefore testing each unordered pair of distinct even vertices and the two cross-adjacencies examines **every possible legal move**, with no false positives. The C++ verifier retrieves the swapped state, counts every undirected edge once, and unions its endpoints in an exact disjoint-set data structure.

3. Independently, the Python verifier represents a matching by an \(80\)-bit incidence vector of the actual cube edges. It enumerates all perfect matchings by pairing the smallest unmatched vertex with each of its still-unmatched neighbors. It explicitly constructs the \(80\) squares from coordinate pairs and tests whether exactly two of a square's edges belong to a matching. As these two edges are necessarily opposite, toggling the full square yields precisely a legal flip. This gives an independent exhaustive construction of all states and all reconfiguration edges, with another exact component computation.

4. Both algorithms return the following table. In the third column, edge counts are summed over **all components** of the specified size, rather than per component.

| Component order | Number of components | Edges in these components |
| ---: | ---: | ---: |
| \(1\) | \(120\) | \(0\) |
| \(4\) | \(80\) | \(320\) |
| \(99{,}280\) | \(1\) | \(359{,}680\) |
| \(489{,}465\) | \(1\) | \(2{,}859{,}360\) |

The sizes sum to \(589{,}185\), and the edge counts sum to \(3{,}219{,}360\). Every vertex in every four-vertex component has degree two. A connected simple graph on four vertices with degree two at every vertex is \(C_4\).

5. For the orbit statements, every cube automorphism used by the Python program has the form \(v\mapsto\pi(v)\oplus a\), for a coordinate permutation \(\pi\in S_5\) and a translation \(a\in\{0,1\}^5\). All \(5!\cdot 2^5=3840\) such actions are applied to a representative frozen matching and a representative four-state component. The first orbit equals exactly the full set of \(120\) frozen matchings; the second equals exactly the set of \(80\) four-state components. These assertions are tested against the entire enumerated graph, not samples.

6. Every square-flip transposes two odd partners in the perfect-matching bijection. Therefore the sign of the bijection changes at every flip, providing a proper bipartition of \(\mathcal F_4(Q_5)\).

Each algorithm uses only integer arithmetic, finite loops/recursions, exact adjacency predicates, and disjoint-set reachability. There are no randomized steps, approximate comparisons, or imposed cutoffs. The exhaustive algorithms, together with the arguments proving complete state and move enumeration, establish the stated finite theorem.

## Verification

Run from the directory containing the embedded source files:

```sh
g++ -O3 -std=c++17 q5_verify_cpp.cpp -o q5_verify_cpp
./q5_verify_cpp
python3 q5_verify_python.py
```

The C++ program asserts the state count, exact flip-edge count, component multiplicities, edges in each component size, and degree-two condition for every four-state component. The Python program uses a different state encoding and independent flip implementation; it asserts the same component census and total edges, degree conditions, and the two automorphism orbits. Expected success markers are `Q5_BIPARTITE_PARTNER_EXHAUSTIVE_PASS`, `Q5_202_COMPONENTS_AND_EXACT_EDGES_PASS`, `Q5_INDEPENDENT_80_EDGE_BITSET_EXHAUSTIVE_PASS`, and `Q5_SYMMETRY_ORBITS_FROZEN_AND_FOUR_CYCLE_COMPONENTS_PASS`.

## Relationship to prior work

Graham and Harary (1988) and Östergård and Pettersson (first published 21 November 2012) established static perfect-matching enumeration on hypercubes, so the total \(589{,}185\) is background, not new. Bonamy and coauthors (2019) study perfect-matching reconfiguration by alternating four-cycle flips on general graphs, but their inspected general results do not determine these five-cube component counts. Klivans and Saldanha (2022) develop an invariant for square flips in higher-dimensional domino tilings and classify the four-dimensional unit-cube example as \(264\) plus eight isolated matchings; their higher-dimensional results involve stabilized extensions and asymptotic two-giant-component behavior, not these exact five-cube counts. Hartarsky, Lichev and Toninelli (2023/2024) study local dimers on unit hypercubes and prove connectivity when moves include alternating cycles of lengths up to \(4d-4\) in dimension \(d\). That is strictly more permissive than square-only switches and does not determine their component partition. Fink (2009) studies a matching graph that joins matchings when their union is a Hamiltonian cycle, a different operation. The \(Q_4\) matching-flip enumeration and frozen-state lower bounds for higher dimensions cannot imply the exact \(Q_5\) census. The distinct proposed contribution is the square-only component census and its frozen-state and component-orbit structure for \(Q_5\).

## Limitations

The classification is computationally exhaustive and reproducible, rather than a short closed-form structural classification of the two large connected graphs. No statement about dimensions above five, shortest path distances within large components, or polynomial-time reconfiguration algorithms is proved. The 2012 perfect-matching enumeration article was available only as abstract/metadata during the comparison, leaving a residual possibility that its inaccessible full text or other historical material contains a related square-flip census. An independent scholarly audit has not been conducted.

## References

- N. Graham and F. Harary, *The number of perfect matchings in a hypercube*, Applied Mathematics Letters **1** (1988), 45–48.
- P. R. J. Östergård and V. H. Pettersson, *Enumerating Perfect Matchings in n-Cubes*, Order **30** (2013), 821–835; first published 21 November 2012; DOI: `10.1007/s11083-012-9279-8`.
- M. Bonamy et al., *The Perfect Matching Reconfiguration Problem*, MFCS (2019), DOI: `10.4230/LIPIcs.MFCS.2019.80`; open preprint `arXiv:1904.06184`.
- C. J. Klivans and N. C. Saldanha, *Domino tilings and flips in dimensions 4 and higher*, Algebraic Combinatorics **5** (2022), 163–185; DOI: `10.5802/alco.205`; open `arXiv:2007.08474`.
- I. Hartarsky, L. Lichev and F. Toninelli, *Local dimer dynamics in higher dimensions*, `arXiv:2304.10930` (2023; revised 2024).
- J. Fink, *Connectivity of Matching Graph of Hypercube*, SIAM Journal on Discrete Mathematics **23** (2009); DOI: `10.1137/070697288` (Hamiltonian-union adjacency).
- T. Mütze, *Combinatorial Gray Codes—An Updated Survey*, Electronic Journal of Combinatorics, Dynamic Surveys DS26 (first published 2023; revised 2024), DOI: `10.37236/11023`; section on matchings and alternating-cycle flips (the more permissive operation).
