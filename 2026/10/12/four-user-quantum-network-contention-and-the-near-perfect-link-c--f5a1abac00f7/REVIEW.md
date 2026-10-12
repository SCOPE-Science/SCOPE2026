# Scientific review: four-user chain-transport contention

## Correctness — PASS

The model and output fidelity are specified exactly. A Schmidt-rank cut argument bounds joint perfect Bell-pair deliveries; disjoint open interval paths attain that bound by swapping. For four ordered endpoints, the three matchings yield the stated contention penalty. Translation multiplicities and uniform demand probabilities give the finite polynomial identity. The parity coefficient formula follows from a positive-composition count. Absolute convergence proves the fixed-link coefficient, while explicit polynomial growth and Riemann sums prove the critical crossover. Independent exact enumeration of edge outcomes and pairings (see `verify.py`) supports the algebra at small sizes. The proof, not its finite tests, establishes the all-size claim. No relaxed-fidelity or physical-device claim is made.

## Originality — PASS, with residual priority risk

The dominant mathematical predecessor is Kim--Popovski, arXiv:2609.39690v1, Appendix C, Eq. (41), whose general perfect-output interval-allocation identity gives an unevaluated optimization for all demand realizations. The present result does **not** claim that interval allocation or the fixed-parameter leading scaling is new. It resolves the finite random-four-user average, the exact contention defect and its constant, and a varying-success-probability scaling regime that the predecessor's fixed-probability asymptotics do not address. Pant et al. (2019) study multiflow routing on two-dimensional networks; Halder et al. (2024) study optimization with fidelity/memory constraints. Searches for matching formulas, aliases, and specializations did not identify a published equivalent. That absence does not prove priority; a prior evaluation of the general interval program might exist.

## Value — PASS

Four active users are the smallest random exclusive-pairing instance with genuine competition between separate sessions. The exact loss isolates that competition from independent path failures and provides a finite-network benchmark for adaptive routing. Its different regimes are structurally informative: at fixed \(p<1\), contention is of order \(N^{-3}\), whereas at \(p=e^{-\lambda/N}\) the total transport is of order \(N\), governed by an explicit decreasing crossover function. This is a mathematically motivated nonuniform parameter boundary, not a tiny arbitrary numerical improvement.

## Residual risks and limitations

The exact physical operating conditions (ideal Bell supply and swaps, heralded link outcomes, one slot, four uniformly selected users, perfect counted Bell pairs) are essential. The general cut-allocation theorem in the motivating paper is stronger in breadth and already implies an algorithmic finite optimization; novelty is claimed only for its analytical evaluation and crossover. Relevant network-routing literature is extensive, so independent priority assessment remains useful.

Self-review: passed. Independent audit: not yet performed.
