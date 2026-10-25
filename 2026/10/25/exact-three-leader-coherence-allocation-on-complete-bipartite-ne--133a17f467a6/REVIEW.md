# Review of exact three-leader allocation on complete bipartite networks

## Correctness — PASS

The stated domain is the unit-conductance complete bipartite graph with part sizes \(2\le p\le q\), three distinct noise-free leaders, and objective \(\operatorname{tr}(L_{FF}^{-1})\). The follower-block spectral decomposition supplies the complete objective for all four feasible leader allocations, including cases in which a follower group is empty. Exact rational differences reduce their ordering to the four displayed inequalities. The factorized cases \(p=2,3,4,5\) and the negative-coefficient proof for \(p\ge6\) exhaust all integer boundaries. A standalone checker confirms symbolic identities and computes 1,876 direct grounded inverses with exact rational arithmetic. No finite computation substitutes for the exhaustive algebraic proof.

## Originality — PASS, with residual risk

Clark, Bushnell and Poovendran (arXiv:1208.0946, 2012) give general leader-selection algorithms based on supermodularity, but no exact complete-bipartite three-leader allocation table. Fitch and Leonard (arXiv:1407.1569, 2014) give the directly relevant noise-free joint-centrality characterization for arbitrary graphs and explicit leader locations on cycles and paths. The general characterization is acknowledged as prior work; it does not itself give the new strict and tied integer allocations across all complete bipartite part sizes. Searches under bipartite coherence, joint centrality, inverse grounded Laplacian, and three-leader placement did not identify an explicit stronger classification. That absence is not proof of novelty, and specialized sources not indexed or accessed remain a risk.

## Value — PASS

The exact three-leader budget is a natural discrete control-design constraint on a fundamental two-population network. The classification reveals a structural change at smaller-part size six: at large imbalance, all three leaders belong to that smaller part for sizes at least six, but only two do for sizes three through five. It identifies every optimizer, not just the minimum score, and resolves nontrivial finite equality boundaries, including the tie at \((p,q)=(5,30)\). A high-degree-only heuristic can be suboptimal on the smallest imbalanced graphs. These are placement decisions, not arbitrary graph labels or a known spectral table recomputation.

## Closest literature and scientific limits

1. A. Clark, L. Bushnell, and R. Poovendran, *A Supermodular Optimization Framework for Leader Selection under Link Noise in Linear Multi-Agent Systems*, arXiv:1208.0946 (2012). Link-noise model and general approximation framework differ from the exact node-noise classification here.
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (2014). Its general noise-free criterion is the closest prior mathematical coverage; its specialized explicit results are for path and cycle graphs, not this parameter-family classification.

No conclusion concerns edge-weight variation, heterogeneous noise, directed graphs, noisy leaders, a different number of leaders, or optimizing an extreme grounded eigenvalue. Indexed-search incompleteness and possible undiscovered specialized coverage remain originality risks.

Self-review: passed. Independent audit: not yet performed.
