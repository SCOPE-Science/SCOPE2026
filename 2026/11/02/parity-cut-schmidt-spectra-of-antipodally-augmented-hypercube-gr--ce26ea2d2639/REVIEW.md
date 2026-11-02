# Self-review

## Correctness — PASS

The claim fixes all graph and state conventions and includes all integers \(n\ge3\) and every nonempty set of coordinates. The graph-state reduction to \(\mathbb F_2\) cut rank is derived via an explicit partial-trace character sum. Cross-cut adjacency is exactly multiplication by the stated group-algebra element. If a linear term remains, a concrete algebra automorphism gives rank \(2^{n-1}\). In the exceptional odd full-parity case, the even-translation subgroup reduces the computation to a sum of independent square-zero two-variable differentials. The tensor-chain homology calculation gives the claimed rank without extrapolating from finite tests. The same proof gives all nonzero Schmidt eigenvalues. The independent implementation compares all nonempty \(S\) through dimension nine and representative larger cases, and directly diagonalizes six small reduced states; their logs are not substituted for the analytic proof.

## Originality — PASS on the material examined; historical priority provisional

Hein–Eisert–Briegel, arXiv:quant-ph/0307130 (full Section III.2 and examples inspected), proves the general cut-rank rule but not its folded-hypercube evaluation. Hashizume–Bentsen–Weber–Daley, arXiv:2102.13117 (full main and supplemental graph-state discussion inspected), studies ordinary \(Q_n\) graph states and samples subgraph ranks, not antipodally augmented \(FQ_n\) with every coordinate-parity cut. Wang et al., arXiv:1101.3386 (full text inspected), defines the same folded graph and studies geometric crossing numbers. Liu–Pan–Cao (2014, abstract examined) derives real spectral data for folded-cube Estrada indices, which does not determine binary cut-rank. The 2023 folded-cube entanglement paper concerns a free-fermion Hamiltonian ground state, not a graph state; its accessible abstract was examined. A specialized earlier binary-adjacency-rank theorem may imply the exceptional correction; this remains a material publication-priority risk. No absolute uniqueness is claimed. The previously treated ordinary-hypercube parity-cut subcase is not considered original.

## Mathematical value — PASS

The extra antipodal perfect matching changes a natural structured quantum cut from full half-system entropy to half that value on every proper odd-coordinate parity cut, despite adding nonlocal entangling gates. The exceptional odd full-parity cut reveals a further exact dyadic defect determined by a characteristic-two tensor differential. The theorem supplies the **entire reduced spectrum**, not just an entropy bound, and applies uniformly to exponentially large qubit networks. This is a natural graph-network/quantum-entanglement invariant with potentially useful benchmarks, rather than an arbitrary small-instance computation.

## Limitations and residual risks

The result is for pure unweighted qubit graph states and specified coordinate-parity cuts only. Direct density-matrix computation is limited to 8- and 16-qubit states; all-parameter validity rests on the symbolic proof. Historical priority could change if older coding-theoretic binary-rank formulas cover antipodal cube cross-adjacency. Related 1990s cube-network coding sources discuss ranks of displacement-generator matrices rather than this \(2^{n-1}\) by \(2^{n-1}\) cut matrix, but not every historical source was available in full.

Self-review: passed. Independent audit: not yet performed.
