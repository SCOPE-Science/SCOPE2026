# Review of exact single-sensor observability resonances of a singly weighted cycle

## Correctness — PASS

The statement specifies all \(n\ge5\), every real \(w>0\), the measured vertex, the weighted Laplacian, and the exact PBH criterion. The proof separates reflection-even and reflection-odd eigenspaces; treats the uniform-edge eigenvalue degeneracy separately; shows the only weight-independent sensor zero is \(6\mid n\); and derives the complete finite list of odd-mode sensor zeros from a Dirichlet/anti-Dirichlet tridiagonal tail. Strict Jacobi interlacing excludes other cross-parity collisions. The converse constructs a nonzero blind eigenvector for each positive listed resonance. The boundary \(n=5\) has an empty resonance index set. Reproducible numerical eigenchecks returned zero mismatches in 816 test cases; they do not constitute an infinite proof.

## Originality — PASS, with literature risk

The closest primary mathematical source is Parlangeli–Notarstefano, arXiv:1109.3556v1, especially its path modes and unweighted-cycle reachability/observability theorems. It characterizes unit-weight paths/cycles, not the complete variation in one undirected edge weight. Xiang–Zhu–Chen–Chen (2013) provides broader weighted and directed network controllability conditions but its named cycle case is directed and its model includes heterogeneous node dynamics, not the stated exact defect resonance formula. Wang–Ni–Lai–Grebogi (2012) treats structural controllability and graph-link changes, not precise PBH failures on the one-weight cycle. Direct exact-formula, alias, parameter, and broader-coverage searches in mathematical result records and primary literature did not reveal an equivalent classification. This is a best-knowledge assessment, not proof that no specialty paper or unpublished note contains an equivalent result.

## Mathematical value — PASS

A single changed edge is the minimal nontrivial deterministic symmetry defect in an undirected ring. The result completely characterizes which such perturbations make a prescribed single sensor sufficient for exact state reconstruction. The dichotomy \(6\mid n\) versus finite exceptional weight sets, and the discrete nonuniform resonances (for example \(n=7\), \(w=1/2\)), supply design constraints invisible to a generic-weight argument. It is a complete natural one-parameter classification, not a routine restatement of path/cycle unweighted gcd criteria.

## Limitations

One fixed sensor, one nonuniform edge, noiseless finite-dimensional consensus and exact observability only; no conditioning guarantees or general sensor-placement assertion. The literature comparison is not an exhaustive survey of every specialized weighted-graph paper. Independent audit and validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
