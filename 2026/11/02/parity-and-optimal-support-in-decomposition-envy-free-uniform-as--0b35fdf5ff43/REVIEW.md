# Scientific review

## Correctness — PASS

The result concerns the uniform bistochastic matrix and common strict preference order, with positive support on distinct permutation matchings. The proof establishes the marginal support bound, proves the global impossibility of exactly one extra permutation using the shared sub-\(1/n\) weights, constructs an exact rank-reversing family for every even \(n\), constructs \(2n\) balanced assignments for odd \(n\), and derives the unique three-agent six-weight solution. The exact-fraction verifier tests explicit constructions and re-solves the complete finite three-agent constraint matrix; these finite tests corroborate, rather than substitute for, the general proof.

## Originality — PASS (with access qualification)

The closest primary paper is Kawase et al., arXiv:2604.16973v1 (18 April 2026), especially Example 1, Definitions 1–2 and Theorems 1–2. It shows both a failing cyclic three-agent decomposition and a qualifying six-permutation one, but the accessible full main text does not assert uniqueness or minimum support, nor a parity-dependent optimal-support law. The later Li et al. paper arXiv:2609.35192v1 (28 September 2026) studies broader feasibility and complexity, according to its abstract, but complete text could not be inspected. Published indexed records focused on stochastic-dominance envy-freeness and random-priority lotteries, not the present support-minimization statement. Search absence does not establish uniqueness; unindexed or inaccessible equivalences remain risks.

## Mathematical value — PASS

The original motivating example demonstrates that implementing a fair marginal assignment with a small Birkhoff support can create systematically unequal realized envy. The quantity minimized here is precisely the number of discrete matchings needed to implement the **same uniform outcome** without that violation. The sharp even-size family, parity gap, uniform-matrix support hole, and unique three-agent decomposition distinguish a meaningful implementation resource from mere existence of a fair lottery. The unresolved odd-size optimum beyond three agents is clearly delimited.

## Scope and residual risks

Claims are not made for heterogeneous rankings, nonuniform matrices, or the exact odd-size support at \(n\geq5\). The September 2026 source's full text was not available, and no independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
