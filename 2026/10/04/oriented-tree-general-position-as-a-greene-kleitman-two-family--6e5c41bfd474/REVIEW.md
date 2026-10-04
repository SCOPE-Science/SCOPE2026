# Same-model review

## Correctness
PASS. Reachability is a partial order because an oriented tree is acyclic. A three-element reachability chain is exactly three vertices appearing in order on the unique directed tree path between the first and last vertices; uniqueness makes that path geodesic. Conversely, any directed geodesic containing three selected vertices supplies such a chain. Hence general-position sets are precisely two-families, and the Greene–Kleitman theorem at \(k=2\) proves the min–max equality. The embedded exhaustive verifier independently checks the three formulations on all labeled oriented trees through six vertices.

## Originality
PASS. The closest primary paper, arXiv:2604.15909, treats oriented-tree lower bounds and out-arborescences but explicitly asks for an arbitrary-tree formula in Problem 5.2. Full-text and alias searches did not locate a reachability-poset/two-family formulation. Greene–Kleitman (1976) supplies the classical poset min–max theorem but not the directed-general-position identification. Residual risk remains from unindexed or very recent independent work.

## Value
PASS. The result addresses a stated 2026 open direction for an entire graph class and gives an exact structural formula, rather than another special orientation or finite-order computation. The reduction also makes the large toolkit for finite-poset two-families and chain partitions immediately applicable to oriented-tree general position.

## Closest literature and limitations
The direct anchor is Chandran S. V. et al., arXiv:2604.15909 (17 April 2026), especially its tree section and Problem 5.2. Greene and Kleitman, JCTA 20 (1976), provide the supporting two-family min–max theorem; Cameron, European J. Combin. 7 (1986), provides the related acyclic-digraph path-partition extension. The resulting formula is a reachability-poset min–max characterization, not a closed formula in elementary tree statistics, and the proof does not extend unchanged to DAGs with shortcuts.

Same-model review: passed. Independent audit: not yet performed.
