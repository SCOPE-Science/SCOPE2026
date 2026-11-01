# Scientific review

## Correctness — PASS
For a primitive two-cycle, the two firing-indicator vectors sum to a constant by the connected graph Laplacian kernel. Nonfixed cycles force complementary firing vectors. At every vertex the first-step chip interval is exactly of length equal to its cross-cut degree; the independent offsets sum to the stated energy polynomial, and passing from the two colorings to the unoriented cut divides the state count by two. The maximum-cut endpoints and their coefficients follow from positivity and the fact that every maximum cut gives positive cross-degree at every vertex. The tree recursion and Pell specialization are derived algebraically. The supplied verifier independently enumerates 1,821,396 full configurations across 72 finite graphs, and validates both polynomial counts and extreme-energy identities. Its outputs do not replace the general proof.

## Originality — PASS, qualified
The closest general published antecedent is Jiang (arXiv:1003.0943, Proposition 2.5), proving equal per-vertex firing counts in a periodic orbit, rather than an exact state/orbit count. Jiang–Scully–Zhang (arXiv:1211.6786, especially Sections 6–7) characterize possible firing words and tree-like behavior but do not present the unrestricted energy-resolved cut polynomial or maximum-cut orbit threshold. Bitar–Goles (1992) prove the tree period bound; its full text was inaccessible and historical coverage is a specific residual risk. Later results about a middle energy band concern eventual periods, not the exact distribution of primitive two-cycle orbits. Searches for cut-degree products, MAX-CUT energy thresholds, Pell path counts, and equivalent counting statements disclosed no dominating formula in accessible materials. Earlier special-family enumerations cannot imply this all-graph result by themselves.

## Value — PASS
This theorem connects a recurrent-state count in a deterministic dynamics to a canonical optimization invariant of its interaction graph. The exact first and last accessible conserved totals and the multiplicity of extremal orbits become MAX-CUT and maximum-cut counts; the natural low-energy existence problem is NP-complete. The exact cut polynomial supplies all energy shells on arbitrary graphs, and an efficient tree evaluation yields a nontrivial Pell sequence for paths. This goes beyond classifying permitted periods or collecting computational cases.

## Limitations and closest literature
The 1992 source was accessible only through bibliographic data and abstract despite open-access searching; institutional full text could not be obtained. Unindexed equivalent formulations remain possible. The 2026 middle-stair paper was compared at theorem/abstract level rather than treated as a full-text exclusion. Only primitive period-two orbits are counted, and no independent external validation has been conducted.

Self-review: passed. Independent audit: not yet performed.
