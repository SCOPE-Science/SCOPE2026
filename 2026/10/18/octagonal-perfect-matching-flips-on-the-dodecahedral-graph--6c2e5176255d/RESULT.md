# Octagonal perfect-matching flips on the dodecahedral graph

## Finding

The twenty-vertex dodecahedral graph \(D=\operatorname{GP}(10,2)\) has a connected perfect-matching reconfiguration graph under **shortest-even-cycle flips**. Namely, let \(\mathcal R_8(D)\) have as vertices the perfect matchings of \(D\), with \(M\) adjacent to \(N\) exactly when their symmetric difference \(M\mathbin\triangle N\) consists of the eight edges of one simple eight-cycle. The precise numerical and structural conclusions are:

- The 36 matching configurations support exactly 120 distinct undirected flips, and \(\operatorname{rad}(\mathcal R_8(D))=\operatorname{diam}(\mathcal R_8(D))=3\). Every matching configuration has eccentricity three.
- Exactly six matchings have reconfiguration degree ten and complementary two-factor cycle lengths \((5,5,10)\); their distance-layer sizes, including the initial vertex, are \((1,10,15,10)\).
- The other thirty matchings have degree six and a single Hamiltonian complementary twenty-cycle; their distance-layer sizes are \((1,6,19,10)\).
- The six degree-ten configurations form an independent set. Every degree-six configuration is adjacent to exactly two of them, and each unordered pair of degree-ten configurations has exactly two common degree-six neighbours. The neighbours of each degree-ten configuration induce one ten-cycle.
- The graph has exactly 30 simple eight-cycles, each the boundary of a union of two edge-sharing pentagonal faces; precisely eight perfect matchings alternate around each such cycle. No simple six-cycle occurs, so eight is the **minimum possible length of an alternating even-cycle flip** in \(D\).

These conclusions describe the **octagon-restricted** reconfiguration graph, not the graph obtained by permitting arbitrary-length alternating cycles. The already-known total of 36 perfect matchings is not asserted to be new.

## Assumptions and scope

Use vertex labels \(0,\ldots,19\). For each \(i\in\mathbb Z/10\mathbb Z\), put an outer vertex \(u_i=i\) and an inner vertex \(v_i=10+i\). The thirty edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\) for all ten values of \(i\). This is the ordinary simple cubic dodecahedral graph \(\operatorname{GP}(10,2)\).

A perfect matching is a subset of ten graph edges incident exactly once at every vertex. A simple cycle is vertex-distinct except for its returning endpoint. A legal elementary flip exchanges exactly the four matching edges on an alternating simple eight-cycle with the four nonmatching edges on that cycle, retaining all other edges. All graph labels, the flip length, and the graph's single fixed order are part of the domain. No claim is made for arbitrary generalized Petersen graphs or other fullerenes.

## Proof

This is an exhaustive finite proof with a complete, executable enumeration certificate, rather than extrapolation from a bounded sample. Two independent reconstructions are supplied as `verify_pairwise.py` and `verify_faces.py`; their enumerated state and transition data are in `states_edges.json`.

**Step 1 (complete state set).** Starting with all twenty vertices unmatched, choose an unmatched vertex and branch over every still-unmatched neighbour as its unique matching partner. Repeat until no unmatched vertex remains. Every perfect matching follows exactly one branch at every step, and each terminal branch is a perfect matching. The first program chooses the smallest unmatched vertex; the second chooses a vertex with the fewest available neighbours and uses a distinct edge representation. Both generate exactly 36 distinct full matchings. Each program asserts these cardinalities and checks perfect incidence.

**Step 2 (all legal moves).** The first program considers every unordered pair of the 36 matchings (630 pairs). Their symmetric difference is a disjoint union of even cycles, found by traversing its degree-two components. Such a pair is adjacent exactly when this decomposition is the single length-eight cycle; this construction gives 120 edges. Independently, the second program enumerates all simple cycles of lengths five, six, and eight from the explicit 20-vertex adjacency lists. There are 12 pentagonal faces, no six-cycles, and 30 eight-cycles; the eight-cycles are exactly the symmetric differences of the boundaries of the 30 edge-sharing pairs of pentagonal faces. For each eight-cycle and each matching the second program tests whether it contains four mutually disjoint cycle edges, then toggles that cycle. Each eight-cycle is alternating for eight matchings; counting orientations gives \(30\cdot8/2=120\) undirected flips.

**Step 3 (independent all-pairs metrics).** The two programs canonically order matching edge bitmasks and their complete adjacency lists. They compute the same SHA-256 of this canonical binary-free JSON graph representation: `a70573c1719c0680ca78fc3919e5fc78b77a442c557fc17916c5968f7b23790c`. One computes 36 breadth-first searches; the other uses all-pairs Floyd–Warshall relaxation on the independently constructed graph. Both show that every target is reachable in at most three moves, and that every source has at least one target at distance three. Each independently verifies the exact layer arrays for the two degree classes.

**Step 4 (fine structure).** Because \(D\) is cubic, the complement of each ten-edge perfect matching is a spanning two-regular graph. Explicit degree-two component traversal partitions the complement types into thirty Hamiltonian \((20)\) cycles and six \((5,5,10)\) decompositions, perfectly matching the degree-six and degree-ten vertices of the flip graph. Direct adjacency checks on the full certificate establish that the latter six are independent, that each other vertex has exactly two such neighbours, and that any two of the six have exactly two common neighbours. For each distinguished vertex, the induced graph on its ten neighbours is verified two-regular and connected; hence it is one \(C_{10}\). No inference from numerical graph fingerprints alone is used: both programs explicitly test these assertions on their independently generated edge sets.

The exhaustiveness of the branch tree, the simple-cycle depth-first search, the 630 unordered matching-pair comparisons, and the exhaustive finite graph-distance algorithms jointly prove every quantified conclusion for this labeled graph. No probabilistic sampling, optimization timeout, or unverified extrapolation occurs.

## Verification

Run with a standard Python 3 interpreter, requiring no third-party modules:

```
python3 verify_pairwise.py
python3 verify_faces.py
```

Both commands must finish with `"status": "VERIFY_OK"`. The exact reference outputs are `output_pairwise.txt` and `output_faces.txt`. Both programs compute the same full graph certificate fingerprint `a70573c1719c0680ca78fc3919e5fc78b77a442c557fc17916c5968f7b23790c`. The standalone `states_edges.json` lists all 30 graph edges, 36 matching masks, and every neighbour index, so all edge transitions and shortest distances can be reconstructed without relying on an opaque executable or a previously published table. Inspect and run the embedded files as a single directory.

## Relationship to prior work

Ye, Qi, and Zhang's paper on fullerene resonance (first publicly submitted as arXiv:0801.1483 on 2008-01-09) addresses *hexagonal-face* resonance, a natural operation that provides no moves on the all-pentagon dodecahedron. This motivates using the boundaries of two neighbouring pentagons as the shortest available even cycles. Fujita's exact dodecahedral matching enumeration gives the total 36, which is background rather than a novelty claim. The 2015 mathematical discussion of this count also separates the six exceptional matchings from the other thirty without determining octagonal-flip transitions.

Ito and collaborators study transformations along **unrestricted** alternating cycles and general complexity; their connectivity observation does not establish connectivity under eight-cycle restrictions, and their shortest distances are for a different graph. Aluoch studies resonance graphs under cycle-independence and width restrictions, yielding bipartite graphs. The collection of all thirty eight-cycles here is dependent in cycle space, and the resulting graph has triangles, so those special conclusions do not apply. None of these inspected sources identifies the exact dodecahedral octagonal flip graph or its degree, distance, and ten-cycle-neighbourhood structure.

## Limitations

This is a single, canonical finite graph. The proof is exhaustive and reproducible for this graph only; it does not establish an infinite-family classification. The known count of 36 matchings and the six-versus-thirty complement split are not new claims on their own. Historical publication coverage is not guaranteed: equivalent work in unindexed sources or supplementary tables could exist.

## References

1. D. Ye, Z. Qi, and H. Zhang, *On k-Resonant Fullerene Graphs*, arXiv:0801.1483 (first version publicly submitted 2008-01-09); SIAM Journal on Discrete Mathematics 23 (2009), 1023–1044, DOI: 10.1137/080712763.
2. S. Fujita, *Restricted Enumerations ... Enumeration of Kekulé Structures and Perfect Matchings of Graphs*, MATCH Communications in Mathematical and in Computer Chemistry 69 (2013), 333–354; https://match.pmf.kg.ac.rs/electronic_versions/Match69/n2/match69n2_333-354.pdf.
3. *Number of perfect matchings of the Dodecahedron*, MathOverflow question 192159 and answers (2015-01-05 onward), https://mathoverflow.net/questions/192159/number-of-perfect-matchings-of-the-dodecahedron.
4. T. Ito, N. Kakimura, N. Kamiyama, Y. Kobayashi, and Y. Okamoto, *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*, arXiv:1907.01700 (2019).
5. J. Aluoch, *Resonance Graph of Perfect Matchings*, master's thesis, Middle Tennessee State University (2019), https://jewlscholar.mtsu.edu/items/68c98b53-6ec9-40cd-91c2-a9f6dfdce27a.
