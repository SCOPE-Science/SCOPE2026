# Self-review: odd-cycle reduced-magic capacity

## Correctness — PASS

The quantum/Pauli hypotheses and the reduced affine-norm definition are explicit. The binary adjacency kernel is one-dimensional because odd-cycle two-step recurrence forces constant vectors, excluding product dependencies in every commuting context. The odd-cycle stable-set description is proved by examining positive-coordinate vertices and path faces; its gauge exactly equals the signed-affine minimum \(\ell_1\)-norm up to the floor one. The pair uncertainty bound is attained. The free-fermion step is justified on **both** central sectors by symplectic quotient reduction, and odd-cycle gauge invariance of the skew spectrum supplies the same cotangent maximum for all sign patterns. Strict concavity and two exact endpoint inequalities pin down the transition at \(C_{11}\). Actual packaged symbolic, matrix and LP checks corroborate these steps; finite checks do not prove the infinite-length result.

## Originality — PASS, residual priority risk

Closest source [1], arXiv:2607.26154v1, gives the framework and a \(\sqrt\omega\) capacity theorem only for perfect frustration graphs. The present odd cycles are minimally nonperfect, and the extra facet gives capacity greater than \(\sqrt2\) for exactly three lengths. Source [2], arXiv:2511.13531v1, supplies classical odd-hole facets and quantum **quadratic** squared-expectation bounds but not the present absolute-value resource capacity. Source [3], arXiv:2305.15625v1, implies the free-fermion solvability mechanism, not the combined reduced-magic theorem or witness crossover. Source [4], arXiv:2602.18939v1, provides the projected-magic definition. The graph/polytope and fermion ingredients are credited; the precise combined all-length sharp capacity and threshold were not identified by the searches or full-text comparisons. Residual risk: an unindexed combination of existing results could imply the complete result; independent literature priority is unverified.

## Value — PASS

The first nonperfect forbidden induced subgraphs of the perfect-graph approach are odd holes. A sharp closed reduced-resource value for every state and a **finite, exact transition** between qualitatively different optimal witnesses directly answer what that approach leaves open on this minimal family. The result supplies measurement-design limits and a constructive family of attaining states across all cycle lengths. It does not assert a paper-sized advance or a full-state resource computation.

## Sources and boundaries

Primary: Liu et al., https://arxiv.org/html/2607.26154v1 (Results and Appendix B); Xu et al., https://arxiv.org/html/2511.13531v1 (classical facets, Theorem 2 and Appendix A.1); Chapman--Elman--Mann, https://arxiv.org/html/2305.15625v1 (generalized Jordan--Wigner mapping and cycle symmetries); Varela et al., https://arxiv.org/html/2602.18939v1 (Section III). Remaining scientific risks are priority through indirect combinations, and any overlooked Pauli-algebra subtlety in representing central sectors. The explicitly documented elementary central-sector argument avoids treating a numerical diagonalization as proof. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
