# Scientific review

## Correctness
PASS. Proved the private-coordinate lemma, the multigraph reduction (including parallels) and three-vertex cover from the full hit trace. All seven-edge multigraphs with such a cover are encoded by three core multiplicities and a multiset of 3-coordinate peripheral vectors. The standalone exhaustive verifier enumerates 9,177 profiles (independently re-counted by a coefficient formula), finds at most 124 of the 128 hit traces, and checks explicit witnesses for ranks 1–6. A separate size proof gives the sharp ground-size onsets. Verified script execution completed successfully.

## Originality
PASS. Originality checks compared the exact Kneser disjointness adjacency with Johnson/Hamming adjacency results, general closed-neighborhood VC algorithms, and recent SRG classifications. Neither these primary papers nor the closest published search results entail the full rank-three open-neighborhood step function or its complete seven-edge obstruction. Searches are limited; specialized unindexed coverage remains a residual risk.

The closest primary sources are the original 2020 Johnson/Hamming VC paper and the 2024 generic graph VC algorithm; neither states the Kneser rank-three open-neighborhood step function. The 2026 strongly regular graph work has a different graph class. Unindexed overlap remains possible.

## Value
PASS. The edge relation on a natural fixed-rank class of distance-regular Kneser graphs has a complete exact finite-VC profile with a nontrivial sharp onset at 13. This complements known Johnson/Hamming structural-tameness results while distinguishing disjointness adjacency (maximum six) from Johnson adjacency (maximum four); it replaces only-instance computation by a universal exhaustive obstruction and explicit witnesses, directly relevant to VC-based learning/sample bounds and finite model-theoretic dependence.

## Limitations
Only open neighborhoods of rank-three Kneser graphs; the sharp global upper bound uses an independently replayable complete finite obstruction computation. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
