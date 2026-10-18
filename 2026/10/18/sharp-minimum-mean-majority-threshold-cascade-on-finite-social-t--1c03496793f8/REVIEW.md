# Self-review

## Correctness — PASS

The propagation lemma is exact because the active set remains connected and an unseeded vertex of degree at least three can be adjacent to at most one active vertex while inactive. This proves the component sum \(S=|H|+\sum_j(m_j^2+b_jm_j)\), not just an empirical pattern. Both lower bounds and their equality conditions follow from positive integer component sizes, positive boundary counts and the tree degree sum. The explicit leaf-attachment construction realizes the degree signatures for every \(n\ge4\). The 984-tree replay checks the calculations, but only the general structural argument establishes the theorem for all orders.

## Originality — PASS, subject to bibliographic risk

Watts (2002) establishes the vulnerable-degree condition and random-network cascade questions; Gleeson–Cahalane (2007) computes ensemble-averaged cascade fractions; Whitney (2009) gives finite random-network dynamics; Pei et al. (2017) studies seed influence maximization. These are not equivalent to minimizing the uniform-seed expected final cascade among all exact-order trees, nor do their inspected results give the stated complete equality classification. One related published network-result search returned fixed-threshold influence and graph structural extremals, neither covering the theorem. The known vulnerable-vertex observation is essential background, not presented as new. A prior exact finite-tree optimization may nevertheless exist; novelty is assessed against the material actually inspected, not proved by unsuccessful searches.

## Mathematical value — PASS

An exact natural extremum over **all** connected tree-shaped contact networks answers a concrete design question: how little diffusion is unavoidable if the location of the sole initiating adopter is uniformly unknown? The complete minimizer classification exhibits a nontrivial topology difference—branching degree-three cores minimize average exposure, and a star generally does not. The sharp lower bound tends to \(3/2\) while a path permits full propagation. This goes beyond a computation for an arbitrary small graph or a degree-count exercise because it solves the dynamics for every tree and identifies all optimal network topologies.

## Limitations and evidence

The threshold convention is inclusive, the seed is uniform, the graph is a finite tree, and all adopters remain active. The finite script does not certify arbitrary orders. Other update rules, graph cycles and nonuniform recruitment are outside the theorem. Watts and Gleeson–Cahalane were available in full text and their model/results sections were inspected; Whitney's full-text model section and the relevant parts of Pei et al. were inspected. Related results may be overlooked, especially among threshold-vulnerability and tree cascade papers. Independent audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
