# Same-model review

## Correctness — PASS
The finite claim is reconstructed from definitions. `verify.py` enumerates all \(120\) permutations, builds the distance-at-least-three compatibility graph, exhausts every maximal clique, and checks the complete \(240\)-element stated symmetry action. It obtains maximum size \(10\), exactly \(192\) maxima, and orbit sizes \(24,48,120\) with stabilizers \(10,5,2\). The three pair-distance spectra are recomputed directly. The proof makes no claim about the full automorphism group.

## Originality — PASS
The exact numerical optimum \(10\) is prior work and is explicitly excluded from the novelty claim. The foundational 2009/2010 paper, the 2024 exact-bounds paper, the 2025 upper-bound paper, exact-parameter web searches, and published-finding corpus alias/equivalence searches were compared at the statement/implication level. The later theorem \(P(n,n-2)=10\) covers the size component but does not imply a count of all attaining subsets or their symmetry orbits. No inspected source stated the \(192\) count or the \(24,48,120\) decomposition. Residual risk remains from an unindexed finite census.

## Value — PASS
The case \(n=5\) is the natural smallest member of the exact family \(P(n,n-2)=10\), and a complete extremizer classification adds structural information beyond the known optimum. Three inequivalent symmetry types with distinct distance spectra provide a compact base case for later structural or recursive work.

The main scientific limitation is finite scope: no classification for larger \(n\) is claimed, and only the explicit natural \(240\)-element isometry subgroup is used.

Same-model review: passed. Independent audit: not yet performed.
