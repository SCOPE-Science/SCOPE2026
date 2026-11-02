# Self-review

## Correctness — PASS

The real Hermitian trace-norm unit ball reduces the induced norm to pure inputs, and local-unitary covariance reduces each such input to one Schmidt parameter. Explicit diagonalization gives the exact two-by-two block and every remaining diagonal entry, yielding the displayed piecewise formula \(F_n(u)\). Its concave branch has a unique critical point in the branch; its other branch is bounded by the product-state value. The algebraic inequality \((1-c)^2(c^2+2c+3)>0\) proves that the concave-branch maximum dominates for all relevant dimensions. Hermitian trace/spectral duality then gives the second norm. The separable bound follows from convexity and an attained product-state calculation. The standalone checker passed 958 supplementary numerical assertions. No infinite assertion relies on a finite enumeration.

## Originality — PASS, qualified

The closest inspected 2023 paper, arXiv:2305.00460, derives separability bounds for the nuclear norm of a Bloch-coordinate correlation **matrix**, not the trace norm of the centered physical operator or its induced real-Hermitian projection norm. A previous exact one-body marginal-projection norm concerns a different sum of local conditional expectations and implies neither the two-body formula nor entangled extremality. Searches for tensor-depolarizing complements, Hermitian induced trace norms, quantum correlation projections, Schmidt optimization and aliases did not reveal a decisive equivalent or a general theorem implying the formula. An older general noncommutative projection formula may exist under terminology not recovered by these searches; absence from search results is not a uniqueness certificate.

## Mathematical value — PASS

The tensor product of two traceless local projections is a canonical two-body correlation extraction operator. This result exactly measures its endpoint Banach-space norm for all qubit–qudit dimensions, resolves the optimizing entanglement degree and proves a strict, attained separable-versus-entangled amplification gap. The result therefore gives a concrete sharp norm estimate and a family of sufficient entanglement witnesses, not merely a recomputation of a known Hilbert–Schmidt projection.

## Closest literature and limitations

X.-N. Zhu, J. Wang, G. Bao, M. Li, S.-Q. Shen and S.-M. Fei, *A Family of Bipartite Separability Criteria Based on Bloch Representation of Density Matrices*, arXiv:2305.00460v1, first posted 2023-04-30; full text inspected (abstract, definitions, theorems, examples, conclusions and references). Its Ky Fan/nuclear norms concern Bloch coefficient arrays, not the physical centered operator's Schatten norm. The calculation applies only to Hermitian matrices on \(\mathbb C^2\otimes\mathbb C^n\), not arbitrary complex matrices, ancilla-stabilized norms, general higher-dimensional pairs, or all entanglement-detection problems. Independent historical and mathematical checks are not available.

Self-review: passed. Independent audit: not yet performed.
