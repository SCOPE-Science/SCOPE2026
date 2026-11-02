# Scientific review: A single-pair versus multi-pair price threshold for spectral-gap design of complete graphs

## Correctness — PASS

All parameters have explicit domains: \(n\ge4\), \(1\le k\le\lfloor n/2floor\), and positive prices/budget. The proof identifies the unit-gap normalization and constructs a valid positive-semidefinite dual \(X_s\). Its edge lengths and trace give a universal lower bound. Exact uniform and matching-deleted primal allocations attain the bound, with complete eigenspace decompositions. Complementary slackness proves unique uniform weights strictly below the threshold and deletion of every costly edge strictly above it. The exact-rational standalone verifier ran 35,388 assertions on the stated finite instances; the all-parameter claim is supported by the analytic proof.

## Originality — PASS (qualified)

Sun–Boyd–Xiao–Diaconis (2006) provide the general continuous-time SDP and embedding dual, not this matching-size-dependent two-price threshold or the full optimizer rigidity statements. Boyd–Diaconis–Parrilo–Xiao (2007) address discrete-time SLEM and uniform complete graphs. Ghosh–Boyd (2006) address convex relaxations of *unweighted graph families*. Literature and semantic record searches used equivalent language (priced algebraic connectivity, fastest mixing Markov process, matching-deleted complete graph and symmetric edge-weight design). No inspected source dominated the precise result. A sufficiently specialized unlocated reference could still cover it, so this is a best-knowledge novelty assessment rather than proof of first discovery.

## Value — PASS

The exact transition from uniform conductances to mandatory whole-matching deletion is an operational design decision. It distinguishes one costly connection from multiple disjoint ones, giving a genuinely dimension-independent price threshold in the latter case. The theorem also yields the optimum spectral gap for every continuous price and budget, not just one isolated numerical example.

## Closest literature and limitations

Primary literature: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf; https://arxiv.org/pdf/0709.0955; https://web.stanford.edu/~boyd/papers/pdf/eigbounds_laplacian.pdf. The result assumes a matching of costly edges in a complete graph, two positive price classes and unnormalized continuous-time Laplacian spectral gap. It does not treat arbitrary expensive-edge subgraphs or classify every critical/above-critical optimizer. No independent external review has been conducted.

Self-review: passed. Independent audit: not yet performed.
