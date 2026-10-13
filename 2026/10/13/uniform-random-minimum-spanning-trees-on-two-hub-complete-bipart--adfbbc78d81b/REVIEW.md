# Scientific review: uniform minimum spanning trees on two-hub complete bipartite graphs

## Correctness — PASS

Every spanning tree of \(K_{2,n}\) has one and only one doubled right-side vertex. For a fixed doubled vertex the minimizing tree chooses the lighter incident edge at each other vertex; its total weight equals the sum of all column minima plus the doubled vertex's column maximum. The review reconstructed the deterministic minimization and the one-to-one tree indexing, including the \(n=2\) boundary. For independent identically distributed atomless pairs the maxima are independent identically distributed, while the within-pair orientation signs are independent fair coins independent of all maxima. This yields the exact probability \(1/(n\,2^{n-1})\) for every tree and verifies the full range of quantifiers without asymptotics. The stated two-edge probabilities and covariances follow by conditioning on the unique doubled vertex.

The standalone checker enumerates all edge-order permutations for \(n=2,3,4\) and all \(9!\) permutations on \(K_{3,3}\), using exact integer counts and rational checks. This finite evidence is supplementary: the universal proof is the symmetry and deterministic-minimization argument, not extrapolation from finite experiments.

## Originality — PASS, with remaining priority risk

Tang and Zhang (arXiv:2605.01444, first posted 2026-05-02) prove results about pairwise edge correlations on \(K_n\) and mention sufficiently large balanced \(K_{n,n}\); their relevant full-text passages do not identify the exact tree law on \(K_{2,n}\). Gupta (arXiv:2608.06816; complete accessible source `paper/main.tex`, primary MSC2020 60C05) establishes a universal factor-eight correlation bound and strict pairwise negative correlation on \(K_n\), which do not imply equality of two random spanning-tree distributions. The 2021 paper by Albin and collaborators characterizes uniform-spanning-tree edge usage, a different random-tree sampling law.

Searches for both models' equality on \(K_{2,n}\), balanced biclique and theta-graph aliases, randomized Kruskal bases, and dominating more general distributional statements found no directly covering public result. A broader, older classification of graphs where random Kruskal spanning trees are uniform might already imply the result, and indexing gaps remain; these are substantive priority risks, not evidence of uniqueness.

## Value — PASS

This identifies an exact full probability law on an infinite family of **non-cactus**, multiply cyclic graphs, rather than merely proving another pairwise bound. It yields quantitative strict negative covariance for all edge pairs and provides a transparent, distribution-free benchmark for the 2026 question of how far random minimum spanning trees deviate from uniform spanning trees. The exact finite \(K_{3,3}\) counterexample demonstrates the coincidence is a structural phenomenon rather than a general consequence of bipartiteness. No broad graph classification, optimal global correlation factor, or new claim about \(K_{n,n}\) is asserted.

Self-review: passed. Independent audit: not yet performed.
