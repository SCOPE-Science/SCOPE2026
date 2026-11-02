# Self-review

## Correctness — PASS

The global rigidity proof uses the exact block matrix \(F_G\), observes \(F_G^3=0\iff (BB^{\mathsf T})B=0\), and shows that connectedness forces all columns of \(BB^{\mathsf T}\) identical; symmetry and an existing edge give \(J_n\), hence exactly even complete graphs. Independent rank arguments determine all Jordan blocks and the swapping periodic subsystem. Exact finite-field preimage sizes establish the orbit, basin, and entrance-time formulas for each admitted parameter, including \(n=2\) and odd \(n=3\). Two stand-alone checkers corroborate all stated finite instances. The proof, not exhaustive experiments, handles arbitrary orders and characteristic-two field sizes.

## Originality — PASS, with residual historical risk

The general finite-linear-dynamics framework in Moreno–Bollman–Aviño-Díaz does not state connected-subdivision extinction rigidity. Gadouleau–Richard's nilpotent Boolean-function existence results allow selecting a suitable function for a graph and so cannot imply the identity for a *fixed* open-neighbor sum map. Barrett et al. optimize matrix rank over admissible symmetric matrices, not all iterates of the prescribed adjacency matrix. The subdivision-corona spectra paper treats different graph operations and spectra. Direct research-record searches and accessible prior-claim comparisons identified no dominating result. The closest prior subdivision-Kneser and subdivision-complete-bipartite dynamical claims concern distinct base graphs; the latter overlaps only at the trivial complete-graph edge \(K_2\), not the all-connected-graph rigidity or odd-clique swap classification. Unindexed literature may contain a rediscovery; absence from search results does not prove novelty.

## Value — PASS

The rigidity theorem characterizes **all** connected simple base graphs admitting uniform extinction after three iterations under a fixed local linear rule, a structural statement rather than a selected example. The even/odd clique dichotomy gives exact Jordan decompositions, sharp extinction or entrance times, and every periodic orbit and attraction basin. It contrasts a rigid extinction class with exponentially many recurrent states under one-vertex changes of clique order, a meaningful relationship between graph structure and global dynamics.

## Closest literature, scientific limitations and remaining risk

Primary references [1]–[4] are compared in RESULT.md and in the structured review. Their full available passages were inspected at the methods or theorem level. The result is restricted to characteristic-two, unweighted zero-diagonal dynamics on ordinary edge subdivisions of connected simple graphs; it makes no statement for different update functions or general signed/weighted interactions. The documented historical-overlap risk requires independent expert evaluation.

Self-review: passed. Independent audit: not yet performed.
