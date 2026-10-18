# Scientific review

## Correctness — PASS

The fully labeled twenty-vertex cubic graph and legal move are specified without external conventions. Two independent exhaustive perfect-matching generators each produce 36 states; one builds all 630 pairwise symmetric differences, while the other enumerates all 30 simple octagons and toggles them directly. Both independently determine the same 120 transitions and the same SHA-256 graph fingerprint. Breadth-first search and Floyd–Warshall separately recover all distances. A full complement two-factor calculation, rather than a mere degree correlation, establishes the thirty Hamiltonian and six \((5,5,10)\) types and their identical distance distributions, neighbour relations, and ten-cycle induced neighbourhoods. Both programs run without nonstandard libraries; their actual outputs and complete state certificate accompany this result. Because the enumeration is exhaustive for a fixed finite graph, it proves these finite facts but no claim for other graphs.

## Originality — PASS with residual risk

The 36 perfect matchings and six-versus-thirty decomposition are known, notably in Fujita (2013) and in a 2015 discussion, and are expressly excluded as independent novelty claims. The earlier fullerene paper arXiv:0801.1483 treats alternating **hexagons**, nonexistent here. The full arXiv:1907.01700 preprint defines unrestricted alternating-cycle moves and proves algorithmic results rather than the dodecahedron's octagonal-only diameter or graph structure. Aluoch's bipartite-resonance conclusions depend on cycle independence and width hypotheses that the whole octagonal cycle family does not satisfy. Targeted searches under exact and equivalent terms, together with comparisons against mathematical record entries and accessible historical claims, yielded no dominating statement. This is a best-knowledge originality conclusion, not proof that no unindexed equivalent exists.

## Value — PASS

The dodecahedron is the minimal all-pentagon fullerene, where ordinary hexagonal resonance is empty. Replacing face flips with the **shortest even perimeter naturally available** (two adjacent pentagons) is a motivated generalization rather than an arbitrary subset. It is nontrivial that every Kekulé matching lies in one component with diameter three, and the six-versus-thirty state-type split has a concrete local structural explanation through the ten-cycle neighbourhoods and common-neighbour multiplicity. These exact benchmarks may guide investigations of shortest even-cycle resonance on other non-bipartite polyhedral graphs. Their finite scope is explicit; no broader theorem is claimed.

## Closest literature and remaining limits

Ye–Qi–Zhang, arXiv:0801.1483: hexagonal-face resonance only. Fujita, MATCH 69 (2013) 333–354: count of matchings only. Ito et al., arXiv:1907.01700: unrestricted alternating-cycle shortest reconfiguration. Aluoch (2019): dependent-cycle and width assumptions differ. The exact current graph is computed, not symbolically classified as a member of an infinite family; publication-priority risks from inaccessible or unindexed material remain.

Self-review: passed. Independent audit: not yet performed.
