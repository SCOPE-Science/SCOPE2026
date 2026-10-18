# Scientific review: Poisson extreme-edge support-loss limit

## Correctness — PASS

The geometry is normalized in the ambient \((n-1)\)-dimensional zero-sum Euclidean subspace, and the central symmetry factor of two is explicit. For every deterministic distinct-coordinate score vector, exactly \(N_n(s;z)\) edges can prevent support loss exceeding \(s\); Bernoulli independence gives its exact conditional tail. Joint upper/lower Gaussian extremal point-process convergence yields the two independent intensity-\(e^{-x}\) Poisson processes and their random bipartite edge marks. A uniform second-moment spacing bound, using the exponential-transform representation of normal order statistics and geometric first-edge domination, proves uniform integrability. The resulting mean limit, radial normalization, sharp endpoints, and finite atom have each been checked against their quantifiers and boundaries. Exact rational conditional-tail and mean identities were tested on 1,096 graphs over three score vectors; finite Poisson-truncation diagnostics separately tested four probabilities. Finite tests do not prove the asymptotic statements.

## Originality — PASS, with bounded bibliographic risk

Braun, Bruegge and Kahle (arXiv:2204.07239v1) study facets, degree sequences and clustering for the same random edge polytope family. Their theorems do not give Gaussian support losses, a limiting marked extreme-pair process, or mean-width asymptotics. Higashitani, Jochemko and Michałek (arXiv:1807.07678) focus on arithmetic invariants, and Chen, Davis and Korchevskaia (arXiv:2107.12315) on facets and their subgraphs. Relevant mathematical-record results on sparse deterministic edge deletions and tree symmetric-edge polytopes do not imply a dense-random-graph coefficient. A targeted terminology/equivalence search did not identify a covering theorem. An unlocated equivalent probabilistic result under graph-indexed extreme-value terminology remains possible.

## Mathematical value — PASS

Random symmetric edge polytopes already have a substantive geometric/combinatorial theory. This theorem resolves a distinct natural metric observable: the complete limiting distribution of the loss incurred when graph edges are randomly deleted, its strictly positive sharp mean-width coefficient, and two precise density-endpoint regimes. In particular, while prior facet behavior depends on a combinatorial edge-density threshold, the full support-loss law is governed by a continuous marked Poisson extreme-pair model. This is neither a renaming of the complete-graph range nor a routine fixed-deletion perturbation.

## Limitations and validation status

The result concerns fixed \(p\in(0,1)\), annealed mean width and a non-elementary but explicit Poisson expectation. It does not assert concentration of mean width for a typical graph, sparse-joint limits, or a universal bibliographic uniqueness guarantee. Code provides reproducibility checks, not infinite proof or an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
