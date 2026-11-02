# Review

## Correctness

PASS. The graph automorphism average preserves specified values while convexly reducing the operator norm. The hub and outer-pair cases follow from explicit rank-two/rank-three reductions. The hub–outer case reduces to a real skew four-dimensional commutator with explicit Hilbert–Schmidt half-norm and Pfaffian; the singular-value identity determines the norm, and coercivity ensures the minimum is attained. The induced-subgraph comparison proves monotonicity. Lower and upper column bounds with the explicit \(b=1-t^{-1/4}\) witness prove the sharp \(m^{-1/2}\) correction and the stated error. Finite matrix comparisons and optimization checkpoints pass; they do not substitute for the proof.

## Originality

PASS, with literature risk. The available full primary text of Besnard 2021 gives general estimates and prunings rather than the book family; Clare–Li–Poon–Swartz 2024 derives complete formulas for paths and graph-specific background; Swartz 2026 treats general edge deletion without the sharp formula. Nearby exact results on complete bipartite and vertex-glued friendship graphs do not imply the edge-glued book result, because commutator-norm behavior changes with the added central edge. Independent equivalent formulations, including small-graph tables and alternative matrix dualities, have not been exhaustively excluded.

## Mathematical value

PASS. Book graphs are the canonical infinitely many-triangles-sharing-an-edge family. The result completely determines two metric orbits, reduces the third by exact singular invariants, and proves a sharp asymptotic separation of three natural pair types. The fixed-parameter extremum is an exact natural invariant, not an arbitrary data slice; the asymptotic first correction is proved quantitatively, not observed numerically.

## Closest literature and limitations

Besnard, arXiv:2105.09056; Clare–Li–Poon–Swartz, arXiv:2409.04146; Swartz, arXiv:2610.07718. No elementary closed expression for the finite hub–outer minimizing pair is claimed. An equivalent older formulation in spectral triples or four-by-four skew norm optimization remains possible. Independent validation is absent.

Self-review: passed. Independent audit: not yet performed.
