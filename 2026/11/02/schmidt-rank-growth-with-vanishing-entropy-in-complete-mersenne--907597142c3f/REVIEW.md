# Scientific assessment

## Correctness (PASS)

The single claim is the exact finite Schmidt spectrum for complete \((2^j-1)\)-uniform qubit hypergraph states at \(j\ge3\), with block sizes at least \(2^j-1\), and its sequential large-block, then large-arity entropy limit. Lucas' binary congruence gives the exact cyclic sign kernel. Orthogonal compression by Hamming-weight residue identifies the complete nonzero reduced spectrum with \(TT^{\mathsf T}\). The factorization \(F=\boldsymbol1\boldsymbol1^{\mathsf T}-2R\) with \(R\) a reversal permutation yields eigenvalues \((q-2)^2\) once and \(4\) with multiplicity \(q-1\), so rank cannot drop under the specified size assumptions. A root-of-unity filter gives uniform convergence of residue weights for fixed \(q\), and elementary entropy bounds prove the second limit. Direct computational-basis tests, independent cyclic-binomial calculations, and eigenvalue comparisons passed 21 assertions. Finite checks are supporting evidence, not a substitute for the proof.

## Originality (PASS on examined evidence, with risks)

The original hypergraph-state construction and its real equal-weight phase description are due to Rossi et al., *Quantum Hypergraph States* (2012 preprint). Nöller et al., *Symmetric hypergraph states: Entanglement quantification and robust Bell nonlocality* (2023), analyze geometric entanglement and local symmetries for complete symmetric states; the inspected sections do not establish this bipartite reduced-state spectral law. Fajardo and Paraschiv, *Restriction-Based Certificate of Bipartite Schmidt Rank in Hypergraph States* (2026), introduce general sign-matrix and lower-bound methods, but not this full cyclic matrix diagonalization or the entropy-collapse limit. A related power-of-two-uniformity theorem evaluates the distinct arities \(2^j\), and its phase matrix and limiting eigenvalues differ. Searches for Mersenne-arity Schmidt spectra, equivalent cyclic-sign formulas, and stronger general spectral coverage did not find a dominating published statement in the checked sources. Search incompleteness and specialized literature on symmetric Boolean phase states remain genuine priority risks; lack of hits is not treated as uniqueness proof.

## Mathematical value (PASS)

The exact rank persists at an arbitrarily large value \(q\) while the iterated-limit entanglement entropy tends to zero, exhibiting a natural and quantitatively sharp distinction between Schmidt rank and physically accessible von Neumann entropy in complete many-body interaction states. The finite formula evaluates every positive reduced eigenvalue for an unbounded family using only a \(q\times q\) matrix rather than the exponentially larger Hilbert-space matrix. The qualitative rank/entropy separation, explicit purity, and complete spectral convergence are structurally motivated; they are not an arbitrary small-instance calculation or a routine parameter increment.

## Boundaries and residual risk

The model uses pure unweighted qubit states, every hyperedge of the specified cardinality, and blocks containing every residue class. The entropy statement is an iterated limit. No finite-temperature, noisy-state, arbitrary-hypergraph, general-arity, or uniform double-limit assertion is proved. Prior specialized symmetric-state spectral work could reduce historical novelty and requires independent priority review.

Self-review: passed. Independent audit: not yet performed.
