# Independent mathematical audit

## correctness

PASS

PASS. In the incidence poset, a graph vertex is an up beat point exactly when it has degree one; an edge with both endpoints present has a two-point incomparable lower set and is not down beat. Deleting a leaf vertex makes its unique incident edge a down beat point, so the paired deletion exactly realizes one graph leaf-pruning step. Iteration leaves the incidence poset of each cyclic component's graph 2-core and one isolated point from each tree component. The surviving 2-core vertices have degree at least two, surviving edges have two incomparable endpoints, and isolated points have no strict upper/lower set, so the result has no beat points. Stong core uniqueness gives the homotopy classification, and a poset isomorphism of nontrivial incidence components preserves minimal vertices, maximal edges and incidence, hence recovers the simple graph. The exhaustive n<=6 replay is corroborative only.

## originality

PASS

PASS. Standard Stong theory gives beat-point reduction and uniqueness of the core, while Barmak--Minian study smallest finite models of graph homotopy types. The closest same-object 2024 paper explicitly defines graph incidence posets and arranges minimum graph degree at least two so the associated finite spaces are minimal, but its inspected full text does not state arbitrary leaf pruning, identify the core with the graph 2-core, or give the iff classification by C2(G) plus the number of tree components. A Resultary query for incidence-poset/2-core classification returned the audited record as the only direct match; neighboring Stong-core records concern different constructions.

## value

PASS

PASS. This is a natural complete classification for a standard graph-to-finite-space construction. It identifies a canonical, efficiently computable graph invariant exactly with the Stong core, distinguishes finite-space homotopy from weak graph homotopy, and gives an immediate decision criterion. Although the local beat-point moves are elementary, the all-graph core formula and classification are structurally reusable rather than a textbook one-line deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
