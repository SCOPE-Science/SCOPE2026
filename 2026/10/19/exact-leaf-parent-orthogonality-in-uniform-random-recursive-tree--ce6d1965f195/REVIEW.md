# Scientific review

## Correctness — PASS

The tree model, labels, rooting and three disjoint vertex classes are explicit. The increasing-tree root differential equation includes the singleton-child exclusion needed for a protected root. Its formal mixed derivative is calculated without truncating an infinite series, yielding \(c(z)=z b'(z)/2-z^3/[12(1-z)]\). With the normalization \((n-1)!\) recursive trees, coefficient extraction proves the exact cross-covariance for every \(n\ge3\). The standard recursive Bernoulli update separately proves the leaf variance, and the deterministic partition proves orthogonality of leaf and leaf-parent counts. The boundary cases and nonindependence witness are handled. Exact enumeration of 46,233 trees, 118 independent formal-series coefficient checks, and a boundary witness pass. Computations are corroborative, not a replacement for the proof.

## Originality — PASS, residual coverage risk

Devroye–Janson (arXiv:1310.0665v1) gives a fringe-subtree treatment of protected-node proportions in random recursive trees; Mahmoud–Ward (DOI:10.1239/jap/1429282623) computes exact protected-node means and variance growth. Neither inspected source establishes the finite-size cross-covariance of the protected count with leaves or the zero covariance with the number of distinct leaf parents. Related general fringe-limit laws (Holmgren–Janson, arXiv:1406.6883), protected-level-profile asymptotic covariances, and the later leaf-degree treatment of Hartle–Krapivsky (arXiv:2511.04085) were compared. The complete material of the general fringe-limit work and the later leaf-degree study was not available: these are real residual risks of equivalent implicit coverage, not proof of absence. Independent priority audit has not been performed.

## Mathematical value — PASS

The statistics are canonical rooted tree-shape measures, not artificially restricted invariants. A leaf parent's count has positive variability and shares local defining events with the leaf count, yet the covariance vanishes **exactly for every size** while independence fails. The marked generating function gives a structural explanation and an exact cross-moment formula beyond standalone marginal results. The precise rooted convention, finite-size exceptions, and limitation to uniform attachment are material to the statement.

Self-review: passed. Independent audit: not yet performed.
