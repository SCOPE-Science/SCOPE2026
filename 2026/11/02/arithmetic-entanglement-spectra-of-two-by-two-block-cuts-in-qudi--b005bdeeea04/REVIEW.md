# Scientific review: block-cut entropy of qudit rook-graph states

## Correctness — PASS

For every prime \(p\) and positive quadruple \((a,b,c,d)\), the exact cut-rank theorem follows from two independently checkable linear steps: (i) arbitrary margins on each positive-size rectangular block are realizable precisely when their total sums agree; (ii) the entire cut-adjacency kernel on those margins is described by a two-by-two matrix of block sizes modulo \(p\). Its rank gives \(m+n-4+\operatorname{rank}_{\mathbb F_p}M_p\). Direct partial tracing of the prime-dimensional graph state yields a flat nonzero Schmidt spectrum of size \(p^{\operatorname{rank}\Gamma}\). The complete proof is supplied in RESULT.md. The standalone checker passed 1168 cut-rank comparisons and four independent direct quantum-state purity checks. The computation is corroboration, not a substitute for the quantified proof.

## Originality — PASS on examined evidence, provisional

The foundational graph-state partial-rank theorem in Hein–Eisert–Briegel (2003/2004) already reduces bipartite qubit entropy to a finite-field adjacency rank. Looi–Yu–Gheorghiu–Griffiths (2007/2008) provides the more general qudit graph-state construction; Helwig (2013) develops general qudit bipartite-entanglement methods. These statements are antecedents and not claimed as new. The evaluated all-block-size rook-graph rank, its arithmetic determinant trichotomy for all primes and its subextensive entropy law were not found in the inspected source or searches. The same rook-graph state family appears explicitly in Liao–Sanders–Feder (2021/2022), but its accessible abstract focuses on topological quantum order and codes, not the specified block-cut Schmidt spectra. Its full text was not accessible, so direct comparison remains an unresolved priority risk. No failed search is treated as proof of historical uniqueness.

## Mathematical value — PASS

The family of cuts is intrinsic to the product row/column structure of \(K_m\square K_n\), not a chosen exceptional finite computation. For arbitrary prime local dimensions and every four positive block sizes, a constant-size arithmetic matrix determines the full reduced-state spectrum of a state with \(mn\) qudits. Distinct residue classes produce rank-zero, rank-one and rank-two corrections and can change entropy under a change of prime despite an identical interaction graph. This identifies a structural origin of low cut entanglement in a dense, highly connected quantum network and supplies exact scalable benchmarks. It does not establish optimized multipartite Schmidt measures or any noisy-system theorem.

## Closest literature and residual limits

- M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130, full journal text inspected at Eq. (43), https://doi.org/10.1103/PhysRevA.69.062311.
- S. Y. Looi et al., *Quantum Error Correcting Codes Using Qudit Graph States*, arXiv:0712.1979; abstract and publication record inspected.
- W. Helwig, *Absolutely Maximally Entangled Qudit Graph States*, arXiv:1306.2879; public abstract inspected.
- P. Liao, B. C. Sanders, D. L. Feder, *Topological graph states and quantum error correction codes*, arXiv:2112.02502; abstract inspected, full-text comparison unavailable.

The result assumes a pure, uniform unit-weight controlled-phase graph state, a prime local dimension and a two-by-two product block cut; arbitrary cuts, mixed states, defects, and operational topological-coding conclusions are outside scope.

Self-review: passed. Independent audit: not yet performed.
